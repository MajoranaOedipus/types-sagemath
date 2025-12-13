import sage.matrix.matrix_generic_dense
from sage.categories.fields import Fields as Fields
from sage.libs.singular.function import singular_function as singular_function
from sage.rings.polynomial.polynomial_singular_interface import can_convert_to_singular as can_convert_to_singular
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Matrix_mpolynomial_dense(sage.matrix.matrix_generic_dense.Matrix_generic_dense):
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 30)

        Dense matrix over a multivariate polynomial ring over a field.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def determinant(self, algorithm=...) -> Any:
        """Matrix_mpolynomial_dense.determinant(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 512)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- ignored

        EXAMPLES:

        We compute the determinant of the arbitrary `3x3` matrix::

            sage: R = PolynomialRing(QQ, 9, 'x')
            sage: A = matrix(R, 3, R.gens())
            sage: A
            [x0 x1 x2]
            [x3 x4 x5]
            [x6 x7 x8]
            sage: A.determinant()
            -x2*x4*x6 + x1*x5*x6 + x2*x3*x7 - x0*x5*x7 - x1*x3*x8 + x0*x4*x8

        We check if two implementations agree on the result::

            sage: R.<x,y> = QQ[]
            sage: C = matrix(R, [[-6/5*x*y - y^2, -6*y^2 - 1/4*y],
            ....:                [  -1/3*x*y - 3, x*y - x]])
            sage: C.determinant()
            -6/5*x^2*y^2 - 3*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 - 18*y^2 - 3/4*y

            sage: C.change_ring(R.change_ring(QQbar)).det()
            (-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y

        Finally, we check whether the Singular interface is working::

            sage: R.<x,y> = RR[]
            sage: C = matrix(R, [[0.368965517352886*y^2 + 0.425700773972636*x, -0.800362171389760*y^2 - 0.807635502485287],
            ....:                [0.706173539423122*y^2 - 0.915986060298440, 0.897165181570476*y + 0.107903328188376]])
            sage: C.determinant()
            0.565194587390682*y^4 + 0.33102301536914...*y^3 + 0.381923912175852*x*y - 0.122977163520282*y^2 + 0.0459345303240150*x - 0.739782862078649

        ALGORITHM: Calls Singular, libSingular or native implementation.

        TESTS::

            sage: R = PolynomialRing(QQ, 9, 'x')
            sage: matrix(R, 0, 0).det()
            1

            sage: R.<h,y> = QQ[]
            sage: m = matrix([[y,y,y,y]] * 4)  # larger than 3x3
            sage: m.charpoly()   # put charpoly in the cache
            x^4 - 4*y*x^3
            sage: m.det()
            0

        Check :issue:`23535` is fixed::

            sage: x = polygen(QQ)
            sage: K.<a,b> = NumberField([x^2 - 2, x^2 - 5])
            sage: R.<s,t> = K[]
            sage: m = matrix(R, 4, [y^i for i in range(4) for y in [a,b,s,t]])
            sage: m.det()
            (a - b)*s^3*t^2 + (-a + b)*s^2*t^3 + 3*s^3*t + (-3)*s*t^3 + (-5*a + 2*b)*s^3 + (2*a - 5*b)*s^2*t +
            (-2*a + 5*b)*s*t^2 + (5*a - 2*b)*t^3 + 3*b*a*s^2 + (-3*b*a)*t^2 + (10*a - 10*b)*s + (-10*a + 10*b)*t"""
    @overload
    def determinant(self) -> Any:
        """Matrix_mpolynomial_dense.determinant(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 512)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- ignored

        EXAMPLES:

        We compute the determinant of the arbitrary `3x3` matrix::

            sage: R = PolynomialRing(QQ, 9, 'x')
            sage: A = matrix(R, 3, R.gens())
            sage: A
            [x0 x1 x2]
            [x3 x4 x5]
            [x6 x7 x8]
            sage: A.determinant()
            -x2*x4*x6 + x1*x5*x6 + x2*x3*x7 - x0*x5*x7 - x1*x3*x8 + x0*x4*x8

        We check if two implementations agree on the result::

            sage: R.<x,y> = QQ[]
            sage: C = matrix(R, [[-6/5*x*y - y^2, -6*y^2 - 1/4*y],
            ....:                [  -1/3*x*y - 3, x*y - x]])
            sage: C.determinant()
            -6/5*x^2*y^2 - 3*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 - 18*y^2 - 3/4*y

            sage: C.change_ring(R.change_ring(QQbar)).det()
            (-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y

        Finally, we check whether the Singular interface is working::

            sage: R.<x,y> = RR[]
            sage: C = matrix(R, [[0.368965517352886*y^2 + 0.425700773972636*x, -0.800362171389760*y^2 - 0.807635502485287],
            ....:                [0.706173539423122*y^2 - 0.915986060298440, 0.897165181570476*y + 0.107903328188376]])
            sage: C.determinant()
            0.565194587390682*y^4 + 0.33102301536914...*y^3 + 0.381923912175852*x*y - 0.122977163520282*y^2 + 0.0459345303240150*x - 0.739782862078649

        ALGORITHM: Calls Singular, libSingular or native implementation.

        TESTS::

            sage: R = PolynomialRing(QQ, 9, 'x')
            sage: matrix(R, 0, 0).det()
            1

            sage: R.<h,y> = QQ[]
            sage: m = matrix([[y,y,y,y]] * 4)  # larger than 3x3
            sage: m.charpoly()   # put charpoly in the cache
            x^4 - 4*y*x^3
            sage: m.det()
            0

        Check :issue:`23535` is fixed::

            sage: x = polygen(QQ)
            sage: K.<a,b> = NumberField([x^2 - 2, x^2 - 5])
            sage: R.<s,t> = K[]
            sage: m = matrix(R, 4, [y^i for i in range(4) for y in [a,b,s,t]])
            sage: m.det()
            (a - b)*s^3*t^2 + (-a + b)*s^2*t^3 + 3*s^3*t + (-3)*s*t^3 + (-5*a + 2*b)*s^3 + (2*a - 5*b)*s^2*t +
            (-2*a + 5*b)*s*t^2 + (5*a - 2*b)*t^3 + 3*b*a*s^2 + (-3*b*a)*t^2 + (10*a - 10*b)*s + (-10*a + 10*b)*t"""
    @overload
    def determinant(self) -> Any:
        """Matrix_mpolynomial_dense.determinant(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 512)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- ignored

        EXAMPLES:

        We compute the determinant of the arbitrary `3x3` matrix::

            sage: R = PolynomialRing(QQ, 9, 'x')
            sage: A = matrix(R, 3, R.gens())
            sage: A
            [x0 x1 x2]
            [x3 x4 x5]
            [x6 x7 x8]
            sage: A.determinant()
            -x2*x4*x6 + x1*x5*x6 + x2*x3*x7 - x0*x5*x7 - x1*x3*x8 + x0*x4*x8

        We check if two implementations agree on the result::

            sage: R.<x,y> = QQ[]
            sage: C = matrix(R, [[-6/5*x*y - y^2, -6*y^2 - 1/4*y],
            ....:                [  -1/3*x*y - 3, x*y - x]])
            sage: C.determinant()
            -6/5*x^2*y^2 - 3*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 - 18*y^2 - 3/4*y

            sage: C.change_ring(R.change_ring(QQbar)).det()
            (-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y

        Finally, we check whether the Singular interface is working::

            sage: R.<x,y> = RR[]
            sage: C = matrix(R, [[0.368965517352886*y^2 + 0.425700773972636*x, -0.800362171389760*y^2 - 0.807635502485287],
            ....:                [0.706173539423122*y^2 - 0.915986060298440, 0.897165181570476*y + 0.107903328188376]])
            sage: C.determinant()
            0.565194587390682*y^4 + 0.33102301536914...*y^3 + 0.381923912175852*x*y - 0.122977163520282*y^2 + 0.0459345303240150*x - 0.739782862078649

        ALGORITHM: Calls Singular, libSingular or native implementation.

        TESTS::

            sage: R = PolynomialRing(QQ, 9, 'x')
            sage: matrix(R, 0, 0).det()
            1

            sage: R.<h,y> = QQ[]
            sage: m = matrix([[y,y,y,y]] * 4)  # larger than 3x3
            sage: m.charpoly()   # put charpoly in the cache
            x^4 - 4*y*x^3
            sage: m.det()
            0

        Check :issue:`23535` is fixed::

            sage: x = polygen(QQ)
            sage: K.<a,b> = NumberField([x^2 - 2, x^2 - 5])
            sage: R.<s,t> = K[]
            sage: m = matrix(R, 4, [y^i for i in range(4) for y in [a,b,s,t]])
            sage: m.det()
            (a - b)*s^3*t^2 + (-a + b)*s^2*t^3 + 3*s^3*t + (-3)*s*t^3 + (-5*a + 2*b)*s^3 + (2*a - 5*b)*s^2*t +
            (-2*a + 5*b)*s*t^2 + (5*a - 2*b)*t^3 + 3*b*a*s^2 + (-3*b*a)*t^2 + (10*a - 10*b)*s + (-10*a + 10*b)*t"""
    @overload
    def determinant(self) -> Any:
        """Matrix_mpolynomial_dense.determinant(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 512)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- ignored

        EXAMPLES:

        We compute the determinant of the arbitrary `3x3` matrix::

            sage: R = PolynomialRing(QQ, 9, 'x')
            sage: A = matrix(R, 3, R.gens())
            sage: A
            [x0 x1 x2]
            [x3 x4 x5]
            [x6 x7 x8]
            sage: A.determinant()
            -x2*x4*x6 + x1*x5*x6 + x2*x3*x7 - x0*x5*x7 - x1*x3*x8 + x0*x4*x8

        We check if two implementations agree on the result::

            sage: R.<x,y> = QQ[]
            sage: C = matrix(R, [[-6/5*x*y - y^2, -6*y^2 - 1/4*y],
            ....:                [  -1/3*x*y - 3, x*y - x]])
            sage: C.determinant()
            -6/5*x^2*y^2 - 3*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 - 18*y^2 - 3/4*y

            sage: C.change_ring(R.change_ring(QQbar)).det()
            (-6/5)*x^2*y^2 + (-3)*x*y^3 + 6/5*x^2*y + 11/12*x*y^2 + (-18)*y^2 + (-3/4)*y

        Finally, we check whether the Singular interface is working::

            sage: R.<x,y> = RR[]
            sage: C = matrix(R, [[0.368965517352886*y^2 + 0.425700773972636*x, -0.800362171389760*y^2 - 0.807635502485287],
            ....:                [0.706173539423122*y^2 - 0.915986060298440, 0.897165181570476*y + 0.107903328188376]])
            sage: C.determinant()
            0.565194587390682*y^4 + 0.33102301536914...*y^3 + 0.381923912175852*x*y - 0.122977163520282*y^2 + 0.0459345303240150*x - 0.739782862078649

        ALGORITHM: Calls Singular, libSingular or native implementation.

        TESTS::

            sage: R = PolynomialRing(QQ, 9, 'x')
            sage: matrix(R, 0, 0).det()
            1

            sage: R.<h,y> = QQ[]
            sage: m = matrix([[y,y,y,y]] * 4)  # larger than 3x3
            sage: m.charpoly()   # put charpoly in the cache
            x^4 - 4*y*x^3
            sage: m.det()
            0

        Check :issue:`23535` is fixed::

            sage: x = polygen(QQ)
            sage: K.<a,b> = NumberField([x^2 - 2, x^2 - 5])
            sage: R.<s,t> = K[]
            sage: m = matrix(R, 4, [y^i for i in range(4) for y in [a,b,s,t]])
            sage: m.det()
            (a - b)*s^3*t^2 + (-a + b)*s^2*t^3 + 3*s^3*t + (-3)*s*t^3 + (-5*a + 2*b)*s^3 + (2*a - 5*b)*s^2*t +
            (-2*a + 5*b)*s*t^2 + (5*a - 2*b)*t^3 + 3*b*a*s^2 + (-3*b*a)*t^2 + (10*a - 10*b)*s + (-10*a + 10*b)*t"""
    @overload
    def echelon_form(self, algorithm=..., **kwds) -> Any:
        """Matrix_mpolynomial_dense.echelon_form(self, algorithm='row_reduction', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 34)

        Return an echelon form of ``self`` using chosen algorithm.

        By default only a usual row reduction with no divisions or column swaps
        is returned.

        If Gauss-Bareiss algorithm is chosen, column swaps are recorded and can
        be retrieved via :meth:`swapped_columns`.

        INPUT:

        - ``algorithm`` -- string, which algorithm to use (default:
          'row_reduction'). Valid options are:

            - ``'row_reduction'`` (default) -- reduce as far as
              possible, only divide by constant entries

            - ``'frac'`` -- reduced echelon form over fraction field

            - ``'bareiss'`` -- fraction free Gauss-Bareiss algorithm
              with column swaps

        OUTPUT:

        The row echelon form of A depending on the chosen algorithm,
        as an immutable matrix.  Note that ``self`` is *not* changed
        by this command. Use ``A.echelonize()`` to change `A` in
        place.

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(GF(127), 2)
            sage: A = matrix(P, 2, 2, [1, x, 1, y])
            sage: A
            [1 x]
            [1 y]
            sage: A.echelon_form()
            [     1      x]
            [     0 -x + y]


        The reduced row echelon form over the fraction field is as follows::

            sage: A.echelon_form('frac') # over fraction field
            [1 0]
            [0 1]

        Alternatively, the Gauss-Bareiss algorithm may be chosen::

            sage: E = A.echelon_form('bareiss'); E
            [    1     y]
            [    0 x - y]

        After the application of the Gauss-Bareiss algorithm the swapped columns
        may inspected::

            sage: E.swapped_columns(), E.pivots()
            ((0, 1), (0, 1))
            sage: A.swapped_columns(), A.pivots()
            (None, (0, 1))

        Another approach is to row reduce as far as possible::

            sage: A.echelon_form('row_reduction')
            [     1      x]
            [     0 -x + y]"""
    @overload
    def echelon_form(self) -> Any:
        """Matrix_mpolynomial_dense.echelon_form(self, algorithm='row_reduction', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 34)

        Return an echelon form of ``self`` using chosen algorithm.

        By default only a usual row reduction with no divisions or column swaps
        is returned.

        If Gauss-Bareiss algorithm is chosen, column swaps are recorded and can
        be retrieved via :meth:`swapped_columns`.

        INPUT:

        - ``algorithm`` -- string, which algorithm to use (default:
          'row_reduction'). Valid options are:

            - ``'row_reduction'`` (default) -- reduce as far as
              possible, only divide by constant entries

            - ``'frac'`` -- reduced echelon form over fraction field

            - ``'bareiss'`` -- fraction free Gauss-Bareiss algorithm
              with column swaps

        OUTPUT:

        The row echelon form of A depending on the chosen algorithm,
        as an immutable matrix.  Note that ``self`` is *not* changed
        by this command. Use ``A.echelonize()`` to change `A` in
        place.

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(GF(127), 2)
            sage: A = matrix(P, 2, 2, [1, x, 1, y])
            sage: A
            [1 x]
            [1 y]
            sage: A.echelon_form()
            [     1      x]
            [     0 -x + y]


        The reduced row echelon form over the fraction field is as follows::

            sage: A.echelon_form('frac') # over fraction field
            [1 0]
            [0 1]

        Alternatively, the Gauss-Bareiss algorithm may be chosen::

            sage: E = A.echelon_form('bareiss'); E
            [    1     y]
            [    0 x - y]

        After the application of the Gauss-Bareiss algorithm the swapped columns
        may inspected::

            sage: E.swapped_columns(), E.pivots()
            ((0, 1), (0, 1))
            sage: A.swapped_columns(), A.pivots()
            (None, (0, 1))

        Another approach is to row reduce as far as possible::

            sage: A.echelon_form('row_reduction')
            [     1      x]
            [     0 -x + y]"""
    def echelonize(self, algorithm=..., **kwds) -> Any:
        """Matrix_mpolynomial_dense.echelonize(self, algorithm='row_reduction', **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 157)

        Transform ``self`` into a matrix in echelon form over the same base ring as
        ``self``.

        If Gauss-Bareiss algorithm is chosen, column swaps are recorded and can
        be retrieved via :meth:`swapped_columns`.

        INPUT:

        - ``algorithm`` -- string, which algorithm to use. Valid options are:

            - ``'row_reduction'`` -- reduce as far as possible, only
              divide by constant entries

            - ``'bareiss'`` -- fraction free Gauss-Bareiss algorithm
              with column swaps

        EXAMPLES::

            sage: P.<x,y> = PolynomialRing(QQ, 2)
            sage: A = matrix(P, 2, 2, [1/2, x, 1, 3/4*y+1])
            sage: A
            [      1/2         x]
            [        1 3/4*y + 1]

            sage: B = copy(A)
            sage: B.echelonize('bareiss'); B
            [              1       3/4*y + 1]
            [              0 x - 3/8*y - 1/2]

            sage: B = copy(A)
            sage: B.echelonize('row_reduction'); B
            [               1              2*x]
            [               0 -2*x + 3/4*y + 1]

            sage: P.<x,y> = PolynomialRing(QQ, 2)
            sage: A = matrix(P,2,3,[2,x,0,3,y,1]); A
            [2 x 0]
            [3 y 1]

            sage: E = A.echelon_form('bareiss'); E
            [1 3 y]
            [0 2 x]
            sage: E.swapped_columns()
            (2, 0, 1)
            sage: A.pivots()
            (0, 1, 2)"""
    @overload
    def pivots(self) -> Any:
        """Matrix_mpolynomial_dense.pivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 125)

        Return the pivot column positions of this matrix as a list of integers.

        This returns a list, of the position of the first nonzero entry in each
        row of the echelon form.

        OUTPUT: list of Python ints

        EXAMPLES::

            sage: matrix([PolynomialRing(GF(2), 2, 'x').gen()]).pivots()
            (0,)
            sage: K = QQ['x,y']
            sage: x, y = K.gens()
            sage: m = matrix(K, [(-x, 1, y, x - y), (-x*y, y, y^2 - 1, x*y - y^2 + x), (-x*y + x, y - 1, y^2 - y - 2, x*y - y^2 + x + y)])
            sage: m.pivots()
            (0, 2)
            sage: m.rank()
            2"""
    @overload
    def pivots(self) -> Any:
        """Matrix_mpolynomial_dense.pivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 125)

        Return the pivot column positions of this matrix as a list of integers.

        This returns a list, of the position of the first nonzero entry in each
        row of the echelon form.

        OUTPUT: list of Python ints

        EXAMPLES::

            sage: matrix([PolynomialRing(GF(2), 2, 'x').gen()]).pivots()
            (0,)
            sage: K = QQ['x,y']
            sage: x, y = K.gens()
            sage: m = matrix(K, [(-x, 1, y, x - y), (-x*y, y, y^2 - 1, x*y - y^2 + x), (-x*y + x, y - 1, y^2 - y - 2, x*y - y^2 + x + y)])
            sage: m.pivots()
            (0, 2)
            sage: m.rank()
            2"""
    @overload
    def pivots(self) -> Any:
        """Matrix_mpolynomial_dense.pivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 125)

        Return the pivot column positions of this matrix as a list of integers.

        This returns a list, of the position of the first nonzero entry in each
        row of the echelon form.

        OUTPUT: list of Python ints

        EXAMPLES::

            sage: matrix([PolynomialRing(GF(2), 2, 'x').gen()]).pivots()
            (0,)
            sage: K = QQ['x,y']
            sage: x, y = K.gens()
            sage: m = matrix(K, [(-x, 1, y, x - y), (-x*y, y, y^2 - 1, x*y - y^2 + x), (-x*y + x, y - 1, y^2 - y - 2, x*y - y^2 + x + y)])
            sage: m.pivots()
            (0, 2)
            sage: m.rank()
            2"""
    @overload
    def swapped_columns(self) -> Any:
        """Matrix_mpolynomial_dense.swapped_columns(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 424)

        Return which columns were swapped during the Gauss-Bareiss reduction.

        OUTPUT:

        Return a tuple representing the column swaps during the last application
        of the Gauss-Bareiss algorithm (see :meth:`echelon_form` for details).

        The tuple as length equal to the rank of ``self`` and the value at the
        `i`-th position indicates the source column which was put as the `i`-th
        column.

        If no Gauss-Bareiss reduction was performed yet, None is
        returned.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: C = random_matrix(R, 2, 2, terms=2)
            sage: while C.rank() != 2:
            ....:     C = random_matrix(R, 2, 2, terms=2)
            sage: C.swapped_columns()
            sage: E = C.echelon_form('bareiss')
            sage: sorted(E.swapped_columns())
            [0, 1]"""
    @overload
    def swapped_columns(self) -> Any:
        """Matrix_mpolynomial_dense.swapped_columns(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 424)

        Return which columns were swapped during the Gauss-Bareiss reduction.

        OUTPUT:

        Return a tuple representing the column swaps during the last application
        of the Gauss-Bareiss algorithm (see :meth:`echelon_form` for details).

        The tuple as length equal to the rank of ``self`` and the value at the
        `i`-th position indicates the source column which was put as the `i`-th
        column.

        If no Gauss-Bareiss reduction was performed yet, None is
        returned.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: C = random_matrix(R, 2, 2, terms=2)
            sage: while C.rank() != 2:
            ....:     C = random_matrix(R, 2, 2, terms=2)
            sage: C.swapped_columns()
            sage: E = C.echelon_form('bareiss')
            sage: sorted(E.swapped_columns())
            [0, 1]"""
    @overload
    def swapped_columns(self) -> Any:
        """Matrix_mpolynomial_dense.swapped_columns(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_mpolynomial_dense.pyx (starting at line 424)

        Return which columns were swapped during the Gauss-Bareiss reduction.

        OUTPUT:

        Return a tuple representing the column swaps during the last application
        of the Gauss-Bareiss algorithm (see :meth:`echelon_form` for details).

        The tuple as length equal to the rank of ``self`` and the value at the
        `i`-th position indicates the source column which was put as the `i`-th
        column.

        If no Gauss-Bareiss reduction was performed yet, None is
        returned.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: C = random_matrix(R, 2, 2, terms=2)
            sage: while C.rank() != 2:
            ....:     C = random_matrix(R, 2, 2, terms=2)
            sage: C.swapped_columns()
            sage: E = C.echelon_form('bareiss')
            sage: sorted(E.swapped_columns())
            [0, 1]"""
