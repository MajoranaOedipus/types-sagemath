import sage.matrix.matrix_dense
import sage.matrix.matrix_dense as matrix_dense
from sage.arith.misc import binomial as binomial, previous_prime as previous_prime
from sage.categories.category import ZZ as ZZ
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.matrix.misc_flint import matrix_integer_dense_rational_reconstruction as matrix_integer_dense_rational_reconstruction
from sage.misc.verbose import verbose as verbose
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealNumber as RealNumber
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.proof.proof import get_proof_flag as get_proof_flag
from typing import Any, ClassVar, overload

MAX_MODULUS: int
MAX_MODULUS_modn_dense_double: int
MAX_MODULUS_multi_modular: int
echelon_primes_increment: int
echelon_verbose_level: int

class Matrix_cyclo_dense(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_cyclo_dense(parent, entries=None, copy=None, bool coerce=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 110)

                Initialize a newly created cyclotomic matrix.

                INPUT:

                - ``parent`` -- a matrix space over a cyclotomic number field

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries lie in the base ring

                EXAMPLES:

                This function is called implicitly when you create new
                cyclotomic dense matrices::

                    sage: W.<a> = CyclotomicField(100)
                    sage: A = matrix(2, 3, [1, 1/a, 1-a,a, -2/3*a, a^19])
                    sage: A
                    [                        1 -a^39 + a^29 - a^19 + a^9                    -a + 1]
                    [                        a                    -2/3*a                      a^19]
                    sage: TestSuite(A).run()

                TESTS::

                    sage: matrix(W, 2, 1, a)
                    Traceback (most recent call last):
                    ...
                    TypeError: nonzero scalar matrix must be square

                We call __init__ explicitly below::

                    sage: from sage.matrix.matrix_cyclo_dense import Matrix_cyclo_dense
                    sage: A = Matrix_cyclo_dense.__new__(Matrix_cyclo_dense, MatrixSpace(CyclotomicField(3),2), [0,1,2,3], True, True)
                    sage: A.__init__(MatrixSpace(CyclotomicField(3),2), [0,1,2,3], True, True)
                    sage: A
                    [0 1]
                    [2 3]
        """
    @overload
    def charpoly(self, var=..., algorithm=..., proof=...) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    @overload
    def charpoly(self, algorithm=...) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    @overload
    def charpoly(self, algorithm=...) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    @overload
    def charpoly(self, var=...) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_cyclo_dense.charpoly(self, var='x', algorithm='multimodular', proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1269)

        Return the characteristic polynomial of self, as a polynomial
        over the base ring.

        INPUT:

        - ``algorithm`` -- options:

            - ``'multimodular'`` (default): reduce modulo primes, compute
              charpoly mod p, and lift (very fast)
            - ``'pari'``: use pari (quite slow; comparable to Magma v2.14 though)
            - ``'hessenberg'``: put matrix in Hessenberg form (double dog slow)

        - ``proof`` -- boolean (default: ``None``); proof flag determined by
          global linalg proof

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: a = matrix(K, 3, [1,z,1+z^2, z/3,1,2,3,z^2,1-z])
            sage: f = a.charpoly(); f
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: f(a)
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: a.charpoly(algorithm='pari')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3
            sage: a.charpoly(algorithm='hessenberg')
            x^3 + (z - 3)*x^2 + (-16/3*z^2 - 2*z)*x - 2/3*z^3 + 16/3*z^2 - 5*z + 5/3

            sage: Matrix(K, 1, [0]).charpoly()
            x
            sage: Matrix(K, 1, [5]).charpoly(var='y')
            y - 5

            sage: Matrix(CyclotomicField(13),3).charpoly()
            x^3
            sage: Matrix(CyclotomicField(13),3).charpoly()[2].parent()
            Cyclotomic Field of order 13 and degree 12

        TESTS::

            sage: Matrix(CyclotomicField(10),0).charpoly()
            1"""
    def coefficient_bound(self) -> Any:
        """Matrix_cyclo_dense.coefficient_bound(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 950)

        Return an upper bound for the (complex) absolute values of all
        entries of ``self`` with respect to all embeddings.

        Use ``self.height()`` for a sharper bound.

        This is computed using just the Cauchy-Schwarz inequality, i.e.,
        we use the fact that ::

             \\left| \\sum_i a_i\\zeta^i \\right| \\leq \\sum_i |a_i|,

        as `|\\zeta| = 1`.

        EXAMPLES::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [1+z, 0, 9*z+7, -3 + 4*z]); A
            [  z + 1       0]
            [9*z + 7 4*z - 3]
            sage: A.coefficient_bound()
            16

        The above bound is just `9 + 7`, coming from the lower left entry.
        A better bound would be the following::

            sage: (A[1,0]).abs()
            12.997543663..."""
    @overload
    def denominator(self) -> Any:
        """Matrix_cyclo_dense.denominator(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 932)

        Return the denominator of the entries of this matrix.

        OUTPUT: integer; the smallest integer `d` so that ``d * self`` has
        entries in the ring of integers

        EXAMPLES::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [-2/7,2/3*z+z^2,-z,1+z/19]); A
            [       -2/7 z^2 + 2/3*z]
            [         -z  1/19*z + 1]
            sage: d = A.denominator(); d
            399"""
    @overload
    def denominator(self) -> Any:
        """Matrix_cyclo_dense.denominator(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 932)

        Return the denominator of the entries of this matrix.

        OUTPUT: integer; the smallest integer `d` so that ``d * self`` has
        entries in the ring of integers

        EXAMPLES::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [-2/7,2/3*z+z^2,-z,1+z/19]); A
            [       -2/7 z^2 + 2/3*z]
            [         -z  1/19*z + 1]
            sage: d = A.denominator(); d
            399"""
    def echelon_form(self, *args, **kwargs):
        """Matrix_cyclo_dense.echelon_form(self, algorithm='multimodular', height_guess=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1601)

        Find the echelon form of self, using the specified algorithm.

        The result is cached for each algorithm separately.

        EXAMPLES::

            sage: W.<z> = CyclotomicField(3)
            sage: A = matrix(W, 2, 3, [1+z, 2/3, 9*z+7, -3 + 4*z, z, -7*z]); A
            [  z + 1     2/3 9*z + 7]
            [4*z - 3       z    -7*z]
            sage: A.echelon_form()
            [                  1                   0  -192/97*z - 361/97]
            [                  0                   1 1851/97*z + 1272/97]
            sage: A.echelon_form(algorithm='classical')
            [                  1                   0  -192/97*z - 361/97]
            [                  0                   1 1851/97*z + 1272/97]

        We verify that the result is cached and that the caches are separate::

            sage: A.echelon_form() is A.echelon_form()
            True
            sage: A.echelon_form() is A.echelon_form(algorithm='classical')
            False

        TESTS::

            sage: W.<z> = CyclotomicField(13)
            sage: A = Matrix(W, 2,3, [10^30*(1-z)^13, 1, 2, 3, 4, z])
            sage: B = Matrix(W, 2,3, [(1-z)^13, 1, 2, 3, 4, z])
            sage: A.echelon_form() == A.echelon_form('classical')  # long time (4s on sage.math, 2011)
            True
            sage: B.echelon_form() == B.echelon_form('classical')
            True

        A degenerate case with the degree 1 cyclotomic field::

            sage: A = matrix(CyclotomicField(1),2,3,[1,2,3,4,5,6])
            sage: A.echelon_form()
            [ 1  0 -1]
            [ 0  1  2]

        A case that checks the bug in :issue:`3500`::

            sage: cf4 = CyclotomicField(4) ; z4 = cf4.0
            sage: A = Matrix(cf4, 1, 2, [-z4, 1])
            sage: A.echelon_form()
            [    1 zeta4]

        Verify that the matrix on :issue:`10281` works::

            sage: K.<rho> = CyclotomicField(106)
           sage: coeffs = [(18603/107*rho^51 - 11583/107*rho^50 - 19907/107*rho^49 - 13588/107*rho^48 - 8722/107*rho^47 + 2857/107*rho^46 - 19279/107*rho^45 - 16666/107*rho^44 - 11327/107*rho^43 + 3802/107*rho^42 + 18998/107*rho^41 - 10798/107*rho^40 + 16210/107*rho^39 - 13768/107*rho^38 + 15063/107*rho^37 - 14433/107*rho^36 - 19434/107*rho^35 - 12606/107*rho^34 + 3786/107*rho^33 - 17996/107*rho^32 + 12341/107*rho^31 - 15656/107*rho^30 - 19092/107*rho^29 + 8382/107*rho^28 - 18147/107*rho^27 + 14024/107*rho^26 + 18751/107*rho^25 - 8301/107*rho^24 - 20112/107*rho^23 - 14483/107*rho^22 + 4715/107*rho^21 + 20065/107*rho^20 + 15293/107*rho^19 + 10072/107*rho^18 + 4775/107*rho^17 - 953/107*rho^16 - 19782/107*rho^15 - 16020/107*rho^14 + 5633/107*rho^13 - 17618/107*rho^12 - 18187/107*rho^11 + 7492/107*rho^10 + 19165/107*rho^9 - 9988/107*rho^8 - 20042/107*rho^7 + 10109/107*rho^6 - 17677/107*rho^5 - 17723/107*rho^4 - 12489/107*rho^3 - 6321/107*rho^2 - 4082/107*rho - 1378/107, 1, 4*rho + 1), (0, 1, rho + 4)]
            sage: m = matrix(2, coeffs)
            sage: a = m.echelon_form(algorithm='classical')
            sage: b = m.echelon_form(algorithm='multimodular')  # long time (5s on sage.math, 2012)
            sage: a == b  # long time (depends on previous)
            True"""
    def height(self) -> Any:
        """Matrix_cyclo_dense.height(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 992)

        Return the height of ``self``.

        If we let `a_{ij}` be the `i,j` entry of self, then we define
        the height of ``self`` to be

            `\\max_v \\max_{i,j} |a_{ij}|_v`,

        where `v` runs over all complex embeddings of ``self.base_ring()``.

        EXAMPLES::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [1+z, 0, 9*z+7, -3 + 4*z]); A
            [  z + 1       0]
            [9*z + 7 4*z - 3]
            sage: A.height()
            12.997543663...
            sage: (A[1,0]).abs()
            12.997543663..."""
    @overload
    def randomize(self, density=..., num_bound=..., den_bound=..., distribution=..., nonzero=..., *args, **kwds) -> Any:
        """Matrix_cyclo_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1105)

        Randomize the entries of ``self``.

        Choose rational numbers according to ``distribution``, whose
        numerators are bounded by ``num_bound`` and whose denominators are
        bounded by ``den_bound``.

        EXAMPLES::

            sage: A = Matrix(CyclotomicField(5),2,2,range(4)) ; A
            [0 1]
            [2 3]
            sage: A.randomize()
            sage: A   # random output
            [       1/2*zeta5^2 + zeta5                        1/2]
            [        -zeta5^2 + 2*zeta5 -2*zeta5^3 + 2*zeta5^2 + 2]"""
    @overload
    def randomize(self) -> Any:
        """Matrix_cyclo_dense.randomize(self, density=1, num_bound=2, den_bound=2, distribution=None, nonzero=False, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1105)

        Randomize the entries of ``self``.

        Choose rational numbers according to ``distribution``, whose
        numerators are bounded by ``num_bound`` and whose denominators are
        bounded by ``den_bound``.

        EXAMPLES::

            sage: A = Matrix(CyclotomicField(5),2,2,range(4)) ; A
            [0 1]
            [2 3]
            sage: A.randomize()
            sage: A   # random output
            [       1/2*zeta5^2 + zeta5                        1/2]
            [        -zeta5^2 + 2*zeta5 -2*zeta5^3 + 2*zeta5^2 + 2]"""
    @overload
    def set_immutable(self) -> Any:
        """Matrix_cyclo_dense.set_immutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 878)

        Change this matrix so that it is immutable.

        EXAMPLES::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [1,2/3*z+z^2,-z,1+z/2])
            sage: A[0,0] = 10
            sage: A.set_immutable()
            sage: A[0,0] = 20
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

        Note that there is no function to set a matrix to be mutable
        again, since such a function would violate the whole point.
        Instead make a copy, which is always mutable by default.::

            sage: A.set_mutable()
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense' object has no attribute 'set_mutable'...
            sage: B = A.__copy__()
            sage: B[0,0] = 20
            sage: B[0,0]
            20"""
    @overload
    def set_immutable(self) -> Any:
        """Matrix_cyclo_dense.set_immutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 878)

        Change this matrix so that it is immutable.

        EXAMPLES::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [1,2/3*z+z^2,-z,1+z/2])
            sage: A[0,0] = 10
            sage: A.set_immutable()
            sage: A[0,0] = 20
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).

        Note that there is no function to set a matrix to be mutable
        again, since such a function would violate the whole point.
        Instead make a copy, which is always mutable by default.::

            sage: A.set_mutable()
            Traceback (most recent call last):
            ...
            AttributeError: 'sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense' object has no attribute 'set_mutable'...
            sage: B = A.__copy__()
            sage: B[0,0] = 20
            sage: B[0,0]
            20"""
    def tensor_product(self, A, subdivide=...) -> Any:
        """Matrix_cyclo_dense.tensor_product(self, A, subdivide=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 1916)

        Return the tensor product of two matrices.

        INPUT:

        - ``A`` -- a matrix
        - ``subdivide`` -- boolean (default: ``True``); whether or not to return
          natural subdivisions with the matrix

        OUTPUT:

        Replace each element of ``self`` by a copy of ``A``, but first
        create a scalar multiple of ``A`` by the element it replaces.
        So if ``self`` is an `m\\times n` matrix and ``A`` is a
        `p\\times q` matrix, then the tensor product is an `mp\\times nq`
        matrix.  By default, the matrix will be subdivided into
        submatrices of size `p\\times q`.

        EXAMPLES::

            sage: C = CyclotomicField(12)
            sage: M = matrix.random(C, 3, 3)
            sage: N = matrix.random(C, 50, 50)
            sage: M.tensor_product(M) == super(type(M), M).tensor_product(M)
            True
            sage: N = matrix.random(C, 15, 20)
            sage: M.tensor_product(N) == super(type(M), M).tensor_product(N)
            True

        TESTS::

            sage: Mp = matrix.random(C, 2,3)
            sage: Np = matrix.random(C, 4,5)
            sage: subdiv = super(type(Mp),Mp).tensor_product(Np).subdivisions()
            sage: Mp.tensor_product(Np).subdivisions() == subdiv
            True

        Check that `m \\times 0` and `0 \\times m` matrices work
        (:issue:`22769`)::

            sage: m1 = matrix(C, 1, 0, [])
            sage: m2 = matrix(C, 2, 2, [1, 2, 3, 4])
            sage: m1.tensor_product(m2).dimensions()
            (2, 0)
            sage: m2.tensor_product(m1).dimensions()
            (2, 0)
            sage: m3 = matrix(C, 0, 3, [])
            sage: m3.tensor_product(m2).dimensions()
            (0, 6)
            sage: m2.tensor_product(m3).dimensions()
            (0, 6)"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_cyclo_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 810)

        Make a copy of this matrix.

        EXAMPLES:

        We create a cyclotomic matrix::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [1,2/3*z+z^2,-z,1+z/2])

        We make a copy of A::

            sage: C = A.__copy__()

        We make another reference to A::

            sage: B = A

        Changing this reference changes A itself::

            sage: B[0,0] = 10
            sage: A[0,0]
            10

        Changing the copy does not change A::

            sage: C[0,0] = 20
            sage: C[0,0]
            20
            sage: A[0,0]
            10"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_cyclo_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 810)

        Make a copy of this matrix.

        EXAMPLES:

        We create a cyclotomic matrix::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [1,2/3*z+z^2,-z,1+z/2])

        We make a copy of A::

            sage: C = A.__copy__()

        We make another reference to A::

            sage: B = A

        Changing this reference changes A itself::

            sage: B[0,0] = 10
            sage: A[0,0]
            10

        Changing the copy does not change A::

            sage: C[0,0] = 20
            sage: C[0,0]
            20
            sage: A[0,0]
            10"""
    @overload
    def __neg__(self) -> Any:
        """Matrix_cyclo_dense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 847)

        Return the negative of this matrix.

        OUTPUT: matrix

        EXAMPLES::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [1,2/3*z+z^2,-z,1+z/2])
            sage: -A
            [          -1 -z^2 - 2/3*z]
            [           z   -1/2*z - 1]
            sage: A.__neg__()
            [          -1 -z^2 - 2/3*z]
            [           z   -1/2*z - 1]"""
    @overload
    def __neg__(self) -> Any:
        """Matrix_cyclo_dense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_cyclo_dense.pyx (starting at line 847)

        Return the negative of this matrix.

        OUTPUT: matrix

        EXAMPLES::

            sage: W.<z> = CyclotomicField(5)
            sage: A = matrix(W, 2, 2, [1,2/3*z+z^2,-z,1+z/2])
            sage: -A
            [          -1 -z^2 - 2/3*z]
            [           z   -1/2*z - 1]
            sage: A.__neg__()
            [          -1 -z^2 - 2/3*z]
            [           z   -1/2*z - 1]"""
