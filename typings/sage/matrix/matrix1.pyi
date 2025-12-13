import sage as sage
import sage.matrix.matrix0
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Matrix(sage.matrix.matrix0.Matrix):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def augment(self, right, subdivide=...) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, v) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, v) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B, subdivide=...) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B, subdivide=...) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B, subdivide=...) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B, subdivide=...) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, A) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, A) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    @overload
    def augment(self, B) -> Any:
        """Matrix.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1815)

        Return a new matrix formed by appending the matrix (or vector)
        ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from
          ``right``.

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side
        of ``self``.  If ``right`` is a vector (or free module element)
        then in this context it is appropriate to consider it as a
        column vector.  (The code first converts a vector to a 1-column
        matrix.)

        If ``subdivide`` is ``True`` then any column subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``right``.  If the row divisions are
        identical, then they are preserved, otherwise they are
        discarded.  When ``subdivide`` is ``False`` there is no
        subdivision information in the result.

        .. warning::
            If ``subdivide`` is ``True`` then unequal row subdivisions
            will be discarded, since it would be ambiguous how to
            interpret them.  If the subdivision behavior is not what you
            need, you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.get_subdivisions` and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.  You might
            also find :func:`~sage.matrix.constructor.block_matrix` or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Augmenting with a matrix. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(9))
            sage: A.augment(B)
            [ 0  1  2  3  0  1  2]
            [ 4  5  6  7  3  4  5]
            [ 8  9 10 11  6  7  8]

        Augmenting with a vector. ::

            sage: A = matrix(QQ, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.augment(v)
            [  0   2   4 100]
            [  6   8  10 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.augment(v)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, 2 != 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``right``. ::

            sage: A = matrix(QQ, 3, range(12))
            sage: B = matrix(QQ, 3, range(15))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3| 0  1  2  3  4]
            [ 4  5  6  7| 5  6  7  8  9]
            [ 8  9 10 11|10 11 12 13 14]

        Column subdivisions are preserved by augmentation, and enriched,
        if subdivisions are requested.  (So multiple augmentations can
        be recorded.) ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide(None, [1])
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide(None, [2])
            sage: A.augment(B, subdivide=True)
            [0|1|0 1|2]
            [2|3|3 4|5]
            [4|5|6 7|8]

        Row subdivisions can be preserved, but only if they are
        identical.  Otherwise, this information is discarded and must be
        managed separately. ::

            sage: A = matrix(QQ, 3, range(6))
            sage: A.subdivide([1,3], None)
            sage: B = matrix(QQ, 3, range(9))
            sage: B.subdivide([1,3], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [---+-----]
            [2 3|3 4 5]
            [4 5|6 7 8]
            [---+-----]

            sage: A.subdivide([1,2], None)
            sage: A.augment(B, subdivide=True)
            [0 1|0 1 2]
            [2 3|3 4 5]
            [4 5|6 7 8]

        The result retains the base ring of ``self`` by coercing the
        elements of ``right`` into the base ring of ``self``. ::

            sage: A = matrix(QQ, 2, [1,2])
            sage: B = matrix(RR, 2, [sin(1.1), sin(2.2)])
            sage: C = A.augment(B); C                                                   # needs sage.symbolic
            [                  1 183017397/205358938]
            [                  2 106580492/131825561]
            sage: C.parent()                                                            # needs sage.symbolic
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

            sage: D = B.augment(A); D
            [0.89120736006...  1.00000000000000]
            [0.80849640381...  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        Sometimes it is not possible to coerce into the base ring of
        ``self``.  A solution is to change the base ring of ``self`` to
        a more expansive ring.  Here we mix the rationals with a ring of
        polynomials with rational coefficients.  ::

            sage: R.<y> = PolynomialRing(QQ)
            sage: A = matrix(QQ, 1, [1,2])
            sage: B = matrix(R, 1, [y, y^2])

            sage: C = B.augment(A); C
            [  y y^2   1   2]
            sage: C.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

            sage: D = A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: y is not a constant polynomial

            sage: E = A.change_ring(R)
            sage: F = E.augment(B); F
            [  1   2   y y^2]
            sage: F.parent()
            Full MatrixSpace of 1 by 4 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples
        - Rob Beezer (2010-12-07): vector argument, docstring, subdivisions"""
    def block_sum(self, Matrixother) -> Any:
        """Matrix.block_sum(self, Matrix other)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2830)

        Return the block matrix that has ``self`` and ``other`` on the diagonal::

            [ self     0 ]
            [    0 other ]

        EXAMPLES::

            sage: A = matrix(QQ[['t']], 2, range(1, 5))
            sage: A.block_sum(100*A)
            [  1   2   0   0]
            [  3   4   0   0]
            [  0   0 100 200]
            [  0   0 300 400]"""
    def column(self, Py_ssize_ti, from_list=...) -> Any:
        """Matrix.column(self, Py_ssize_t i, from_list=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1402)

        Return the ``i``-th column of this matrix as a vector.

        This column is a dense vector if and only if the matrix is a dense
        matrix.

        INPUT:

        - ``i`` -- integer

        - ``from_list`` -- boolean (default: ``False``); if ``True``, returns the
          ``i``-th element of ``self.columns()`` (see :func:`columns()`),
          which may be faster, but requires building a list of all
          columns the first time it is called after an entry of the
          matrix is changed.

        EXAMPLES::

            sage: a = matrix(2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.column(1)
            (1, 4)

        If the column is negative, it wraps around, just like with list
        indexing, e.g., -1 gives the right-most column::

            sage: a.column(-1)
            (2, 5)

        TESTS::

            sage: a = matrix(2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.column(3)
            Traceback (most recent call last):
            ...
            IndexError: column index out of range
            sage: a.column(-4)
            Traceback (most recent call last):
            ...
            IndexError: column index out of range"""
    @overload
    def column_ambient_module(self, base_ring=..., sparse=...) -> Any:
        """Matrix.column_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 949)

        Return the free module that contains the columns of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.column_ambient_module()
            Vector space of dimension 2 over Ring of integers modulo 5
            sage: M.column(1).parent() == M.column_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.column_ambient_module()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: M.column_ambient_module(QQ)
            Vector space of dimension 3 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.column_ambient_module()
            Vector space of dimension 4 over Rational Field
            sage: M.column_ambient_module(ZZ)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def column_ambient_module(self) -> Any:
        """Matrix.column_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 949)

        Return the free module that contains the columns of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.column_ambient_module()
            Vector space of dimension 2 over Ring of integers modulo 5
            sage: M.column(1).parent() == M.column_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.column_ambient_module()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: M.column_ambient_module(QQ)
            Vector space of dimension 3 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.column_ambient_module()
            Vector space of dimension 4 over Rational Field
            sage: M.column_ambient_module(ZZ)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def column_ambient_module(self) -> Any:
        """Matrix.column_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 949)

        Return the free module that contains the columns of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.column_ambient_module()
            Vector space of dimension 2 over Ring of integers modulo 5
            sage: M.column(1).parent() == M.column_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.column_ambient_module()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: M.column_ambient_module(QQ)
            Vector space of dimension 3 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.column_ambient_module()
            Vector space of dimension 4 over Rational Field
            sage: M.column_ambient_module(ZZ)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def column_ambient_module(self) -> Any:
        """Matrix.column_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 949)

        Return the free module that contains the columns of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.column_ambient_module()
            Vector space of dimension 2 over Ring of integers modulo 5
            sage: M.column(1).parent() == M.column_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.column_ambient_module()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: M.column_ambient_module(QQ)
            Vector space of dimension 3 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.column_ambient_module()
            Vector space of dimension 4 over Rational Field
            sage: M.column_ambient_module(ZZ)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def column_ambient_module(self, QQ) -> Any:
        """Matrix.column_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 949)

        Return the free module that contains the columns of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.column_ambient_module()
            Vector space of dimension 2 over Ring of integers modulo 5
            sage: M.column(1).parent() == M.column_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.column_ambient_module()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: M.column_ambient_module(QQ)
            Vector space of dimension 3 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.column_ambient_module()
            Vector space of dimension 4 over Rational Field
            sage: M.column_ambient_module(ZZ)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def column_ambient_module(self) -> Any:
        """Matrix.column_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 949)

        Return the free module that contains the columns of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.column_ambient_module()
            Vector space of dimension 2 over Ring of integers modulo 5
            sage: M.column(1).parent() == M.column_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.column_ambient_module()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: M.column_ambient_module(QQ)
            Vector space of dimension 3 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.column_ambient_module()
            Vector space of dimension 4 over Rational Field
            sage: M.column_ambient_module(ZZ)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def column_ambient_module(self, ZZ) -> Any:
        """Matrix.column_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 949)

        Return the free module that contains the columns of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.column_ambient_module()
            Vector space of dimension 2 over Ring of integers modulo 5
            sage: M.column(1).parent() == M.column_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.column_ambient_module()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: M.column_ambient_module(QQ)
            Vector space of dimension 3 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.column_ambient_module()
            Vector space of dimension 4 over Rational Field
            sage: M.column_ambient_module(ZZ)
            Ambient free module of rank 4 over the principal ideal domain Integer Ring"""
    @overload
    def columns(self, copy=...) -> Any:
        """Matrix.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1006)

        Return a list of the columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of columns which is safe to change

        If ``self`` is a sparse matrix, columns are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).columns()
            [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).columns()                     # needs sage.symbolic
            [(1.41421356237310, 2.71828182845905), (3.14159265358979, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).columns()
            [(), ()]
            sage: matrix(RR, 2, 0, []).columns()
            []
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.columns()[0])                                                # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse columns.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.columns()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.columns('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def columns(self) -> Any:
        """Matrix.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1006)

        Return a list of the columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of columns which is safe to change

        If ``self`` is a sparse matrix, columns are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).columns()
            [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).columns()                     # needs sage.symbolic
            [(1.41421356237310, 2.71828182845905), (3.14159265358979, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).columns()
            [(), ()]
            sage: matrix(RR, 2, 0, []).columns()
            []
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.columns()[0])                                                # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse columns.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.columns()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.columns('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def columns(self) -> Any:
        """Matrix.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1006)

        Return a list of the columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of columns which is safe to change

        If ``self`` is a sparse matrix, columns are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).columns()
            [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).columns()                     # needs sage.symbolic
            [(1.41421356237310, 2.71828182845905), (3.14159265358979, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).columns()
            [(), ()]
            sage: matrix(RR, 2, 0, []).columns()
            []
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.columns()[0])                                                # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse columns.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.columns()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.columns('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def columns(self) -> Any:
        """Matrix.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1006)

        Return a list of the columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of columns which is safe to change

        If ``self`` is a sparse matrix, columns are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).columns()
            [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).columns()                     # needs sage.symbolic
            [(1.41421356237310, 2.71828182845905), (3.14159265358979, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).columns()
            [(), ()]
            sage: matrix(RR, 2, 0, []).columns()
            []
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.columns()[0])                                                # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse columns.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.columns()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.columns('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def columns(self) -> Any:
        """Matrix.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1006)

        Return a list of the columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of columns which is safe to change

        If ``self`` is a sparse matrix, columns are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).columns()
            [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).columns()                     # needs sage.symbolic
            [(1.41421356237310, 2.71828182845905), (3.14159265358979, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).columns()
            [(), ()]
            sage: matrix(RR, 2, 0, []).columns()
            []
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.columns()[0])                                                # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse columns.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.columns()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.columns('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def columns(self) -> Any:
        """Matrix.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1006)

        Return a list of the columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of columns which is safe to change

        If ``self`` is a sparse matrix, columns are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).columns()
            [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).columns()                     # needs sage.symbolic
            [(1.41421356237310, 2.71828182845905), (3.14159265358979, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).columns()
            [(), ()]
            sage: matrix(RR, 2, 0, []).columns()
            []
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.columns()[0])                                                # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse columns.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.columns()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.columns('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def columns(self) -> Any:
        """Matrix.columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1006)

        Return a list of the columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of columns which is safe to change

        If ``self`` is a sparse matrix, columns are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).columns()
            [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).columns()                     # needs sage.symbolic
            [(1.41421356237310, 2.71828182845905), (3.14159265358979, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).columns()
            [(), ()]
            sage: matrix(RR, 2, 0, []).columns()
            []
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.columns()[0])                                                # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse columns.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.columns()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.columns('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    def delete_columns(self, dcols, check=...) -> Any:
        '''Matrix.delete_columns(self, dcols, check=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2049)

        Return the matrix constructed from deleting the columns with indices in the ``dcols`` list.

        INPUT:

        - ``dcols`` -- list of indices of columns to be deleted from ``self``
        - ``check`` -- boolean (default: ``True``); check whether any index in
          ``dcols`` is out of range

        .. SEEALSO::

            The methods :meth:`delete_rows` and :meth:`matrix_from_columns`
            are related.

        EXAMPLES::

            sage: A = Matrix(3, 4, range(12)); A
            [ 0  1  2  3]
            [ 4  5  6  7]
            [ 8  9 10 11]
            sage: A.delete_columns([0,2])
            [ 1  3]
            [ 5  7]
            [ 9 11]

        ``dcols`` can be a tuple. But only the underlying set of indices matters. ::

            sage: A.delete_columns((2,0,2))
            [ 1  3]
            [ 5  7]
            [ 9 11]

        The default is to check whether any index in ``dcols`` is out of range. ::

            sage: A.delete_columns([-1,2,4])
            Traceback (most recent call last):
            ...
            IndexError: [-1, 4] contains invalid indices
            sage: A.delete_columns([-1,2,4], check=False)
            [ 0  1  3]
            [ 4  5  7]
            [ 8  9 11]

        TESTS:

        The list of indices is checked.  ::

            sage: A.delete_columns("junk")
            Traceback (most recent call last):
            ...
            IndexError: [\'j\', \'k\', \'n\', \'u\'] contains invalid indices

        AUTHORS:

        - Wai Yan Pong (2012-03-05)'''
    def delete_rows(self, drows, check=...) -> Any:
        '''Matrix.delete_rows(self, drows, check=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2147)

        Return the matrix constructed from deleting the rows with indices in the ``drows`` list.

        INPUT:

        - ``drows`` -- list of indices of rows to be deleted from ``self``
        - ``check`` -- boolean (default: ``True``); whether to check if any
          index in ``drows`` is out of range

        .. SEEALSO::

            The methods :meth:`delete_columns` and :meth:`matrix_from_rows`
            are related.

        EXAMPLES::

            sage: A = Matrix(4, 3, range(12)); A
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            sage: A.delete_rows([0,2])
            [ 3  4  5]
            [ 9 10 11]

        ``drows`` can be a tuple. But only the underlying set of indices matters. ::

            sage: A.delete_rows((2,0,2))
            [ 3  4  5]
            [ 9 10 11]

        The default is to check whether the any index in ``drows`` is out of range. ::

            sage: A.delete_rows([-1,2,4])
            Traceback (most recent call last):
            ...
            IndexError: [-1, 4] contains invalid indices
            sage: A.delete_rows([-1,2,4], check=False)
            [ 0  1  2]
            [ 3  4  5]
            [ 9 10 11]

        TESTS:

        The list of indices is checked.  ::

            sage: A.delete_rows("junk")
            Traceback (most recent call last):
            ...
            IndexError: [\'j\', \'k\', \'n\', \'u\'] contains invalid indices

        AUTHORS

        - Wai Yan Pong (2012-03-05)'''
    @overload
    def dense_columns(self, copy=...) -> Any:
        """Matrix.dense_columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1122)

        Return list of the dense columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES:

        An example over the integers::

            sage: a = matrix(3, 3, range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: a.dense_columns()
            [(0, 3, 6), (1, 4, 7), (2, 5, 8)]

        We do an example over a polynomial ring::

            sage: R.<x> = QQ[]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5]); a
            [      x     x^2]
            [  2/3*x x^5 + 1]
            sage: a.dense_columns()
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5], sparse=True)
            sage: c = a.dense_columns(); c
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: parent(c[1])
            Ambient free module of rank 2 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_columns()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_columns(self) -> Any:
        """Matrix.dense_columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1122)

        Return list of the dense columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES:

        An example over the integers::

            sage: a = matrix(3, 3, range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: a.dense_columns()
            [(0, 3, 6), (1, 4, 7), (2, 5, 8)]

        We do an example over a polynomial ring::

            sage: R.<x> = QQ[]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5]); a
            [      x     x^2]
            [  2/3*x x^5 + 1]
            sage: a.dense_columns()
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5], sparse=True)
            sage: c = a.dense_columns(); c
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: parent(c[1])
            Ambient free module of rank 2 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_columns()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_columns(self) -> Any:
        """Matrix.dense_columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1122)

        Return list of the dense columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES:

        An example over the integers::

            sage: a = matrix(3, 3, range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: a.dense_columns()
            [(0, 3, 6), (1, 4, 7), (2, 5, 8)]

        We do an example over a polynomial ring::

            sage: R.<x> = QQ[]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5]); a
            [      x     x^2]
            [  2/3*x x^5 + 1]
            sage: a.dense_columns()
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5], sparse=True)
            sage: c = a.dense_columns(); c
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: parent(c[1])
            Ambient free module of rank 2 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_columns()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_columns(self) -> Any:
        """Matrix.dense_columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1122)

        Return list of the dense columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES:

        An example over the integers::

            sage: a = matrix(3, 3, range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: a.dense_columns()
            [(0, 3, 6), (1, 4, 7), (2, 5, 8)]

        We do an example over a polynomial ring::

            sage: R.<x> = QQ[]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5]); a
            [      x     x^2]
            [  2/3*x x^5 + 1]
            sage: a.dense_columns()
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5], sparse=True)
            sage: c = a.dense_columns(); c
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: parent(c[1])
            Ambient free module of rank 2 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_columns()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_columns(self) -> Any:
        """Matrix.dense_columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1122)

        Return list of the dense columns of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES:

        An example over the integers::

            sage: a = matrix(3, 3, range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: a.dense_columns()
            [(0, 3, 6), (1, 4, 7), (2, 5, 8)]

        We do an example over a polynomial ring::

            sage: R.<x> = QQ[]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5]); a
            [      x     x^2]
            [  2/3*x x^5 + 1]
            sage: a.dense_columns()
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: a = matrix(R, 2, [x,x^2, 2/3*x,1+x^5], sparse=True)
            sage: c = a.dense_columns(); c
            [(x, 2/3*x), (x^2, x^5 + 1)]
            sage: parent(c[1])
            Ambient free module of rank 2 over the principal ideal domain
             Univariate Polynomial Ring in x over Rational Field

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_columns()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_matrix(self) -> Any:
        '''Matrix.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2591)

        If this matrix is sparse, return a dense matrix with the same
        entries. If this matrix is dense, return this matrix (not a copy).

        .. NOTE::

           The definition of "dense" and "sparse" in Sage have nothing to
           do with the number of nonzero entries. Sparse and dense are
           properties of the underlying representation of the matrix.

        EXAMPLES::

            sage: A = MatrixSpace(QQ,2, sparse=True)([1,2,0,1])
            sage: A.is_sparse()
            True
            sage: B = A.dense_matrix()
            sage: B.is_sparse()
            False
            sage: A == B
            True
            sage: B.dense_matrix() is B
            True
            sage: A*B
            [1 4]
            [0 1]
            sage: A.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
            sage: B.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        In Sage, the product of a sparse and a dense matrix is always
        dense::

            sage: (A*B).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: (B*A).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        TESTS:

        Make sure that subdivisions are preserved when switching
        between dense and sparse matrices::

            sage: a = matrix(ZZ, 3, range(9))
            sage: a.subdivide([1,2],2)
            sage: a.subdivisions()
            ([1, 2], [2])
            sage: b = a.sparse_matrix().dense_matrix()
            sage: b.subdivisions()
            ([1, 2], [2])

        Ensure we can compute the correct dense matrix even if the
        dict items are ETuples (see :issue:`17658`)::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: matrix(GF(5^2, "z"), {ETuple((1, 1)): 2}).dense_matrix()              # needs sage.rings.finite_rings
            [0 0]
            [0 2]'''
    @overload
    def dense_matrix(self) -> Any:
        '''Matrix.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2591)

        If this matrix is sparse, return a dense matrix with the same
        entries. If this matrix is dense, return this matrix (not a copy).

        .. NOTE::

           The definition of "dense" and "sparse" in Sage have nothing to
           do with the number of nonzero entries. Sparse and dense are
           properties of the underlying representation of the matrix.

        EXAMPLES::

            sage: A = MatrixSpace(QQ,2, sparse=True)([1,2,0,1])
            sage: A.is_sparse()
            True
            sage: B = A.dense_matrix()
            sage: B.is_sparse()
            False
            sage: A == B
            True
            sage: B.dense_matrix() is B
            True
            sage: A*B
            [1 4]
            [0 1]
            sage: A.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
            sage: B.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        In Sage, the product of a sparse and a dense matrix is always
        dense::

            sage: (A*B).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: (B*A).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        TESTS:

        Make sure that subdivisions are preserved when switching
        between dense and sparse matrices::

            sage: a = matrix(ZZ, 3, range(9))
            sage: a.subdivide([1,2],2)
            sage: a.subdivisions()
            ([1, 2], [2])
            sage: b = a.sparse_matrix().dense_matrix()
            sage: b.subdivisions()
            ([1, 2], [2])

        Ensure we can compute the correct dense matrix even if the
        dict items are ETuples (see :issue:`17658`)::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: matrix(GF(5^2, "z"), {ETuple((1, 1)): 2}).dense_matrix()              # needs sage.rings.finite_rings
            [0 0]
            [0 2]'''
    @overload
    def dense_matrix(self) -> Any:
        '''Matrix.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2591)

        If this matrix is sparse, return a dense matrix with the same
        entries. If this matrix is dense, return this matrix (not a copy).

        .. NOTE::

           The definition of "dense" and "sparse" in Sage have nothing to
           do with the number of nonzero entries. Sparse and dense are
           properties of the underlying representation of the matrix.

        EXAMPLES::

            sage: A = MatrixSpace(QQ,2, sparse=True)([1,2,0,1])
            sage: A.is_sparse()
            True
            sage: B = A.dense_matrix()
            sage: B.is_sparse()
            False
            sage: A == B
            True
            sage: B.dense_matrix() is B
            True
            sage: A*B
            [1 4]
            [0 1]
            sage: A.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
            sage: B.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        In Sage, the product of a sparse and a dense matrix is always
        dense::

            sage: (A*B).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: (B*A).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        TESTS:

        Make sure that subdivisions are preserved when switching
        between dense and sparse matrices::

            sage: a = matrix(ZZ, 3, range(9))
            sage: a.subdivide([1,2],2)
            sage: a.subdivisions()
            ([1, 2], [2])
            sage: b = a.sparse_matrix().dense_matrix()
            sage: b.subdivisions()
            ([1, 2], [2])

        Ensure we can compute the correct dense matrix even if the
        dict items are ETuples (see :issue:`17658`)::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: matrix(GF(5^2, "z"), {ETuple((1, 1)): 2}).dense_matrix()              # needs sage.rings.finite_rings
            [0 0]
            [0 2]'''
    @overload
    def dense_matrix(self) -> Any:
        '''Matrix.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2591)

        If this matrix is sparse, return a dense matrix with the same
        entries. If this matrix is dense, return this matrix (not a copy).

        .. NOTE::

           The definition of "dense" and "sparse" in Sage have nothing to
           do with the number of nonzero entries. Sparse and dense are
           properties of the underlying representation of the matrix.

        EXAMPLES::

            sage: A = MatrixSpace(QQ,2, sparse=True)([1,2,0,1])
            sage: A.is_sparse()
            True
            sage: B = A.dense_matrix()
            sage: B.is_sparse()
            False
            sage: A == B
            True
            sage: B.dense_matrix() is B
            True
            sage: A*B
            [1 4]
            [0 1]
            sage: A.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
            sage: B.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        In Sage, the product of a sparse and a dense matrix is always
        dense::

            sage: (A*B).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: (B*A).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        TESTS:

        Make sure that subdivisions are preserved when switching
        between dense and sparse matrices::

            sage: a = matrix(ZZ, 3, range(9))
            sage: a.subdivide([1,2],2)
            sage: a.subdivisions()
            ([1, 2], [2])
            sage: b = a.sparse_matrix().dense_matrix()
            sage: b.subdivisions()
            ([1, 2], [2])

        Ensure we can compute the correct dense matrix even if the
        dict items are ETuples (see :issue:`17658`)::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: matrix(GF(5^2, "z"), {ETuple((1, 1)): 2}).dense_matrix()              # needs sage.rings.finite_rings
            [0 0]
            [0 2]'''
    @overload
    def dense_matrix(self) -> Any:
        '''Matrix.dense_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2591)

        If this matrix is sparse, return a dense matrix with the same
        entries. If this matrix is dense, return this matrix (not a copy).

        .. NOTE::

           The definition of "dense" and "sparse" in Sage have nothing to
           do with the number of nonzero entries. Sparse and dense are
           properties of the underlying representation of the matrix.

        EXAMPLES::

            sage: A = MatrixSpace(QQ,2, sparse=True)([1,2,0,1])
            sage: A.is_sparse()
            True
            sage: B = A.dense_matrix()
            sage: B.is_sparse()
            False
            sage: A == B
            True
            sage: B.dense_matrix() is B
            True
            sage: A*B
            [1 4]
            [0 1]
            sage: A.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
            sage: B.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        In Sage, the product of a sparse and a dense matrix is always
        dense::

            sage: (A*B).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: (B*A).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        TESTS:

        Make sure that subdivisions are preserved when switching
        between dense and sparse matrices::

            sage: a = matrix(ZZ, 3, range(9))
            sage: a.subdivide([1,2],2)
            sage: a.subdivisions()
            ([1, 2], [2])
            sage: b = a.sparse_matrix().dense_matrix()
            sage: b.subdivisions()
            ([1, 2], [2])

        Ensure we can compute the correct dense matrix even if the
        dict items are ETuples (see :issue:`17658`)::

            sage: from sage.rings.polynomial.polydict import ETuple
            sage: matrix(GF(5^2, "z"), {ETuple((1, 1)): 2}).dense_matrix()              # needs sage.rings.finite_rings
            [0 0]
            [0 2]'''
    @overload
    def dense_rows(self, copy=...) -> Any:
        """Matrix.dense_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1186)

        Return list of the dense rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely (note that the individual vectors in the copy
          should not be modified since they are mutable!)

        EXAMPLES::

            sage: m = matrix(3, range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.dense_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: v is m.dense_rows()
            False
            sage: m.dense_rows(copy=False) is m.dense_rows(copy=False)
            True
            sage: m[0,0] = 10
            sage: m.dense_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_rows(self) -> Any:
        """Matrix.dense_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1186)

        Return list of the dense rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely (note that the individual vectors in the copy
          should not be modified since they are mutable!)

        EXAMPLES::

            sage: m = matrix(3, range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.dense_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: v is m.dense_rows()
            False
            sage: m.dense_rows(copy=False) is m.dense_rows(copy=False)
            True
            sage: m[0,0] = 10
            sage: m.dense_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_rows(self) -> Any:
        """Matrix.dense_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1186)

        Return list of the dense rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely (note that the individual vectors in the copy
          should not be modified since they are mutable!)

        EXAMPLES::

            sage: m = matrix(3, range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.dense_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: v is m.dense_rows()
            False
            sage: m.dense_rows(copy=False) is m.dense_rows(copy=False)
            True
            sage: m[0,0] = 10
            sage: m.dense_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_rows(self) -> Any:
        """Matrix.dense_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1186)

        Return list of the dense rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely (note that the individual vectors in the copy
          should not be modified since they are mutable!)

        EXAMPLES::

            sage: m = matrix(3, range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.dense_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: v is m.dense_rows()
            False
            sage: m.dense_rows(copy=False) is m.dense_rows(copy=False)
            True
            sage: m[0,0] = 10
            sage: m.dense_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def dense_rows(self) -> Any:
        """Matrix.dense_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1186)

        Return list of the dense rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely (note that the individual vectors in the copy
          should not be modified since they are mutable!)

        EXAMPLES::

            sage: m = matrix(3, range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.dense_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: v is m.dense_rows()
            False
            sage: m.dense_rows(copy=False) is m.dense_rows(copy=False)
            True
            sage: m[0,0] = 10
            sage: m.dense_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3)(range(9))
            sage: v = m.dense_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def lift(self) -> Any:
        """Matrix.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 797)

        Return lift of ``self`` to the covering ring of the base ring R,
        which is by definition the ring returned by calling
        cover_ring() on R, or just R itself if the cover_ring method
        is not defined.

        EXAMPLES::

            sage: M = Matrix(Integers(7), 2, 2, [5, 9, 13, 15]); M
            [5 2]
            [6 1]
            sage: M.lift()
            [5 2]
            [6 1]
            sage: parent(M.lift())
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring

        The field QQ doesn't have a cover_ring method::

            sage: hasattr(QQ, 'cover_ring')
            False

        So lifting a matrix over QQ gives back the same exact matrix.

        ::

            sage: B = matrix(QQ, 2, [1..4])
            sage: B.lift()
            [1 2]
            [3 4]
            sage: B.lift() is B
            True"""
    @overload
    def lift(self) -> Any:
        """Matrix.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 797)

        Return lift of ``self`` to the covering ring of the base ring R,
        which is by definition the ring returned by calling
        cover_ring() on R, or just R itself if the cover_ring method
        is not defined.

        EXAMPLES::

            sage: M = Matrix(Integers(7), 2, 2, [5, 9, 13, 15]); M
            [5 2]
            [6 1]
            sage: M.lift()
            [5 2]
            [6 1]
            sage: parent(M.lift())
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring

        The field QQ doesn't have a cover_ring method::

            sage: hasattr(QQ, 'cover_ring')
            False

        So lifting a matrix over QQ gives back the same exact matrix.

        ::

            sage: B = matrix(QQ, 2, [1..4])
            sage: B.lift()
            [1 2]
            [3 4]
            sage: B.lift() is B
            True"""
    @overload
    def lift(self) -> Any:
        """Matrix.lift(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 797)

        Return lift of ``self`` to the covering ring of the base ring R,
        which is by definition the ring returned by calling
        cover_ring() on R, or just R itself if the cover_ring method
        is not defined.

        EXAMPLES::

            sage: M = Matrix(Integers(7), 2, 2, [5, 9, 13, 15]); M
            [5 2]
            [6 1]
            sage: M.lift()
            [5 2]
            [6 1]
            sage: parent(M.lift())
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring

        The field QQ doesn't have a cover_ring method::

            sage: hasattr(QQ, 'cover_ring')
            False

        So lifting a matrix over QQ gives back the same exact matrix.

        ::

            sage: B = matrix(QQ, 2, [1..4])
            sage: B.lift()
            [1 2]
            [3 4]
            sage: B.lift() is B
            True"""
    def lift_centered(self) -> Any:
        """Matrix.lift_centered(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 837)

        Apply the lift_centered method to every entry of ``self``.

        OUTPUT:

        If ``self`` is a matrix over the Integers mod `n`, this method returns the
        unique matrix `m` such that `m` is congruent to ``self`` mod `n` and for
        every entry `m[i,j]` we have `-n/2 < m[i,j] \\leq n/2`. If the
        coefficient ring does not have a cover_ring method, return ``self``.

        EXAMPLES::

            sage: M = Matrix(Integers(8), 2, 4, range(8)); M
            [0 1 2 3]
            [4 5 6 7]
            sage: L = M.lift_centered(); L
            [ 0  1  2  3]
            [ 4 -3 -2 -1]
            sage: parent(L)
            Full MatrixSpace of 2 by 4 dense matrices over Integer Ring

        The returned matrix is congruent to M modulo 8.::

            sage: L.mod(8)
            [0 1 2 3]
            [4 5 6 7]

        The field QQ doesn't have a cover_ring method::

            sage: hasattr(QQ, 'cover_ring')
            False

        So lifting a matrix over QQ gives back the same exact matrix.

        ::

            sage: B = matrix(QQ, 2, [1..4])
            sage: B.lift_centered()
            [1 2]
            [3 4]
            sage: B.lift_centered() is B
            True"""
    def matrix_from_columns(self, columns) -> Any:
        """Matrix.matrix_from_columns(self, columns)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2019)

        Return the matrix constructed from ``self`` using columns with indices
        in the columns list.

        EXAMPLES::

            sage: M = MatrixSpace(Integers(8), 3, 3)
            sage: A = M(range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 0]
            sage: A.matrix_from_columns([2,1])
            [2 1]
            [5 4]
            [0 7]"""
    def matrix_from_rows(self, rows) -> Any:
        """Matrix.matrix_from_rows(self, rows)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2118)

        Return the matrix constructed from ``self`` using rows with indices in
        the rows list.

        EXAMPLES::

            sage: M = MatrixSpace(Integers(8), 3, 3)
            sage: A = M(range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 0]
            sage: A.matrix_from_rows([2,1])
            [6 7 0]
            [3 4 5]"""
    def matrix_from_rows_and_columns(self, rows, columns) -> Any:
        """Matrix.matrix_from_rows_and_columns(self, rows, columns)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2215)

        Return the matrix constructed from ``self`` from the given rows and
        columns.

        EXAMPLES::

            sage: M = MatrixSpace(Integers(8), 3, 3)
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

            sage: A.matrix_from_rows_and_columns([1,1,1], [2,0,0])
            [5 3 3]
            [5 3 3]
            [5 3 3]

        AUTHORS:

        - Jaap Spies (2006-02-18)

        - Didier Deshommes: some Pyrex speedups implemented"""
    @overload
    def matrix_over_field(self) -> Any:
        """Matrix.matrix_over_field(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 780)

        Return copy of this matrix, but with entries viewed as elements of
        the fraction field of the base ring (assuming it is defined).

        EXAMPLES::

            sage: A = MatrixSpace(IntegerRing(),2)([1,2,3,4])
            sage: B = A.matrix_over_field()
            sage: B
            [1 2]
            [3 4]
            sage: B.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field"""
    @overload
    def matrix_over_field(self) -> Any:
        """Matrix.matrix_over_field(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 780)

        Return copy of this matrix, but with entries viewed as elements of
        the fraction field of the base ring (assuming it is defined).

        EXAMPLES::

            sage: A = MatrixSpace(IntegerRing(),2)([1,2,3,4])
            sage: B = A.matrix_over_field()
            sage: B
            [1 2]
            [3 4]
            sage: B.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field"""
    @overload
    def matrix_space(self, nrows=..., ncols=..., sparse=...) -> Any:
        """Matrix.matrix_space(self, nrows=None, ncols=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2704)

        Return the ambient matrix space of ``self``.

        INPUT:

        - ``nrows``, ``ncols`` -- (optional) number of rows and columns in
          returned matrix space

        - ``sparse`` -- whether the returned matrix space uses sparse or
          dense matrices

        EXAMPLES::

            sage: m = matrix(3, [1..9])
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(ncols=2)
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
            sage: m.matrix_space(1)
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(1, 2, True)
            Full MatrixSpace of 1 by 2 sparse matrices over Integer Ring

            sage: M = MatrixSpace(QQ, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, ncols=12)
            Full MatrixSpace of 2 by 12 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, sparse=True)
            Full MatrixSpace of 2 by 3 sparse matrices over Rational Field"""
    @overload
    def matrix_space(self) -> Any:
        """Matrix.matrix_space(self, nrows=None, ncols=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2704)

        Return the ambient matrix space of ``self``.

        INPUT:

        - ``nrows``, ``ncols`` -- (optional) number of rows and columns in
          returned matrix space

        - ``sparse`` -- whether the returned matrix space uses sparse or
          dense matrices

        EXAMPLES::

            sage: m = matrix(3, [1..9])
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(ncols=2)
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
            sage: m.matrix_space(1)
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(1, 2, True)
            Full MatrixSpace of 1 by 2 sparse matrices over Integer Ring

            sage: M = MatrixSpace(QQ, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, ncols=12)
            Full MatrixSpace of 2 by 12 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, sparse=True)
            Full MatrixSpace of 2 by 3 sparse matrices over Rational Field"""
    @overload
    def matrix_space(self, ncols=...) -> Any:
        """Matrix.matrix_space(self, nrows=None, ncols=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2704)

        Return the ambient matrix space of ``self``.

        INPUT:

        - ``nrows``, ``ncols`` -- (optional) number of rows and columns in
          returned matrix space

        - ``sparse`` -- whether the returned matrix space uses sparse or
          dense matrices

        EXAMPLES::

            sage: m = matrix(3, [1..9])
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(ncols=2)
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
            sage: m.matrix_space(1)
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(1, 2, True)
            Full MatrixSpace of 1 by 2 sparse matrices over Integer Ring

            sage: M = MatrixSpace(QQ, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, ncols=12)
            Full MatrixSpace of 2 by 12 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, sparse=True)
            Full MatrixSpace of 2 by 3 sparse matrices over Rational Field"""
    @overload
    def matrix_space(self) -> Any:
        """Matrix.matrix_space(self, nrows=None, ncols=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2704)

        Return the ambient matrix space of ``self``.

        INPUT:

        - ``nrows``, ``ncols`` -- (optional) number of rows and columns in
          returned matrix space

        - ``sparse`` -- whether the returned matrix space uses sparse or
          dense matrices

        EXAMPLES::

            sage: m = matrix(3, [1..9])
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(ncols=2)
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
            sage: m.matrix_space(1)
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(1, 2, True)
            Full MatrixSpace of 1 by 2 sparse matrices over Integer Ring

            sage: M = MatrixSpace(QQ, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, ncols=12)
            Full MatrixSpace of 2 by 12 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, sparse=True)
            Full MatrixSpace of 2 by 3 sparse matrices over Rational Field"""
    @overload
    def matrix_space(self, nrows=..., ncols=...) -> Any:
        """Matrix.matrix_space(self, nrows=None, ncols=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2704)

        Return the ambient matrix space of ``self``.

        INPUT:

        - ``nrows``, ``ncols`` -- (optional) number of rows and columns in
          returned matrix space

        - ``sparse`` -- whether the returned matrix space uses sparse or
          dense matrices

        EXAMPLES::

            sage: m = matrix(3, [1..9])
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(ncols=2)
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
            sage: m.matrix_space(1)
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(1, 2, True)
            Full MatrixSpace of 1 by 2 sparse matrices over Integer Ring

            sage: M = MatrixSpace(QQ, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, ncols=12)
            Full MatrixSpace of 2 by 12 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, sparse=True)
            Full MatrixSpace of 2 by 3 sparse matrices over Rational Field"""
    @overload
    def matrix_space(self, nrows=..., sparse=...) -> Any:
        """Matrix.matrix_space(self, nrows=None, ncols=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2704)

        Return the ambient matrix space of ``self``.

        INPUT:

        - ``nrows``, ``ncols`` -- (optional) number of rows and columns in
          returned matrix space

        - ``sparse`` -- whether the returned matrix space uses sparse or
          dense matrices

        EXAMPLES::

            sage: m = matrix(3, [1..9])
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(ncols=2)
            Full MatrixSpace of 3 by 2 dense matrices over Integer Ring
            sage: m.matrix_space(1)
            Full MatrixSpace of 1 by 3 dense matrices over Integer Ring
            sage: m.matrix_space(1, 2, True)
            Full MatrixSpace of 1 by 2 sparse matrices over Integer Ring

            sage: M = MatrixSpace(QQ, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, ncols=12)
            Full MatrixSpace of 2 by 12 dense matrices over Rational Field
             (using Matrix_generic_dense)
            sage: m.matrix_space(nrows=2, sparse=True)
            Full MatrixSpace of 2 by 3 sparse matrices over Rational Field"""
    @overload
    def new_matrix(self, nrows=..., ncols=..., entries=..., coerce=..., copy=..., sparse=...) -> Any:
        """Matrix.new_matrix(self, nrows=None, ncols=None, entries=None, coerce=True, copy=True, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2758)

        Create a matrix in the parent of this matrix with the given number
        of rows, columns, etc. The default parameters are the same as for
        ``self``.

        INPUT:

        These three variables get sent to :func:`matrix_space`:

        - ``nrows``, ``ncols`` -- number of rows and columns in returned
          matrix. If not specified, defaults to ``None`` and will give a
          matrix of the same size as ``self``.
        - ``sparse`` -- whether returned matrix is sparse or not. Defaults
          to same value as self

        The remaining three variables (``coerce``, ``entries``, and
        ``copy``) are used by
        :func:`sage.matrix.matrix_space.MatrixSpace` to construct the
        new matrix.

        .. warning::

           This function called with no arguments returns the zero
           matrix of the same dimension and sparseness of ``self``.

        EXAMPLES::

            sage: A = matrix(ZZ,2,2,[1,2,3,4]); A
            [1 2]
            [3 4]
            sage: A.new_matrix()
            [0 0]
            [0 0]
            sage: A.new_matrix(1,1)
            [0]
            sage: A.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        ::

            sage: A = matrix(RR,2,3,[1.1,2.2,3.3,4.4,5.5,6.6]); A
            [1.10000000000000 2.20000000000000 3.30000000000000]
            [4.40000000000000 5.50000000000000 6.60000000000000]
            sage: A.new_matrix()
            [0.000000000000000 0.000000000000000 0.000000000000000]
            [0.000000000000000 0.000000000000000 0.000000000000000]
            sage: A.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: M = MatrixSpace(ZZ, 2, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3, sparse=True).parent()
            Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring"""
    @overload
    def new_matrix(self) -> Any:
        """Matrix.new_matrix(self, nrows=None, ncols=None, entries=None, coerce=True, copy=True, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2758)

        Create a matrix in the parent of this matrix with the given number
        of rows, columns, etc. The default parameters are the same as for
        ``self``.

        INPUT:

        These three variables get sent to :func:`matrix_space`:

        - ``nrows``, ``ncols`` -- number of rows and columns in returned
          matrix. If not specified, defaults to ``None`` and will give a
          matrix of the same size as ``self``.
        - ``sparse`` -- whether returned matrix is sparse or not. Defaults
          to same value as self

        The remaining three variables (``coerce``, ``entries``, and
        ``copy``) are used by
        :func:`sage.matrix.matrix_space.MatrixSpace` to construct the
        new matrix.

        .. warning::

           This function called with no arguments returns the zero
           matrix of the same dimension and sparseness of ``self``.

        EXAMPLES::

            sage: A = matrix(ZZ,2,2,[1,2,3,4]); A
            [1 2]
            [3 4]
            sage: A.new_matrix()
            [0 0]
            [0 0]
            sage: A.new_matrix(1,1)
            [0]
            sage: A.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        ::

            sage: A = matrix(RR,2,3,[1.1,2.2,3.3,4.4,5.5,6.6]); A
            [1.10000000000000 2.20000000000000 3.30000000000000]
            [4.40000000000000 5.50000000000000 6.60000000000000]
            sage: A.new_matrix()
            [0.000000000000000 0.000000000000000 0.000000000000000]
            [0.000000000000000 0.000000000000000 0.000000000000000]
            sage: A.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: M = MatrixSpace(ZZ, 2, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3, sparse=True).parent()
            Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring"""
    @overload
    def new_matrix(self) -> Any:
        """Matrix.new_matrix(self, nrows=None, ncols=None, entries=None, coerce=True, copy=True, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2758)

        Create a matrix in the parent of this matrix with the given number
        of rows, columns, etc. The default parameters are the same as for
        ``self``.

        INPUT:

        These three variables get sent to :func:`matrix_space`:

        - ``nrows``, ``ncols`` -- number of rows and columns in returned
          matrix. If not specified, defaults to ``None`` and will give a
          matrix of the same size as ``self``.
        - ``sparse`` -- whether returned matrix is sparse or not. Defaults
          to same value as self

        The remaining three variables (``coerce``, ``entries``, and
        ``copy``) are used by
        :func:`sage.matrix.matrix_space.MatrixSpace` to construct the
        new matrix.

        .. warning::

           This function called with no arguments returns the zero
           matrix of the same dimension and sparseness of ``self``.

        EXAMPLES::

            sage: A = matrix(ZZ,2,2,[1,2,3,4]); A
            [1 2]
            [3 4]
            sage: A.new_matrix()
            [0 0]
            [0 0]
            sage: A.new_matrix(1,1)
            [0]
            sage: A.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        ::

            sage: A = matrix(RR,2,3,[1.1,2.2,3.3,4.4,5.5,6.6]); A
            [1.10000000000000 2.20000000000000 3.30000000000000]
            [4.40000000000000 5.50000000000000 6.60000000000000]
            sage: A.new_matrix()
            [0.000000000000000 0.000000000000000 0.000000000000000]
            [0.000000000000000 0.000000000000000 0.000000000000000]
            sage: A.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: M = MatrixSpace(ZZ, 2, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3, sparse=True).parent()
            Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring"""
    @overload
    def new_matrix(self) -> Any:
        """Matrix.new_matrix(self, nrows=None, ncols=None, entries=None, coerce=True, copy=True, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2758)

        Create a matrix in the parent of this matrix with the given number
        of rows, columns, etc. The default parameters are the same as for
        ``self``.

        INPUT:

        These three variables get sent to :func:`matrix_space`:

        - ``nrows``, ``ncols`` -- number of rows and columns in returned
          matrix. If not specified, defaults to ``None`` and will give a
          matrix of the same size as ``self``.
        - ``sparse`` -- whether returned matrix is sparse or not. Defaults
          to same value as self

        The remaining three variables (``coerce``, ``entries``, and
        ``copy``) are used by
        :func:`sage.matrix.matrix_space.MatrixSpace` to construct the
        new matrix.

        .. warning::

           This function called with no arguments returns the zero
           matrix of the same dimension and sparseness of ``self``.

        EXAMPLES::

            sage: A = matrix(ZZ,2,2,[1,2,3,4]); A
            [1 2]
            [3 4]
            sage: A.new_matrix()
            [0 0]
            [0 0]
            sage: A.new_matrix(1,1)
            [0]
            sage: A.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        ::

            sage: A = matrix(RR,2,3,[1.1,2.2,3.3,4.4,5.5,6.6]); A
            [1.10000000000000 2.20000000000000 3.30000000000000]
            [4.40000000000000 5.50000000000000 6.60000000000000]
            sage: A.new_matrix()
            [0.000000000000000 0.000000000000000 0.000000000000000]
            [0.000000000000000 0.000000000000000 0.000000000000000]
            sage: A.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: M = MatrixSpace(ZZ, 2, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3, sparse=True).parent()
            Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring"""
    @overload
    def new_matrix(self) -> Any:
        """Matrix.new_matrix(self, nrows=None, ncols=None, entries=None, coerce=True, copy=True, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2758)

        Create a matrix in the parent of this matrix with the given number
        of rows, columns, etc. The default parameters are the same as for
        ``self``.

        INPUT:

        These three variables get sent to :func:`matrix_space`:

        - ``nrows``, ``ncols`` -- number of rows and columns in returned
          matrix. If not specified, defaults to ``None`` and will give a
          matrix of the same size as ``self``.
        - ``sparse`` -- whether returned matrix is sparse or not. Defaults
          to same value as self

        The remaining three variables (``coerce``, ``entries``, and
        ``copy``) are used by
        :func:`sage.matrix.matrix_space.MatrixSpace` to construct the
        new matrix.

        .. warning::

           This function called with no arguments returns the zero
           matrix of the same dimension and sparseness of ``self``.

        EXAMPLES::

            sage: A = matrix(ZZ,2,2,[1,2,3,4]); A
            [1 2]
            [3 4]
            sage: A.new_matrix()
            [0 0]
            [0 0]
            sage: A.new_matrix(1,1)
            [0]
            sage: A.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring

        ::

            sage: A = matrix(RR,2,3,[1.1,2.2,3.3,4.4,5.5,6.6]); A
            [1.10000000000000 2.20000000000000 3.30000000000000]
            [4.40000000000000 5.50000000000000 6.60000000000000]
            sage: A.new_matrix()
            [0.000000000000000 0.000000000000000 0.000000000000000]
            [0.000000000000000 0.000000000000000 0.000000000000000]
            sage: A.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: M = MatrixSpace(ZZ, 2, 3, implementation='generic')
            sage: m = M.an_element()
            sage: m.new_matrix().parent()
            Full MatrixSpace of 2 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
             (using Matrix_generic_dense)
            sage: m.new_matrix(3,3, sparse=True).parent()
            Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring"""
    @overload
    def numpy(self, dtype=..., copy=...) -> Any:
        """Matrix.numpy(self, dtype=None, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 676)

        Return the Numpy matrix associated to this matrix.

        INPUT:

        - ``dtype`` -- the desired data-type for the array. If not given,
          then the type will be determined as the minimum type required
          to hold the objects in the sequence.

        - ``copy`` -- if `self` is already an `ndarray`, then this flag
          determines whether the data is copied (the default), or whether
          a view is constructed.

        EXAMPLES::

            sage: # needs numpy
            sage: a = matrix(3, range(12))
            sage: a.numpy()
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]])
            sage: a.numpy('f')
            array([[  0.,   1.,   2.,   3.],
                   [  4.,   5.,   6.,   7.],
                   [  8.,   9.,  10.,  11.]], dtype=float32)
            sage: a.numpy('d')
            array([[  0.,   1.,   2.,   3.],
                   [  4.,   5.,   6.,   7.],
                   [  8.,   9.,  10.,  11.]])
            sage: a.numpy('B')
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]], dtype=uint8)

        Type ``numpy.typecodes`` for a list of the possible
        typecodes::

            sage: import numpy                            # needs numpy
            sage: numpy.typecodes.items()                 # needs numpy # random
            [('All', '?bhilqpBHILQPefdgFDGSUVOMm'), ('AllFloat', 'efdgFDG'),
            ...

        For instance, you can see possibilities for real floating point numbers::

            sage: numpy.typecodes['Float']                # needs numpy
            'efdg'

        Alternatively, numpy automatically calls this function (via
        the magic :meth:`__array__` method) to convert Sage matrices
        to numpy arrays::

            sage: # needs numpy
            sage: import numpy
            sage: b = numpy.array(a); b
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]])
            sage: b.dtype
            dtype('int32')  # 32-bit
            dtype('int64')  # 64-bit
            sage: b.shape
            (3, 4)"""
    @overload
    def numpy(self) -> Any:
        """Matrix.numpy(self, dtype=None, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 676)

        Return the Numpy matrix associated to this matrix.

        INPUT:

        - ``dtype`` -- the desired data-type for the array. If not given,
          then the type will be determined as the minimum type required
          to hold the objects in the sequence.

        - ``copy`` -- if `self` is already an `ndarray`, then this flag
          determines whether the data is copied (the default), or whether
          a view is constructed.

        EXAMPLES::

            sage: # needs numpy
            sage: a = matrix(3, range(12))
            sage: a.numpy()
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]])
            sage: a.numpy('f')
            array([[  0.,   1.,   2.,   3.],
                   [  4.,   5.,   6.,   7.],
                   [  8.,   9.,  10.,  11.]], dtype=float32)
            sage: a.numpy('d')
            array([[  0.,   1.,   2.,   3.],
                   [  4.,   5.,   6.,   7.],
                   [  8.,   9.,  10.,  11.]])
            sage: a.numpy('B')
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]], dtype=uint8)

        Type ``numpy.typecodes`` for a list of the possible
        typecodes::

            sage: import numpy                            # needs numpy
            sage: numpy.typecodes.items()                 # needs numpy # random
            [('All', '?bhilqpBHILQPefdgFDGSUVOMm'), ('AllFloat', 'efdgFDG'),
            ...

        For instance, you can see possibilities for real floating point numbers::

            sage: numpy.typecodes['Float']                # needs numpy
            'efdg'

        Alternatively, numpy automatically calls this function (via
        the magic :meth:`__array__` method) to convert Sage matrices
        to numpy arrays::

            sage: # needs numpy
            sage: import numpy
            sage: b = numpy.array(a); b
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]])
            sage: b.dtype
            dtype('int32')  # 32-bit
            dtype('int64')  # 64-bit
            sage: b.shape
            (3, 4)"""
    def row(self, Py_ssize_ti, from_list=...) -> Any:
        """Matrix.row(self, Py_ssize_t i, from_list=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1461)

        Return the ``i``-th row of this matrix as a vector.

        This row is a dense vector if and only if the matrix is a dense
        matrix.

        INPUT:

        - ``i`` -- integer

        - ``from_list`` -- boolean (default: ``False``); if ``True``, returns the
          ``i``-th element of ``self.rows()`` (see :func:`rows`), which
          may be faster, but requires building a list of all rows the
          first time it is called after an entry of the matrix is
          changed.

        EXAMPLES::

            sage: a = matrix(2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.row(0)
            (0, 1, 2)
            sage: a.row(1)
            (3, 4, 5)
            sage: a.row(-1)  # last row
            (3, 4, 5)

        TESTS::

            sage: a = matrix(2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.row(2)
            Traceback (most recent call last):
            ...
            IndexError: row index out of range
            sage: a.row(-3)
            Traceback (most recent call last):
            ...
            IndexError: row index out of range"""
    @overload
    def row_ambient_module(self, base_ring=..., sparse=...) -> Any:
        """Matrix.row_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 892)

        Return the free module that contains the rows of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.row_ambient_module()
            Vector space of dimension 3 over Ring of integers modulo 5
            sage: M.row(1).parent() == M.row_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.row_ambient_module()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: M.row_ambient_module(QQ)
            Vector space of dimension 4 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.row_ambient_module()
            Vector space of dimension 5 over Rational Field
            sage: M.row_ambient_module(ZZ)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring"""
    @overload
    def row_ambient_module(self) -> Any:
        """Matrix.row_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 892)

        Return the free module that contains the rows of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.row_ambient_module()
            Vector space of dimension 3 over Ring of integers modulo 5
            sage: M.row(1).parent() == M.row_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.row_ambient_module()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: M.row_ambient_module(QQ)
            Vector space of dimension 4 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.row_ambient_module()
            Vector space of dimension 5 over Rational Field
            sage: M.row_ambient_module(ZZ)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring"""
    @overload
    def row_ambient_module(self) -> Any:
        """Matrix.row_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 892)

        Return the free module that contains the rows of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.row_ambient_module()
            Vector space of dimension 3 over Ring of integers modulo 5
            sage: M.row(1).parent() == M.row_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.row_ambient_module()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: M.row_ambient_module(QQ)
            Vector space of dimension 4 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.row_ambient_module()
            Vector space of dimension 5 over Rational Field
            sage: M.row_ambient_module(ZZ)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring"""
    @overload
    def row_ambient_module(self) -> Any:
        """Matrix.row_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 892)

        Return the free module that contains the rows of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.row_ambient_module()
            Vector space of dimension 3 over Ring of integers modulo 5
            sage: M.row(1).parent() == M.row_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.row_ambient_module()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: M.row_ambient_module(QQ)
            Vector space of dimension 4 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.row_ambient_module()
            Vector space of dimension 5 over Rational Field
            sage: M.row_ambient_module(ZZ)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring"""
    @overload
    def row_ambient_module(self, QQ) -> Any:
        """Matrix.row_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 892)

        Return the free module that contains the rows of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.row_ambient_module()
            Vector space of dimension 3 over Ring of integers modulo 5
            sage: M.row(1).parent() == M.row_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.row_ambient_module()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: M.row_ambient_module(QQ)
            Vector space of dimension 4 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.row_ambient_module()
            Vector space of dimension 5 over Rational Field
            sage: M.row_ambient_module(ZZ)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring"""
    @overload
    def row_ambient_module(self) -> Any:
        """Matrix.row_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 892)

        Return the free module that contains the rows of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.row_ambient_module()
            Vector space of dimension 3 over Ring of integers modulo 5
            sage: M.row(1).parent() == M.row_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.row_ambient_module()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: M.row_ambient_module(QQ)
            Vector space of dimension 4 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.row_ambient_module()
            Vector space of dimension 5 over Rational Field
            sage: M.row_ambient_module(ZZ)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring"""
    @overload
    def row_ambient_module(self, ZZ) -> Any:
        """Matrix.row_ambient_module(self, base_ring=None, sparse=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 892)

        Return the free module that contains the rows of the matrix.

        EXAMPLES::

            sage: M = matrix(Zmod(5), 2, 3)
            sage: M.row_ambient_module()
            Vector space of dimension 3 over Ring of integers modulo 5
            sage: M.row(1).parent() == M.row_ambient_module()
            True

            sage: M = Matrix(ZZ, 3, 4)
            sage: M.row_ambient_module()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: M.row_ambient_module(QQ)
            Vector space of dimension 4 over Rational Field

            sage: M = Matrix(QQ, 4, 5)
            sage: M.row_ambient_module()
            Vector space of dimension 5 over Rational Field
            sage: M.row_ambient_module(ZZ)
            Ambient free module of rank 5 over the principal ideal domain Integer Ring"""
    @overload
    def rows(self, copy=...) -> Any:
        """Matrix.rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1064)

        Return a list of the rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of rows which is safe to change

        If ``self`` is a sparse matrix, rows are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).rows()
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).rows()                        # needs sage.symbolic
            [(1.41421356237310, 3.14159265358979), (2.71828182845905, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).rows()
            []
            sage: matrix(RR, 2, 0, []).rows()
            [(), ()]
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.rows()[0])                                                   # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse rows.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.rows()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.rows('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def rows(self) -> Any:
        """Matrix.rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1064)

        Return a list of the rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of rows which is safe to change

        If ``self`` is a sparse matrix, rows are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).rows()
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).rows()                        # needs sage.symbolic
            [(1.41421356237310, 3.14159265358979), (2.71828182845905, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).rows()
            []
            sage: matrix(RR, 2, 0, []).rows()
            [(), ()]
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.rows()[0])                                                   # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse rows.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.rows()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.rows('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def rows(self) -> Any:
        """Matrix.rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1064)

        Return a list of the rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of rows which is safe to change

        If ``self`` is a sparse matrix, rows are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).rows()
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).rows()                        # needs sage.symbolic
            [(1.41421356237310, 3.14159265358979), (2.71828182845905, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).rows()
            []
            sage: matrix(RR, 2, 0, []).rows()
            [(), ()]
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.rows()[0])                                                   # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse rows.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.rows()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.rows('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def rows(self) -> Any:
        """Matrix.rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1064)

        Return a list of the rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of rows which is safe to change

        If ``self`` is a sparse matrix, rows are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).rows()
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).rows()                        # needs sage.symbolic
            [(1.41421356237310, 3.14159265358979), (2.71828182845905, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).rows()
            []
            sage: matrix(RR, 2, 0, []).rows()
            [(), ()]
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.rows()[0])                                                   # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse rows.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.rows()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.rows('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def rows(self) -> Any:
        """Matrix.rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1064)

        Return a list of the rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of rows which is safe to change

        If ``self`` is a sparse matrix, rows are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).rows()
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).rows()                        # needs sage.symbolic
            [(1.41421356237310, 3.14159265358979), (2.71828182845905, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).rows()
            []
            sage: matrix(RR, 2, 0, []).rows()
            [(), ()]
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.rows()[0])                                                   # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse rows.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.rows()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.rows('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def rows(self) -> Any:
        """Matrix.rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1064)

        Return a list of the rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of rows which is safe to change

        If ``self`` is a sparse matrix, rows are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).rows()
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).rows()                        # needs sage.symbolic
            [(1.41421356237310, 3.14159265358979), (2.71828182845905, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).rows()
            []
            sage: matrix(RR, 2, 0, []).rows()
            [(), ()]
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.rows()[0])                                                   # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse rows.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.rows()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.rows('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    @overload
    def rows(self) -> Any:
        """Matrix.rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1064)

        Return a list of the rows of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy of the list
          of rows which is safe to change

        If ``self`` is a sparse matrix, rows are returned as sparse vectors,
        otherwise returned vectors are dense.

        EXAMPLES::

            sage: matrix(3, [1..9]).rows()
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
            sage: matrix(RR, 2, [sqrt(2), pi, exp(1), 0]).rows()                        # needs sage.symbolic
            [(1.41421356237310, 3.14159265358979), (2.71828182845905, 0.000000000000000)]
            sage: matrix(RR, 0, 2, []).rows()
            []
            sage: matrix(RR, 2, 0, []).rows()
            [(), ()]
            sage: m = matrix(RR, 3, 3, {(1,2): pi, (2, 2): -1, (0,1): sqrt(2)})         # needs sage.symbolic
            sage: parent(m.rows()[0])                                                   # needs sage.symbolic
            Sparse vector space of dimension 3 over Real Field with 53 bits of precision

        Sparse matrices produce sparse rows.  ::

            sage: A = matrix(QQ, 2, range(4), sparse=True)
            sage: v = A.rows()[0]
            sage: v.is_sparse()
            True

        TESTS::

            sage: A = matrix(QQ, 4, range(16))
            sage: A.rows('junk')
            Traceback (most recent call last):
            ...
            ValueError: 'copy' must be ``True`` or False, not junk"""
    def set_column(self, col, v) -> Any:
        """Matrix.set_column(self, col, v)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2406)

        Set the entries of column ``col`` to the entries of ``v``.

        INPUT:

        - ``col`` -- index of column to be set

        - ``v`` -- list or vector of the new entries

        OUTPUT:

        Changes the matrix in-place, so there is no output.

        EXAMPLES:

        New entries may be contained in a vector.::

            sage: A = matrix(QQ, 5, range(25))
            sage: u = vector(QQ, [0, -1, -2, -3, -4])
            sage: A.set_column(2, u)
            sage: A
            [ 0  1  0  3  4]
            [ 5  6 -1  8  9]
            [10 11 -2 13 14]
            [15 16 -3 18 19]
            [20 21 -4 23 24]

        New entries may be in any sort of list.::

            sage: A = matrix([[1, 2], [3, 4]]); A
            [1 2]
            [3 4]
            sage: A.set_column(0, [0, 0]); A
            [0 2]
            [0 4]
            sage: A.set_column(1, (0, 0)); A
            [0 0]
            [0 0]

        TESTS::

            sage: A = matrix([[1, 2], [3, 4]])
            sage: A.set_column(2, [0, 0]); A
            Traceback (most recent call last):
            ...
            ValueError: column number must be between 0 and 1 (inclusive), not 2

            sage: A.set_column(0, [0, 0, 0])
            Traceback (most recent call last):
            ...
            ValueError: list of new entries must be of length 2 (not 3)

            sage: A = matrix(2, [1, 2, 3, 4])
            sage: A.set_column(0, [1/4, 1]); A
            Traceback (most recent call last):
            ...
            TypeError: Cannot set column with Rational Field elements
            over Integer Ring, use change_ring first."""
    def set_row(self, row, v) -> Any:
        """Matrix.set_row(self, row, v)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2333)

        Set the entries of row ``row`` to the entries of ``v``.

        INPUT:

        - ``row`` -- index of row to be set

        - ``v`` -- list or vector of the new entries

        OUTPUT:

        Changes the matrix in-place, so there is no output.

        EXAMPLES:

        New entries may be contained in a vector.::

            sage: A = matrix(QQ, 5, range(25))
            sage: u = vector(QQ, [0, -1, -2, -3, -4])
            sage: A.set_row(2, u)
            sage: A
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [ 0 -1 -2 -3 -4]
            [15 16 17 18 19]
            [20 21 22 23 24]

        New entries may be in any sort of list.::

            sage: A = matrix([[1, 2], [3, 4]]); A
            [1 2]
            [3 4]
            sage: A.set_row(0, [0, 0]); A
            [0 0]
            [3 4]
            sage: A.set_row(1, (0, 0)); A
            [0 0]
            [0 0]

        TESTS::

            sage: A = matrix([[1, 2], [3, 4]])
            sage: A.set_row(2, [0, 0]); A
            Traceback (most recent call last):
            ...
            ValueError: row number must be between 0 and 1 (inclusive), not 2

            sage: A.set_row(0, [0, 0, 0])
            Traceback (most recent call last):
            ...
            ValueError: list of new entries must be of length 2 (not 3)

            sage: A = matrix(2, [1, 2, 3, 4])
            sage: A.set_row(0, [1/3, 1]); A
            Traceback (most recent call last):
            ...
            TypeError: Cannot set row with Rational Field elements over Integer Ring, use change_ring first."""
    @overload
    def sparse_columns(self, copy=...) -> Any:
        """Matrix.sparse_columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1242)

        Return a list of the columns of ``self`` as sparse vectors (or free module elements).

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES::

            sage: a = matrix(2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: v = a.sparse_columns(); v
            [(0, 3), (1, 4), (2, 5)]
            sage: v[1].is_sparse()
            True

        TESTS:

        Columns of sparse matrices having no columns were fixed on :issue:`10714`::

            sage: m = matrix(10, 0, sparse=True)
            sage: m.ncols()
            0
            sage: m.columns()
            []

        Check that the returned columns are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9))
            sage: v = m.sparse_columns()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def sparse_columns(self) -> Any:
        """Matrix.sparse_columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1242)

        Return a list of the columns of ``self`` as sparse vectors (or free module elements).

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES::

            sage: a = matrix(2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: v = a.sparse_columns(); v
            [(0, 3), (1, 4), (2, 5)]
            sage: v[1].is_sparse()
            True

        TESTS:

        Columns of sparse matrices having no columns were fixed on :issue:`10714`::

            sage: m = matrix(10, 0, sparse=True)
            sage: m.ncols()
            0
            sage: m.columns()
            []

        Check that the returned columns are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9))
            sage: v = m.sparse_columns()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def sparse_columns(self) -> Any:
        """Matrix.sparse_columns(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1242)

        Return a list of the columns of ``self`` as sparse vectors (or free module elements).

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES::

            sage: a = matrix(2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: v = a.sparse_columns(); v
            [(0, 3), (1, 4), (2, 5)]
            sage: v[1].is_sparse()
            True

        TESTS:

        Columns of sparse matrices having no columns were fixed on :issue:`10714`::

            sage: m = matrix(10, 0, sparse=True)
            sage: m.ncols()
            0
            sage: m.columns()
            []

        Check that the returned columns are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9))
            sage: v = m.sparse_columns()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def sparse_matrix(self) -> Any:
        '''Matrix.sparse_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2660)

        If this matrix is dense, return a sparse matrix with the same
        entries. If this matrix is sparse, return this matrix (not a
        copy).

        .. NOTE::

           The definition of "dense" and "sparse" in Sage have nothing
           to do with the number of nonzero entries. Sparse and dense are
           properties of the underlying representation of the matrix.

        EXAMPLES::

            sage: A = MatrixSpace(QQ,2, sparse=False)([1,2,0,1])
            sage: A.is_sparse()
            False
            sage: B = A.sparse_matrix()
            sage: B.is_sparse()
            True
            sage: A == B
            True
            sage: B.sparse_matrix() is B
            True
            sage: A*B
            [1 4]
            [0 1]
            sage: A.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: B.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
            sage: (A*B).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: (B*A).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field'''
    @overload
    def sparse_matrix(self) -> Any:
        '''Matrix.sparse_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2660)

        If this matrix is dense, return a sparse matrix with the same
        entries. If this matrix is sparse, return this matrix (not a
        copy).

        .. NOTE::

           The definition of "dense" and "sparse" in Sage have nothing
           to do with the number of nonzero entries. Sparse and dense are
           properties of the underlying representation of the matrix.

        EXAMPLES::

            sage: A = MatrixSpace(QQ,2, sparse=False)([1,2,0,1])
            sage: A.is_sparse()
            False
            sage: B = A.sparse_matrix()
            sage: B.is_sparse()
            True
            sage: A == B
            True
            sage: B.sparse_matrix() is B
            True
            sage: A*B
            [1 4]
            [0 1]
            sage: A.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: B.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
            sage: (A*B).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: (B*A).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field'''
    @overload
    def sparse_matrix(self) -> Any:
        '''Matrix.sparse_matrix(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2660)

        If this matrix is dense, return a sparse matrix with the same
        entries. If this matrix is sparse, return this matrix (not a
        copy).

        .. NOTE::

           The definition of "dense" and "sparse" in Sage have nothing
           to do with the number of nonzero entries. Sparse and dense are
           properties of the underlying representation of the matrix.

        EXAMPLES::

            sage: A = MatrixSpace(QQ,2, sparse=False)([1,2,0,1])
            sage: A.is_sparse()
            False
            sage: B = A.sparse_matrix()
            sage: B.is_sparse()
            True
            sage: A == B
            True
            sage: B.sparse_matrix() is B
            True
            sage: A*B
            [1 4]
            [0 1]
            sage: A.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: B.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Rational Field
            sage: (A*B).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: (B*A).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field'''
    @overload
    def sparse_rows(self, copy=...) -> Any:
        """Matrix.sparse_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1319)

        Return a list of the rows of ``self`` as sparse vectors (or free module elements).

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.sparse_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: m.sparse_rows(copy=False) is m.sparse_rows(copy=False)
            True
            sage: v[1].is_sparse()
            True
            sage: m[0,0] = 10
            sage: m.sparse_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Rows of sparse matrices having no rows were fixed on :issue:`10714`::

            sage: m = matrix(0, 10, sparse=True)
            sage: m.nrows()
            0
            sage: m.rows()
            []

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9))
            sage: v = m.sparse_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def sparse_rows(self) -> Any:
        """Matrix.sparse_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1319)

        Return a list of the rows of ``self`` as sparse vectors (or free module elements).

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.sparse_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: m.sparse_rows(copy=False) is m.sparse_rows(copy=False)
            True
            sage: v[1].is_sparse()
            True
            sage: m[0,0] = 10
            sage: m.sparse_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Rows of sparse matrices having no rows were fixed on :issue:`10714`::

            sage: m = matrix(0, 10, sparse=True)
            sage: m.nrows()
            0
            sage: m.rows()
            []

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9))
            sage: v = m.sparse_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def sparse_rows(self) -> Any:
        """Matrix.sparse_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1319)

        Return a list of the rows of ``self`` as sparse vectors (or free module elements).

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.sparse_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: m.sparse_rows(copy=False) is m.sparse_rows(copy=False)
            True
            sage: v[1].is_sparse()
            True
            sage: m[0,0] = 10
            sage: m.sparse_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Rows of sparse matrices having no rows were fixed on :issue:`10714`::

            sage: m = matrix(0, 10, sparse=True)
            sage: m.nrows()
            0
            sage: m.rows()
            []

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9))
            sage: v = m.sparse_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def sparse_rows(self) -> Any:
        """Matrix.sparse_rows(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1319)

        Return a list of the rows of ``self`` as sparse vectors (or free module elements).

        INPUT:

        - ``copy`` -- boolean (default: ``True``); if ``True``, return a copy so you can
          modify it safely

        EXAMPLES::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9)); m
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = m.sparse_rows(); v
            [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
            sage: m.sparse_rows(copy=False) is m.sparse_rows(copy=False)
            True
            sage: v[1].is_sparse()
            True
            sage: m[0,0] = 10
            sage: m.sparse_rows()
            [(10, 1, 2), (3, 4, 5), (6, 7, 8)]

        TESTS:

        Rows of sparse matrices having no rows were fixed on :issue:`10714`::

            sage: m = matrix(0, 10, sparse=True)
            sage: m.nrows()
            0
            sage: m.rows()
            []

        Check that the returned rows are immutable as per :issue:`14874`::

            sage: m = Mat(ZZ, 3, 3, sparse=True)(range(9))
            sage: v = m.sparse_rows()
            sage: [x.is_mutable() for x in v]
            [False, False, False]"""
    @overload
    def stack(self, bottom, subdivide=...) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, v) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, v) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B, subdivide=...) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B, subdivide=...) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B, subdivide=...) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B, subdivide=...) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B, A) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, A) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, B) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, N) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, M) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, N) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, M) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    @overload
    def stack(self, N) -> Any:
        """Matrix.stack(self, bottom, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 1522)

        Return a new matrix formed by appending the matrix (or vector)
        ``bottom`` below ``self``::

            [  self  ]
            [ bottom ]

        INPUT:

        - ``bottom`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``bottom``

        OUTPUT:

        A new matrix formed by appending ``bottom`` beneath ``self``.
        If ``bottom`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a row vector.  (The code first
        converts a vector to a 1-row matrix.)

        If ``subdivide`` is ``True`` then any row subdivisions for
        the two matrices are preserved, and a new subdivision is added
        between ``self`` and ``bottom``.  If the column divisions are
        identical, then they are preserved, otherwise they are discarded.
        When ``subdivide`` is ``False`` there is no subdivision information
        in the result.

        .. warning::

            If ``subdivide`` is ``True`` then unequal column subdivisions
            will be discarded, since it would be ambiguous how to interpret
            them.  If the subdivision behavior is not what you need,
            you can manage subdivisions yourself with methods like
            :meth:`~sage.matrix.matrix2.Matrix.subdivisions`
            and
            :meth:`~sage.matrix.matrix2.Matrix.subdivide`.
            You might also find :func:`~sage.matrix.constructor.block_matrix`
            or
            :func:`~sage.matrix.constructor.block_diagonal_matrix`
            useful and simpler in some instances.

        EXAMPLES:

        Stacking with a matrix. ::

            sage: A = matrix(QQ, 4, 3, range(12))
            sage: B = matrix(QQ, 3, 3, range(9))
            sage: A.stack(B)
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]
            [ 9 10 11]
            [ 0  1  2]
            [ 3  4  5]
            [ 6  7  8]

        Stacking with a vector. ::

            sage: A = matrix(QQ, 3, 2, [0, 2, 4, 6, 8, 10])
            sage: v = vector(QQ, 2, [100, 200])
            sage: A.stack(v)
            [  0   2]
            [  4   6]
            [  8  10]
            [100 200]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(RR, [[1, 2],[3, 4]])
            sage: B = matrix(RR, [[10, 20, 30], [40, 50, 60]])
            sage: A.stack(B)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

            sage: v = vector(RR, [100, 200, 300])
            sage: A.stack(v)
            Traceback (most recent call last):
            ...
            TypeError: number of columns must be the same, not 2 and 3

        Setting ``subdivide`` to ``True`` will, in its simplest form,
        add a subdivision between ``self`` and ``bottom``. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        Row subdivisions are preserved by stacking, and enriched,
        if subdivisions are requested.  (So multiple stackings can
        be recorded.) ::

            sage: A = matrix(QQ, 2, 4, range(8))
            sage: A.subdivide([1], None)
            sage: B = matrix(QQ, 3, 4, range(12))
            sage: B.subdivide([2], None)
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3]
            [-----------]
            [ 4  5  6  7]
            [-----------]
            [ 0  1  2  3]
            [ 4  5  6  7]
            [-----------]
            [ 8  9 10 11]

        Column subdivisions can be preserved, but only if they are identical.
        Otherwise, this information is discarded and must be managed
        separately. ::

            sage: A = matrix(QQ, 2, 5, range(10))
            sage: A.subdivide(None, [2,4])
            sage: B = matrix(QQ, 3, 5, range(15))
            sage: B.subdivide(None, [2,4])
            sage: A.stack(B, subdivide=True)
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [-----+-----+--]
            [ 0  1| 2  3| 4]
            [ 5  6| 7  8| 9]
            [10 11|12 13|14]

            sage: A.subdivide(None, [1,2])
            sage: A.stack(B, subdivide=True)
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [--------------]
            [ 0  1  2  3  4]
            [ 5  6  7  8  9]
            [10 11 12 13 14]

        The base ring of the result is the common parent for the base
        rings of ``self`` and ``bottom``. In particular, the parent for
        ``A.stack(B)`` and ``B.stack(A)`` should be equal::

            sage: A = matrix(QQ, 1, 2, [1,2])
            sage: B = matrix(RR, 1, 2, [sin(1.1), sin(2.2)])
            sage: C = A.stack(B); C
            [ 1.00000000000000  2.00000000000000]
            [0.891207360061435 0.808496403819590]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

            sage: D = B.stack(A); D
            [0.891207360061435 0.808496403819590]
            [ 1.00000000000000  2.00000000000000]
            sage: D.parent()
            Full MatrixSpace of 2 by 2 dense matrices
             over Real Field with 53 bits of precision

        ::

            sage: R.<y> = PolynomialRing(ZZ)
            sage: A = matrix(QQ, 1, 2, [1, 2/3])
            sage: B = matrix(R, 1, 2, [y, y^2])

            sage: C = A.stack(B); C
            [  1 2/3]
            [  y y^2]
            sage: C.parent()
            Full MatrixSpace of 2 by 2 dense matrices over
             Univariate Polynomial Ring in y over Rational Field

        Stacking a dense matrix atop a sparse one returns a sparse
        matrix::

            sage: M = Matrix(ZZ, 2, 3, range(6), sparse=False)
            sage: N = diagonal_matrix([10,11,12], sparse=True)
            sage: P = M.stack(N); P
            [ 0  1  2]
            [ 3  4  5]
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            sage: P.is_sparse()
            True
            sage: P = N.stack(M); P
            [10  0  0]
            [ 0 11  0]
            [ 0  0 12]
            [ 0  1  2]
            [ 3  4  5]
            sage: P.is_sparse()
            True

        One can stack matrices over different rings (:issue:`16399`). ::

            sage: M = Matrix(ZZ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]
            sage: N.stack(M)
            [10 11 12]
            [ 0  1  2]
            [ 3  4  5]

        TESTS:

        A legacy test from the original implementation.  ::

            sage: M = Matrix(QQ, 2, 3, range(6))
            sage: N = Matrix(QQ, 1, 3, [10,11,12])
            sage: M.stack(N)
            [ 0  1  2]
            [ 3  4  5]
            [10 11 12]

        Non-matrices fail gracefully::

            sage: M.stack(polygen(QQ))
            Traceback (most recent call last):
            ...
            TypeError: a matrix must be stacked with another matrix or a vector

        AUTHORS:

        - Rob Beezer (2011-03-19): rewritten to mirror code for :meth:`augment`

        - Jeroen Demeyer (2015-01-06): refactor, see :issue:`16399`.
          Put all boilerplate in one place (here) and put the actual
          type-dependent implementation in ``_stack_impl``."""
    def submatrix(self, Py_ssize_trow=..., Py_ssize_tcol=..., Py_ssize_tnrows=..., Py_ssize_tncols=...) -> Any:
        """Matrix.submatrix(self, Py_ssize_t row=0, Py_ssize_t col=0, Py_ssize_t nrows=-1, Py_ssize_t ncols=-1)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2274)

        Return the matrix constructed from ``self`` using the specified
        range of rows and columns.

        INPUT:

        - ``row``, ``col`` -- index of the starting row and column (indices
          start at zero)

        - ``nrows``, ``ncols`` -- (optional) number of rows and columns to
          take. If not provided, take all rows below and all columns to
          the right of the starting entry.

        .. SEEALSO::

            The functions :func:`matrix_from_rows`,
            :func:`matrix_from_columns`, and
            :func:`matrix_from_rows_and_columns` allow one to select
            arbitrary subsets of rows and/or columns.

        EXAMPLES:

        Take the `3 \\times 3` submatrix starting from entry (1,1) in a
        `4 \\times 4` matrix::

            sage: m = matrix(4, [1..16])
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

            sage: m.submatrix(1, 1, 0)
            []
            sage: parent(m.submatrix(1, 1, 0))
            Full MatrixSpace of 0 by 3 dense matrices over Integer Ring"""
    @overload
    def zero_pattern_matrix(self, ring=...) -> Any:
        """Matrix.zero_pattern_matrix(self, ring=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2480)

        Return a matrix that contains one for corresponding zero entries.

        All other entries are zero.

        INPUT:

        - ``ring`` -- (optional); base ring of the output; default is ``ZZ``

        OUTPUT:

        A new dense matrix with same dimensions as ``self``
        and with base ring ``ring``.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, [1,2,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

            sage: M = Matrix(QQ, 2, [1,2/3,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

        Default base ring for the output is ``ZZ``::

            sage: M.zero_pattern_matrix().base_ring()
            Integer Ring

        Specify a different base ring for the output::

            sage: M.zero_pattern_matrix(GF(2)).base_ring()
            Finite Field of size 2

        Examples for different base rings for ``self``::

            sage: M = Matrix(Zmod(8), 3, 2, [2, 3, 9, 8, 1, 0]); M
            [2 3]
            [1 0]
            [1 0]
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]
            [0 1]

        ::

            sage: W.<a> = CyclotomicField(100)                                          # needs sage.rings.number_field
            sage: M = Matrix(2, 3, [a, a/2, 0, a^2, a^100-1, a^2 - a]); M               # needs sage.rings.number_field
            [      a   1/2*a       0]
            [    a^2       0 a^2 - a]
            sage: M.zero_pattern_matrix()                                               # needs sage.rings.number_field
            [0 0 1]
            [0 1 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(2^4)
            sage: l = [a^2 + 1, a^3 + 1, 0, 0, a, a^3 + a + 1, a + 1,
            ....:      a + 1, a^2, a^3 + a + 1, a^3 + a, a^3 + a]
            sage: M = Matrix(K, 3, 4, l); M
            [    a^2 + 1     a^3 + 1           0           0]
            [          a a^3 + a + 1       a + 1       a + 1]
            [        a^2 a^3 + a + 1     a^3 + a     a^3 + a]
            sage: M.zero_pattern_matrix()
            [0 0 1 1]
            [0 0 0 0]
            [0 0 0 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(25)
            sage: M = Matrix(K, 2, 3, [0, 2, 3, 5, a, a^2])
            sage: M
            [    0     2     3]
            [    0     a a + 3]
            sage: M.zero_pattern_matrix()
            [1 0 0]
            [1 0 0]

        .. NOTE::

            This method can be optimized by improving
            :meth:`get_is_zero_unsafe` for derived matrix classes."""
    @overload
    def zero_pattern_matrix(self) -> Any:
        """Matrix.zero_pattern_matrix(self, ring=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2480)

        Return a matrix that contains one for corresponding zero entries.

        All other entries are zero.

        INPUT:

        - ``ring`` -- (optional); base ring of the output; default is ``ZZ``

        OUTPUT:

        A new dense matrix with same dimensions as ``self``
        and with base ring ``ring``.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, [1,2,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

            sage: M = Matrix(QQ, 2, [1,2/3,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

        Default base ring for the output is ``ZZ``::

            sage: M.zero_pattern_matrix().base_ring()
            Integer Ring

        Specify a different base ring for the output::

            sage: M.zero_pattern_matrix(GF(2)).base_ring()
            Finite Field of size 2

        Examples for different base rings for ``self``::

            sage: M = Matrix(Zmod(8), 3, 2, [2, 3, 9, 8, 1, 0]); M
            [2 3]
            [1 0]
            [1 0]
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]
            [0 1]

        ::

            sage: W.<a> = CyclotomicField(100)                                          # needs sage.rings.number_field
            sage: M = Matrix(2, 3, [a, a/2, 0, a^2, a^100-1, a^2 - a]); M               # needs sage.rings.number_field
            [      a   1/2*a       0]
            [    a^2       0 a^2 - a]
            sage: M.zero_pattern_matrix()                                               # needs sage.rings.number_field
            [0 0 1]
            [0 1 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(2^4)
            sage: l = [a^2 + 1, a^3 + 1, 0, 0, a, a^3 + a + 1, a + 1,
            ....:      a + 1, a^2, a^3 + a + 1, a^3 + a, a^3 + a]
            sage: M = Matrix(K, 3, 4, l); M
            [    a^2 + 1     a^3 + 1           0           0]
            [          a a^3 + a + 1       a + 1       a + 1]
            [        a^2 a^3 + a + 1     a^3 + a     a^3 + a]
            sage: M.zero_pattern_matrix()
            [0 0 1 1]
            [0 0 0 0]
            [0 0 0 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(25)
            sage: M = Matrix(K, 2, 3, [0, 2, 3, 5, a, a^2])
            sage: M
            [    0     2     3]
            [    0     a a + 3]
            sage: M.zero_pattern_matrix()
            [1 0 0]
            [1 0 0]

        .. NOTE::

            This method can be optimized by improving
            :meth:`get_is_zero_unsafe` for derived matrix classes."""
    @overload
    def zero_pattern_matrix(self) -> Any:
        """Matrix.zero_pattern_matrix(self, ring=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2480)

        Return a matrix that contains one for corresponding zero entries.

        All other entries are zero.

        INPUT:

        - ``ring`` -- (optional); base ring of the output; default is ``ZZ``

        OUTPUT:

        A new dense matrix with same dimensions as ``self``
        and with base ring ``ring``.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, [1,2,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

            sage: M = Matrix(QQ, 2, [1,2/3,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

        Default base ring for the output is ``ZZ``::

            sage: M.zero_pattern_matrix().base_ring()
            Integer Ring

        Specify a different base ring for the output::

            sage: M.zero_pattern_matrix(GF(2)).base_ring()
            Finite Field of size 2

        Examples for different base rings for ``self``::

            sage: M = Matrix(Zmod(8), 3, 2, [2, 3, 9, 8, 1, 0]); M
            [2 3]
            [1 0]
            [1 0]
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]
            [0 1]

        ::

            sage: W.<a> = CyclotomicField(100)                                          # needs sage.rings.number_field
            sage: M = Matrix(2, 3, [a, a/2, 0, a^2, a^100-1, a^2 - a]); M               # needs sage.rings.number_field
            [      a   1/2*a       0]
            [    a^2       0 a^2 - a]
            sage: M.zero_pattern_matrix()                                               # needs sage.rings.number_field
            [0 0 1]
            [0 1 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(2^4)
            sage: l = [a^2 + 1, a^3 + 1, 0, 0, a, a^3 + a + 1, a + 1,
            ....:      a + 1, a^2, a^3 + a + 1, a^3 + a, a^3 + a]
            sage: M = Matrix(K, 3, 4, l); M
            [    a^2 + 1     a^3 + 1           0           0]
            [          a a^3 + a + 1       a + 1       a + 1]
            [        a^2 a^3 + a + 1     a^3 + a     a^3 + a]
            sage: M.zero_pattern_matrix()
            [0 0 1 1]
            [0 0 0 0]
            [0 0 0 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(25)
            sage: M = Matrix(K, 2, 3, [0, 2, 3, 5, a, a^2])
            sage: M
            [    0     2     3]
            [    0     a a + 3]
            sage: M.zero_pattern_matrix()
            [1 0 0]
            [1 0 0]

        .. NOTE::

            This method can be optimized by improving
            :meth:`get_is_zero_unsafe` for derived matrix classes."""
    @overload
    def zero_pattern_matrix(self) -> Any:
        """Matrix.zero_pattern_matrix(self, ring=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2480)

        Return a matrix that contains one for corresponding zero entries.

        All other entries are zero.

        INPUT:

        - ``ring`` -- (optional); base ring of the output; default is ``ZZ``

        OUTPUT:

        A new dense matrix with same dimensions as ``self``
        and with base ring ``ring``.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, [1,2,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

            sage: M = Matrix(QQ, 2, [1,2/3,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

        Default base ring for the output is ``ZZ``::

            sage: M.zero_pattern_matrix().base_ring()
            Integer Ring

        Specify a different base ring for the output::

            sage: M.zero_pattern_matrix(GF(2)).base_ring()
            Finite Field of size 2

        Examples for different base rings for ``self``::

            sage: M = Matrix(Zmod(8), 3, 2, [2, 3, 9, 8, 1, 0]); M
            [2 3]
            [1 0]
            [1 0]
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]
            [0 1]

        ::

            sage: W.<a> = CyclotomicField(100)                                          # needs sage.rings.number_field
            sage: M = Matrix(2, 3, [a, a/2, 0, a^2, a^100-1, a^2 - a]); M               # needs sage.rings.number_field
            [      a   1/2*a       0]
            [    a^2       0 a^2 - a]
            sage: M.zero_pattern_matrix()                                               # needs sage.rings.number_field
            [0 0 1]
            [0 1 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(2^4)
            sage: l = [a^2 + 1, a^3 + 1, 0, 0, a, a^3 + a + 1, a + 1,
            ....:      a + 1, a^2, a^3 + a + 1, a^3 + a, a^3 + a]
            sage: M = Matrix(K, 3, 4, l); M
            [    a^2 + 1     a^3 + 1           0           0]
            [          a a^3 + a + 1       a + 1       a + 1]
            [        a^2 a^3 + a + 1     a^3 + a     a^3 + a]
            sage: M.zero_pattern_matrix()
            [0 0 1 1]
            [0 0 0 0]
            [0 0 0 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(25)
            sage: M = Matrix(K, 2, 3, [0, 2, 3, 5, a, a^2])
            sage: M
            [    0     2     3]
            [    0     a a + 3]
            sage: M.zero_pattern_matrix()
            [1 0 0]
            [1 0 0]

        .. NOTE::

            This method can be optimized by improving
            :meth:`get_is_zero_unsafe` for derived matrix classes."""
    @overload
    def zero_pattern_matrix(self) -> Any:
        """Matrix.zero_pattern_matrix(self, ring=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2480)

        Return a matrix that contains one for corresponding zero entries.

        All other entries are zero.

        INPUT:

        - ``ring`` -- (optional); base ring of the output; default is ``ZZ``

        OUTPUT:

        A new dense matrix with same dimensions as ``self``
        and with base ring ``ring``.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, [1,2,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

            sage: M = Matrix(QQ, 2, [1,2/3,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

        Default base ring for the output is ``ZZ``::

            sage: M.zero_pattern_matrix().base_ring()
            Integer Ring

        Specify a different base ring for the output::

            sage: M.zero_pattern_matrix(GF(2)).base_ring()
            Finite Field of size 2

        Examples for different base rings for ``self``::

            sage: M = Matrix(Zmod(8), 3, 2, [2, 3, 9, 8, 1, 0]); M
            [2 3]
            [1 0]
            [1 0]
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]
            [0 1]

        ::

            sage: W.<a> = CyclotomicField(100)                                          # needs sage.rings.number_field
            sage: M = Matrix(2, 3, [a, a/2, 0, a^2, a^100-1, a^2 - a]); M               # needs sage.rings.number_field
            [      a   1/2*a       0]
            [    a^2       0 a^2 - a]
            sage: M.zero_pattern_matrix()                                               # needs sage.rings.number_field
            [0 0 1]
            [0 1 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(2^4)
            sage: l = [a^2 + 1, a^3 + 1, 0, 0, a, a^3 + a + 1, a + 1,
            ....:      a + 1, a^2, a^3 + a + 1, a^3 + a, a^3 + a]
            sage: M = Matrix(K, 3, 4, l); M
            [    a^2 + 1     a^3 + 1           0           0]
            [          a a^3 + a + 1       a + 1       a + 1]
            [        a^2 a^3 + a + 1     a^3 + a     a^3 + a]
            sage: M.zero_pattern_matrix()
            [0 0 1 1]
            [0 0 0 0]
            [0 0 0 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(25)
            sage: M = Matrix(K, 2, 3, [0, 2, 3, 5, a, a^2])
            sage: M
            [    0     2     3]
            [    0     a a + 3]
            sage: M.zero_pattern_matrix()
            [1 0 0]
            [1 0 0]

        .. NOTE::

            This method can be optimized by improving
            :meth:`get_is_zero_unsafe` for derived matrix classes."""
    @overload
    def zero_pattern_matrix(self) -> Any:
        """Matrix.zero_pattern_matrix(self, ring=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2480)

        Return a matrix that contains one for corresponding zero entries.

        All other entries are zero.

        INPUT:

        - ``ring`` -- (optional); base ring of the output; default is ``ZZ``

        OUTPUT:

        A new dense matrix with same dimensions as ``self``
        and with base ring ``ring``.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, [1,2,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

            sage: M = Matrix(QQ, 2, [1,2/3,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

        Default base ring for the output is ``ZZ``::

            sage: M.zero_pattern_matrix().base_ring()
            Integer Ring

        Specify a different base ring for the output::

            sage: M.zero_pattern_matrix(GF(2)).base_ring()
            Finite Field of size 2

        Examples for different base rings for ``self``::

            sage: M = Matrix(Zmod(8), 3, 2, [2, 3, 9, 8, 1, 0]); M
            [2 3]
            [1 0]
            [1 0]
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]
            [0 1]

        ::

            sage: W.<a> = CyclotomicField(100)                                          # needs sage.rings.number_field
            sage: M = Matrix(2, 3, [a, a/2, 0, a^2, a^100-1, a^2 - a]); M               # needs sage.rings.number_field
            [      a   1/2*a       0]
            [    a^2       0 a^2 - a]
            sage: M.zero_pattern_matrix()                                               # needs sage.rings.number_field
            [0 0 1]
            [0 1 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(2^4)
            sage: l = [a^2 + 1, a^3 + 1, 0, 0, a, a^3 + a + 1, a + 1,
            ....:      a + 1, a^2, a^3 + a + 1, a^3 + a, a^3 + a]
            sage: M = Matrix(K, 3, 4, l); M
            [    a^2 + 1     a^3 + 1           0           0]
            [          a a^3 + a + 1       a + 1       a + 1]
            [        a^2 a^3 + a + 1     a^3 + a     a^3 + a]
            sage: M.zero_pattern_matrix()
            [0 0 1 1]
            [0 0 0 0]
            [0 0 0 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(25)
            sage: M = Matrix(K, 2, 3, [0, 2, 3, 5, a, a^2])
            sage: M
            [    0     2     3]
            [    0     a a + 3]
            sage: M.zero_pattern_matrix()
            [1 0 0]
            [1 0 0]

        .. NOTE::

            This method can be optimized by improving
            :meth:`get_is_zero_unsafe` for derived matrix classes."""
    @overload
    def zero_pattern_matrix(self) -> Any:
        """Matrix.zero_pattern_matrix(self, ring=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2480)

        Return a matrix that contains one for corresponding zero entries.

        All other entries are zero.

        INPUT:

        - ``ring`` -- (optional); base ring of the output; default is ``ZZ``

        OUTPUT:

        A new dense matrix with same dimensions as ``self``
        and with base ring ``ring``.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, [1,2,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

            sage: M = Matrix(QQ, 2, [1,2/3,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

        Default base ring for the output is ``ZZ``::

            sage: M.zero_pattern_matrix().base_ring()
            Integer Ring

        Specify a different base ring for the output::

            sage: M.zero_pattern_matrix(GF(2)).base_ring()
            Finite Field of size 2

        Examples for different base rings for ``self``::

            sage: M = Matrix(Zmod(8), 3, 2, [2, 3, 9, 8, 1, 0]); M
            [2 3]
            [1 0]
            [1 0]
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]
            [0 1]

        ::

            sage: W.<a> = CyclotomicField(100)                                          # needs sage.rings.number_field
            sage: M = Matrix(2, 3, [a, a/2, 0, a^2, a^100-1, a^2 - a]); M               # needs sage.rings.number_field
            [      a   1/2*a       0]
            [    a^2       0 a^2 - a]
            sage: M.zero_pattern_matrix()                                               # needs sage.rings.number_field
            [0 0 1]
            [0 1 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(2^4)
            sage: l = [a^2 + 1, a^3 + 1, 0, 0, a, a^3 + a + 1, a + 1,
            ....:      a + 1, a^2, a^3 + a + 1, a^3 + a, a^3 + a]
            sage: M = Matrix(K, 3, 4, l); M
            [    a^2 + 1     a^3 + 1           0           0]
            [          a a^3 + a + 1       a + 1       a + 1]
            [        a^2 a^3 + a + 1     a^3 + a     a^3 + a]
            sage: M.zero_pattern_matrix()
            [0 0 1 1]
            [0 0 0 0]
            [0 0 0 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(25)
            sage: M = Matrix(K, 2, 3, [0, 2, 3, 5, a, a^2])
            sage: M
            [    0     2     3]
            [    0     a a + 3]
            sage: M.zero_pattern_matrix()
            [1 0 0]
            [1 0 0]

        .. NOTE::

            This method can be optimized by improving
            :meth:`get_is_zero_unsafe` for derived matrix classes."""
    @overload
    def zero_pattern_matrix(self) -> Any:
        """Matrix.zero_pattern_matrix(self, ring=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 2480)

        Return a matrix that contains one for corresponding zero entries.

        All other entries are zero.

        INPUT:

        - ``ring`` -- (optional); base ring of the output; default is ``ZZ``

        OUTPUT:

        A new dense matrix with same dimensions as ``self``
        and with base ring ``ring``.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, [1,2,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

            sage: M = Matrix(QQ, 2, [1,2/3,-2,0])
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]

        Default base ring for the output is ``ZZ``::

            sage: M.zero_pattern_matrix().base_ring()
            Integer Ring

        Specify a different base ring for the output::

            sage: M.zero_pattern_matrix(GF(2)).base_ring()
            Finite Field of size 2

        Examples for different base rings for ``self``::

            sage: M = Matrix(Zmod(8), 3, 2, [2, 3, 9, 8, 1, 0]); M
            [2 3]
            [1 0]
            [1 0]
            sage: M.zero_pattern_matrix()
            [0 0]
            [0 1]
            [0 1]

        ::

            sage: W.<a> = CyclotomicField(100)                                          # needs sage.rings.number_field
            sage: M = Matrix(2, 3, [a, a/2, 0, a^2, a^100-1, a^2 - a]); M               # needs sage.rings.number_field
            [      a   1/2*a       0]
            [    a^2       0 a^2 - a]
            sage: M.zero_pattern_matrix()                                               # needs sage.rings.number_field
            [0 0 1]
            [0 1 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(2^4)
            sage: l = [a^2 + 1, a^3 + 1, 0, 0, a, a^3 + a + 1, a + 1,
            ....:      a + 1, a^2, a^3 + a + 1, a^3 + a, a^3 + a]
            sage: M = Matrix(K, 3, 4, l); M
            [    a^2 + 1     a^3 + 1           0           0]
            [          a a^3 + a + 1       a + 1       a + 1]
            [        a^2 a^3 + a + 1     a^3 + a     a^3 + a]
            sage: M.zero_pattern_matrix()
            [0 0 1 1]
            [0 0 0 0]
            [0 0 0 0]

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(25)
            sage: M = Matrix(K, 2, 3, [0, 2, 3, 5, a, a^2])
            sage: M
            [    0     2     3]
            [    0     a a + 3]
            sage: M.zero_pattern_matrix()
            [1 0 0]
            [1 0 0]

        .. NOTE::

            This method can be optimized by improving
            :meth:`get_is_zero_unsafe` for derived matrix classes."""
    def __array__(self, *args, **kwargs):
        """Matrix.numpy(self, dtype=None, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 676)

        Return the Numpy matrix associated to this matrix.

        INPUT:

        - ``dtype`` -- the desired data-type for the array. If not given,
          then the type will be determined as the minimum type required
          to hold the objects in the sequence.

        - ``copy`` -- if `self` is already an `ndarray`, then this flag
          determines whether the data is copied (the default), or whether
          a view is constructed.

        EXAMPLES::

            sage: # needs numpy
            sage: a = matrix(3, range(12))
            sage: a.numpy()
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]])
            sage: a.numpy('f')
            array([[  0.,   1.,   2.,   3.],
                   [  4.,   5.,   6.,   7.],
                   [  8.,   9.,  10.,  11.]], dtype=float32)
            sage: a.numpy('d')
            array([[  0.,   1.,   2.,   3.],
                   [  4.,   5.,   6.,   7.],
                   [  8.,   9.,  10.,  11.]])
            sage: a.numpy('B')
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]], dtype=uint8)

        Type ``numpy.typecodes`` for a list of the possible
        typecodes::

            sage: import numpy                            # needs numpy
            sage: numpy.typecodes.items()                 # needs numpy # random
            [('All', '?bhilqpBHILQPefdgFDGSUVOMm'), ('AllFloat', 'efdgFDG'),
            ...

        For instance, you can see possibilities for real floating point numbers::

            sage: numpy.typecodes['Float']                # needs numpy
            'efdg'

        Alternatively, numpy automatically calls this function (via
        the magic :meth:`__array__` method) to convert Sage matrices
        to numpy arrays::

            sage: # needs numpy
            sage: import numpy
            sage: b = numpy.array(a); b
            array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]])
            sage: b.dtype
            dtype('int32')  # 32-bit
            dtype('int64')  # 64-bit
            sage: b.shape
            (3, 4)"""
    def __pari__(self) -> Any:
        """Matrix.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix1.pyx (starting at line 62)

        Return the Pari matrix corresponding to ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: a = matrix(R,2,[x+1,2/3,  x^2/2, 1+x^3]); a
            [  x + 1     2/3]
            [1/2*x^2 x^3 + 1]
            sage: b = pari(a); b  # indirect doctest                                    # needs sage.libs.pari
            [x + 1, 2/3; 1/2*x^2, x^3 + 1]
            sage: a.determinant()
            x^4 + x^3 - 1/3*x^2 + x + 1
            sage: b.matdet()                                                            # needs sage.libs.pari
            x^4 + x^3 - 1/3*x^2 + x + 1

        This function preserves precision for entries of inexact type (e.g.
        reals)::

            sage: R = RealField(4)       # 4 bits of precision
            sage: a = matrix(R, 2, [1, 2, 3, 1]); a
            [1.0 2.0]
            [3.0 1.0]
            sage: b = pari(a); b                                                        # needs sage.libs.pari
            [1.000000000, 2.000000000; 3.000000000, 1.000000000] # 32-bit
            [1.00000000000000, 2.00000000000000; 3.00000000000000, 1.00000000000000] # 64-bit"""
