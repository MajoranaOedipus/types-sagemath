import sage.matrix.matrix_dense
import sage.matrix.matrix_space as matrix_space
from sage.arith.misc import is_prime as is_prime
from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.timing import cputime as cputime
from sage.misc.verbose import get_verbose as get_verbose, verbose as verbose
from sage.parallel.parallelism import Parallelism as Parallelism
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.proof.proof import get_proof_flag as get_proof_flag
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

MAX_MODULUS: int

class Matrix_modn_dense_double(Matrix_modn_dense_template):
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_double.pyx (starting at line 48)

        Dense matrices over `\\ZZ/n\\ZZ` for `n < 94906266` using LinBox's ``Modular<double>``.

        These are matrices with integer entries mod ``n`` represented as
        floating-point numbers in a 64-bit word for use with LinBox routines.
        This allows for ``n`` up to `94906266`. By default, the analogous
        ``Matrix_modn_dense_float`` class is used for smaller moduli, specifically
        for ``n`` up to `2^{8}`.

        Routines here are for the most basic access, see the
        ``matrix_modn_dense_template.pxi`` file for higher-level routines.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class Matrix_modn_dense_template(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_modn_dense_template(parent, entries=None, copy=None, bool coerce=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 482)

                Create a new matrix.

                INPUT:

                - ``parent`` -- a matrix space

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- perform modular reduction first?

                EXAMPLES::

                    sage: A = random_matrix(GF(3),1000,1000)
                    sage: type(A)
                    <class 'sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float'>
                    sage: A = random_matrix(Integers(10),1000,1000)
                    sage: type(A)
                    <class 'sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float'>
                    sage: A = random_matrix(Integers(2^16),1000,1000)
                    sage: type(A)
                    <class 'sage.matrix.matrix_modn_dense_double.Matrix_modn_dense_double'>

                TESTS::

                    sage: Matrix(GF(7), 2, 2, [-1, int(-2), GF(7)(-3), 1/4])
                    [6 5]
                    [4 2]

                    sage: Matrix(GF(6434383), 2, 2, [-1, int(-2), GF(7)(-3), 1/4])              # needs sage.rings.finite_rings
                    [6434382 6434381]
                    [      4 1608596]

                    sage: Matrix(Integers(4618990), 2, 2, [-1, int(-2), GF(7)(-3), 1/7])        # needs sage.rings.finite_rings
                    [4618989 4618988]
                    [      4 2639423]

                    sage: Matrix(IntegerModRing(200), [[int(2**128+1), int(2**256+1), int(2**1024+1)]])        # needs sage.rings.finite_rings
                    [ 57 137  17]
        """
    @overload
    def charpoly(self, var=..., algorithm=...) -> Any:
        """Matrix_modn_dense_template.charpoly(self, var='x', algorithm='linbox')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1273)

        Return the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- 'generic', 'linbox' or 'all' (default: linbox)

        EXAMPLES::

            sage: A = random_matrix(GF(19), 10, 10)
            sage: B = copy(A)
            sage: char_p = A.characteristic_polynomial()
            sage: char_p(A) == 0
            True
            sage: B == A              # A is not modified
            True

            sage: min_p = A.minimal_polynomial(proof=True)
            sage: min_p.divides(char_p)
            True

        ::

            sage: A = random_matrix(GF(2916337), 7, 7)                                  # needs sage.rings.finite_rings
            sage: B = copy(A)
            sage: char_p = A.characteristic_polynomial()
            sage: char_p(A) == 0
            True
            sage: B == A               # A is not modified
            True

            sage: min_p = A.minimal_polynomial(proof=True)
            sage: min_p.divides(char_p)
            True

            sage: A = Mat(Integers(6),3,3)(range(9))
            sage: A.charpoly()
            x^3

        TESTS::

            sage: for i in range(10):
            ....:     A = random_matrix(GF(17), 50, 50, density=0.1)
            ....:     _ = A.characteristic_polynomial(algorithm='all')

            sage: A = random_matrix(GF(19), 0, 0)
            sage: A.minimal_polynomial()
            1

            sage: A = random_matrix(GF(19), 0, 1)
            sage: A.minimal_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = random_matrix(GF(19), 1, 0)
            sage: A.minimal_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = matrix(GF(19), 10, 10)
            sage: A.minimal_polynomial()                                                # needs sage.libs.pari
            x

            sage: A = random_matrix(GF(4198973), 0, 0)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            1

            sage: A = random_matrix(GF(4198973), 0, 1)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = random_matrix(GF(4198973), 1, 0)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = matrix(GF(4198973), 10, 10)                                       # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            x

            sage: A = Mat(GF(7),3,3)([0, 1, 2] * 3)
            sage: A.charpoly()
            x^3 + 4*x^2

        ALGORITHM: Uses LinBox if ``self.base_ring()`` is a field,
        otherwise use Hessenberg form algorithm.

        TESTS:

        The cached polynomial should be independent of the ``var``
        argument (:issue:`12292`). We check (indirectly) that the
        second call uses the cached value by noting that its result is
        not cached. The polynomial here is not unique, so we only
        check the polynomial's variable.

            sage: M = MatrixSpace(Integers(37), 2)
            sage: A = M(range(0, 2^2))
            sage: type(A)
            <class 'sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float'>
            sage: A.charpoly('x').variables()
            (x,)
            sage: A.charpoly('y').variables()
            (y,)
            sage: A._cache['charpoly_linbox'].variables()
            (x,)"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_modn_dense_template.charpoly(self, var='x', algorithm='linbox')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1273)

        Return the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- 'generic', 'linbox' or 'all' (default: linbox)

        EXAMPLES::

            sage: A = random_matrix(GF(19), 10, 10)
            sage: B = copy(A)
            sage: char_p = A.characteristic_polynomial()
            sage: char_p(A) == 0
            True
            sage: B == A              # A is not modified
            True

            sage: min_p = A.minimal_polynomial(proof=True)
            sage: min_p.divides(char_p)
            True

        ::

            sage: A = random_matrix(GF(2916337), 7, 7)                                  # needs sage.rings.finite_rings
            sage: B = copy(A)
            sage: char_p = A.characteristic_polynomial()
            sage: char_p(A) == 0
            True
            sage: B == A               # A is not modified
            True

            sage: min_p = A.minimal_polynomial(proof=True)
            sage: min_p.divides(char_p)
            True

            sage: A = Mat(Integers(6),3,3)(range(9))
            sage: A.charpoly()
            x^3

        TESTS::

            sage: for i in range(10):
            ....:     A = random_matrix(GF(17), 50, 50, density=0.1)
            ....:     _ = A.characteristic_polynomial(algorithm='all')

            sage: A = random_matrix(GF(19), 0, 0)
            sage: A.minimal_polynomial()
            1

            sage: A = random_matrix(GF(19), 0, 1)
            sage: A.minimal_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = random_matrix(GF(19), 1, 0)
            sage: A.minimal_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = matrix(GF(19), 10, 10)
            sage: A.minimal_polynomial()                                                # needs sage.libs.pari
            x

            sage: A = random_matrix(GF(4198973), 0, 0)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            1

            sage: A = random_matrix(GF(4198973), 0, 1)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = random_matrix(GF(4198973), 1, 0)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = matrix(GF(4198973), 10, 10)                                       # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            x

            sage: A = Mat(GF(7),3,3)([0, 1, 2] * 3)
            sage: A.charpoly()
            x^3 + 4*x^2

        ALGORITHM: Uses LinBox if ``self.base_ring()`` is a field,
        otherwise use Hessenberg form algorithm.

        TESTS:

        The cached polynomial should be independent of the ``var``
        argument (:issue:`12292`). We check (indirectly) that the
        second call uses the cached value by noting that its result is
        not cached. The polynomial here is not unique, so we only
        check the polynomial's variable.

            sage: M = MatrixSpace(Integers(37), 2)
            sage: A = M(range(0, 2^2))
            sage: type(A)
            <class 'sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float'>
            sage: A.charpoly('x').variables()
            (x,)
            sage: A.charpoly('y').variables()
            (y,)
            sage: A._cache['charpoly_linbox'].variables()
            (x,)"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_modn_dense_template.charpoly(self, var='x', algorithm='linbox')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1273)

        Return the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- 'generic', 'linbox' or 'all' (default: linbox)

        EXAMPLES::

            sage: A = random_matrix(GF(19), 10, 10)
            sage: B = copy(A)
            sage: char_p = A.characteristic_polynomial()
            sage: char_p(A) == 0
            True
            sage: B == A              # A is not modified
            True

            sage: min_p = A.minimal_polynomial(proof=True)
            sage: min_p.divides(char_p)
            True

        ::

            sage: A = random_matrix(GF(2916337), 7, 7)                                  # needs sage.rings.finite_rings
            sage: B = copy(A)
            sage: char_p = A.characteristic_polynomial()
            sage: char_p(A) == 0
            True
            sage: B == A               # A is not modified
            True

            sage: min_p = A.minimal_polynomial(proof=True)
            sage: min_p.divides(char_p)
            True

            sage: A = Mat(Integers(6),3,3)(range(9))
            sage: A.charpoly()
            x^3

        TESTS::

            sage: for i in range(10):
            ....:     A = random_matrix(GF(17), 50, 50, density=0.1)
            ....:     _ = A.characteristic_polynomial(algorithm='all')

            sage: A = random_matrix(GF(19), 0, 0)
            sage: A.minimal_polynomial()
            1

            sage: A = random_matrix(GF(19), 0, 1)
            sage: A.minimal_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = random_matrix(GF(19), 1, 0)
            sage: A.minimal_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = matrix(GF(19), 10, 10)
            sage: A.minimal_polynomial()                                                # needs sage.libs.pari
            x

            sage: A = random_matrix(GF(4198973), 0, 0)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            1

            sage: A = random_matrix(GF(4198973), 0, 1)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = random_matrix(GF(4198973), 1, 0)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = matrix(GF(4198973), 10, 10)                                       # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            x

            sage: A = Mat(GF(7),3,3)([0, 1, 2] * 3)
            sage: A.charpoly()
            x^3 + 4*x^2

        ALGORITHM: Uses LinBox if ``self.base_ring()`` is a field,
        otherwise use Hessenberg form algorithm.

        TESTS:

        The cached polynomial should be independent of the ``var``
        argument (:issue:`12292`). We check (indirectly) that the
        second call uses the cached value by noting that its result is
        not cached. The polynomial here is not unique, so we only
        check the polynomial's variable.

            sage: M = MatrixSpace(Integers(37), 2)
            sage: A = M(range(0, 2^2))
            sage: type(A)
            <class 'sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float'>
            sage: A.charpoly('x').variables()
            (x,)
            sage: A.charpoly('y').variables()
            (y,)
            sage: A._cache['charpoly_linbox'].variables()
            (x,)"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def determinant(self) -> Any:
        """Matrix_modn_dense_template.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2188)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: s = set()
            sage: while s != set(GF(7)):
            ....:     A = random_matrix(GF(7), 10, 10)
            ....:     s.add(A.determinant())

        ::

            sage: A = random_matrix(GF(7), 100, 100)
            sage: A.determinant() == A.transpose().determinant()
            True

            sage: B = random_matrix(GF(7), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 10)
            sage: A.determinant().parent() is GF(16007)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 100, 100)
            sage: A.determinant().parent() is GF(16007)
            True
            sage: A.determinant() == A.transpose().determinant()
            True
            sage: B = random_matrix(GF(16007), 100, 100)
            sage: (A*B).determinant() == A.determinant() * B.determinant()
            True

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),200)
            sage: B = copy(A)
            sage: Parallelism().set('linbox', nproc=2)
            sage: d = A.determinant()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: e = B.determinant()
            sage: d==e
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0); A.det()
            1

            sage: A = random_matrix(GF(7), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = random_matrix(GF(7), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

            sage: A = matrix(GF(7), 5, 5); A.det()                                      # needs sage.libs.pari
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0); A.det()
            1
            sage: A = random_matrix(GF(16007), 0, 1); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = random_matrix(GF(16007), 1, 0); A.det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix
            sage: A = matrix(GF(16007), 5, 5); A.det()
            0"""
    @overload
    def echelonize(self, algorithm=..., **kwds) -> Any:
        """Matrix_modn_dense_template.echelonize(self, algorithm='linbox_noefd', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1581)

        Put ``self`` in reduced row echelon form.

        INPUT:

        - ``self`` -- a mutable matrix

        - ``algorithm``

          - ``linbox`` -- uses the LinBox library (wrapping fflas-ffpack)

          - ``linbox_noefd`` -- uses the FFPACK directly, less memory and faster (default)

          - ``gauss`` -- uses a custom slower `O(n^3)` Gauss
            elimination implemented in Sage

          - ``all`` -- compute using both algorithms and verify that
            the results are the same

        - ``**kwds`` -- these are all ignored

        OUTPUT: ``self`` is put in reduced row echelon form

        - the rank of ``self`` is computed and cached

        - the pivot columns of ``self`` are computed and cached

        - the fact that ``self`` is now in echelon form is recorded and
          cached so future calls to echelonize return immediately

        EXAMPLES::

            sage: A = random_matrix(GF(7), 10, 20)
            sage: E = A.echelon_form()
            sage: A.row_space() == E.row_space()
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in E.rows() if r)
            True

        ::

            sage: A = random_matrix(GF(13), 10, 10)
            sage: while A.rank() != 10:
            ....:     A = random_matrix(GF(13), 10, 10)
            sage: MS = parent(A)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: A.rank()
            10
            sage: C = B.submatrix(0,10,10,10)
            sage: ~A == C
            True

        ::

            sage: A = random_matrix(Integers(10), 10, 20)
            sage: A.echelon_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 10'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 20)
            sage: E = A.echelon_form()
            sage: A.row_space() == E.row_space()
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in E.rows() if r)
            True

        ::

            sage: A = random_matrix(Integers(10000), 10, 20)
            sage: A.echelon_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 10000'.

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),100,200)
            sage: Parallelism().set('linbox', nproc=2)
            sage: E = A.echelon_form()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: F = A.echelon_form()
            sage: E==F
            True

        TESTS::

            sage: A = random_matrix(GF(7),  0, 10)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(7), 10,  0)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(7),  0,  0)
            sage: A.echelon_form()
            []
            sage: A = matrix(GF(7),  10,  10)
            sage: A.echelon_form()
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007),  0, 10)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(16007), 10,  0)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(16007),  0,  0)
            sage: A.echelon_form()
            []
            sage: A = matrix(GF(16007),  10,  10)
            sage: A.echelon_form()
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]

            sage: A = matrix(GF(97),3,4,range(12))
            sage: A.echelonize(); A
            [ 1  0 96 95]
            [ 0  1  2  3]
            [ 0  0  0  0]
            sage: A.pivots()
            (0, 1)

            sage: for p in (3,17,97,127,1048573):
            ....:    for i in range(10):
            ....:        A = random_matrix(GF(3), 100, 100)
            ....:        A.echelonize(algorithm='all')"""
    @overload
    def echelonize(self) -> Any:
        """Matrix_modn_dense_template.echelonize(self, algorithm='linbox_noefd', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1581)

        Put ``self`` in reduced row echelon form.

        INPUT:

        - ``self`` -- a mutable matrix

        - ``algorithm``

          - ``linbox`` -- uses the LinBox library (wrapping fflas-ffpack)

          - ``linbox_noefd`` -- uses the FFPACK directly, less memory and faster (default)

          - ``gauss`` -- uses a custom slower `O(n^3)` Gauss
            elimination implemented in Sage

          - ``all`` -- compute using both algorithms and verify that
            the results are the same

        - ``**kwds`` -- these are all ignored

        OUTPUT: ``self`` is put in reduced row echelon form

        - the rank of ``self`` is computed and cached

        - the pivot columns of ``self`` are computed and cached

        - the fact that ``self`` is now in echelon form is recorded and
          cached so future calls to echelonize return immediately

        EXAMPLES::

            sage: A = random_matrix(GF(7), 10, 20)
            sage: E = A.echelon_form()
            sage: A.row_space() == E.row_space()
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in E.rows() if r)
            True

        ::

            sage: A = random_matrix(GF(13), 10, 10)
            sage: while A.rank() != 10:
            ....:     A = random_matrix(GF(13), 10, 10)
            sage: MS = parent(A)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: A.rank()
            10
            sage: C = B.submatrix(0,10,10,10)
            sage: ~A == C
            True

        ::

            sage: A = random_matrix(Integers(10), 10, 20)
            sage: A.echelon_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 10'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 20)
            sage: E = A.echelon_form()
            sage: A.row_space() == E.row_space()
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in E.rows() if r)
            True

        ::

            sage: A = random_matrix(Integers(10000), 10, 20)
            sage: A.echelon_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 10000'.

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),100,200)
            sage: Parallelism().set('linbox', nproc=2)
            sage: E = A.echelon_form()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: F = A.echelon_form()
            sage: E==F
            True

        TESTS::

            sage: A = random_matrix(GF(7),  0, 10)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(7), 10,  0)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(7),  0,  0)
            sage: A.echelon_form()
            []
            sage: A = matrix(GF(7),  10,  10)
            sage: A.echelon_form()
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007),  0, 10)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(16007), 10,  0)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(16007),  0,  0)
            sage: A.echelon_form()
            []
            sage: A = matrix(GF(16007),  10,  10)
            sage: A.echelon_form()
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]

            sage: A = matrix(GF(97),3,4,range(12))
            sage: A.echelonize(); A
            [ 1  0 96 95]
            [ 0  1  2  3]
            [ 0  0  0  0]
            sage: A.pivots()
            (0, 1)

            sage: for p in (3,17,97,127,1048573):
            ....:    for i in range(10):
            ....:        A = random_matrix(GF(3), 100, 100)
            ....:        A.echelonize(algorithm='all')"""
    @overload
    def echelonize(self) -> Any:
        """Matrix_modn_dense_template.echelonize(self, algorithm='linbox_noefd', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1581)

        Put ``self`` in reduced row echelon form.

        INPUT:

        - ``self`` -- a mutable matrix

        - ``algorithm``

          - ``linbox`` -- uses the LinBox library (wrapping fflas-ffpack)

          - ``linbox_noefd`` -- uses the FFPACK directly, less memory and faster (default)

          - ``gauss`` -- uses a custom slower `O(n^3)` Gauss
            elimination implemented in Sage

          - ``all`` -- compute using both algorithms and verify that
            the results are the same

        - ``**kwds`` -- these are all ignored

        OUTPUT: ``self`` is put in reduced row echelon form

        - the rank of ``self`` is computed and cached

        - the pivot columns of ``self`` are computed and cached

        - the fact that ``self`` is now in echelon form is recorded and
          cached so future calls to echelonize return immediately

        EXAMPLES::

            sage: A = random_matrix(GF(7), 10, 20)
            sage: E = A.echelon_form()
            sage: A.row_space() == E.row_space()
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in E.rows() if r)
            True

        ::

            sage: A = random_matrix(GF(13), 10, 10)
            sage: while A.rank() != 10:
            ....:     A = random_matrix(GF(13), 10, 10)
            sage: MS = parent(A)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: A.rank()
            10
            sage: C = B.submatrix(0,10,10,10)
            sage: ~A == C
            True

        ::

            sage: A = random_matrix(Integers(10), 10, 20)
            sage: A.echelon_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 10'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 20)
            sage: E = A.echelon_form()
            sage: A.row_space() == E.row_space()
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in E.rows() if r)
            True

        ::

            sage: A = random_matrix(Integers(10000), 10, 20)
            sage: A.echelon_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 10000'.

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),100,200)
            sage: Parallelism().set('linbox', nproc=2)
            sage: E = A.echelon_form()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: F = A.echelon_form()
            sage: E==F
            True

        TESTS::

            sage: A = random_matrix(GF(7),  0, 10)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(7), 10,  0)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(7),  0,  0)
            sage: A.echelon_form()
            []
            sage: A = matrix(GF(7),  10,  10)
            sage: A.echelon_form()
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007),  0, 10)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(16007), 10,  0)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(16007),  0,  0)
            sage: A.echelon_form()
            []
            sage: A = matrix(GF(16007),  10,  10)
            sage: A.echelon_form()
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]

            sage: A = matrix(GF(97),3,4,range(12))
            sage: A.echelonize(); A
            [ 1  0 96 95]
            [ 0  1  2  3]
            [ 0  0  0  0]
            sage: A.pivots()
            (0, 1)

            sage: for p in (3,17,97,127,1048573):
            ....:    for i in range(10):
            ....:        A = random_matrix(GF(3), 100, 100)
            ....:        A.echelonize(algorithm='all')"""
    @overload
    def echelonize(self, algorithm=...) -> Any:
        """Matrix_modn_dense_template.echelonize(self, algorithm='linbox_noefd', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1581)

        Put ``self`` in reduced row echelon form.

        INPUT:

        - ``self`` -- a mutable matrix

        - ``algorithm``

          - ``linbox`` -- uses the LinBox library (wrapping fflas-ffpack)

          - ``linbox_noefd`` -- uses the FFPACK directly, less memory and faster (default)

          - ``gauss`` -- uses a custom slower `O(n^3)` Gauss
            elimination implemented in Sage

          - ``all`` -- compute using both algorithms and verify that
            the results are the same

        - ``**kwds`` -- these are all ignored

        OUTPUT: ``self`` is put in reduced row echelon form

        - the rank of ``self`` is computed and cached

        - the pivot columns of ``self`` are computed and cached

        - the fact that ``self`` is now in echelon form is recorded and
          cached so future calls to echelonize return immediately

        EXAMPLES::

            sage: A = random_matrix(GF(7), 10, 20)
            sage: E = A.echelon_form()
            sage: A.row_space() == E.row_space()
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in E.rows() if r)
            True

        ::

            sage: A = random_matrix(GF(13), 10, 10)
            sage: while A.rank() != 10:
            ....:     A = random_matrix(GF(13), 10, 10)
            sage: MS = parent(A)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: A.rank()
            10
            sage: C = B.submatrix(0,10,10,10)
            sage: ~A == C
            True

        ::

            sage: A = random_matrix(Integers(10), 10, 20)
            sage: A.echelon_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 10'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 10, 20)
            sage: E = A.echelon_form()
            sage: A.row_space() == E.row_space()
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in E.rows() if r)
            True

        ::

            sage: A = random_matrix(Integers(10000), 10, 20)
            sage: A.echelon_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 10000'.

        Parallel computation::

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(65521),100,200)
            sage: Parallelism().set('linbox', nproc=2)
            sage: E = A.echelon_form()
            sage: Parallelism().set('linbox', nproc=1) # switch off parallelization
            sage: F = A.echelon_form()
            sage: E==F
            True

        TESTS::

            sage: A = random_matrix(GF(7),  0, 10)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(7), 10,  0)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(7),  0,  0)
            sage: A.echelon_form()
            []
            sage: A = matrix(GF(7),  10,  10)
            sage: A.echelon_form()
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007),  0, 10)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(16007), 10,  0)
            sage: A.echelon_form()
            []
            sage: A = random_matrix(GF(16007),  0,  0)
            sage: A.echelon_form()
            []
            sage: A = matrix(GF(16007),  10,  10)
            sage: A.echelon_form()
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0]

            sage: A = matrix(GF(97),3,4,range(12))
            sage: A.echelonize(); A
            [ 1  0 96 95]
            [ 0  1  2  3]
            [ 0  0  0  0]
            sage: A.pivots()
            (0, 1)

            sage: for p in (3,17,97,127,1048573):
            ....:    for i in range(10):
            ....:        A = random_matrix(GF(3), 100, 100)
            ....:        A.echelonize(algorithm='all')"""
    @overload
    def hessenbergize(self) -> Any:
        """Matrix_modn_dense_template.hessenbergize(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1963)

        Transform ``self`` in place to its Hessenberg form.

        EXAMPLES::

            sage: A = random_matrix(GF(17), 10, 10, density=0.1)
            sage: B = copy(A)
            sage: A.hessenbergize()
            sage: all(A[i,j] == 0 for j in range(10) for i in range(j+2, 10))
            True
            sage: A.charpoly() == B.charpoly()
            True"""
    @overload
    def hessenbergize(self) -> Any:
        """Matrix_modn_dense_template.hessenbergize(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1963)

        Transform ``self`` in place to its Hessenberg form.

        EXAMPLES::

            sage: A = random_matrix(GF(17), 10, 10, density=0.1)
            sage: B = copy(A)
            sage: A.hessenbergize()
            sage: all(A[i,j] == 0 for j in range(10) for i in range(j+2, 10))
            True
            sage: A.charpoly() == B.charpoly()
            True"""
    @overload
    def lift(self) -> Any:
        """Matrix_modn_dense_template.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2738)

        Return the lift of this matrix to the integers.

        EXAMPLES::

            sage: A = matrix(GF(7),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

            sage: # needs sage.rings.finite_rings
            sage: A = matrix(GF(16007),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

        Subdivisions are preserved when lifting::

            sage: A.subdivide([], [1,1]); A
            [1||2 3]
            [4||5 6]
            sage: A.lift()
            [1||2 3]
            [4||5 6]"""
    @overload
    def lift(self) -> Any:
        """Matrix_modn_dense_template.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2738)

        Return the lift of this matrix to the integers.

        EXAMPLES::

            sage: A = matrix(GF(7),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

            sage: # needs sage.rings.finite_rings
            sage: A = matrix(GF(16007),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

        Subdivisions are preserved when lifting::

            sage: A.subdivide([], [1,1]); A
            [1||2 3]
            [4||5 6]
            sage: A.lift()
            [1||2 3]
            [4||5 6]"""
    @overload
    def lift(self) -> Any:
        """Matrix_modn_dense_template.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2738)

        Return the lift of this matrix to the integers.

        EXAMPLES::

            sage: A = matrix(GF(7),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

            sage: # needs sage.rings.finite_rings
            sage: A = matrix(GF(16007),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

        Subdivisions are preserved when lifting::

            sage: A.subdivide([], [1,1]); A
            [1||2 3]
            [4||5 6]
            sage: A.lift()
            [1||2 3]
            [4||5 6]"""
    @overload
    def lift(self) -> Any:
        """Matrix_modn_dense_template.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2738)

        Return the lift of this matrix to the integers.

        EXAMPLES::

            sage: A = matrix(GF(7),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

            sage: # needs sage.rings.finite_rings
            sage: A = matrix(GF(16007),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

        Subdivisions are preserved when lifting::

            sage: A.subdivide([], [1,1]); A
            [1||2 3]
            [4||5 6]
            sage: A.lift()
            [1||2 3]
            [4||5 6]"""
    @overload
    def lift(self) -> Any:
        """Matrix_modn_dense_template.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2738)

        Return the lift of this matrix to the integers.

        EXAMPLES::

            sage: A = matrix(GF(7),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

            sage: # needs sage.rings.finite_rings
            sage: A = matrix(GF(16007),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

        Subdivisions are preserved when lifting::

            sage: A.subdivide([], [1,1]); A
            [1||2 3]
            [4||5 6]
            sage: A.lift()
            [1||2 3]
            [4||5 6]"""
    @overload
    def lift(self) -> Any:
        """Matrix_modn_dense_template.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2738)

        Return the lift of this matrix to the integers.

        EXAMPLES::

            sage: A = matrix(GF(7),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

            sage: # needs sage.rings.finite_rings
            sage: A = matrix(GF(16007),2,3,[1..6])
            sage: A.lift()
            [1 2 3]
            [4 5 6]
            sage: A.lift().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring

        Subdivisions are preserved when lifting::

            sage: A.subdivide([], [1,1]); A
            [1||2 3]
            [4||5 6]
            sage: A.lift()
            [1||2 3]
            [4||5 6]"""
    def matrix_from_columns(self, columns) -> Any:
        """Matrix_modn_dense_template.matrix_from_columns(self, columns)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 3086)

        Return the matrix constructed from ``self`` using columns with indices
        in the columns list.

        EXAMPLES::

            sage: M = MatrixSpace(Integers(8),3,3)
            sage: A = M(range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 0]
            sage: A.matrix_from_columns([2,1])
            [2 1]
            [5 4]
            [0 7]"""
    def matrix_from_rows(self, rows) -> Any:
        """Matrix_modn_dense_template.matrix_from_rows(self, rows)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 3116)

        Return the matrix constructed from ``self`` using rows with indices in
        the rows list.

        EXAMPLES::

            sage: M = MatrixSpace(Integers(8),3,3)
            sage: A = M(range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 0]
            sage: A.matrix_from_rows([2,1])
            [6 7 0]
            [3 4 5]"""
    def matrix_from_rows_and_columns(self, rows, columns) -> Any:
        """Matrix_modn_dense_template.matrix_from_rows_and_columns(self, rows, columns)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 3145)

        Return the matrix constructed from ``self`` from the given rows and
        columns.

        EXAMPLES::

            sage: M = MatrixSpace(Integers(8),3,3)
            sage: A = M(range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 0]
            sage: A.matrix_from_rows_and_columns([1], [0,2])
            [3 5]
            sage: A.matrix_from_rows_and_columns([1,2], [1,2])
            [4 5]
            [7 0]

        Note that row and column indices can be reordered or repeated::

            sage: A.matrix_from_rows_and_columns([2,1], [2,1])
            [0 7]
            [5 4]

        For example here we take from row 1 columns 2 then 0 twice, and do
        this 3 times::

            sage: A.matrix_from_rows_and_columns([1,1,1],[2,0,0])
            [5 3 3]
            [5 3 3]
            [5 3 3]

        AUTHORS:

        - Jaap Spies (2006-02-18)

        - Didier Deshommes: some Pyrex speedups implemented"""
    def minpoly(self, *args, **kwargs):
        """Matrix_modn_dense_template.minpoly(self, var='x', algorithm='linbox', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1410)

        Return the minimal polynomial of ``self``.

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- ``generic`` or ``linbox`` (default:
          ``linbox``)

        - ``proof`` -- (default: ``True``) whether to provably return
          the true minimal polynomial; if ``False``, we only guarantee
          to return a divisor of the minimal polynomial.  There are
          also certainly cases where the computed results is
          frequently not exactly equal to the minimal polynomial (but
          is instead merely a divisor of it).

         .. warning::

             If ``proof=True``, minpoly is insanely slow compared to
             ``proof=False``. This matters since proof=True is the
             default, unless you first type
             ``proof.linear_algebra(False)``.

        EXAMPLES::

            sage: A = random_matrix(GF(17), 10, 10)
            sage: B = copy(A)
            sage: min_p = A.minimal_polynomial(proof=True)
            sage: min_p(A) == 0
            True
            sage: B == A
            True

            sage: char_p = A.characteristic_polynomial()
            sage: min_p.divides(char_p)
            True

        ::

            sage: A = random_matrix(GF(1214471), 10, 10)                                # needs sage.rings.finite_rings
            sage: B = copy(A)
            sage: min_p = A.minimal_polynomial(proof=True)
            sage: min_p(A) == 0
            True
            sage: B == A
            True

            sage: char_p = A.characteristic_polynomial()
            sage: min_p.divides(char_p)
            True

        TESTS::

            sage: A = random_matrix(GF(17), 0, 0)
            sage: A.minimal_polynomial()
            1

            sage: A = random_matrix(GF(17), 0, 1)
            sage: A.minimal_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = random_matrix(GF(17), 1, 0)
            sage: A.minimal_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = matrix(GF(17), 10, 10)
            sage: A.minimal_polynomial()                                                # needs sage.libs.pari
            x

        ::

            sage: A = random_matrix(GF(2535919), 0, 0)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            1

            sage: A = random_matrix(GF(2535919), 0, 1)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = random_matrix(GF(2535919), 1, 0)                                  # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: matrix must be square

            sage: A = matrix(GF(2535919), 10, 10)                                       # needs sage.rings.finite_rings
            sage: A.minimal_polynomial()                                                # needs sage.rings.finite_rings
            x

        EXAMPLES::

            sage: R.<x>=GF(3)[]
            sage: A = matrix(GF(3),2,[0,0,1,2])
            sage: A.minpoly()
            x^2 + x

            sage: A.minpoly(proof=False) in [x, x+1, x^2+x]
            True"""
    @overload
    def randomize(self, density=..., nonzero=...) -> Any:
        """Matrix_modn_dense_template.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2534)

        Randomize ``density`` proportion of the entries of this
        matrix, leaving the rest unchanged.

        INPUT:

        - ``density`` -- integer; proportion (roughly) to be considered
          for changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new
          entries are forced to be nonzero

        OUTPUT: none, the matrix is modified in-space

        EXAMPLES::

            sage: A = matrix(GF(5), 5, 5, 0)
            sage: total_count = 0
            sage: from collections import defaultdict
            sage: dic = defaultdict(Integer)
            sage: def add_samples(density):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(GF(5), 5, 5, 0)
            ....:         A.randomize(density)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: add_samples(1.0)
            sage: while not all(abs(dic[a]/total_count - 1/5) < 0.01 for a in dic):
            ....:     add_samples(1.0)

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     density_sum += random_matrix(GF(5), 1000, 1000, density=density).density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: expected_density = 1.0 - (999/1000)^500
            sage: expected_density
            0.3936...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5)

        The matrix is updated instead of overwritten::

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = random_matrix(GF(5), 1000, 1000, density=density)
            ....:     A.randomize(density=density, nonzero=True)
            ....:     density_sum += A.density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: expected_density = 1.0 - (999/1000)^1000
            sage: expected_density
            0.6323...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1)
            sage: expected_density = 1.0 - (999/1000)^200
            sage: expected_density
            0.1813...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.1)"""
    @overload
    def randomize(self, density) -> Any:
        """Matrix_modn_dense_template.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2534)

        Randomize ``density`` proportion of the entries of this
        matrix, leaving the rest unchanged.

        INPUT:

        - ``density`` -- integer; proportion (roughly) to be considered
          for changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new
          entries are forced to be nonzero

        OUTPUT: none, the matrix is modified in-space

        EXAMPLES::

            sage: A = matrix(GF(5), 5, 5, 0)
            sage: total_count = 0
            sage: from collections import defaultdict
            sage: dic = defaultdict(Integer)
            sage: def add_samples(density):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(GF(5), 5, 5, 0)
            ....:         A.randomize(density)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: add_samples(1.0)
            sage: while not all(abs(dic[a]/total_count - 1/5) < 0.01 for a in dic):
            ....:     add_samples(1.0)

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     density_sum += random_matrix(GF(5), 1000, 1000, density=density).density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: expected_density = 1.0 - (999/1000)^500
            sage: expected_density
            0.3936...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5)

        The matrix is updated instead of overwritten::

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = random_matrix(GF(5), 1000, 1000, density=density)
            ....:     A.randomize(density=density, nonzero=True)
            ....:     density_sum += A.density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: expected_density = 1.0 - (999/1000)^1000
            sage: expected_density
            0.6323...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1)
            sage: expected_density = 1.0 - (999/1000)^200
            sage: expected_density
            0.1813...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.1)"""
    @overload
    def randomize(self, density=..., nonzero=...) -> Any:
        """Matrix_modn_dense_template.randomize(self, density=1, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2534)

        Randomize ``density`` proportion of the entries of this
        matrix, leaving the rest unchanged.

        INPUT:

        - ``density`` -- integer; proportion (roughly) to be considered
          for changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new
          entries are forced to be nonzero

        OUTPUT: none, the matrix is modified in-space

        EXAMPLES::

            sage: A = matrix(GF(5), 5, 5, 0)
            sage: total_count = 0
            sage: from collections import defaultdict
            sage: dic = defaultdict(Integer)
            sage: def add_samples(density):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(GF(5), 5, 5, 0)
            ....:         A.randomize(density)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: add_samples(1.0)
            sage: while not all(abs(dic[a]/total_count - 1/5) < 0.01 for a in dic):
            ....:     add_samples(1.0)

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     density_sum += random_matrix(GF(5), 1000, 1000, density=density).density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: expected_density = 1.0 - (999/1000)^500
            sage: expected_density
            0.3936...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5)

        The matrix is updated instead of overwritten::

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = random_matrix(GF(5), 1000, 1000, density=density)
            ....:     A.randomize(density=density, nonzero=True)
            ....:     density_sum += A.density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: expected_density = 1.0 - (999/1000)^1000
            sage: expected_density
            0.6323...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1)
            sage: expected_density = 1.0 - (999/1000)^200
            sage: expected_density
            0.1813...
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.1)"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_dense_template.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2107)

        Return the rank of this matrix.

        EXAMPLES::

            sage: A = random_matrix(GF(3), 100, 100)
            sage: B = copy(A)
            sage: _ = A.rank()
            sage: B == A
            True

            sage: A = random_matrix(GF(3), 100, 100, density=0.01)
            sage: A.transpose().rank() == A.rank()
            True

            sage: A = matrix(GF(3), 100, 100)
            sage: A.rank()
            0

        Rank is not implemented over the integers modulo a composite
        yet.::

            sage: M = matrix(Integers(4), 2, [2,2,2,2])
            sage: M.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        ::

            sage: # needs sage.rings.finite_rings
            sage: while True:
            ....:     A = random_matrix(GF(16007), 100, 100)
            ....:     if A.rank() == 100:
            ....:         break
            sage: B = copy(A)
            sage: A.rank()
            100
            sage: B == A
            True
            sage: MS = A.parent()
            sage: MS(1) == ~A*A
            True

        TESTS::

            sage: A = random_matrix(GF(7), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(7), 0, 1)
            sage: A.rank()
            0

            sage: # needs sage.rings.finite_rings
            sage: A = random_matrix(GF(16007), 0, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 1, 0)
            sage: A.rank()
            0
            sage: A = random_matrix(GF(16007), 0, 1)
            sage: A.rank()
            0"""
    @overload
    def right_kernel_matrix(self, algorithm=..., basis=...) -> Any:
        """Matrix_modn_dense_template.right_kernel_matrix(self, algorithm='linbox', basis='echelon')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1854)

        Return a matrix whose rows form a basis for the right kernel
        of ``self``.

        If the base ring is the ring of integers modulo a composite,
        the keyword arguments are ignored and the computation is
        delegated to :meth:`Matrix_dense.right_kernel_matrix`.

        INPUT:

        - ``algorithm`` -- (default: ``'linbox'``) a parameter that is
          passed on to ``self.echelon_form``, if computation of an echelon
          form is required; see that routine for allowable values

        - ``basis`` -- (default: ``'echelon'``) a keyword that describes the
          format of the basis returned, allowable values are:

          - ``'echelon'``: the basis matrix is in echelon form
          - ``'pivot'``: the basis matrix is such that the submatrix obtained
             by taking the columns that in ``self`` contain no pivots, is the
             identity matrix
          - ``'computed'``: no work is done to transform the basis; in
             the current implementation the result is the negative of
             that returned by ``'pivot'``

        OUTPUT:

        A matrix ``X`` whose rows are a basis for the right kernel of
        ``self``. This means that ``self * X.transpose()`` is a zero matrix.

        The result is not cached, but the routine benefits when ``self`` is
        known to be in echelon form already.

        EXAMPLES::

            sage: M = matrix(GF(5),6,6,range(36))
            sage: M.right_kernel_matrix(basis='computed')
            [4 2 4 0 0 0]
            [3 3 0 4 0 0]
            [2 4 0 0 4 0]
            [1 0 0 0 0 4]
            sage: M.right_kernel_matrix(basis='pivot')
            [1 3 1 0 0 0]
            [2 2 0 1 0 0]
            [3 1 0 0 1 0]
            [4 0 0 0 0 1]
            sage: M.right_kernel_matrix()
            [1 0 0 0 0 4]
            [0 1 0 0 1 3]
            [0 0 1 0 2 2]
            [0 0 0 1 3 1]
            sage: M * M.right_kernel_matrix().transpose()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]"""
    @overload
    def right_kernel_matrix(self, basis=...) -> Any:
        """Matrix_modn_dense_template.right_kernel_matrix(self, algorithm='linbox', basis='echelon')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1854)

        Return a matrix whose rows form a basis for the right kernel
        of ``self``.

        If the base ring is the ring of integers modulo a composite,
        the keyword arguments are ignored and the computation is
        delegated to :meth:`Matrix_dense.right_kernel_matrix`.

        INPUT:

        - ``algorithm`` -- (default: ``'linbox'``) a parameter that is
          passed on to ``self.echelon_form``, if computation of an echelon
          form is required; see that routine for allowable values

        - ``basis`` -- (default: ``'echelon'``) a keyword that describes the
          format of the basis returned, allowable values are:

          - ``'echelon'``: the basis matrix is in echelon form
          - ``'pivot'``: the basis matrix is such that the submatrix obtained
             by taking the columns that in ``self`` contain no pivots, is the
             identity matrix
          - ``'computed'``: no work is done to transform the basis; in
             the current implementation the result is the negative of
             that returned by ``'pivot'``

        OUTPUT:

        A matrix ``X`` whose rows are a basis for the right kernel of
        ``self``. This means that ``self * X.transpose()`` is a zero matrix.

        The result is not cached, but the routine benefits when ``self`` is
        known to be in echelon form already.

        EXAMPLES::

            sage: M = matrix(GF(5),6,6,range(36))
            sage: M.right_kernel_matrix(basis='computed')
            [4 2 4 0 0 0]
            [3 3 0 4 0 0]
            [2 4 0 0 4 0]
            [1 0 0 0 0 4]
            sage: M.right_kernel_matrix(basis='pivot')
            [1 3 1 0 0 0]
            [2 2 0 1 0 0]
            [3 1 0 0 1 0]
            [4 0 0 0 0 1]
            sage: M.right_kernel_matrix()
            [1 0 0 0 0 4]
            [0 1 0 0 1 3]
            [0 0 1 0 2 2]
            [0 0 0 1 3 1]
            sage: M * M.right_kernel_matrix().transpose()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]"""
    @overload
    def right_kernel_matrix(self, basis=...) -> Any:
        """Matrix_modn_dense_template.right_kernel_matrix(self, algorithm='linbox', basis='echelon')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1854)

        Return a matrix whose rows form a basis for the right kernel
        of ``self``.

        If the base ring is the ring of integers modulo a composite,
        the keyword arguments are ignored and the computation is
        delegated to :meth:`Matrix_dense.right_kernel_matrix`.

        INPUT:

        - ``algorithm`` -- (default: ``'linbox'``) a parameter that is
          passed on to ``self.echelon_form``, if computation of an echelon
          form is required; see that routine for allowable values

        - ``basis`` -- (default: ``'echelon'``) a keyword that describes the
          format of the basis returned, allowable values are:

          - ``'echelon'``: the basis matrix is in echelon form
          - ``'pivot'``: the basis matrix is such that the submatrix obtained
             by taking the columns that in ``self`` contain no pivots, is the
             identity matrix
          - ``'computed'``: no work is done to transform the basis; in
             the current implementation the result is the negative of
             that returned by ``'pivot'``

        OUTPUT:

        A matrix ``X`` whose rows are a basis for the right kernel of
        ``self``. This means that ``self * X.transpose()`` is a zero matrix.

        The result is not cached, but the routine benefits when ``self`` is
        known to be in echelon form already.

        EXAMPLES::

            sage: M = matrix(GF(5),6,6,range(36))
            sage: M.right_kernel_matrix(basis='computed')
            [4 2 4 0 0 0]
            [3 3 0 4 0 0]
            [2 4 0 0 4 0]
            [1 0 0 0 0 4]
            sage: M.right_kernel_matrix(basis='pivot')
            [1 3 1 0 0 0]
            [2 2 0 1 0 0]
            [3 1 0 0 1 0]
            [4 0 0 0 0 1]
            sage: M.right_kernel_matrix()
            [1 0 0 0 0 4]
            [0 1 0 0 1 3]
            [0 0 1 0 2 2]
            [0 0 0 1 3 1]
            sage: M * M.right_kernel_matrix().transpose()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]"""
    @overload
    def right_kernel_matrix(self) -> Any:
        """Matrix_modn_dense_template.right_kernel_matrix(self, algorithm='linbox', basis='echelon')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1854)

        Return a matrix whose rows form a basis for the right kernel
        of ``self``.

        If the base ring is the ring of integers modulo a composite,
        the keyword arguments are ignored and the computation is
        delegated to :meth:`Matrix_dense.right_kernel_matrix`.

        INPUT:

        - ``algorithm`` -- (default: ``'linbox'``) a parameter that is
          passed on to ``self.echelon_form``, if computation of an echelon
          form is required; see that routine for allowable values

        - ``basis`` -- (default: ``'echelon'``) a keyword that describes the
          format of the basis returned, allowable values are:

          - ``'echelon'``: the basis matrix is in echelon form
          - ``'pivot'``: the basis matrix is such that the submatrix obtained
             by taking the columns that in ``self`` contain no pivots, is the
             identity matrix
          - ``'computed'``: no work is done to transform the basis; in
             the current implementation the result is the negative of
             that returned by ``'pivot'``

        OUTPUT:

        A matrix ``X`` whose rows are a basis for the right kernel of
        ``self``. This means that ``self * X.transpose()`` is a zero matrix.

        The result is not cached, but the routine benefits when ``self`` is
        known to be in echelon form already.

        EXAMPLES::

            sage: M = matrix(GF(5),6,6,range(36))
            sage: M.right_kernel_matrix(basis='computed')
            [4 2 4 0 0 0]
            [3 3 0 4 0 0]
            [2 4 0 0 4 0]
            [1 0 0 0 0 4]
            sage: M.right_kernel_matrix(basis='pivot')
            [1 3 1 0 0 0]
            [2 2 0 1 0 0]
            [3 1 0 0 1 0]
            [4 0 0 0 0 1]
            sage: M.right_kernel_matrix()
            [1 0 0 0 0 4]
            [0 1 0 0 1 3]
            [0 0 1 0 2 2]
            [0 0 0 1 3 1]
            sage: M * M.right_kernel_matrix().transpose()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]"""
    @overload
    def right_kernel_matrix(self) -> Any:
        """Matrix_modn_dense_template.right_kernel_matrix(self, algorithm='linbox', basis='echelon')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 1854)

        Return a matrix whose rows form a basis for the right kernel
        of ``self``.

        If the base ring is the ring of integers modulo a composite,
        the keyword arguments are ignored and the computation is
        delegated to :meth:`Matrix_dense.right_kernel_matrix`.

        INPUT:

        - ``algorithm`` -- (default: ``'linbox'``) a parameter that is
          passed on to ``self.echelon_form``, if computation of an echelon
          form is required; see that routine for allowable values

        - ``basis`` -- (default: ``'echelon'``) a keyword that describes the
          format of the basis returned, allowable values are:

          - ``'echelon'``: the basis matrix is in echelon form
          - ``'pivot'``: the basis matrix is such that the submatrix obtained
             by taking the columns that in ``self`` contain no pivots, is the
             identity matrix
          - ``'computed'``: no work is done to transform the basis; in
             the current implementation the result is the negative of
             that returned by ``'pivot'``

        OUTPUT:

        A matrix ``X`` whose rows are a basis for the right kernel of
        ``self``. This means that ``self * X.transpose()`` is a zero matrix.

        The result is not cached, but the routine benefits when ``self`` is
        known to be in echelon form already.

        EXAMPLES::

            sage: M = matrix(GF(5),6,6,range(36))
            sage: M.right_kernel_matrix(basis='computed')
            [4 2 4 0 0 0]
            [3 3 0 4 0 0]
            [2 4 0 0 4 0]
            [1 0 0 0 0 4]
            sage: M.right_kernel_matrix(basis='pivot')
            [1 3 1 0 0 0]
            [2 2 0 1 0 0]
            [3 1 0 0 1 0]
            [4 0 0 0 0 1]
            sage: M.right_kernel_matrix()
            [1 0 0 0 0 4]
            [0 1 0 0 1 3]
            [0 0 1 0 2 2]
            [0 0 0 1 3 1]
            sage: M * M.right_kernel_matrix().transpose()
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]
            [0 0 0 0]"""
    def submatrix(self, Py_ssize_trow=..., Py_ssize_tcol=..., Py_ssize_tnrows=..., Py_ssize_tncols=...) -> Any:
        """Matrix_modn_dense_template.submatrix(self, Py_ssize_t row=0, Py_ssize_t col=0, Py_ssize_t nrows=-1, Py_ssize_t ncols=-1)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2969)

        Return the matrix constructed from ``self`` using the specified
        range of rows and columns.

        INPUT:

        - ``row``, ``col`` -- index of the starting row and column;
          indices start at zero

        - ``nrows``, ``ncols`` -- (optional) number of rows and columns to
          take; if not provided, take all rows below and all columns to
          the right of the starting entry

        .. SEEALSO::

            The functions :func:`matrix_from_rows`,
            :func:`matrix_from_columns`, and
            :func:`matrix_from_rows_and_columns` allow one to select
            arbitrary subsets of rows and/or columns.

        EXAMPLES:

        Take the `3 \\times 3` submatrix starting from entry `(1,1)` in a
        `4 \\times 4` matrix::

            sage: m = matrix(GF(17),4, [1..16])
            sage: m.submatrix(1, 1)
            [ 6  7  8]
            [10 11 12]
            [14 15 16]

        Same thing, except take only two rows::

            sage: m.submatrix(1, 1, 2)
            [ 6  7  8]
            [10 11 12]

        And now take only one column::

            sage: m.submatrix(1, 1, 2, 1)
            [ 6]
            [10]

        You can take zero rows or columns if you want::

            sage: m.submatrix(0, 0, 0)
            []
            sage: parent(m.submatrix(0, 0, 0))
            Full MatrixSpace of 0 by 4 dense matrices over Finite Field of size 17"""
    @overload
    def transpose(self) -> Any:
        """Matrix_modn_dense_template.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2783)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that
        the original matrix is not changed. ::

            sage: M = MatrixSpace(GF(41),  2)
            sage: A = M([1,2,3,4])
            sage: B = A.transpose()
            sage: B
            [1 3]
            [2 4]
            sage: A
            [1 2]
            [3 4]

        ``.T`` is a convenient shortcut for the transpose::

           sage: A.T
           [1 3]
           [2 4]

        ::

            sage: A.subdivide(None, 1); A
            [1|2]
            [3|4]
            sage: A.transpose()
            [1 3]
            [---]
            [2 4]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_modn_dense_template.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2783)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that
        the original matrix is not changed. ::

            sage: M = MatrixSpace(GF(41),  2)
            sage: A = M([1,2,3,4])
            sage: B = A.transpose()
            sage: B
            [1 3]
            [2 4]
            sage: A
            [1 2]
            [3 4]

        ``.T`` is a convenient shortcut for the transpose::

           sage: A.T
           [1 3]
           [2 4]

        ::

            sage: A.subdivide(None, 1); A
            [1|2]
            [3|4]
            sage: A.transpose()
            [1 3]
            [---]
            [2 4]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_modn_dense_template.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 2783)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that
        the original matrix is not changed. ::

            sage: M = MatrixSpace(GF(41),  2)
            sage: A = M([1,2,3,4])
            sage: B = A.transpose()
            sage: B
            [1 3]
            [2 4]
            sage: A
            [1 2]
            [3 4]

        ``.T`` is a convenient shortcut for the transpose::

           sage: A.T
           [1 3]
           [2 4]

        ::

            sage: A.subdivide(None, 1); A
            [1|2]
            [3|4]
            sage: A.transpose()
            [1 3]
            [---]
            [2 4]"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """Matrix_modn_dense_template.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 843)

        EXAMPLES::

            sage: A = random_matrix(GF(127), 100, 100)
            sage: copy(A) == A
            True
            sage: copy(A) is A
            False"""
    def __neg__(self) -> Any:
        """Matrix_modn_dense_template.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_dense_template.pxi (starting at line 776)

        EXAMPLES::

            sage: A = matrix(GF(19), 3, 3, range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 8]

            sage: -A
            [ 0 18 17]
            [16 15 14]
            [13 12 11]"""
