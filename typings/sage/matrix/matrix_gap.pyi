import sage.matrix.matrix_dense
from sage.categories.fields import Fields as Fields
from sage.libs.gap.libgap import libgap as libgap
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Matrix_gap(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_gap(parent, entries=None, copy=None, bool coerce=True)

    File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 19)

    A Sage matrix wrapper over a GAP matrix.

    EXAMPLES::

        sage: M = MatrixSpace(ZZ, 2, implementation='gap')
        sage: m1 = M([1, 0, 2, -3])
        sage: m2 = M([2, 2, 5, -1])
        sage: type(m1)
        <class 'sage.matrix.matrix_gap.Matrix_gap'>

        sage: m1 * m2
        [  2   2]
        [-11   7]
        sage: type(m1 * m2)
        <class 'sage.matrix.matrix_gap.Matrix_gap'>

        sage: M = MatrixSpace(QQ, 5, 3, implementation='gap')
        sage: m = M(range(15))
        sage: m.left_kernel()
        Vector space of degree 5 and dimension 3 over Rational Field
        Basis matrix:
        [ 1  0  0 -4  3]
        [ 0  1  0 -3  2]
        [ 0  0  1 -2  1]

        sage: M = MatrixSpace(ZZ, 10, implementation='gap')
        sage: m = M(range(100))
        sage: m.transpose().parent() is M
        True

        sage: # needs sage.rings.number_field
        sage: UCF = UniversalCyclotomicField()
        sage: M = MatrixSpace(UCF, 3, implementation='gap')
        sage: m = M([UCF.zeta(i) for i in range(1,10)])
        sage: m
        [               1               -1             E(3)]
        [            E(4)             E(5)          -E(3)^2]
        [            E(7)             E(8) -E(9)^4 - E(9)^7]
        sage: (m^2)[1,2]
        E(180)^32 - E(180)^33 + E(180)^68 - E(180)^69 + E(180)^104 - E(180)^141 - E(180)^156 + E(180)^176 - E(180)^177

    TESTS::

        sage: rings = [ZZ, QQ, UniversalCyclotomicField(), GF(2), GF(3)]
        sage: rings += [UniversalCyclotomicField()]                                     # needs sage.rings.number_field
        sage: for ring in rings:
        ....:     M = MatrixSpace(ring, 2, implementation='gap')
        ....:     TestSuite(M).run(skip=['_test_construction'])
        ....:     M = MatrixSpace(ring, 2, 3, implementation='gap')
        ....:     TestSuite(M).run(skip=['_test_construction'])"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 72)

                INPUT:

                - ``parent`` -- a matrix space

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``True`` (the default), convert elements to the
                  base ring before passing them to GAP. If ``False``, pass the
                  elements to GAP as given.

                TESTS::

                    sage: M = MatrixSpace(ZZ, 2, implementation='gap')
                    sage: M(0)
                    [0 0]
                    [0 0]
                    sage: M(1)
                    [1 0]
                    [0 1]
                    sage: M(2)
                    [2 0]
                    [0 2]
                    sage: type(M(0))
                    <class 'sage.matrix.matrix_gap.Matrix_gap'>
                    sage: type(M(1))
                    <class 'sage.matrix.matrix_gap.Matrix_gap'>
                    sage: type(M(2))
                    <class 'sage.matrix.matrix_gap.Matrix_gap'>

                    sage: M = MatrixSpace(QQ, 2, 3, implementation='gap')
                    sage: M(0)
                    [0 0 0]
                    [0 0 0]
                    sage: M(1)
                    Traceback (most recent call last):
                    ...
                    TypeError: nonzero scalar matrix must be square
                    sage: MatrixSpace(QQ, 1, 2, implementation='gap')(0)
                    [0 0]
                    sage: MatrixSpace(QQ, 2, 1, implementation='gap')(0)
                    [0]
                    [0]
        """
    @overload
    def determinant(self) -> Any:
        """Matrix_gap.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 425)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).determinant()
            1
            sage: M([2, 1, 3, 3]).determinant()
            3

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).determinant())
            Universal Cyclotomic Field"""
    @overload
    def determinant(self) -> Any:
        """Matrix_gap.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 425)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).determinant()
            1
            sage: M([2, 1, 3, 3]).determinant()
            3

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).determinant())
            Universal Cyclotomic Field"""
    @overload
    def determinant(self) -> Any:
        """Matrix_gap.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 425)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).determinant()
            1
            sage: M([2, 1, 3, 3]).determinant()
            3

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).determinant())
            Universal Cyclotomic Field"""
    @overload
    def determinant(self) -> Any:
        """Matrix_gap.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 425)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).determinant()
            1
            sage: M([2, 1, 3, 3]).determinant()
            3

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).determinant())
            Universal Cyclotomic Field"""
    @overload
    def determinant(self) -> Any:
        """Matrix_gap.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 425)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).determinant()
            1
            sage: M([2, 1, 3, 3]).determinant()
            3

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).determinant())
            Universal Cyclotomic Field"""
    @overload
    def determinant(self) -> Any:
        """Matrix_gap.determinant(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 425)

        Return the determinant of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).determinant()
            1
            sage: M([2, 1, 3, 3]).determinant()
            3

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).determinant())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).determinant())
            Universal Cyclotomic Field"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_gap.elementary_divisors(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 512)

        Return the list of elementary divisors of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 5, implementation='gap')
            sage: T = M([(i+1)**(j+1) for i in range(5) for j in range(5)])
            sage: T.elementary_divisors()
            [1, 2, 6, 24, 120]"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_gap.elementary_divisors(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 512)

        Return the list of elementary divisors of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 5, implementation='gap')
            sage: T = M([(i+1)**(j+1) for i in range(5) for j in range(5)])
            sage: T.elementary_divisors()
            [1, 2, 6, 24, 120]"""
    @overload
    def gap(self) -> GapElement:
        """Matrix_gap.gap(self) -> GapElement

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 169)

        Return the underlying gap object.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: m = M([1,2,2,1]).gap()
            sage: m
            [ [ 1, 2 ], [ 2, 1 ] ]
            sage: type(m)
            <class 'sage.libs.gap.element.GapElement_List'>

            sage: m.MatrixAutomorphisms()
            Group([ (1,2) ])"""
    @overload
    def gap(self) -> Any:
        """Matrix_gap.gap(self) -> GapElement

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 169)

        Return the underlying gap object.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: m = M([1,2,2,1]).gap()
            sage: m
            [ [ 1, 2 ], [ 2, 1 ] ]
            sage: type(m)
            <class 'sage.libs.gap.element.GapElement_List'>

            sage: m.MatrixAutomorphisms()
            Group([ (1,2) ])"""
    def minimal_polynomial(self, *args, **kwargs):
        """Matrix_gap.minpoly(self, var='x', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 497)

        Compute the minimal polynomial.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([0, 1, -1, -1]).minpoly()
            x^2 + x + 1"""
    @overload
    def minpoly(self, var=..., **kwds) -> Any:
        """Matrix_gap.minpoly(self, var='x', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 497)

        Compute the minimal polynomial.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([0, 1, -1, -1]).minpoly()
            x^2 + x + 1"""
    @overload
    def minpoly(self) -> Any:
        """Matrix_gap.minpoly(self, var='x', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 497)

        Compute the minimal polynomial.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([0, 1, -1, -1]).minpoly()
            x^2 + x + 1"""
    @overload
    def rank(self) -> Any:
        """Matrix_gap.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 483)

        Return the rank of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).rank()
            2
            sage: M([2, 1, 4, 2]).rank()
            1"""
    @overload
    def rank(self) -> Any:
        """Matrix_gap.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 483)

        Return the rank of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).rank()
            2
            sage: M([2, 1, 4, 2]).rank()
            1"""
    @overload
    def rank(self) -> Any:
        """Matrix_gap.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 483)

        Return the rank of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).rank()
            2
            sage: M([2, 1, 4, 2]).rank()
            1"""
    @overload
    def trace(self) -> Any:
        """Matrix_gap.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 454)

        Return the trace of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).trace()
            3
            sage: M([2, 1, 3, 3]).trace()
            5

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).trace())
            Universal Cyclotomic Field"""
    @overload
    def trace(self) -> Any:
        """Matrix_gap.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 454)

        Return the trace of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).trace()
            3
            sage: M([2, 1, 3, 3]).trace()
            5

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).trace())
            Universal Cyclotomic Field"""
    @overload
    def trace(self) -> Any:
        """Matrix_gap.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 454)

        Return the trace of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).trace()
            3
            sage: M([2, 1, 3, 3]).trace()
            5

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).trace())
            Universal Cyclotomic Field"""
    @overload
    def trace(self) -> Any:
        """Matrix_gap.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 454)

        Return the trace of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).trace()
            3
            sage: M([2, 1, 3, 3]).trace()
            5

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).trace())
            Universal Cyclotomic Field"""
    @overload
    def trace(self) -> Any:
        """Matrix_gap.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 454)

        Return the trace of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).trace()
            3
            sage: M([2, 1, 3, 3]).trace()
            5

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).trace())
            Universal Cyclotomic Field"""
    @overload
    def trace(self) -> Any:
        """Matrix_gap.trace(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 454)

        Return the trace of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: M([2, 1, 1, 1]).trace()
            3
            sage: M([2, 1, 3, 3]).trace()
            5

        TESTS::

            sage: M = MatrixSpace(ZZ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Integer Ring

            sage: M = MatrixSpace(QQ, 1, implementation='gap')
            sage: parent(M(1).trace())
            Rational Field

            sage: # needs sage.rings.number_field
            sage: M = MatrixSpace(UniversalCyclotomicField(), 1, implementation='gap')
            sage: parent(M(1).trace())
            Universal Cyclotomic Field"""
    @overload
    def transpose(self) -> Any:
        """Matrix_gap.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 369)

        Return the transpose of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: M([4,2,23,52]).transpose()
            [ 4 23]
            [ 2 52]

            sage: M = MatrixSpace(QQ, 1, 3, implementation='gap')
            sage: M([4,2,52]).transpose()
            [ 4]
            [ 2]
            [52]

        TESTS::

            sage: M = MatrixSpace(QQ, 2, 3, implementation='gap')
            sage: m = M(range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: m.transpose()
            [0|3]
            [1|4]
            [-+-]
            [2|5]

            sage: M = MatrixSpace(QQ, 0, 2, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: M = MatrixSpace(QQ, 2, 0, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_gap.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 369)

        Return the transpose of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: M([4,2,23,52]).transpose()
            [ 4 23]
            [ 2 52]

            sage: M = MatrixSpace(QQ, 1, 3, implementation='gap')
            sage: M([4,2,52]).transpose()
            [ 4]
            [ 2]
            [52]

        TESTS::

            sage: M = MatrixSpace(QQ, 2, 3, implementation='gap')
            sage: m = M(range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: m.transpose()
            [0|3]
            [1|4]
            [-+-]
            [2|5]

            sage: M = MatrixSpace(QQ, 0, 2, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: M = MatrixSpace(QQ, 2, 0, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_gap.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 369)

        Return the transpose of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: M([4,2,23,52]).transpose()
            [ 4 23]
            [ 2 52]

            sage: M = MatrixSpace(QQ, 1, 3, implementation='gap')
            sage: M([4,2,52]).transpose()
            [ 4]
            [ 2]
            [52]

        TESTS::

            sage: M = MatrixSpace(QQ, 2, 3, implementation='gap')
            sage: m = M(range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: m.transpose()
            [0|3]
            [1|4]
            [-+-]
            [2|5]

            sage: M = MatrixSpace(QQ, 0, 2, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: M = MatrixSpace(QQ, 2, 0, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_gap.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 369)

        Return the transpose of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: M([4,2,23,52]).transpose()
            [ 4 23]
            [ 2 52]

            sage: M = MatrixSpace(QQ, 1, 3, implementation='gap')
            sage: M([4,2,52]).transpose()
            [ 4]
            [ 2]
            [52]

        TESTS::

            sage: M = MatrixSpace(QQ, 2, 3, implementation='gap')
            sage: m = M(range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: m.transpose()
            [0|3]
            [1|4]
            [-+-]
            [2|5]

            sage: M = MatrixSpace(QQ, 0, 2, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: M = MatrixSpace(QQ, 2, 0, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_gap.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 369)

        Return the transpose of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: M([4,2,23,52]).transpose()
            [ 4 23]
            [ 2 52]

            sage: M = MatrixSpace(QQ, 1, 3, implementation='gap')
            sage: M([4,2,52]).transpose()
            [ 4]
            [ 2]
            [52]

        TESTS::

            sage: M = MatrixSpace(QQ, 2, 3, implementation='gap')
            sage: m = M(range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: m.transpose()
            [0|3]
            [1|4]
            [-+-]
            [2|5]

            sage: M = MatrixSpace(QQ, 0, 2, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: M = MatrixSpace(QQ, 2, 0, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def transpose(self) -> Any:
        """Matrix_gap.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 369)

        Return the transpose of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: M([4,2,23,52]).transpose()
            [ 4 23]
            [ 2 52]

            sage: M = MatrixSpace(QQ, 1, 3, implementation='gap')
            sage: M([4,2,52]).transpose()
            [ 4]
            [ 2]
            [52]

        TESTS::

            sage: M = MatrixSpace(QQ, 2, 3, implementation='gap')
            sage: m = M(range(6))
            sage: m.subdivide([1],[2])
            sage: m
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: m.transpose()
            [0|3]
            [1|4]
            [-+-]
            [2|5]

            sage: M = MatrixSpace(QQ, 0, 2, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([],[1])
            sage: m.subdivisions()
            ([], [1])
            sage: m.transpose().subdivisions()
            ([1], [])

            sage: M = MatrixSpace(QQ, 2, 0, implementation='gap')
            sage: m = M([])
            sage: m.subdivide([1],[])
            sage: m.subdivisions()
            ([1], [])
            sage: m.transpose().subdivisions()
            ([], [1])"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_gap.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 136)

        TESTS::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: m1 = M([1,2,0,3])
            sage: m2 = m1.__copy__()
            sage: m2
            [1 2]
            [0 3]
            sage: m1[0,1] = -2
            sage: m1
            [ 1 -2]
            [ 0  3]
            sage: m2
            [1 2]
            [0 3]"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_gap.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 136)

        TESTS::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: m1 = M([1,2,0,3])
            sage: m2 = m1.__copy__()
            sage: m2
            [1 2]
            [0 3]
            sage: m1[0,1] = -2
            sage: m1
            [ 1 -2]
            [ 0  3]
            sage: m2
            [1 2]
            [0 3]"""
    def __invert__(self) -> Any:
        """Matrix_gap.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 310)

        TESTS::

            sage: M = MatrixSpace(QQ, 2, implementation='gap')
            sage: ~M([4,2,2,2])
            [ 1/2 -1/2]
            [-1/2    1]"""
    def __neg__(self) -> Any:
        """Matrix_gap.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 296)

        TESTS::

            sage: M = MatrixSpace(ZZ, 2, 3, implementation='gap')
            sage: m = M([1, -1, 3, 2, -5, 1])
            sage: -m
            [-1  1 -3]
            [-2  5 -1]"""
    def __reduce__(self) -> Any:
        """Matrix_gap.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gap.pyx (starting at line 158)

        TESTS::

            sage: M = MatrixSpace(ZZ, 2, implementation='gap')
            sage: m = M([1,2,1,2])
            sage: loads(dumps(m)) == m
            True"""
