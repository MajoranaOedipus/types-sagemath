import sage as sage
import sage.matrix.matrix2
from sage.categories.rings import Rings as Rings
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class Matrix_sparse(sage.matrix.matrix2.Matrix):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def antitranspose(self) -> Any:
        """Matrix_sparse.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 441)

        Return the antitranspose of ``self``, without changing ``self``.

        This is the mirror image along the other diagonal.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, sparse=True)
            sage: A = M([1,2,3,4]); A
            [1 2]
            [3 4]
            sage: A.antitranspose()
            [4 2]
            [3 1]

        .. SEEALSO:: :meth:`transpose`"""
    @overload
    def antitranspose(self) -> Any:
        """Matrix_sparse.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 441)

        Return the antitranspose of ``self``, without changing ``self``.

        This is the mirror image along the other diagonal.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, sparse=True)
            sage: A = M([1,2,3,4]); A
            [1 2]
            [3 4]
            sage: A.antitranspose()
            [4 2]
            [3 1]

        .. SEEALSO:: :meth:`transpose`"""
    @overload
    def apply_map(self, phi, R=..., sparse=...) -> Any:
        """Matrix_sparse.apply_map(self, phi, R=None, sparse=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 648)

        Apply the given map ``phi`` (an arbitrary Python function or callable
        object) to this matrix.

        If ``R`` is not given, automatically determine the base ring
        of the resulting matrix.

        INPUT:

        - ``phi`` -- arbitrary Python function or callable object

        - ``R`` -- (optional) ring

        - ``sparse`` -- boolean (default: ``True``); whether to return
          a sparse or a dense matrix

        OUTPUT: a matrix over ``R``

        EXAMPLES::

            sage: m = matrix(ZZ, 10000, {(1,2): 17}, sparse=True)

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: f = lambda x: k(x)
            sage: n = m.apply_map(f)
            sage: n.parent()
            Full MatrixSpace of 10000 by 10000 sparse matrices
             over Finite Field in a of size 3^2
            sage: n[1, 2]
            2

        An example where the codomain is explicitly specified.

        ::

            sage: n = m.apply_map(lambda x: x%3, GF(3))
            sage: n.parent()
            Full MatrixSpace of 10000 by 10000 sparse matrices
             over Finite Field of size 3
            sage: n[1, 2]
            2

        If we did not specify the codomain, the resulting matrix in the
        above case ends up over `\\ZZ` again::

            sage: n = m.apply_map(lambda x: x%3)
            sage: n.parent()
            Full MatrixSpace of 10000 by 10000 sparse matrices over Integer Ring
            sage: n[1, 2]
            2

        If ``self`` is subdivided, the result will be as well::

            sage: m = matrix(2, 2, [0, 0, 3, 0])
            sage: m.subdivide(None, 1); m
            [0|0]
            [3|0]
            sage: m.apply_map(lambda x: x*x)
            [0|0]
            [9|0]

        If the map sends zero to a nonzero value, then it may be useful to
        get the result as a dense matrix.

        ::

            sage: m = matrix(ZZ, 3, 3, [0] * 7 + [1,2], sparse=True); m
            [0 0 0]
            [0 0 0]
            [0 1 2]
            sage: parent(m)
            Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring
            sage: n = m.apply_map(lambda x: x+polygen(QQ), sparse=False); n
            [    x     x     x]
            [    x     x     x]
            [    x x + 1 x + 2]
            sage: parent(n)
            Full MatrixSpace of 3 by 3 dense matrices over Univariate Polynomial Ring in x over Rational Field

        TESTS::

            sage: m = matrix([], sparse=True)
            sage: m.apply_map(lambda x: x*x) == m
            True

            sage: m.apply_map(lambda x: x*x, sparse=False).parent()
            Full MatrixSpace of 0 by 0 dense matrices over Integer Ring

        Check that we do not unnecessarily apply phi to 0 in the sparse case::

            sage: m = matrix(QQ, 2, 2, range(1, 5), sparse=True)
            sage: m.apply_map(lambda x: 1/x)
            [  1 1/2]
            [1/3 1/4]

        Test subdivisions when phi maps 0 to nonzero::

            sage: m = matrix(2, 2, [0, 0, 3, 0])
            sage: m.subdivide(None, 1); m
            [0|0]
            [3|0]
            sage: m.apply_map(lambda x: x+1)
            [1|1]
            [4|1]

        When applying a map to a sparse zero matrix, the codomain is determined
        from the image of zero (:issue:`29214`)::

            sage: matrix(RR, 2, 2, sparse=True).apply_map(floor).base_ring() is ZZ
            True"""
    @overload
    def apply_map(self, f) -> Any:
        """Matrix_sparse.apply_map(self, phi, R=None, sparse=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 648)

        Apply the given map ``phi`` (an arbitrary Python function or callable
        object) to this matrix.

        If ``R`` is not given, automatically determine the base ring
        of the resulting matrix.

        INPUT:

        - ``phi`` -- arbitrary Python function or callable object

        - ``R`` -- (optional) ring

        - ``sparse`` -- boolean (default: ``True``); whether to return
          a sparse or a dense matrix

        OUTPUT: a matrix over ``R``

        EXAMPLES::

            sage: m = matrix(ZZ, 10000, {(1,2): 17}, sparse=True)

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: f = lambda x: k(x)
            sage: n = m.apply_map(f)
            sage: n.parent()
            Full MatrixSpace of 10000 by 10000 sparse matrices
             over Finite Field in a of size 3^2
            sage: n[1, 2]
            2

        An example where the codomain is explicitly specified.

        ::

            sage: n = m.apply_map(lambda x: x%3, GF(3))
            sage: n.parent()
            Full MatrixSpace of 10000 by 10000 sparse matrices
             over Finite Field of size 3
            sage: n[1, 2]
            2

        If we did not specify the codomain, the resulting matrix in the
        above case ends up over `\\ZZ` again::

            sage: n = m.apply_map(lambda x: x%3)
            sage: n.parent()
            Full MatrixSpace of 10000 by 10000 sparse matrices over Integer Ring
            sage: n[1, 2]
            2

        If ``self`` is subdivided, the result will be as well::

            sage: m = matrix(2, 2, [0, 0, 3, 0])
            sage: m.subdivide(None, 1); m
            [0|0]
            [3|0]
            sage: m.apply_map(lambda x: x*x)
            [0|0]
            [9|0]

        If the map sends zero to a nonzero value, then it may be useful to
        get the result as a dense matrix.

        ::

            sage: m = matrix(ZZ, 3, 3, [0] * 7 + [1,2], sparse=True); m
            [0 0 0]
            [0 0 0]
            [0 1 2]
            sage: parent(m)
            Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring
            sage: n = m.apply_map(lambda x: x+polygen(QQ), sparse=False); n
            [    x     x     x]
            [    x     x     x]
            [    x x + 1 x + 2]
            sage: parent(n)
            Full MatrixSpace of 3 by 3 dense matrices over Univariate Polynomial Ring in x over Rational Field

        TESTS::

            sage: m = matrix([], sparse=True)
            sage: m.apply_map(lambda x: x*x) == m
            True

            sage: m.apply_map(lambda x: x*x, sparse=False).parent()
            Full MatrixSpace of 0 by 0 dense matrices over Integer Ring

        Check that we do not unnecessarily apply phi to 0 in the sparse case::

            sage: m = matrix(QQ, 2, 2, range(1, 5), sparse=True)
            sage: m.apply_map(lambda x: 1/x)
            [  1 1/2]
            [1/3 1/4]

        Test subdivisions when phi maps 0 to nonzero::

            sage: m = matrix(2, 2, [0, 0, 3, 0])
            sage: m.subdivide(None, 1); m
            [0|0]
            [3|0]
            sage: m.apply_map(lambda x: x+1)
            [1|1]
            [4|1]

        When applying a map to a sparse zero matrix, the codomain is determined
        from the image of zero (:issue:`29214`)::

            sage: matrix(RR, 2, 2, sparse=True).apply_map(floor).base_ring() is ZZ
            True"""
    @overload
    def apply_morphism(self, phi) -> Any:
        """Matrix_sparse.apply_morphism(self, phi)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 617)

        Apply the morphism ``phi`` to the coefficients of this sparse matrix.

        The resulting matrix is over the codomain of ``phi``.

        INPUT:

        - ``phi`` -- a morphism, so ``phi`` is callable and
           ``phi.domain()`` and ``phi.codomain()`` are defined. The
           codomain must be a ring.

        OUTPUT: a matrix over the codomain of ``phi``

        EXAMPLES::

            sage: m = matrix(ZZ, 3, range(9), sparse=True)
            sage: phi = ZZ.hom(GF(5))
            sage: m.apply_morphism(phi)
            [0 1 2]
            [3 4 0]
            [1 2 3]
            sage: m.apply_morphism(phi).parent()
            Full MatrixSpace of 3 by 3 sparse matrices
             over Finite Field of size 5"""
    @overload
    def apply_morphism(self, phi) -> Any:
        """Matrix_sparse.apply_morphism(self, phi)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 617)

        Apply the morphism ``phi`` to the coefficients of this sparse matrix.

        The resulting matrix is over the codomain of ``phi``.

        INPUT:

        - ``phi`` -- a morphism, so ``phi`` is callable and
           ``phi.domain()`` and ``phi.codomain()`` are defined. The
           codomain must be a ring.

        OUTPUT: a matrix over the codomain of ``phi``

        EXAMPLES::

            sage: m = matrix(ZZ, 3, range(9), sparse=True)
            sage: phi = ZZ.hom(GF(5))
            sage: m.apply_morphism(phi)
            [0 1 2]
            [3 4 0]
            [1 2 3]
            sage: m.apply_morphism(phi).parent()
            Full MatrixSpace of 3 by 3 sparse matrices
             over Finite Field of size 5"""
    @overload
    def apply_morphism(self, phi) -> Any:
        """Matrix_sparse.apply_morphism(self, phi)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 617)

        Apply the morphism ``phi`` to the coefficients of this sparse matrix.

        The resulting matrix is over the codomain of ``phi``.

        INPUT:

        - ``phi`` -- a morphism, so ``phi`` is callable and
           ``phi.domain()`` and ``phi.codomain()`` are defined. The
           codomain must be a ring.

        OUTPUT: a matrix over the codomain of ``phi``

        EXAMPLES::

            sage: m = matrix(ZZ, 3, range(9), sparse=True)
            sage: phi = ZZ.hom(GF(5))
            sage: m.apply_morphism(phi)
            [0 1 2]
            [3 4 0]
            [1 2 3]
            sage: m.apply_morphism(phi).parent()
            Full MatrixSpace of 3 by 3 sparse matrices
             over Finite Field of size 5"""
    @overload
    def augment(self, right, subdivide=...) -> Any:
        """Matrix_sparse.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 1048)

        Return the augmented matrix of the form::

            [self | right].

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, 2, sparse=True)
            sage: A = M([1,2, 3,4])
            sage: A
            [1 2]
            [3 4]
            sage: N = MatrixSpace(QQ, 2, 1, sparse=True)
            sage: B = N([9,8])
            sage: B
            [9]
            [8]
            sage: A.augment(B)
            [1 2 9]
            [3 4 8]
            sage: B.augment(A)
            [9 1 2]
            [8 3 4]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(QQ, 3, 4, range(12), sparse=True)
            sage: v = vector(QQ, 3, range(3), sparse=True)
            sage: A.augment(v)
            [ 0  1  2  3  0]
            [ 4  5  6  7  1]
            [ 8  9 10 11  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(QQ, 3, 5, range(15), sparse=True)
            sage: B = matrix(QQ, 3, 3, range(9), sparse=True)
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        TESTS:

        Verify that :issue:`12689` is fixed::

            sage: A = identity_matrix(QQ, 2, sparse=True)
            sage: B = identity_matrix(ZZ, 2, sparse=True)
            sage: A.augment(B)
            [1 0 1 0]
            [0 1 0 1]"""
    @overload
    def augment(self, B) -> Any:
        """Matrix_sparse.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 1048)

        Return the augmented matrix of the form::

            [self | right].

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, 2, sparse=True)
            sage: A = M([1,2, 3,4])
            sage: A
            [1 2]
            [3 4]
            sage: N = MatrixSpace(QQ, 2, 1, sparse=True)
            sage: B = N([9,8])
            sage: B
            [9]
            [8]
            sage: A.augment(B)
            [1 2 9]
            [3 4 8]
            sage: B.augment(A)
            [9 1 2]
            [8 3 4]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(QQ, 3, 4, range(12), sparse=True)
            sage: v = vector(QQ, 3, range(3), sparse=True)
            sage: A.augment(v)
            [ 0  1  2  3  0]
            [ 4  5  6  7  1]
            [ 8  9 10 11  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(QQ, 3, 5, range(15), sparse=True)
            sage: B = matrix(QQ, 3, 3, range(9), sparse=True)
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        TESTS:

        Verify that :issue:`12689` is fixed::

            sage: A = identity_matrix(QQ, 2, sparse=True)
            sage: B = identity_matrix(ZZ, 2, sparse=True)
            sage: A.augment(B)
            [1 0 1 0]
            [0 1 0 1]"""
    @overload
    def augment(self, A) -> Any:
        """Matrix_sparse.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 1048)

        Return the augmented matrix of the form::

            [self | right].

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, 2, sparse=True)
            sage: A = M([1,2, 3,4])
            sage: A
            [1 2]
            [3 4]
            sage: N = MatrixSpace(QQ, 2, 1, sparse=True)
            sage: B = N([9,8])
            sage: B
            [9]
            [8]
            sage: A.augment(B)
            [1 2 9]
            [3 4 8]
            sage: B.augment(A)
            [9 1 2]
            [8 3 4]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(QQ, 3, 4, range(12), sparse=True)
            sage: v = vector(QQ, 3, range(3), sparse=True)
            sage: A.augment(v)
            [ 0  1  2  3  0]
            [ 4  5  6  7  1]
            [ 8  9 10 11  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(QQ, 3, 5, range(15), sparse=True)
            sage: B = matrix(QQ, 3, 3, range(9), sparse=True)
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        TESTS:

        Verify that :issue:`12689` is fixed::

            sage: A = identity_matrix(QQ, 2, sparse=True)
            sage: B = identity_matrix(ZZ, 2, sparse=True)
            sage: A.augment(B)
            [1 0 1 0]
            [0 1 0 1]"""
    @overload
    def augment(self, v) -> Any:
        """Matrix_sparse.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 1048)

        Return the augmented matrix of the form::

            [self | right].

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, 2, sparse=True)
            sage: A = M([1,2, 3,4])
            sage: A
            [1 2]
            [3 4]
            sage: N = MatrixSpace(QQ, 2, 1, sparse=True)
            sage: B = N([9,8])
            sage: B
            [9]
            [8]
            sage: A.augment(B)
            [1 2 9]
            [3 4 8]
            sage: B.augment(A)
            [9 1 2]
            [8 3 4]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(QQ, 3, 4, range(12), sparse=True)
            sage: v = vector(QQ, 3, range(3), sparse=True)
            sage: A.augment(v)
            [ 0  1  2  3  0]
            [ 4  5  6  7  1]
            [ 8  9 10 11  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(QQ, 3, 5, range(15), sparse=True)
            sage: B = matrix(QQ, 3, 3, range(9), sparse=True)
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        TESTS:

        Verify that :issue:`12689` is fixed::

            sage: A = identity_matrix(QQ, 2, sparse=True)
            sage: B = identity_matrix(ZZ, 2, sparse=True)
            sage: A.augment(B)
            [1 0 1 0]
            [0 1 0 1]"""
    @overload
    def augment(self, B, subdivide=...) -> Any:
        """Matrix_sparse.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 1048)

        Return the augmented matrix of the form::

            [self | right].

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, 2, sparse=True)
            sage: A = M([1,2, 3,4])
            sage: A
            [1 2]
            [3 4]
            sage: N = MatrixSpace(QQ, 2, 1, sparse=True)
            sage: B = N([9,8])
            sage: B
            [9]
            [8]
            sage: A.augment(B)
            [1 2 9]
            [3 4 8]
            sage: B.augment(A)
            [9 1 2]
            [8 3 4]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(QQ, 3, 4, range(12), sparse=True)
            sage: v = vector(QQ, 3, range(3), sparse=True)
            sage: A.augment(v)
            [ 0  1  2  3  0]
            [ 4  5  6  7  1]
            [ 8  9 10 11  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(QQ, 3, 5, range(15), sparse=True)
            sage: B = matrix(QQ, 3, 3, range(9), sparse=True)
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        TESTS:

        Verify that :issue:`12689` is fixed::

            sage: A = identity_matrix(QQ, 2, sparse=True)
            sage: B = identity_matrix(ZZ, 2, sparse=True)
            sage: A.augment(B)
            [1 0 1 0]
            [0 1 0 1]"""
    @overload
    def augment(self, B) -> Any:
        """Matrix_sparse.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 1048)

        Return the augmented matrix of the form::

            [self | right].

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, 2, sparse=True)
            sage: A = M([1,2, 3,4])
            sage: A
            [1 2]
            [3 4]
            sage: N = MatrixSpace(QQ, 2, 1, sparse=True)
            sage: B = N([9,8])
            sage: B
            [9]
            [8]
            sage: A.augment(B)
            [1 2 9]
            [3 4 8]
            sage: B.augment(A)
            [9 1 2]
            [8 3 4]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(QQ, 3, 4, range(12), sparse=True)
            sage: v = vector(QQ, 3, range(3), sparse=True)
            sage: A.augment(v)
            [ 0  1  2  3  0]
            [ 4  5  6  7  1]
            [ 8  9 10 11  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(QQ, 3, 5, range(15), sparse=True)
            sage: B = matrix(QQ, 3, 3, range(9), sparse=True)
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        TESTS:

        Verify that :issue:`12689` is fixed::

            sage: A = identity_matrix(QQ, 2, sparse=True)
            sage: B = identity_matrix(ZZ, 2, sparse=True)
            sage: A.augment(B)
            [1 0 1 0]
            [0 1 0 1]"""
    def change_ring(self, ring) -> Any:
        """Matrix_sparse.change_ring(self, ring)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 36)

        Return the matrix obtained by coercing the entries of this matrix
        into the given ring.

        Always returns a copy (unless ``self`` is immutable, in which case
        returns ``self``).

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: A = matrix(QQ['x,y'], 2, [0,-1,2*x,-2], sparse=True); A
            [  0  -1]
            [2*x  -2]
            sage: A.change_ring(QQ['x,y,z'])
            [  0  -1]
            [2*x  -2]

        Subdivisions are preserved when changing rings::

            sage: A.subdivide([2],[]); A
            [  0  -1]
            [2*x  -2]
            [-------]
            sage: A.change_ring(RR['x,y'])
            [                 0  -1.00000000000000]
            [2.00000000000000*x  -2.00000000000000]
            [-------------------------------------]"""
    @overload
    def charpoly(self, var=..., **kwds) -> Any:
        """Matrix_sparse.charpoly(self, var='x', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 516)

        Return the characteristic polynomial of this matrix.

        .. NOTE::

            the generic sparse charpoly implementation in Sage is to
            just compute the charpoly of the corresponding dense
            matrix, so this could use a lot of memory. In particular,
            for this matrix, the charpoly will be computed using a
            dense algorithm.

        EXAMPLES::

            sage: A = matrix(ZZ, 4, range(16), sparse=True)
            sage: A.charpoly()
            x^4 - 30*x^3 - 80*x^2
            sage: A.charpoly('y')
            y^4 - 30*y^3 - 80*y^2
            sage: A.charpoly()
            x^4 - 30*x^3 - 80*x^2"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_sparse.charpoly(self, var='x', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 516)

        Return the characteristic polynomial of this matrix.

        .. NOTE::

            the generic sparse charpoly implementation in Sage is to
            just compute the charpoly of the corresponding dense
            matrix, so this could use a lot of memory. In particular,
            for this matrix, the charpoly will be computed using a
            dense algorithm.

        EXAMPLES::

            sage: A = matrix(ZZ, 4, range(16), sparse=True)
            sage: A.charpoly()
            x^4 - 30*x^3 - 80*x^2
            sage: A.charpoly('y')
            y^4 - 30*y^3 - 80*y^2
            sage: A.charpoly()
            x^4 - 30*x^3 - 80*x^2"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_sparse.charpoly(self, var='x', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 516)

        Return the characteristic polynomial of this matrix.

        .. NOTE::

            the generic sparse charpoly implementation in Sage is to
            just compute the charpoly of the corresponding dense
            matrix, so this could use a lot of memory. In particular,
            for this matrix, the charpoly will be computed using a
            dense algorithm.

        EXAMPLES::

            sage: A = matrix(ZZ, 4, range(16), sparse=True)
            sage: A.charpoly()
            x^4 - 30*x^3 - 80*x^2
            sage: A.charpoly('y')
            y^4 - 30*y^3 - 80*y^2
            sage: A.charpoly()
            x^4 - 30*x^3 - 80*x^2"""
    @overload
    def density(self) -> Any:
        """Matrix_sparse.density(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 841)

        Return the density of the matrix.

        By density we understand the ratio of the number of nonzero
        positions and the number ``self.nrows() * self.ncols()``,
        i.e. the number of possible nonzero positions.

        EXAMPLES::

            sage: a = matrix([[],[],[],[]], sparse=True); a.density()
            0
            sage: a = matrix(5000,5000,{(1,2): 1}); a.density()
            1/25000000"""
    @overload
    def density(self) -> Any:
        """Matrix_sparse.density(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 841)

        Return the density of the matrix.

        By density we understand the ratio of the number of nonzero
        positions and the number ``self.nrows() * self.ncols()``,
        i.e. the number of possible nonzero positions.

        EXAMPLES::

            sage: a = matrix([[],[],[],[]], sparse=True); a.density()
            0
            sage: a = matrix(5000,5000,{(1,2): 1}); a.density()
            1/25000000"""
    @overload
    def density(self) -> Any:
        """Matrix_sparse.density(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 841)

        Return the density of the matrix.

        By density we understand the ratio of the number of nonzero
        positions and the number ``self.nrows() * self.ncols()``,
        i.e. the number of possible nonzero positions.

        EXAMPLES::

            sage: a = matrix([[],[],[],[]], sparse=True); a.density()
            0
            sage: a = matrix(5000,5000,{(1,2): 1}); a.density()
            1/25000000"""
    def determinant(self, **kwds) -> Any:
        """Matrix_sparse.determinant(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 545)

        Return the determinant of this matrix.

        .. NOTE::

            the generic sparse determinant implementation in Sage is
            to just compute the determinant of the corresponding dense
            matrix, so this could use a lot of memory. In particular,
            for this matrix, the determinant will be computed using a
            dense algorithm.

        EXAMPLES::

            sage: A = matrix(ZZ, 4, range(16), sparse=True)
            sage: B = A + identity_matrix(ZZ, 4, sparse=True)
            sage: B.det()
            -49"""
    def matrix_from_rows_and_columns(self, rows, columns) -> Any:
        """Matrix_sparse.matrix_from_rows_and_columns(self, rows, columns)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 863)

        Return the matrix constructed from ``self`` from the given rows and
        columns.

        EXAMPLES::

            sage: M = MatrixSpace(Integers(8),3,3, sparse=True)
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
        this 3 times.

        ::

            sage: A.matrix_from_rows_and_columns([1,1,1],[2,0,0])
            [5 3 3]
            [5 3 3]
            [5 3 3]

        We can efficiently extract large submatrices::

            sage: A = random_matrix(ZZ, 100000, density=.00005, sparse=True)  # long time (4s on sage.math, 2012)
            sage: B = A[50000:,:50000]        # long time
            sage: count = 0
            sage: for i, j in A.nonzero_positions():  # long time
            ....:     if i >= 50000 and j < 50000:
            ....:         assert B[i-50000, j] == A[i, j]
            ....:         count += 1
            sage: count == sum(1 for _ in B.nonzero_positions())  # long time
            True

        We must pass in a list of indices::

            sage: A = random_matrix(ZZ,100,density=.02,sparse=True)
            sage: A.matrix_from_rows_and_columns(1,[2,3])
            Traceback (most recent call last):
            ...
            TypeError: 'sage.rings.integer.Integer' object is not iterable

            sage: A.matrix_from_rows_and_columns([1,2],3)
            Traceback (most recent call last):
            ...
            TypeError: 'sage.rings.integer.Integer' object is not iterable

        AUTHORS:

        - Jaap Spies (2006-02-18)

        - Didier Deshommes: some Pyrex speedups implemented

        - Jason Grout: sparse matrix optimizations"""
    @overload
    def transpose(self) -> Any:
        """Matrix_sparse.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 402)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES: We create a matrix, compute its transpose, and note that
        the original matrix is not changed.

        ::

            sage: M = MatrixSpace(QQ, 2, sparse=True)
            sage: A = M([1,2,3,4]); A
            [1 2]
            [3 4]
            sage: B = A.transpose(); B
            [1 3]
            [2 4]

        ``.T`` is a convenient shortcut for the transpose::

           sage: A.T
           [1 3]
           [2 4]

        .. SEEALSO:: :meth:`antitranspose`"""
    @overload
    def transpose(self) -> Any:
        """Matrix_sparse.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 402)

        Return the transpose of ``self``, without changing ``self``.

        EXAMPLES: We create a matrix, compute its transpose, and note that
        the original matrix is not changed.

        ::

            sage: M = MatrixSpace(QQ, 2, sparse=True)
            sage: A = M([1,2,3,4]); A
            [1 2]
            [3 4]
            sage: B = A.transpose(); B
            [1 3]
            [2 4]

        ``.T`` is a convenient shortcut for the transpose::

           sage: A.T
           [1 3]
           [2 4]

        .. SEEALSO:: :meth:`antitranspose`"""
    def __copy__(self) -> Any:
        """Matrix_sparse.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_sparse.pyx (starting at line 78)

        Return a copy of this matrix. Changing the entries of the copy will
        not change the entries of this matrix.

        EXAMPLES::

            sage: A = matrix(QQ['x,y'], 2, [0,-1,2,-2], sparse=True); A
            [ 0 -1]
            [ 2 -2]
            sage: B = copy(A); B
            [ 0 -1]
            [ 2 -2]
            sage: B is A
            False
            sage: B[0,0]=10; B
            [10 -1]
            [ 2 -2]
            sage: A
            [ 0 -1]
            [ 2 -2]"""
