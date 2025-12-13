import sage as sage
import sage.matrix.matrix_dense
from sage.categories.category import ZZ as ZZ
from sage.categories.rings import Rings as Rings
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.matrix.matrix2 import decomp_seq as decomp_seq
from sage.misc.verbose import verbose as verbose
from sage.rings.integer_ring import IntegerRing_class as IntegerRing_class
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class MatrixWindow:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class Matrix_rational_dense(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_rational_dense(parent, entries=None, copy=None, bool coerce=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 161)

                INPUT:

                - ``parent`` -- a matrix space over ``QQ``

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries are of type :class:`Rational`

                TESTS::

                    sage: matrix(QQ, 2, 2, 1/4)
                    [1/4   0]
                    [  0 1/4]
                    sage: matrix(QQ, 3, 1, [1/2, -3/4, 0])
                    [ 1/2]
                    [-3/4]
                    [   0]
                    sage: matrix(QQ, 2, 2, 0.5)
                    [1/2   0]
                    [  0 1/2]
        """
    @overload
    def BKZ(self) -> Any:
        """Matrix_rational_dense.BKZ(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2998)

        Return the result of running Block Korkin-Zolotarev reduction on
        ``self`` interpreted as a lattice.

        The arguments ``*args`` and ``**kwargs`` are passed onto
        :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.BKZ`,
        see there for more details.

        EXAMPLES::

            sage: A = Matrix(QQ, 3, 3, [1/n for n in range(1, 10)])
            sage: A.BKZ()
            [ 1/28 -1/40 -1/18]
            [ 1/28 -1/40  1/18]
            [-1/14 -1/40     0]

            sage: A = random_matrix(QQ, 10, 10)
            sage: d = lcm(a.denom() for a in A.list())
            sage: A.BKZ() == (A * d).change_ring(ZZ).BKZ() / d
            True"""
    @overload
    def BKZ(self) -> Any:
        """Matrix_rational_dense.BKZ(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2998)

        Return the result of running Block Korkin-Zolotarev reduction on
        ``self`` interpreted as a lattice.

        The arguments ``*args`` and ``**kwargs`` are passed onto
        :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.BKZ`,
        see there for more details.

        EXAMPLES::

            sage: A = Matrix(QQ, 3, 3, [1/n for n in range(1, 10)])
            sage: A.BKZ()
            [ 1/28 -1/40 -1/18]
            [ 1/28 -1/40  1/18]
            [-1/14 -1/40     0]

            sage: A = random_matrix(QQ, 10, 10)
            sage: d = lcm(a.denom() for a in A.list())
            sage: A.BKZ() == (A * d).change_ring(ZZ).BKZ() / d
            True"""
    @overload
    def BKZ(self, *args, **kwargs) -> Any:
        """Matrix_rational_dense.BKZ(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2998)

        Return the result of running Block Korkin-Zolotarev reduction on
        ``self`` interpreted as a lattice.

        The arguments ``*args`` and ``**kwargs`` are passed onto
        :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.BKZ`,
        see there for more details.

        EXAMPLES::

            sage: A = Matrix(QQ, 3, 3, [1/n for n in range(1, 10)])
            sage: A.BKZ()
            [ 1/28 -1/40 -1/18]
            [ 1/28 -1/40  1/18]
            [-1/14 -1/40     0]

            sage: A = random_matrix(QQ, 10, 10)
            sage: d = lcm(a.denom() for a in A.list())
            sage: A.BKZ() == (A * d).change_ring(ZZ).BKZ() / d
            True"""
    @overload
    def LLL(self) -> Any:
        """Matrix_rational_dense.LLL(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 3023)

        Return an LLL reduced or approximated LLL reduced lattice for
        ``self`` interpreted as a lattice.

        The arguments ``*args`` and ``**kwargs`` are passed onto
        :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL`,
        see there for more details.

        EXAMPLES::

            sage: A = Matrix(QQ, 3, 3, [1/n for n in range(1, 10)])
            sage: A.LLL()
            [ 1/28 -1/40 -1/18]
            [ 1/28 -1/40  1/18]
            [    0 -3/40     0]
            sage: L, U = A.LLL(transformation=True)
            sage: U * A == L
            True

            sage: A = random_matrix(QQ, 10, 10)
            sage: d = lcm(a.denom() for a in A.list())
            sage: A.LLL() == (A * d).change_ring(ZZ).LLL() / d
            True"""
    @overload
    def LLL(self, transformation=...) -> Any:
        """Matrix_rational_dense.LLL(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 3023)

        Return an LLL reduced or approximated LLL reduced lattice for
        ``self`` interpreted as a lattice.

        The arguments ``*args`` and ``**kwargs`` are passed onto
        :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL`,
        see there for more details.

        EXAMPLES::

            sage: A = Matrix(QQ, 3, 3, [1/n for n in range(1, 10)])
            sage: A.LLL()
            [ 1/28 -1/40 -1/18]
            [ 1/28 -1/40  1/18]
            [    0 -3/40     0]
            sage: L, U = A.LLL(transformation=True)
            sage: U * A == L
            True

            sage: A = random_matrix(QQ, 10, 10)
            sage: d = lcm(a.denom() for a in A.list())
            sage: A.LLL() == (A * d).change_ring(ZZ).LLL() / d
            True"""
    @overload
    def LLL(self) -> Any:
        """Matrix_rational_dense.LLL(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 3023)

        Return an LLL reduced or approximated LLL reduced lattice for
        ``self`` interpreted as a lattice.

        The arguments ``*args`` and ``**kwargs`` are passed onto
        :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL`,
        see there for more details.

        EXAMPLES::

            sage: A = Matrix(QQ, 3, 3, [1/n for n in range(1, 10)])
            sage: A.LLL()
            [ 1/28 -1/40 -1/18]
            [ 1/28 -1/40  1/18]
            [    0 -3/40     0]
            sage: L, U = A.LLL(transformation=True)
            sage: U * A == L
            True

            sage: A = random_matrix(QQ, 10, 10)
            sage: d = lcm(a.denom() for a in A.list())
            sage: A.LLL() == (A * d).change_ring(ZZ).LLL() / d
            True"""
    @overload
    def LLL(self, *args, **kwargs) -> Any:
        """Matrix_rational_dense.LLL(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 3023)

        Return an LLL reduced or approximated LLL reduced lattice for
        ``self`` interpreted as a lattice.

        The arguments ``*args`` and ``**kwargs`` are passed onto
        :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL`,
        see there for more details.

        EXAMPLES::

            sage: A = Matrix(QQ, 3, 3, [1/n for n in range(1, 10)])
            sage: A.LLL()
            [ 1/28 -1/40 -1/18]
            [ 1/28 -1/40  1/18]
            [    0 -3/40     0]
            sage: L, U = A.LLL(transformation=True)
            sage: U * A == L
            True

            sage: A = random_matrix(QQ, 10, 10)
            sage: d = lcm(a.denom() for a in A.list())
            sage: A.LLL() == (A * d).change_ring(ZZ).LLL() / d
            True"""
    def add_to_entry(self, Py_ssize_ti, Py_ssize_tj, elt) -> Any:
        """Matrix_rational_dense.add_to_entry(self, Py_ssize_t i, Py_ssize_t j, elt)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 228)

        Add ``elt`` to the entry at position ``(i,j)``.

        EXAMPLES::

            sage: m = matrix(QQ, 2, 2)
            sage: m.add_to_entry(0, 0, -1/3)
            sage: m
            [-1/3    0]
            [   0    0]"""
    @overload
    def antitranspose(self) -> Any:
        """Matrix_rational_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2651)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(QQ,2,3,range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
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
        """Matrix_rational_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2651)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(QQ,2,3,range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
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
        """Matrix_rational_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2651)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(QQ,2,3,range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
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
    def change_ring(self, R) -> Any:
        """Matrix_rational_dense.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1458)

        Create the matrix over R with entries the entries of ``self`` coerced
        into R.

        EXAMPLES::

            sage: a = matrix(QQ,2,[1/2,-1,2,3])
            sage: a.change_ring(GF(3))
            [2 2]
            [2 0]
            sage: a.change_ring(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: matrix has denominators so can...t change to ZZ
            sage: b = a.change_ring(QQ['x']); b
            [1/2  -1]
            [  2   3]
            sage: b.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field

        TESTS:

        Make sure that subdivisions are preserved when changing rings::

            sage: a = matrix(QQ, 3, range(9))
            sage: a.subdivide(2,1); a
            [0|1 2]
            [3|4 5]
            [-+---]
            [6|7 8]
            sage: a.change_ring(ZZ).change_ring(QQ)
            [0|1 2]
            [3|4 5]
            [-+---]
            [6|7 8]
            sage: a.change_ring(GF(3))
            [0|1 2]
            [0|1 2]
            [-+---]
            [0|1 2]"""
    @overload
    def change_ring(self, ZZ) -> Any:
        """Matrix_rational_dense.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1458)

        Create the matrix over R with entries the entries of ``self`` coerced
        into R.

        EXAMPLES::

            sage: a = matrix(QQ,2,[1/2,-1,2,3])
            sage: a.change_ring(GF(3))
            [2 2]
            [2 0]
            sage: a.change_ring(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: matrix has denominators so can...t change to ZZ
            sage: b = a.change_ring(QQ['x']); b
            [1/2  -1]
            [  2   3]
            sage: b.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field

        TESTS:

        Make sure that subdivisions are preserved when changing rings::

            sage: a = matrix(QQ, 3, range(9))
            sage: a.subdivide(2,1); a
            [0|1 2]
            [3|4 5]
            [-+---]
            [6|7 8]
            sage: a.change_ring(ZZ).change_ring(QQ)
            [0|1 2]
            [3|4 5]
            [-+---]
            [6|7 8]
            sage: a.change_ring(GF(3))
            [0|1 2]
            [0|1 2]
            [-+---]
            [0|1 2]"""
    @overload
    def change_ring(self, ZZ, QQ) -> Any:
        """Matrix_rational_dense.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1458)

        Create the matrix over R with entries the entries of ``self`` coerced
        into R.

        EXAMPLES::

            sage: a = matrix(QQ,2,[1/2,-1,2,3])
            sage: a.change_ring(GF(3))
            [2 2]
            [2 0]
            sage: a.change_ring(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: matrix has denominators so can...t change to ZZ
            sage: b = a.change_ring(QQ['x']); b
            [1/2  -1]
            [  2   3]
            sage: b.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Univariate Polynomial Ring in x over Rational Field

        TESTS:

        Make sure that subdivisions are preserved when changing rings::

            sage: a = matrix(QQ, 3, range(9))
            sage: a.subdivide(2,1); a
            [0|1 2]
            [3|4 5]
            [-+---]
            [6|7 8]
            sage: a.change_ring(ZZ).change_ring(QQ)
            [0|1 2]
            [3|4 5]
            [-+---]
            [6|7 8]
            sage: a.change_ring(GF(3))
            [0|1 2]
            [0|1 2]
            [-+---]
            [0|1 2]"""
    def charpoly(self, var=..., algorithm=...) -> Any:
        """Matrix_rational_dense.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1008)

        Return the characteristic polynomial of this matrix.

        .. NOTE::

            The characteristic polynomial is defined as `\\det(xI-A)`.

        INPUT:

        - ``var`` -- (optional) name of the variable as a string

        - ``algorithm`` -- an optional specification of an algorithm. It can be
          one of:

           - ``None``: (default) will use flint for small dimensions and linbox
             otherwise

           - ``'flint'``: uses flint library

           - ``'linbox'``: uses linbox library

           - ``'generic'``: uses Sage generic implementation

        OUTPUT: a polynomial over the rational numbers

        EXAMPLES::

            sage: a = matrix(QQ, 3, [4/3, 2/5, 1/5, 4, -3/2, 0, 0, -2/3, 3/4])
            sage: f = a.charpoly(); f
            x^3 - 7/12*x^2 - 149/40*x + 97/30
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]

        TESTS:

        The cached polynomial should be independent of the ``var``
        argument (:issue:`12292`). We check (indirectly) that the
        second call uses the cached value by noting that its result is
        not cached::

            sage: M = MatrixSpace(QQ, 2)
            sage: A = M(range(0, 2^2))
            sage: type(A)
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
            sage: A.charpoly('x')
            x^2 - 3*x - 2
            sage: A.charpoly('y')
            y^2 - 3*y - 2
            sage: A._cache['charpoly']
            x^2 - 3*x - 2

        Check consistency::

            sage: for _ in range(100):
            ....:     dim = randint(0, 10)
            ....:     m = random_matrix(QQ, dim, num_bound=8, den_bound=8)
            ....:     p_flint = m.charpoly(algorithm='flint'); m._clear_cache()
            ....:     p_linbox = m.charpoly(algorithm='linbox'); m._clear_cache()
            ....:     p_generic = m.charpoly(algorithm='generic')
            ....:     assert p_flint == p_linbox == p_generic"""
    def column(self, Py_ssize_ti, from_list=...) -> Any:
        """Matrix_rational_dense.column(self, Py_ssize_t i, from_list=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2950)

        Return the `i`-th column of this matrix as a dense vector.

        INPUT:

        - ``i`` -- integer

        - ``from_list`` -- ignored

        EXAMPLES::

            sage: m = matrix(QQ, 3, 2, [1/5,-2/3,3/4,4/9,-1,0])
            sage: m.column(1)
            (-2/3, 4/9, 0)
            sage: m.column(1,from_list=True)
            (-2/3, 4/9, 0)
            sage: m.column(-1)
            (-2/3, 4/9, 0)
            sage: m.column(-2)
            (1/5, 3/4, -1)

            sage: m.column(2)
            Traceback (most recent call last):
            ...
            IndexError: column index out of range
            sage: m.column(-3)
            Traceback (most recent call last):
            ...
            IndexError: column index out of range"""
    @overload
    def decomposition(self, is_diagonalizable=..., dual=..., algorithm=..., height_guess=..., proof=...) -> Any:
        """Matrix_rational_dense.decomposition(self, is_diagonalizable=False, dual=False, algorithm=None, height_guess=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1921)

        Return the decomposition of the free module on which this matrix A
        acts from the right (i.e., the action is x goes to x A), along with
        whether this matrix acts irreducibly on each factor. The factors
        are guaranteed to be sorted in the same way as the corresponding
        factors of the characteristic polynomial.

        Let A be the matrix acting from the on the vector space V of column
        vectors. Assume that A is square. This function computes maximal
        subspaces W_1, ..., W_n corresponding to Galois conjugacy classes
        of eigenvalues of A. More precisely, let f(X) be the characteristic
        polynomial of A. This function computes the subspace
        `W_i = ker(g_(A)^n)`, where g_i(X) is an irreducible
        factor of f(X) and g_i(X) exactly divides f(X). If the optional
        parameter is_diagonalizable is True, then we let W_i = ker(g(A)),
        since then we know that ker(g(A)) = `ker(g(A)^n)`.

        If dual is True, also returns the corresponding decomposition of V
        under the action of the transpose of A. The factors are guaranteed
        to correspond.

        INPUT:

        - ``is_diagonalizable`` -- ignored

        - ``dual`` -- whether to also return decompositions for
          the dual

        - ``algorithm`` -- an optional specification of an algorithm

           - ``None`` -- (default) use default algorithm for computing Echelon
             forms

           - 'multimodular': much better if the answers
             factors have small height

        - ``height_guess`` -- positive integer; only used by
          the multimodular algorithm

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          proof.linear_algebra or sage.structure.proof); only used by the
          multimodular algorithm. Note that the Sage global default is
          proof=True.


        .. NOTE::

           IMPORTANT: If you expect that the subspaces in the answer
           are spanned by vectors with small height coordinates, use
           algorithm='multimodular' and height_guess=1; this is
           potentially much faster than the default. If you know for a
           fact the answer will be very small, use
           algorithm='multimodular', height_guess=bound on height,
           proof=False.

        You can get very very fast decomposition with proof=False.

        EXAMPLES::

            sage: a = matrix(QQ,3,[1..9])
            sage: a.decomposition()
            [(Vector space of degree 3 and dimension 1 over Rational Field
              Basis matrix:
              [ 1 -2  1],
              True),
             (Vector space of degree 3 and dimension 2 over Rational Field
              Basis matrix:
              [ 1  0 -1]
              [ 0  1  2],
              True)]"""
    @overload
    def decomposition(self) -> Any:
        """Matrix_rational_dense.decomposition(self, is_diagonalizable=False, dual=False, algorithm=None, height_guess=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1921)

        Return the decomposition of the free module on which this matrix A
        acts from the right (i.e., the action is x goes to x A), along with
        whether this matrix acts irreducibly on each factor. The factors
        are guaranteed to be sorted in the same way as the corresponding
        factors of the characteristic polynomial.

        Let A be the matrix acting from the on the vector space V of column
        vectors. Assume that A is square. This function computes maximal
        subspaces W_1, ..., W_n corresponding to Galois conjugacy classes
        of eigenvalues of A. More precisely, let f(X) be the characteristic
        polynomial of A. This function computes the subspace
        `W_i = ker(g_(A)^n)`, where g_i(X) is an irreducible
        factor of f(X) and g_i(X) exactly divides f(X). If the optional
        parameter is_diagonalizable is True, then we let W_i = ker(g(A)),
        since then we know that ker(g(A)) = `ker(g(A)^n)`.

        If dual is True, also returns the corresponding decomposition of V
        under the action of the transpose of A. The factors are guaranteed
        to correspond.

        INPUT:

        - ``is_diagonalizable`` -- ignored

        - ``dual`` -- whether to also return decompositions for
          the dual

        - ``algorithm`` -- an optional specification of an algorithm

           - ``None`` -- (default) use default algorithm for computing Echelon
             forms

           - 'multimodular': much better if the answers
             factors have small height

        - ``height_guess`` -- positive integer; only used by
          the multimodular algorithm

        - ``proof`` -- boolean or ``None`` (default: ``None``, see
          proof.linear_algebra or sage.structure.proof); only used by the
          multimodular algorithm. Note that the Sage global default is
          proof=True.


        .. NOTE::

           IMPORTANT: If you expect that the subspaces in the answer
           are spanned by vectors with small height coordinates, use
           algorithm='multimodular' and height_guess=1; this is
           potentially much faster than the default. If you know for a
           fact the answer will be very small, use
           algorithm='multimodular', height_guess=bound on height,
           proof=False.

        You can get very very fast decomposition with proof=False.

        EXAMPLES::

            sage: a = matrix(QQ,3,[1..9])
            sage: a.decomposition()
            [(Vector space of degree 3 and dimension 1 over Rational Field
              Basis matrix:
              [ 1 -2  1],
              True),
             (Vector space of degree 3 and dimension 2 over Rational Field
              Basis matrix:
              [ 1  0 -1]
              [ 0  1  2],
              True)]"""
    @overload
    def denominator(self) -> Any:
        """Matrix_rational_dense.denominator(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 919)

        Return the denominator of this matrix.

        OUTPUT: a Sage Integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6)); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.denominator()
            293

            sage: matrix(QQ, 2, [1/2, 1/3, 1/4, 1/5]).denominator()
            60"""
    @overload
    def denominator(self) -> Any:
        """Matrix_rational_dense.denominator(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 919)

        Return the denominator of this matrix.

        OUTPUT: a Sage Integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6)); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.denominator()
            293

            sage: matrix(QQ, 2, [1/2, 1/3, 1/4, 1/5]).denominator()
            60"""
    @overload
    def denominator(self) -> Any:
        """Matrix_rational_dense.denominator(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 919)

        Return the denominator of this matrix.

        OUTPUT: a Sage Integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6)); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.denominator()
            293

            sage: matrix(QQ, 2, [1/2, 1/3, 1/4, 1/5]).denominator()
            60"""
    @overload
    def determinant(self, algorithm=..., proof=...) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def determinant(self) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def determinant(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def determinant(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def determinant(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def determinant(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def determinant(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def determinant(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def determinant(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.determinant(self, algorithm=None, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 794)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'integer\'``: removes denominator and call determinant on the corresponding
             integer matrix

          - ``\'generic\'``: calls the generic Sage implementation

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

        .. NOTE::

           It would be *VERY VERY* hard for det to fail even with
           proof=False.

        EXAMPLES::

            sage: m = matrix(QQ,3,[1,2/3,4/5, 2,2,2, 5,3,2/5])
            sage: m.determinant()
            -34/15
            sage: m.charpoly()
            x^3 - 17/5*x^2 - 122/15*x + 34/15

            sage: m = matrix(QQ, 3, [(1/i)**j for i in range(2,5) for j in range(3)])
            sage: m.determinant(algorithm=\'flint\')
            -1/288

            sage: m = matrix(QQ, 4, [(-1)**n/n for n in range(1,17)])
            sage: m.determinant(algorithm=\'pari\')
            2/70945875

            sage: m = matrix(QQ, 5, [1/(i+j+1) for i in range(5) for j in range(5)])
            sage: m.determinant(algorithm=\'integer\')
            1/266716800000

        On non-square matrices, the method raises a :exc:`ValueError`::

            sage: matrix(QQ, 2, 3).determinant(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'integer\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix
            sage: matrix(QQ, 2, 3).determinant(algorithm=\'generic\')
            Traceback (most recent call last):
            ...
            ValueError: non square matrix

        TESTS:

        Check that the four algorithms agree::

            sage: for _ in range(20):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     det_flint = m.determinant("flint"); m._clear_cache()
            ....:     det_pari = m.determinant("pari"); m._clear_cache()
            ....:     det_int = m.determinant("integer"); m._clear_cache()
            ....:     det_gen = m.determinant("generic")
            ....:     assert det_flint == det_pari == det_int == det_gen'''
    @overload
    def echelon_form(self, algorithm=..., height_guess=..., proof=..., **kwds) -> Any:
        """Matrix_rational_dense.echelon_form(self, algorithm=None, height_guess=None, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1635)

        Return the echelon form of this matrix.

        The (row) echelon form of a matrix, see :wikipedia:`Row_echelon_form`,
        is the matrix obtained by performing Gauss elimination on the rows
        of the matrix.

        INPUT: See :meth:`echelonize` for the options.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelon_form()
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]
            sage: a.echelon_form(algorithm='multimodular')
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        The result is an immutable matrix, so if you want to modify the result
        then you need to make a copy.  This checks that :issue:`10543` is
        fixed.::

            sage: A = matrix(QQ, 2, range(6))
            sage: E = A.echelon_form()
            sage: E.is_mutable()
            False
            sage: F = copy(E)
            sage: F[0,0] = 50
            sage: F
            [50  0 -1]
            [ 0  1  2]

        TESTS:

        Check consistency::

            sage: for _ in range(100):
            ....:     nrows = randint(0, 30)
            ....:     ncols = randint(0, 30)
            ....:     m = random_matrix(QQ, nrows, ncols, num_bound=10, den_bound=10)
            ....:     ech_flint = m.echelon_form('flint'); m._clear_cache()
            ....:     ech_padic = m.echelon_form('padic'); m._clear_cache()
            ....:     ech_multi = m.echelon_form('multimodular'); m._clear_cache()
            ....:     ech_class = m.echelon_form('classical')
            ....:     assert ech_flint == ech_padic == ech_multi == ech_class"""
    @overload
    def echelon_form(self) -> Any:
        """Matrix_rational_dense.echelon_form(self, algorithm=None, height_guess=None, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1635)

        Return the echelon form of this matrix.

        The (row) echelon form of a matrix, see :wikipedia:`Row_echelon_form`,
        is the matrix obtained by performing Gauss elimination on the rows
        of the matrix.

        INPUT: See :meth:`echelonize` for the options.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelon_form()
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]
            sage: a.echelon_form(algorithm='multimodular')
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        The result is an immutable matrix, so if you want to modify the result
        then you need to make a copy.  This checks that :issue:`10543` is
        fixed.::

            sage: A = matrix(QQ, 2, range(6))
            sage: E = A.echelon_form()
            sage: E.is_mutable()
            False
            sage: F = copy(E)
            sage: F[0,0] = 50
            sage: F
            [50  0 -1]
            [ 0  1  2]

        TESTS:

        Check consistency::

            sage: for _ in range(100):
            ....:     nrows = randint(0, 30)
            ....:     ncols = randint(0, 30)
            ....:     m = random_matrix(QQ, nrows, ncols, num_bound=10, den_bound=10)
            ....:     ech_flint = m.echelon_form('flint'); m._clear_cache()
            ....:     ech_padic = m.echelon_form('padic'); m._clear_cache()
            ....:     ech_multi = m.echelon_form('multimodular'); m._clear_cache()
            ....:     ech_class = m.echelon_form('classical')
            ....:     assert ech_flint == ech_padic == ech_multi == ech_class"""
    @overload
    def echelon_form(self, algorithm=...) -> Any:
        """Matrix_rational_dense.echelon_form(self, algorithm=None, height_guess=None, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1635)

        Return the echelon form of this matrix.

        The (row) echelon form of a matrix, see :wikipedia:`Row_echelon_form`,
        is the matrix obtained by performing Gauss elimination on the rows
        of the matrix.

        INPUT: See :meth:`echelonize` for the options.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelon_form()
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]
            sage: a.echelon_form(algorithm='multimodular')
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        The result is an immutable matrix, so if you want to modify the result
        then you need to make a copy.  This checks that :issue:`10543` is
        fixed.::

            sage: A = matrix(QQ, 2, range(6))
            sage: E = A.echelon_form()
            sage: E.is_mutable()
            False
            sage: F = copy(E)
            sage: F[0,0] = 50
            sage: F
            [50  0 -1]
            [ 0  1  2]

        TESTS:

        Check consistency::

            sage: for _ in range(100):
            ....:     nrows = randint(0, 30)
            ....:     ncols = randint(0, 30)
            ....:     m = random_matrix(QQ, nrows, ncols, num_bound=10, den_bound=10)
            ....:     ech_flint = m.echelon_form('flint'); m._clear_cache()
            ....:     ech_padic = m.echelon_form('padic'); m._clear_cache()
            ....:     ech_multi = m.echelon_form('multimodular'); m._clear_cache()
            ....:     ech_class = m.echelon_form('classical')
            ....:     assert ech_flint == ech_padic == ech_multi == ech_class"""
    @overload
    def echelon_form(self) -> Any:
        """Matrix_rational_dense.echelon_form(self, algorithm=None, height_guess=None, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1635)

        Return the echelon form of this matrix.

        The (row) echelon form of a matrix, see :wikipedia:`Row_echelon_form`,
        is the matrix obtained by performing Gauss elimination on the rows
        of the matrix.

        INPUT: See :meth:`echelonize` for the options.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelon_form()
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]
            sage: a.echelon_form(algorithm='multimodular')
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        The result is an immutable matrix, so if you want to modify the result
        then you need to make a copy.  This checks that :issue:`10543` is
        fixed.::

            sage: A = matrix(QQ, 2, range(6))
            sage: E = A.echelon_form()
            sage: E.is_mutable()
            False
            sage: F = copy(E)
            sage: F[0,0] = 50
            sage: F
            [50  0 -1]
            [ 0  1  2]

        TESTS:

        Check consistency::

            sage: for _ in range(100):
            ....:     nrows = randint(0, 30)
            ....:     ncols = randint(0, 30)
            ....:     m = random_matrix(QQ, nrows, ncols, num_bound=10, den_bound=10)
            ....:     ech_flint = m.echelon_form('flint'); m._clear_cache()
            ....:     ech_padic = m.echelon_form('padic'); m._clear_cache()
            ....:     ech_multi = m.echelon_form('multimodular'); m._clear_cache()
            ....:     ech_class = m.echelon_form('classical')
            ....:     assert ech_flint == ech_padic == ech_multi == ech_class"""
    @overload
    def echelonize(self, algorithm=..., height_guess=..., proof=..., **kwds) -> Any:
        '''Matrix_rational_dense.echelonize(self, algorithm=None, height_guess=None, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1532)

        Transform the matrix ``self`` into reduced row echelon form
        in place.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. One of

          - ``None``: (default) try to pick the best choice,

          - ``\'flint\'``: use flint library
            `function <https://flintlib.org/doc/fmpq_mat.html#c.fmpq_mat_rref>`_,
            which automatically chooses between
            `classical algorithm <https://flintlib.org/doc/fmpq_mat.html#c.fmpq_mat_rref_classical>`_
            (Gaussian elimination),
            `fraction-free multimodular <https://flintlib.org/doc/fmpz_mat.html#c.fmpz_mat_rref_mul>`_,
            and `fraction-free LU decomposition <https://flintlib.org/doc/fmpz_mat.html#c.fmpz_mat_rref_fflu>`_,

          - ``\'flint:classical\'``, ``\'flint:multimodular\'``, ``\'flint:fflu\'``: use the
            flint library as above, but select an algorithm explicitly,

          - ``\'padic\'``: an algorithm based on the IML `p`-adic solver,

          - ``\'multimodular\'``: uses a multimodular algorithm implemented in Cython
            that uses linbox modulo many primes,
            see :func:`~sage.matrix.misc.matrix_rational_echelon_form_multimodular`,

          - ``\'classical\'``: just clear each column using Gauss elimination.

        - ``height_guess``, ``**kwds`` -- all passed to the
          ``\'multimodular\'`` algorithm; ignored by other algorithms

        - ``proof`` -- boolean or ``None`` (default: None, see
          proof.linear_algebra or sage.structure.proof). Passed to the
          ``\'multimodular\'`` algorithm. Note that the Sage global default is
          ``proof=True``.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelonize()
            sage: a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        ::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5
            sage: a.echelonize(algorithm=\'multimodular\')
            sage: a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        TESTS:

        Echelonizing a matrix in place throws away the cache of
        the old matrix (:issue:`14506`)::

            sage: for algo in ["flint", "padic", "multimodular", "classical", "flint:classical",
            ....:              "flint:multimodular", "flint:fflu"]:
            ....:      a = Matrix(QQ, [[1,2],[3,4]])
            ....:      _ = a.det()          # fills the cache
            ....:      _ = a._clear_denom() # fills the cache
            ....:      a.echelonize(algorithm=algo)
            ....:      assert sorted(a._cache.keys()) == [\'echelon_form\', \'in_echelon_form\', \'pivots\', \'rank\'], (algo, a._cache.keys())'''
    @overload
    def echelonize(self) -> Any:
        '''Matrix_rational_dense.echelonize(self, algorithm=None, height_guess=None, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1532)

        Transform the matrix ``self`` into reduced row echelon form
        in place.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. One of

          - ``None``: (default) try to pick the best choice,

          - ``\'flint\'``: use flint library
            `function <https://flintlib.org/doc/fmpq_mat.html#c.fmpq_mat_rref>`_,
            which automatically chooses between
            `classical algorithm <https://flintlib.org/doc/fmpq_mat.html#c.fmpq_mat_rref_classical>`_
            (Gaussian elimination),
            `fraction-free multimodular <https://flintlib.org/doc/fmpz_mat.html#c.fmpz_mat_rref_mul>`_,
            and `fraction-free LU decomposition <https://flintlib.org/doc/fmpz_mat.html#c.fmpz_mat_rref_fflu>`_,

          - ``\'flint:classical\'``, ``\'flint:multimodular\'``, ``\'flint:fflu\'``: use the
            flint library as above, but select an algorithm explicitly,

          - ``\'padic\'``: an algorithm based on the IML `p`-adic solver,

          - ``\'multimodular\'``: uses a multimodular algorithm implemented in Cython
            that uses linbox modulo many primes,
            see :func:`~sage.matrix.misc.matrix_rational_echelon_form_multimodular`,

          - ``\'classical\'``: just clear each column using Gauss elimination.

        - ``height_guess``, ``**kwds`` -- all passed to the
          ``\'multimodular\'`` algorithm; ignored by other algorithms

        - ``proof`` -- boolean or ``None`` (default: None, see
          proof.linear_algebra or sage.structure.proof). Passed to the
          ``\'multimodular\'`` algorithm. Note that the Sage global default is
          ``proof=True``.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelonize()
            sage: a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        ::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5
            sage: a.echelonize(algorithm=\'multimodular\')
            sage: a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        TESTS:

        Echelonizing a matrix in place throws away the cache of
        the old matrix (:issue:`14506`)::

            sage: for algo in ["flint", "padic", "multimodular", "classical", "flint:classical",
            ....:              "flint:multimodular", "flint:fflu"]:
            ....:      a = Matrix(QQ, [[1,2],[3,4]])
            ....:      _ = a.det()          # fills the cache
            ....:      _ = a._clear_denom() # fills the cache
            ....:      a.echelonize(algorithm=algo)
            ....:      assert sorted(a._cache.keys()) == [\'echelon_form\', \'in_echelon_form\', \'pivots\', \'rank\'], (algo, a._cache.keys())'''
    @overload
    def echelonize(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.echelonize(self, algorithm=None, height_guess=None, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1532)

        Transform the matrix ``self`` into reduced row echelon form
        in place.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. One of

          - ``None``: (default) try to pick the best choice,

          - ``\'flint\'``: use flint library
            `function <https://flintlib.org/doc/fmpq_mat.html#c.fmpq_mat_rref>`_,
            which automatically chooses between
            `classical algorithm <https://flintlib.org/doc/fmpq_mat.html#c.fmpq_mat_rref_classical>`_
            (Gaussian elimination),
            `fraction-free multimodular <https://flintlib.org/doc/fmpz_mat.html#c.fmpz_mat_rref_mul>`_,
            and `fraction-free LU decomposition <https://flintlib.org/doc/fmpz_mat.html#c.fmpz_mat_rref_fflu>`_,

          - ``\'flint:classical\'``, ``\'flint:multimodular\'``, ``\'flint:fflu\'``: use the
            flint library as above, but select an algorithm explicitly,

          - ``\'padic\'``: an algorithm based on the IML `p`-adic solver,

          - ``\'multimodular\'``: uses a multimodular algorithm implemented in Cython
            that uses linbox modulo many primes,
            see :func:`~sage.matrix.misc.matrix_rational_echelon_form_multimodular`,

          - ``\'classical\'``: just clear each column using Gauss elimination.

        - ``height_guess``, ``**kwds`` -- all passed to the
          ``\'multimodular\'`` algorithm; ignored by other algorithms

        - ``proof`` -- boolean or ``None`` (default: None, see
          proof.linear_algebra or sage.structure.proof). Passed to the
          ``\'multimodular\'`` algorithm. Note that the Sage global default is
          ``proof=True``.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelonize()
            sage: a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        ::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5
            sage: a.echelonize(algorithm=\'multimodular\')
            sage: a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        TESTS:

        Echelonizing a matrix in place throws away the cache of
        the old matrix (:issue:`14506`)::

            sage: for algo in ["flint", "padic", "multimodular", "classical", "flint:classical",
            ....:              "flint:multimodular", "flint:fflu"]:
            ....:      a = Matrix(QQ, [[1,2],[3,4]])
            ....:      _ = a.det()          # fills the cache
            ....:      _ = a._clear_denom() # fills the cache
            ....:      a.echelonize(algorithm=algo)
            ....:      assert sorted(a._cache.keys()) == [\'echelon_form\', \'in_echelon_form\', \'pivots\', \'rank\'], (algo, a._cache.keys())'''
    @overload
    def echelonize(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.echelonize(self, algorithm=None, height_guess=None, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1532)

        Transform the matrix ``self`` into reduced row echelon form
        in place.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. One of

          - ``None``: (default) try to pick the best choice,

          - ``\'flint\'``: use flint library
            `function <https://flintlib.org/doc/fmpq_mat.html#c.fmpq_mat_rref>`_,
            which automatically chooses between
            `classical algorithm <https://flintlib.org/doc/fmpq_mat.html#c.fmpq_mat_rref_classical>`_
            (Gaussian elimination),
            `fraction-free multimodular <https://flintlib.org/doc/fmpz_mat.html#c.fmpz_mat_rref_mul>`_,
            and `fraction-free LU decomposition <https://flintlib.org/doc/fmpz_mat.html#c.fmpz_mat_rref_fflu>`_,

          - ``\'flint:classical\'``, ``\'flint:multimodular\'``, ``\'flint:fflu\'``: use the
            flint library as above, but select an algorithm explicitly,

          - ``\'padic\'``: an algorithm based on the IML `p`-adic solver,

          - ``\'multimodular\'``: uses a multimodular algorithm implemented in Cython
            that uses linbox modulo many primes,
            see :func:`~sage.matrix.misc.matrix_rational_echelon_form_multimodular`,

          - ``\'classical\'``: just clear each column using Gauss elimination.

        - ``height_guess``, ``**kwds`` -- all passed to the
          ``\'multimodular\'`` algorithm; ignored by other algorithms

        - ``proof`` -- boolean or ``None`` (default: None, see
          proof.linear_algebra or sage.structure.proof). Passed to the
          ``\'multimodular\'`` algorithm. Note that the Sage global default is
          ``proof=True``.

        EXAMPLES::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5; a
            [1/19  1/5    2    3]
            [   4    5    6    7]
            [   8    9   10   11]
            [  12   13   14   15]
            sage: a.echelonize()
            sage: a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        ::

            sage: a = matrix(QQ, 4, range(16)); a[0,0] = 1/19; a[0,1] = 1/5
            sage: a.echelonize(algorithm=\'multimodular\')
            sage: a
            [      1       0       0 -76/157]
            [      0       1       0  -5/157]
            [      0       0       1 238/157]
            [      0       0       0       0]

        TESTS:

        Echelonizing a matrix in place throws away the cache of
        the old matrix (:issue:`14506`)::

            sage: for algo in ["flint", "padic", "multimodular", "classical", "flint:classical",
            ....:              "flint:multimodular", "flint:fflu"]:
            ....:      a = Matrix(QQ, [[1,2],[3,4]])
            ....:      _ = a.det()          # fills the cache
            ....:      _ = a._clear_denom() # fills the cache
            ....:      a.echelonize(algorithm=algo)
            ....:      assert sorted(a._cache.keys()) == [\'echelon_form\', \'in_echelon_form\', \'pivots\', \'rank\'], (algo, a._cache.keys())'''
    @overload
    def height(self) -> Any:
        """Matrix_rational_dense.height(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1282)

        Return the height of this matrix, which is the maximum of the
        absolute values of all numerators and denominators of entries in
        this matrix.

        OUTPUT: integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6)); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.height()
            5007"""
    @overload
    def height(self) -> Any:
        """Matrix_rational_dense.height(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1282)

        Return the height of this matrix, which is the maximum of the
        absolute values of all numerators and denominators of entries in
        this matrix.

        OUTPUT: integer

        EXAMPLES::

            sage: b = matrix(QQ,2,range(6)); b[0,0]=-5007/293; b
            [-5007/293         1         2]
            [        3         4         5]
            sage: b.height()
            5007"""
    @overload
    def inverse(self, algorithm=..., check_invertible=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    @overload
    def inverse(self, algorithm=...) -> Any:
        '''Matrix_rational_dense.inverse(self, algorithm=None, check_invertible=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 687)

        Return the inverse of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. It can be one of

          - ``None``: (default) uses flint

          - ``\'flint\'``: uses flint library

          - ``\'pari\'``: uses PARI library

          - ``\'iml\'``: uses IML library

        - ``check_invertible`` -- only used when ``algorithm=iml``; whether to
          check that matrix is invertible

        EXAMPLES::

            sage: a = matrix(QQ,3,[1,2,5,3,2,1,1,1,1,])
            sage: a.inverse()
            [1/2 3/2  -4]
            [ -1  -2   7]
            [1/2 1/2  -2]

            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse(algorithm=\'flint\')
            [-3/82  5/82]
            [17/82 -1/82]
            sage: a.inverse(algorithm=\'flint\')  * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 2, [-1, 5, 12, -3])
            sage: a.inverse(algorithm=\'iml\')
            [1/19 5/57]
            [4/19 1/57]
            sage: a.inverse(algorithm=\'iml\') * a
            [1 0]
            [0 1]

            sage: a = matrix(QQ, 4, primes_first_n(16))
            sage: a.inverse(algorithm=\'pari\')
            [   3/11  -12/55    -1/5    2/11]
            [  -5/11   -2/55    3/10   -3/22]
            [ -13/22 307/440   -1/10   -9/88]
            [  15/22  -37/88       0    7/88]

        On singular matrices this method raises a :exc:`ZeroDivisionError`::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm=\'flint\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'iml\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a.inverse(algorithm=\'pari\')
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        TESTS::

            sage: a = matrix(QQ, 2)
            sage: a.inverse(algorithm="IAmNotAnAlgorithm")
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm \'IAmNotAnAlgorithm\'

            sage: for _ in range(30):
            ....:     dim = randint(1, 20)
            ....:     a = random_matrix(QQ, dim, num_bound=10, den_bound=10)
            ....:     while a.rank() != dim: a = random_matrix(QQ, dim)
            ....:     inv_flint = a.inverse(algorithm=\'flint\')
            ....:     inv_pari = a.inverse(algorithm=\'pari\')
            ....:     inv_iml = a.inverse(algorithm=\'iml\')
            ....:     assert inv_flint == inv_pari == inv_iml'''
    def is_LLL_reduced(self, delta=..., eta=...) -> Any:
        """Matrix_rational_dense.is_LLL_reduced(self, delta=None, eta=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 3054)

        Return ``True`` if this lattice is `(\\delta, \\eta)`-LLL reduced.
        For a definition of LLL reduction, see
        :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL`.

        EXAMPLES::

            sage: A = random_matrix(QQ, 10, 10)
            sage: L = A.LLL()
            sage: A.is_LLL_reduced()
            False
            sage: L.is_LLL_reduced()
            True"""
    def matrix_from_columns(self, columns) -> Any:
        """Matrix_rational_dense.matrix_from_columns(self, columns)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 194)

        Return the matrix constructed from ``self`` using columns with indices
        in the columns list.

        EXAMPLES::

            sage: A = matrix(QQ, 3, range(9))
            sage: A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: A.matrix_from_columns([2,1])
            [2 1]
            [5 4]
            [8 7]
            sage: A.matrix_from_columns((2,1,0,2))
            [2 1 0 2]
            [5 4 3 5]
            [8 7 6 8]"""
    @overload
    def minpoly(self, var=..., algorithm=...) -> Any:
        """Matrix_rational_dense.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1092)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (optional) the variable name as a string (default: ``'x'``)

        - ``algorithm`` -- an optional specification of an algorithm. It can
          be one of

           - ``None``: (default) will use linbox

           - ``'linbox'``: uses the linbox library

           - ``'generic'``: uses the generic Sage implementation

        OUTPUT: a polynomial over the rationals

        EXAMPLES::

            sage: a = matrix(QQ, 3, [4/3, 2/5, 1/5, 4, -3/2, 0, 0, -2/3, 3/4])
            sage: f = a.minpoly(); f
            x^3 - 7/12*x^2 - 149/40*x + 97/30
            sage: a = Mat(ZZ,4)(range(16))
            sage: f = a.minpoly(); f.factor()
            x * (x^2 - 30*x - 80)
            sage: f(a) == 0
            True

        ::

            sage: a = matrix(QQ, 4, [1..4^2])
            sage: factor(a.minpoly())
            x * (x^2 - 34*x - 80)
            sage: factor(a.minpoly('y'))
            y * (y^2 - 34*y - 80)
            sage: factor(a.charpoly())
            x^2 * (x^2 - 34*x - 80)
            sage: b = matrix(QQ, 4, [-1, 2, 2, 0, 0, 4, 2, 2, 0, 0, -1, -2, 0, -4, 0, 4])
            sage: a = matrix(QQ, 4, [1, 1, 0,0, 0,1,0,0, 0,0,5,0, 0,0,0,5])
            sage: c = b^(-1)*a*b
            sage: factor(c.minpoly())
            (x - 5) * (x - 1)^2
            sage: factor(c.charpoly())
            (x - 5)^2 * (x - 1)^2

        Check consistency::

            sage: for _ in range(100):
            ....:     dim = randint(0, 10)
            ....:     m = random_matrix(QQ, dim, num_bound=8, den_bound=8)
            ....:     p_linbox = m.charpoly(algorithm='linbox'); m._clear_cache()
            ....:     p_generic = m.charpoly(algorithm='generic')
            ....:     assert p_linbox == p_generic"""
    @overload
    def minpoly(self) -> Any:
        """Matrix_rational_dense.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1092)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (optional) the variable name as a string (default: ``'x'``)

        - ``algorithm`` -- an optional specification of an algorithm. It can
          be one of

           - ``None``: (default) will use linbox

           - ``'linbox'``: uses the linbox library

           - ``'generic'``: uses the generic Sage implementation

        OUTPUT: a polynomial over the rationals

        EXAMPLES::

            sage: a = matrix(QQ, 3, [4/3, 2/5, 1/5, 4, -3/2, 0, 0, -2/3, 3/4])
            sage: f = a.minpoly(); f
            x^3 - 7/12*x^2 - 149/40*x + 97/30
            sage: a = Mat(ZZ,4)(range(16))
            sage: f = a.minpoly(); f.factor()
            x * (x^2 - 30*x - 80)
            sage: f(a) == 0
            True

        ::

            sage: a = matrix(QQ, 4, [1..4^2])
            sage: factor(a.minpoly())
            x * (x^2 - 34*x - 80)
            sage: factor(a.minpoly('y'))
            y * (y^2 - 34*y - 80)
            sage: factor(a.charpoly())
            x^2 * (x^2 - 34*x - 80)
            sage: b = matrix(QQ, 4, [-1, 2, 2, 0, 0, 4, 2, 2, 0, 0, -1, -2, 0, -4, 0, 4])
            sage: a = matrix(QQ, 4, [1, 1, 0,0, 0,1,0,0, 0,0,5,0, 0,0,0,5])
            sage: c = b^(-1)*a*b
            sage: factor(c.minpoly())
            (x - 5) * (x - 1)^2
            sage: factor(c.charpoly())
            (x - 5)^2 * (x - 1)^2

        Check consistency::

            sage: for _ in range(100):
            ....:     dim = randint(0, 10)
            ....:     m = random_matrix(QQ, dim, num_bound=8, den_bound=8)
            ....:     p_linbox = m.charpoly(algorithm='linbox'); m._clear_cache()
            ....:     p_generic = m.charpoly(algorithm='generic')
            ....:     assert p_linbox == p_generic"""
    @overload
    def minpoly(self) -> Any:
        """Matrix_rational_dense.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1092)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (optional) the variable name as a string (default: ``'x'``)

        - ``algorithm`` -- an optional specification of an algorithm. It can
          be one of

           - ``None``: (default) will use linbox

           - ``'linbox'``: uses the linbox library

           - ``'generic'``: uses the generic Sage implementation

        OUTPUT: a polynomial over the rationals

        EXAMPLES::

            sage: a = matrix(QQ, 3, [4/3, 2/5, 1/5, 4, -3/2, 0, 0, -2/3, 3/4])
            sage: f = a.minpoly(); f
            x^3 - 7/12*x^2 - 149/40*x + 97/30
            sage: a = Mat(ZZ,4)(range(16))
            sage: f = a.minpoly(); f.factor()
            x * (x^2 - 30*x - 80)
            sage: f(a) == 0
            True

        ::

            sage: a = matrix(QQ, 4, [1..4^2])
            sage: factor(a.minpoly())
            x * (x^2 - 34*x - 80)
            sage: factor(a.minpoly('y'))
            y * (y^2 - 34*y - 80)
            sage: factor(a.charpoly())
            x^2 * (x^2 - 34*x - 80)
            sage: b = matrix(QQ, 4, [-1, 2, 2, 0, 0, 4, 2, 2, 0, 0, -1, -2, 0, -4, 0, 4])
            sage: a = matrix(QQ, 4, [1, 1, 0,0, 0,1,0,0, 0,0,5,0, 0,0,0,5])
            sage: c = b^(-1)*a*b
            sage: factor(c.minpoly())
            (x - 5) * (x - 1)^2
            sage: factor(c.charpoly())
            (x - 5)^2 * (x - 1)^2

        Check consistency::

            sage: for _ in range(100):
            ....:     dim = randint(0, 10)
            ....:     m = random_matrix(QQ, dim, num_bound=8, den_bound=8)
            ....:     p_linbox = m.charpoly(algorithm='linbox'); m._clear_cache()
            ....:     p_generic = m.charpoly(algorithm='generic')
            ....:     assert p_linbox == p_generic"""
    @overload
    def minpoly(self) -> Any:
        """Matrix_rational_dense.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1092)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (optional) the variable name as a string (default: ``'x'``)

        - ``algorithm`` -- an optional specification of an algorithm. It can
          be one of

           - ``None``: (default) will use linbox

           - ``'linbox'``: uses the linbox library

           - ``'generic'``: uses the generic Sage implementation

        OUTPUT: a polynomial over the rationals

        EXAMPLES::

            sage: a = matrix(QQ, 3, [4/3, 2/5, 1/5, 4, -3/2, 0, 0, -2/3, 3/4])
            sage: f = a.minpoly(); f
            x^3 - 7/12*x^2 - 149/40*x + 97/30
            sage: a = Mat(ZZ,4)(range(16))
            sage: f = a.minpoly(); f.factor()
            x * (x^2 - 30*x - 80)
            sage: f(a) == 0
            True

        ::

            sage: a = matrix(QQ, 4, [1..4^2])
            sage: factor(a.minpoly())
            x * (x^2 - 34*x - 80)
            sage: factor(a.minpoly('y'))
            y * (y^2 - 34*y - 80)
            sage: factor(a.charpoly())
            x^2 * (x^2 - 34*x - 80)
            sage: b = matrix(QQ, 4, [-1, 2, 2, 0, 0, 4, 2, 2, 0, 0, -1, -2, 0, -4, 0, 4])
            sage: a = matrix(QQ, 4, [1, 1, 0,0, 0,1,0,0, 0,0,5,0, 0,0,0,5])
            sage: c = b^(-1)*a*b
            sage: factor(c.minpoly())
            (x - 5) * (x - 1)^2
            sage: factor(c.charpoly())
            (x - 5)^2 * (x - 1)^2

        Check consistency::

            sage: for _ in range(100):
            ....:     dim = randint(0, 10)
            ....:     m = random_matrix(QQ, dim, num_bound=8, den_bound=8)
            ....:     p_linbox = m.charpoly(algorithm='linbox'); m._clear_cache()
            ....:     p_generic = m.charpoly(algorithm='generic')
            ....:     assert p_linbox == p_generic"""
    @overload
    def minpoly(self) -> Any:
        """Matrix_rational_dense.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1092)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (optional) the variable name as a string (default: ``'x'``)

        - ``algorithm`` -- an optional specification of an algorithm. It can
          be one of

           - ``None``: (default) will use linbox

           - ``'linbox'``: uses the linbox library

           - ``'generic'``: uses the generic Sage implementation

        OUTPUT: a polynomial over the rationals

        EXAMPLES::

            sage: a = matrix(QQ, 3, [4/3, 2/5, 1/5, 4, -3/2, 0, 0, -2/3, 3/4])
            sage: f = a.minpoly(); f
            x^3 - 7/12*x^2 - 149/40*x + 97/30
            sage: a = Mat(ZZ,4)(range(16))
            sage: f = a.minpoly(); f.factor()
            x * (x^2 - 30*x - 80)
            sage: f(a) == 0
            True

        ::

            sage: a = matrix(QQ, 4, [1..4^2])
            sage: factor(a.minpoly())
            x * (x^2 - 34*x - 80)
            sage: factor(a.minpoly('y'))
            y * (y^2 - 34*y - 80)
            sage: factor(a.charpoly())
            x^2 * (x^2 - 34*x - 80)
            sage: b = matrix(QQ, 4, [-1, 2, 2, 0, 0, 4, 2, 2, 0, 0, -1, -2, 0, -4, 0, 4])
            sage: a = matrix(QQ, 4, [1, 1, 0,0, 0,1,0,0, 0,0,5,0, 0,0,0,5])
            sage: c = b^(-1)*a*b
            sage: factor(c.minpoly())
            (x - 5) * (x - 1)^2
            sage: factor(c.charpoly())
            (x - 5)^2 * (x - 1)^2

        Check consistency::

            sage: for _ in range(100):
            ....:     dim = randint(0, 10)
            ....:     m = random_matrix(QQ, dim, num_bound=8, den_bound=8)
            ....:     p_linbox = m.charpoly(algorithm='linbox'); m._clear_cache()
            ....:     p_generic = m.charpoly(algorithm='generic')
            ....:     assert p_linbox == p_generic"""
    def prod_of_row_sums(self, cols) -> Any:
        """Matrix_rational_dense.prod_of_row_sums(self, cols)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 1361)"""
    @overload
    def randomize(self, density=..., num_bound=..., den_bound=..., distribution=..., nonzero=...) -> Any:
        """Matrix_rational_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2273)

        Randomize ``density`` proportion of the entries of this matrix, leaving
        the rest unchanged.

        If ``x`` and ``y`` are given, randomized entries of this matrix have
        numerators and denominators bounded by ``x`` and ``y`` and have
        density 1.

        INPUT:

        - ``density`` -- number between 0 and 1 (default: 1)

        - ``num_bound`` -- numerator bound (default: 2)

        - ``den_bound`` -- denominator bound (default: 2)

        - ``distribution`` -- ``None`` or '1/n' (default: ``None``); if '1/n'
          then ``num_bound``, ``den_bound`` are ignored and numbers are chosen
          using the GMP function ``mpq_randomize_entry_recip_uniform``

        OUTPUT: none; the matrix is modified in-space

        EXAMPLES:

        The default distribution::

            sage: from collections import defaultdict
            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: def add_samples(distribution=None):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(QQ, 2, 4, 0)
            ....:         A.randomize(distribution=distribution)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: expected = {-2: 1/9, -1: 3/18, -1/2: 1/18, 0: 3/9,
            ....:             1/2: 1/18, 1: 3/18, 2: 1/9}
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - expected[a]) < 0.001 for a in dic):
            ....:     add_samples()

        The distribution ``'1/n'``::

            sage: def mpq_randomize_entry_recip_uniform():
            ....:     r = 2*random() - 1
            ....:     if r == 0: r = 1
            ....:     num = int(4/(5*r))
            ....:     r = random()
            ....:     if r == 0: r = 1
            ....:     den = int(1/random())
            ....:     return Integer(num)/Integer(den)

            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: dic2 = defaultdict(Integer)
            sage: add_samples('1/n')
            sage: for _ in range(8):
            ....:     dic2[mpq_randomize_entry_recip_uniform()] += 1
            sage: while not all(abs(dic[a] - dic2[a])/total_count < 0.005 for a in dic):
            ....:     add_samples('1/n')
            ....:     for _ in range(800):
            ....:         dic2[mpq_randomize_entry_recip_uniform()] += 1

        The default can be used to obtain matrices of different rank::

            sage: ranks = [False]*11
            sage: while not all(ranks):
            ....:     for dens in (0.05, 0.1, 0.2, 0.5):
            ....:         A = Matrix(QQ, 10, 10, 0)
            ....:         A.randomize(dens)
            ....:         ranks[A.rank()] = True

        The default density is `6/9`::

            sage: def add_sample(density, num_rows, num_cols):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = Matrix(QQ, num_rows, num_cols, 0)
            ....:     A.randomize(density)
            ....:     density_sum += float(A.density())

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9
            sage: add_sample(1.0, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(1.0, 100, 100)

        The modified density depends on the number of columns::

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*0.5
            sage: add_sample(0.5, 100, 2)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 2)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*(1.0 - (99/100)^50)
            sage: expected_density
            0.263...

            sage: add_sample(0.5, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 100)

        Modifying the bounds for numerator and denominator::

            sage: num_dic = defaultdict(Integer)
            sage: den_dic = defaultdict(Integer)
            sage: while not (all(num_dic[i] for i in range(-200, 201))
            ....:            and all(den_dic[i] for i in range(1, 101))):
            ....:     a = matrix(QQ, 2, 4)
            ....:     a.randomize(num_bound=200, den_bound=100)
            ....:     for q in a.list():
            ....:         num_dic[q.numerator()] += 1
            ....:         den_dic[q.denominator()] += 1
            sage: len(num_dic)
            401
            sage: len(den_dic)
            100

        TESTS:

        Check that the option ``nonzero`` is meaningful (:issue:`22970`)::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: b = a.__copy__()
            sage: b.randomize(nonzero=True)
            sage: a == b
            False
            sage: any(b[i,j].is_zero() for i in range(10) for j in range(10))
            False

        Check that :issue:`34103` is fixed::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: a.randomize(nonzero=True, distribution='1/n')
            sage: bool(a)
            True"""
    @overload
    def randomize(self, distribution=...) -> Any:
        """Matrix_rational_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2273)

        Randomize ``density`` proportion of the entries of this matrix, leaving
        the rest unchanged.

        If ``x`` and ``y`` are given, randomized entries of this matrix have
        numerators and denominators bounded by ``x`` and ``y`` and have
        density 1.

        INPUT:

        - ``density`` -- number between 0 and 1 (default: 1)

        - ``num_bound`` -- numerator bound (default: 2)

        - ``den_bound`` -- denominator bound (default: 2)

        - ``distribution`` -- ``None`` or '1/n' (default: ``None``); if '1/n'
          then ``num_bound``, ``den_bound`` are ignored and numbers are chosen
          using the GMP function ``mpq_randomize_entry_recip_uniform``

        OUTPUT: none; the matrix is modified in-space

        EXAMPLES:

        The default distribution::

            sage: from collections import defaultdict
            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: def add_samples(distribution=None):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(QQ, 2, 4, 0)
            ....:         A.randomize(distribution=distribution)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: expected = {-2: 1/9, -1: 3/18, -1/2: 1/18, 0: 3/9,
            ....:             1/2: 1/18, 1: 3/18, 2: 1/9}
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - expected[a]) < 0.001 for a in dic):
            ....:     add_samples()

        The distribution ``'1/n'``::

            sage: def mpq_randomize_entry_recip_uniform():
            ....:     r = 2*random() - 1
            ....:     if r == 0: r = 1
            ....:     num = int(4/(5*r))
            ....:     r = random()
            ....:     if r == 0: r = 1
            ....:     den = int(1/random())
            ....:     return Integer(num)/Integer(den)

            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: dic2 = defaultdict(Integer)
            sage: add_samples('1/n')
            sage: for _ in range(8):
            ....:     dic2[mpq_randomize_entry_recip_uniform()] += 1
            sage: while not all(abs(dic[a] - dic2[a])/total_count < 0.005 for a in dic):
            ....:     add_samples('1/n')
            ....:     for _ in range(800):
            ....:         dic2[mpq_randomize_entry_recip_uniform()] += 1

        The default can be used to obtain matrices of different rank::

            sage: ranks = [False]*11
            sage: while not all(ranks):
            ....:     for dens in (0.05, 0.1, 0.2, 0.5):
            ....:         A = Matrix(QQ, 10, 10, 0)
            ....:         A.randomize(dens)
            ....:         ranks[A.rank()] = True

        The default density is `6/9`::

            sage: def add_sample(density, num_rows, num_cols):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = Matrix(QQ, num_rows, num_cols, 0)
            ....:     A.randomize(density)
            ....:     density_sum += float(A.density())

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9
            sage: add_sample(1.0, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(1.0, 100, 100)

        The modified density depends on the number of columns::

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*0.5
            sage: add_sample(0.5, 100, 2)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 2)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*(1.0 - (99/100)^50)
            sage: expected_density
            0.263...

            sage: add_sample(0.5, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 100)

        Modifying the bounds for numerator and denominator::

            sage: num_dic = defaultdict(Integer)
            sage: den_dic = defaultdict(Integer)
            sage: while not (all(num_dic[i] for i in range(-200, 201))
            ....:            and all(den_dic[i] for i in range(1, 101))):
            ....:     a = matrix(QQ, 2, 4)
            ....:     a.randomize(num_bound=200, den_bound=100)
            ....:     for q in a.list():
            ....:         num_dic[q.numerator()] += 1
            ....:         den_dic[q.denominator()] += 1
            sage: len(num_dic)
            401
            sage: len(den_dic)
            100

        TESTS:

        Check that the option ``nonzero`` is meaningful (:issue:`22970`)::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: b = a.__copy__()
            sage: b.randomize(nonzero=True)
            sage: a == b
            False
            sage: any(b[i,j].is_zero() for i in range(10) for j in range(10))
            False

        Check that :issue:`34103` is fixed::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: a.randomize(nonzero=True, distribution='1/n')
            sage: bool(a)
            True"""
    @overload
    def randomize(self, dens) -> Any:
        """Matrix_rational_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2273)

        Randomize ``density`` proportion of the entries of this matrix, leaving
        the rest unchanged.

        If ``x`` and ``y`` are given, randomized entries of this matrix have
        numerators and denominators bounded by ``x`` and ``y`` and have
        density 1.

        INPUT:

        - ``density`` -- number between 0 and 1 (default: 1)

        - ``num_bound`` -- numerator bound (default: 2)

        - ``den_bound`` -- denominator bound (default: 2)

        - ``distribution`` -- ``None`` or '1/n' (default: ``None``); if '1/n'
          then ``num_bound``, ``den_bound`` are ignored and numbers are chosen
          using the GMP function ``mpq_randomize_entry_recip_uniform``

        OUTPUT: none; the matrix is modified in-space

        EXAMPLES:

        The default distribution::

            sage: from collections import defaultdict
            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: def add_samples(distribution=None):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(QQ, 2, 4, 0)
            ....:         A.randomize(distribution=distribution)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: expected = {-2: 1/9, -1: 3/18, -1/2: 1/18, 0: 3/9,
            ....:             1/2: 1/18, 1: 3/18, 2: 1/9}
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - expected[a]) < 0.001 for a in dic):
            ....:     add_samples()

        The distribution ``'1/n'``::

            sage: def mpq_randomize_entry_recip_uniform():
            ....:     r = 2*random() - 1
            ....:     if r == 0: r = 1
            ....:     num = int(4/(5*r))
            ....:     r = random()
            ....:     if r == 0: r = 1
            ....:     den = int(1/random())
            ....:     return Integer(num)/Integer(den)

            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: dic2 = defaultdict(Integer)
            sage: add_samples('1/n')
            sage: for _ in range(8):
            ....:     dic2[mpq_randomize_entry_recip_uniform()] += 1
            sage: while not all(abs(dic[a] - dic2[a])/total_count < 0.005 for a in dic):
            ....:     add_samples('1/n')
            ....:     for _ in range(800):
            ....:         dic2[mpq_randomize_entry_recip_uniform()] += 1

        The default can be used to obtain matrices of different rank::

            sage: ranks = [False]*11
            sage: while not all(ranks):
            ....:     for dens in (0.05, 0.1, 0.2, 0.5):
            ....:         A = Matrix(QQ, 10, 10, 0)
            ....:         A.randomize(dens)
            ....:         ranks[A.rank()] = True

        The default density is `6/9`::

            sage: def add_sample(density, num_rows, num_cols):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = Matrix(QQ, num_rows, num_cols, 0)
            ....:     A.randomize(density)
            ....:     density_sum += float(A.density())

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9
            sage: add_sample(1.0, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(1.0, 100, 100)

        The modified density depends on the number of columns::

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*0.5
            sage: add_sample(0.5, 100, 2)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 2)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*(1.0 - (99/100)^50)
            sage: expected_density
            0.263...

            sage: add_sample(0.5, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 100)

        Modifying the bounds for numerator and denominator::

            sage: num_dic = defaultdict(Integer)
            sage: den_dic = defaultdict(Integer)
            sage: while not (all(num_dic[i] for i in range(-200, 201))
            ....:            and all(den_dic[i] for i in range(1, 101))):
            ....:     a = matrix(QQ, 2, 4)
            ....:     a.randomize(num_bound=200, den_bound=100)
            ....:     for q in a.list():
            ....:         num_dic[q.numerator()] += 1
            ....:         den_dic[q.denominator()] += 1
            sage: len(num_dic)
            401
            sage: len(den_dic)
            100

        TESTS:

        Check that the option ``nonzero`` is meaningful (:issue:`22970`)::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: b = a.__copy__()
            sage: b.randomize(nonzero=True)
            sage: a == b
            False
            sage: any(b[i,j].is_zero() for i in range(10) for j in range(10))
            False

        Check that :issue:`34103` is fixed::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: a.randomize(nonzero=True, distribution='1/n')
            sage: bool(a)
            True"""
    @overload
    def randomize(self, density) -> Any:
        """Matrix_rational_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2273)

        Randomize ``density`` proportion of the entries of this matrix, leaving
        the rest unchanged.

        If ``x`` and ``y`` are given, randomized entries of this matrix have
        numerators and denominators bounded by ``x`` and ``y`` and have
        density 1.

        INPUT:

        - ``density`` -- number between 0 and 1 (default: 1)

        - ``num_bound`` -- numerator bound (default: 2)

        - ``den_bound`` -- denominator bound (default: 2)

        - ``distribution`` -- ``None`` or '1/n' (default: ``None``); if '1/n'
          then ``num_bound``, ``den_bound`` are ignored and numbers are chosen
          using the GMP function ``mpq_randomize_entry_recip_uniform``

        OUTPUT: none; the matrix is modified in-space

        EXAMPLES:

        The default distribution::

            sage: from collections import defaultdict
            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: def add_samples(distribution=None):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(QQ, 2, 4, 0)
            ....:         A.randomize(distribution=distribution)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: expected = {-2: 1/9, -1: 3/18, -1/2: 1/18, 0: 3/9,
            ....:             1/2: 1/18, 1: 3/18, 2: 1/9}
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - expected[a]) < 0.001 for a in dic):
            ....:     add_samples()

        The distribution ``'1/n'``::

            sage: def mpq_randomize_entry_recip_uniform():
            ....:     r = 2*random() - 1
            ....:     if r == 0: r = 1
            ....:     num = int(4/(5*r))
            ....:     r = random()
            ....:     if r == 0: r = 1
            ....:     den = int(1/random())
            ....:     return Integer(num)/Integer(den)

            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: dic2 = defaultdict(Integer)
            sage: add_samples('1/n')
            sage: for _ in range(8):
            ....:     dic2[mpq_randomize_entry_recip_uniform()] += 1
            sage: while not all(abs(dic[a] - dic2[a])/total_count < 0.005 for a in dic):
            ....:     add_samples('1/n')
            ....:     for _ in range(800):
            ....:         dic2[mpq_randomize_entry_recip_uniform()] += 1

        The default can be used to obtain matrices of different rank::

            sage: ranks = [False]*11
            sage: while not all(ranks):
            ....:     for dens in (0.05, 0.1, 0.2, 0.5):
            ....:         A = Matrix(QQ, 10, 10, 0)
            ....:         A.randomize(dens)
            ....:         ranks[A.rank()] = True

        The default density is `6/9`::

            sage: def add_sample(density, num_rows, num_cols):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = Matrix(QQ, num_rows, num_cols, 0)
            ....:     A.randomize(density)
            ....:     density_sum += float(A.density())

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9
            sage: add_sample(1.0, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(1.0, 100, 100)

        The modified density depends on the number of columns::

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*0.5
            sage: add_sample(0.5, 100, 2)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 2)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*(1.0 - (99/100)^50)
            sage: expected_density
            0.263...

            sage: add_sample(0.5, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 100)

        Modifying the bounds for numerator and denominator::

            sage: num_dic = defaultdict(Integer)
            sage: den_dic = defaultdict(Integer)
            sage: while not (all(num_dic[i] for i in range(-200, 201))
            ....:            and all(den_dic[i] for i in range(1, 101))):
            ....:     a = matrix(QQ, 2, 4)
            ....:     a.randomize(num_bound=200, den_bound=100)
            ....:     for q in a.list():
            ....:         num_dic[q.numerator()] += 1
            ....:         den_dic[q.denominator()] += 1
            sage: len(num_dic)
            401
            sage: len(den_dic)
            100

        TESTS:

        Check that the option ``nonzero`` is meaningful (:issue:`22970`)::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: b = a.__copy__()
            sage: b.randomize(nonzero=True)
            sage: a == b
            False
            sage: any(b[i,j].is_zero() for i in range(10) for j in range(10))
            False

        Check that :issue:`34103` is fixed::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: a.randomize(nonzero=True, distribution='1/n')
            sage: bool(a)
            True"""
    @overload
    def randomize(self, num_bound=..., den_bound=...) -> Any:
        """Matrix_rational_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2273)

        Randomize ``density`` proportion of the entries of this matrix, leaving
        the rest unchanged.

        If ``x`` and ``y`` are given, randomized entries of this matrix have
        numerators and denominators bounded by ``x`` and ``y`` and have
        density 1.

        INPUT:

        - ``density`` -- number between 0 and 1 (default: 1)

        - ``num_bound`` -- numerator bound (default: 2)

        - ``den_bound`` -- denominator bound (default: 2)

        - ``distribution`` -- ``None`` or '1/n' (default: ``None``); if '1/n'
          then ``num_bound``, ``den_bound`` are ignored and numbers are chosen
          using the GMP function ``mpq_randomize_entry_recip_uniform``

        OUTPUT: none; the matrix is modified in-space

        EXAMPLES:

        The default distribution::

            sage: from collections import defaultdict
            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: def add_samples(distribution=None):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(QQ, 2, 4, 0)
            ....:         A.randomize(distribution=distribution)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: expected = {-2: 1/9, -1: 3/18, -1/2: 1/18, 0: 3/9,
            ....:             1/2: 1/18, 1: 3/18, 2: 1/9}
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - expected[a]) < 0.001 for a in dic):
            ....:     add_samples()

        The distribution ``'1/n'``::

            sage: def mpq_randomize_entry_recip_uniform():
            ....:     r = 2*random() - 1
            ....:     if r == 0: r = 1
            ....:     num = int(4/(5*r))
            ....:     r = random()
            ....:     if r == 0: r = 1
            ....:     den = int(1/random())
            ....:     return Integer(num)/Integer(den)

            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: dic2 = defaultdict(Integer)
            sage: add_samples('1/n')
            sage: for _ in range(8):
            ....:     dic2[mpq_randomize_entry_recip_uniform()] += 1
            sage: while not all(abs(dic[a] - dic2[a])/total_count < 0.005 for a in dic):
            ....:     add_samples('1/n')
            ....:     for _ in range(800):
            ....:         dic2[mpq_randomize_entry_recip_uniform()] += 1

        The default can be used to obtain matrices of different rank::

            sage: ranks = [False]*11
            sage: while not all(ranks):
            ....:     for dens in (0.05, 0.1, 0.2, 0.5):
            ....:         A = Matrix(QQ, 10, 10, 0)
            ....:         A.randomize(dens)
            ....:         ranks[A.rank()] = True

        The default density is `6/9`::

            sage: def add_sample(density, num_rows, num_cols):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = Matrix(QQ, num_rows, num_cols, 0)
            ....:     A.randomize(density)
            ....:     density_sum += float(A.density())

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9
            sage: add_sample(1.0, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(1.0, 100, 100)

        The modified density depends on the number of columns::

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*0.5
            sage: add_sample(0.5, 100, 2)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 2)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*(1.0 - (99/100)^50)
            sage: expected_density
            0.263...

            sage: add_sample(0.5, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 100)

        Modifying the bounds for numerator and denominator::

            sage: num_dic = defaultdict(Integer)
            sage: den_dic = defaultdict(Integer)
            sage: while not (all(num_dic[i] for i in range(-200, 201))
            ....:            and all(den_dic[i] for i in range(1, 101))):
            ....:     a = matrix(QQ, 2, 4)
            ....:     a.randomize(num_bound=200, den_bound=100)
            ....:     for q in a.list():
            ....:         num_dic[q.numerator()] += 1
            ....:         den_dic[q.denominator()] += 1
            sage: len(num_dic)
            401
            sage: len(den_dic)
            100

        TESTS:

        Check that the option ``nonzero`` is meaningful (:issue:`22970`)::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: b = a.__copy__()
            sage: b.randomize(nonzero=True)
            sage: a == b
            False
            sage: any(b[i,j].is_zero() for i in range(10) for j in range(10))
            False

        Check that :issue:`34103` is fixed::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: a.randomize(nonzero=True, distribution='1/n')
            sage: bool(a)
            True"""
    @overload
    def randomize(self, nonzero=...) -> Any:
        """Matrix_rational_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2273)

        Randomize ``density`` proportion of the entries of this matrix, leaving
        the rest unchanged.

        If ``x`` and ``y`` are given, randomized entries of this matrix have
        numerators and denominators bounded by ``x`` and ``y`` and have
        density 1.

        INPUT:

        - ``density`` -- number between 0 and 1 (default: 1)

        - ``num_bound`` -- numerator bound (default: 2)

        - ``den_bound`` -- denominator bound (default: 2)

        - ``distribution`` -- ``None`` or '1/n' (default: ``None``); if '1/n'
          then ``num_bound``, ``den_bound`` are ignored and numbers are chosen
          using the GMP function ``mpq_randomize_entry_recip_uniform``

        OUTPUT: none; the matrix is modified in-space

        EXAMPLES:

        The default distribution::

            sage: from collections import defaultdict
            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: def add_samples(distribution=None):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(QQ, 2, 4, 0)
            ....:         A.randomize(distribution=distribution)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: expected = {-2: 1/9, -1: 3/18, -1/2: 1/18, 0: 3/9,
            ....:             1/2: 1/18, 1: 3/18, 2: 1/9}
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - expected[a]) < 0.001 for a in dic):
            ....:     add_samples()

        The distribution ``'1/n'``::

            sage: def mpq_randomize_entry_recip_uniform():
            ....:     r = 2*random() - 1
            ....:     if r == 0: r = 1
            ....:     num = int(4/(5*r))
            ....:     r = random()
            ....:     if r == 0: r = 1
            ....:     den = int(1/random())
            ....:     return Integer(num)/Integer(den)

            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: dic2 = defaultdict(Integer)
            sage: add_samples('1/n')
            sage: for _ in range(8):
            ....:     dic2[mpq_randomize_entry_recip_uniform()] += 1
            sage: while not all(abs(dic[a] - dic2[a])/total_count < 0.005 for a in dic):
            ....:     add_samples('1/n')
            ....:     for _ in range(800):
            ....:         dic2[mpq_randomize_entry_recip_uniform()] += 1

        The default can be used to obtain matrices of different rank::

            sage: ranks = [False]*11
            sage: while not all(ranks):
            ....:     for dens in (0.05, 0.1, 0.2, 0.5):
            ....:         A = Matrix(QQ, 10, 10, 0)
            ....:         A.randomize(dens)
            ....:         ranks[A.rank()] = True

        The default density is `6/9`::

            sage: def add_sample(density, num_rows, num_cols):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = Matrix(QQ, num_rows, num_cols, 0)
            ....:     A.randomize(density)
            ....:     density_sum += float(A.density())

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9
            sage: add_sample(1.0, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(1.0, 100, 100)

        The modified density depends on the number of columns::

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*0.5
            sage: add_sample(0.5, 100, 2)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 2)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*(1.0 - (99/100)^50)
            sage: expected_density
            0.263...

            sage: add_sample(0.5, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 100)

        Modifying the bounds for numerator and denominator::

            sage: num_dic = defaultdict(Integer)
            sage: den_dic = defaultdict(Integer)
            sage: while not (all(num_dic[i] for i in range(-200, 201))
            ....:            and all(den_dic[i] for i in range(1, 101))):
            ....:     a = matrix(QQ, 2, 4)
            ....:     a.randomize(num_bound=200, den_bound=100)
            ....:     for q in a.list():
            ....:         num_dic[q.numerator()] += 1
            ....:         den_dic[q.denominator()] += 1
            sage: len(num_dic)
            401
            sage: len(den_dic)
            100

        TESTS:

        Check that the option ``nonzero`` is meaningful (:issue:`22970`)::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: b = a.__copy__()
            sage: b.randomize(nonzero=True)
            sage: a == b
            False
            sage: any(b[i,j].is_zero() for i in range(10) for j in range(10))
            False

        Check that :issue:`34103` is fixed::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: a.randomize(nonzero=True, distribution='1/n')
            sage: bool(a)
            True"""
    @overload
    def randomize(self, nonzero=..., distribution=...) -> Any:
        """Matrix_rational_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2273)

        Randomize ``density`` proportion of the entries of this matrix, leaving
        the rest unchanged.

        If ``x`` and ``y`` are given, randomized entries of this matrix have
        numerators and denominators bounded by ``x`` and ``y`` and have
        density 1.

        INPUT:

        - ``density`` -- number between 0 and 1 (default: 1)

        - ``num_bound`` -- numerator bound (default: 2)

        - ``den_bound`` -- denominator bound (default: 2)

        - ``distribution`` -- ``None`` or '1/n' (default: ``None``); if '1/n'
          then ``num_bound``, ``den_bound`` are ignored and numbers are chosen
          using the GMP function ``mpq_randomize_entry_recip_uniform``

        OUTPUT: none; the matrix is modified in-space

        EXAMPLES:

        The default distribution::

            sage: from collections import defaultdict
            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: def add_samples(distribution=None):
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(QQ, 2, 4, 0)
            ....:         A.randomize(distribution=distribution)
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0

            sage: expected = {-2: 1/9, -1: 3/18, -1/2: 1/18, 0: 3/9,
            ....:             1/2: 1/18, 1: 3/18, 2: 1/9}
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - expected[a]) < 0.001 for a in dic):
            ....:     add_samples()

        The distribution ``'1/n'``::

            sage: def mpq_randomize_entry_recip_uniform():
            ....:     r = 2*random() - 1
            ....:     if r == 0: r = 1
            ....:     num = int(4/(5*r))
            ....:     r = random()
            ....:     if r == 0: r = 1
            ....:     den = int(1/random())
            ....:     return Integer(num)/Integer(den)

            sage: total_count = 0
            sage: dic = defaultdict(Integer)
            sage: dic2 = defaultdict(Integer)
            sage: add_samples('1/n')
            sage: for _ in range(8):
            ....:     dic2[mpq_randomize_entry_recip_uniform()] += 1
            sage: while not all(abs(dic[a] - dic2[a])/total_count < 0.005 for a in dic):
            ....:     add_samples('1/n')
            ....:     for _ in range(800):
            ....:         dic2[mpq_randomize_entry_recip_uniform()] += 1

        The default can be used to obtain matrices of different rank::

            sage: ranks = [False]*11
            sage: while not all(ranks):
            ....:     for dens in (0.05, 0.1, 0.2, 0.5):
            ....:         A = Matrix(QQ, 10, 10, 0)
            ....:         A.randomize(dens)
            ....:         ranks[A.rank()] = True

        The default density is `6/9`::

            sage: def add_sample(density, num_rows, num_cols):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = Matrix(QQ, num_rows, num_cols, 0)
            ....:     A.randomize(density)
            ....:     density_sum += float(A.density())

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9
            sage: add_sample(1.0, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(1.0, 100, 100)

        The modified density depends on the number of columns::

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*0.5
            sage: add_sample(0.5, 100, 2)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 2)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: expected_density = 6/9*(1.0 - (99/100)^50)
            sage: expected_density
            0.263...

            sage: add_sample(0.5, 100, 100)
            sage: while abs(density_sum/total_count - expected_density) > 0.001:
            ....:     add_sample(0.5, 100, 100)

        Modifying the bounds for numerator and denominator::

            sage: num_dic = defaultdict(Integer)
            sage: den_dic = defaultdict(Integer)
            sage: while not (all(num_dic[i] for i in range(-200, 201))
            ....:            and all(den_dic[i] for i in range(1, 101))):
            ....:     a = matrix(QQ, 2, 4)
            ....:     a.randomize(num_bound=200, den_bound=100)
            ....:     for q in a.list():
            ....:         num_dic[q.numerator()] += 1
            ....:         den_dic[q.denominator()] += 1
            sage: len(num_dic)
            401
            sage: len(den_dic)
            100

        TESTS:

        Check that the option ``nonzero`` is meaningful (:issue:`22970`)::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: b = a.__copy__()
            sage: b.randomize(nonzero=True)
            sage: a == b
            False
            sage: any(b[i,j].is_zero() for i in range(10) for j in range(10))
            False

        Check that :issue:`34103` is fixed::

            sage: a = matrix(QQ, 10, 10, 1)
            sage: a.randomize(nonzero=True, distribution='1/n')
            sage: bool(a)
            True"""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_rational_dense.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2540)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. One of

          - ``None`` -- (default) will use flint

          - ``'flint'`` -- uses the flint library

          - ``'pari'`` -- uses the PARI library

          - ``'integer'`` -- eliminate denominators and calls the rank function
            on the corresponding integer matrix

        EXAMPLES::

            sage: matrix(QQ,3,[1..9]).rank()
            2
            sage: matrix(QQ,100,[1..100^2]).rank()
            2

        TESTS::

            sage: for _ in range(100):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=2, density=0.5)
            ....:     r_pari = m.rank('pari'); m._clear_cache()
            ....:     r_flint = m.rank('flint'); m._clear_cache()
            ....:     r_int = m.rank('integer'); m._clear_cache()
            ....:     assert r_pari == r_flint == r_int"""
    @overload
    def rank(self) -> Any:
        """Matrix_rational_dense.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2540)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. One of

          - ``None`` -- (default) will use flint

          - ``'flint'`` -- uses the flint library

          - ``'pari'`` -- uses the PARI library

          - ``'integer'`` -- eliminate denominators and calls the rank function
            on the corresponding integer matrix

        EXAMPLES::

            sage: matrix(QQ,3,[1..9]).rank()
            2
            sage: matrix(QQ,100,[1..100^2]).rank()
            2

        TESTS::

            sage: for _ in range(100):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=2, density=0.5)
            ....:     r_pari = m.rank('pari'); m._clear_cache()
            ....:     r_flint = m.rank('flint'); m._clear_cache()
            ....:     r_int = m.rank('integer'); m._clear_cache()
            ....:     assert r_pari == r_flint == r_int"""
    @overload
    def rank(self) -> Any:
        """Matrix_rational_dense.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2540)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- an optional specification of an algorithm. One of

          - ``None`` -- (default) will use flint

          - ``'flint'`` -- uses the flint library

          - ``'pari'`` -- uses the PARI library

          - ``'integer'`` -- eliminate denominators and calls the rank function
            on the corresponding integer matrix

        EXAMPLES::

            sage: matrix(QQ,3,[1..9]).rank()
            2
            sage: matrix(QQ,100,[1..100^2]).rank()
            2

        TESTS::

            sage: for _ in range(100):
            ....:     dim = randint(0, 30)
            ....:     m = random_matrix(QQ, dim, num_bound=2, density=0.5)
            ....:     r_pari = m.rank('pari'); m._clear_cache()
            ....:     r_flint = m.rank('flint'); m._clear_cache()
            ....:     r_int = m.rank('integer'); m._clear_cache()
            ....:     assert r_pari == r_flint == r_int"""
    def row(self, Py_ssize_ti, from_list=...) -> Any:
        """Matrix_rational_dense.row(self, Py_ssize_t i, from_list=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2906)

        Return the `i`-th row of this matrix as a dense vector.

        INPUT:

        - ``i`` -- integer

        - ``from_list`` -- ignored

        EXAMPLES::

            sage: m = matrix(QQ, 2, [1/5, -2/3, 3/4, 4/9])
            sage: m.row(0)
            (1/5, -2/3)
            sage: m.row(1)
            (3/4, 4/9)
            sage: m.row(1, from_list=True)
            (3/4, 4/9)
            sage: m.row(-2)
            (1/5, -2/3)

            sage: m.row(2)
            Traceback (most recent call last):
            ...
            IndexError: row index out of range
            sage: m.row(-3)
            Traceback (most recent call last):
            ...
            IndexError: row index out of range"""
    def set_row_to_multiple_of_row(self, Py_ssize_ti, Py_ssize_tj, s) -> Any:
        """Matrix_rational_dense.set_row_to_multiple_of_row(self, Py_ssize_t i, Py_ssize_t j, s)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2705)

        Set row i equal to s times row j.

        EXAMPLES::

            sage: a = matrix(QQ,2,3,range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.set_row_to_multiple_of_row(1,0,-3)
            sage: a
            [ 0  1  2]
            [ 0 -3 -6]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_rational_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2595)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that the
        original matrix is not changed.

        ::

            sage: A = matrix(QQ, 2, 3, range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
            sage: B = A.transpose()
            sage: print(B)
            [0 3]
            [1 4]
            [2 5]
            sage: print(A)
            [0 1 2]
            [3 4 5]

        ``.T`` is a convenient shortcut for the transpose::

            sage: print(A.T)
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
        """Matrix_rational_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2595)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that the
        original matrix is not changed.

        ::

            sage: A = matrix(QQ, 2, 3, range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
            sage: B = A.transpose()
            sage: print(B)
            [0 3]
            [1 4]
            [2 5]
            sage: print(A)
            [0 1 2]
            [3 4 5]

        ``.T`` is a convenient shortcut for the transpose::

            sage: print(A.T)
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
        """Matrix_rational_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2595)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that the
        original matrix is not changed.

        ::

            sage: A = matrix(QQ, 2, 3, range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
            sage: B = A.transpose()
            sage: print(B)
            [0 3]
            [1 4]
            [2 5]
            sage: print(A)
            [0 1 2]
            [3 4 5]

        ``.T`` is a convenient shortcut for the transpose::

            sage: print(A.T)
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
    def __copy__(self) -> Any:
        """Matrix_rational_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 603)

        Copy a matrix over QQ.

        TESTS::

            sage: a = matrix(QQ, 3, [1/n for n in range(1,10)])
            sage: b = a.__copy__()
            sage: a == b
            True
            sage: a is b
            False
            sage: b[0,0] = 5
            sage: a == b
            False

            sage: a.subdivide(2, 1)
            sage: b = a.__copy__()
            sage: b.subdivisions()
            ([2], [1])
            sage: a.subdivide(2, 2)
            sage: b.subdivisions()
            ([2], [1])"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_rational_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 603)

        Copy a matrix over QQ.

        TESTS::

            sage: a = matrix(QQ, 3, [1/n for n in range(1,10)])
            sage: b = a.__copy__()
            sage: a == b
            True
            sage: a is b
            False
            sage: b[0,0] = 5
            sage: a == b
            False

            sage: a.subdivide(2, 1)
            sage: b = a.__copy__()
            sage: b.subdivisions()
            ([2], [1])
            sage: a.subdivide(2, 2)
            sage: b.subdivisions()
            ([2], [1])"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_rational_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 603)

        Copy a matrix over QQ.

        TESTS::

            sage: a = matrix(QQ, 3, [1/n for n in range(1,10)])
            sage: b = a.__copy__()
            sage: a == b
            True
            sage: a is b
            False
            sage: b[0,0] = 5
            sage: a == b
            False

            sage: a.subdivide(2, 1)
            sage: b = a.__copy__()
            sage: b.subdivisions()
            ([2], [1])
            sage: a.subdivide(2, 2)
            sage: b.subdivisions()
            ([2], [1])"""
    def __invert__(self) -> Any:
        """Matrix_rational_dense.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 645)

        EXAMPLES::

            sage: a = matrix(QQ,3,range(9))
            sage: a.inverse()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular
            sage: a = matrix(QQ, 2, [1, 5, 17, 3])
            sage: a.inverse()
            [-3/82  5/82]
            [17/82 -1/82]
            sage: ~matrix(QQ, 2, 3)
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be a square matrix"""
    def __neg__(self) -> Any:
        """Matrix_rational_dense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 586)

        Negate a matrix over QQ.

        EXAMPLES::

            sage: a = matrix(QQ, 3, [1/n for n in range(1,10)])
            sage: -a
            [  -1 -1/2 -1/3]
            [-1/4 -1/5 -1/6]
            [-1/7 -1/8 -1/9]"""
    @overload
    def __pari__(self) -> Any:
        """Matrix_rational_dense.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2800)

        Return pari version of this matrix.

        EXAMPLES::

            sage: matrix(QQ,2,[1/5,-2/3,3/4,4/9]).__pari__()
            [1/5, -2/3; 3/4, 4/9]"""
    @overload
    def __pari__(self) -> Any:
        """Matrix_rational_dense.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_rational_dense.pyx (starting at line 2800)

        Return pari version of this matrix.

        EXAMPLES::

            sage: matrix(QQ,2,[1/5,-2/3,3/4,4/9]).__pari__()
            [1/5, -2/3; 3/4, 4/9]"""
