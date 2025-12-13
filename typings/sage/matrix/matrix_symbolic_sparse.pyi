import sage.matrix.matrix_generic_sparse
from sage.matrix.constructor import matrix as matrix
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.factorization import Factorization as Factorization
from typing import Any, ClassVar, overload

class Matrix_symbolic_sparse(sage.matrix.matrix_generic_sparse.Matrix_generic_sparse):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def arguments(self) -> Any:
        """Matrix_symbolic_sparse.arguments(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 883)

        Return a tuple of the arguments that ``self`` can take.

        EXAMPLES::

            sage: var('x,y,z')
            (x, y, z)
            sage: M = MatrixSpace(SR,2,2, sparse=True)
            sage: M(x).arguments()
            (x,)
            sage: M(x+sin(x)).arguments()
            (x,)"""
    @overload
    def arguments(self) -> Any:
        """Matrix_symbolic_sparse.arguments(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 883)

        Return a tuple of the arguments that ``self`` can take.

        EXAMPLES::

            sage: var('x,y,z')
            (x, y, z)
            sage: M = MatrixSpace(SR,2,2, sparse=True)
            sage: M(x).arguments()
            (x,)
            sage: M(x+sin(x)).arguments()
            (x,)"""
    @overload
    def arguments(self) -> Any:
        """Matrix_symbolic_sparse.arguments(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 883)

        Return a tuple of the arguments that ``self`` can take.

        EXAMPLES::

            sage: var('x,y,z')
            (x, y, z)
            sage: M = MatrixSpace(SR,2,2, sparse=True)
            sage: M(x).arguments()
            (x,)
            sage: M(x+sin(x)).arguments()
            (x,)"""
    @overload
    def canonicalize_radical(self) -> Any:
        """Matrix_symbolic_sparse.canonicalize_radical(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 807)

        Choose a canonical branch of each entry of ``self`` by calling
        :meth:`Expression.canonicalize_radical()` componentwise.

        EXAMPLES::

            sage: var('x','y')
            (x, y)
            sage: l1 = [sqrt(2)*sqrt(3)*sqrt(6) , log(x*y)]
            sage: l2 = [sin(x/(x^2 + x)) , 1]
            sage: m = matrix([l1, l2], sparse=True)
            sage: m
            [sqrt(6)*sqrt(3)*sqrt(2)                log(x*y)]
            [       sin(x/(x^2 + x))                       1]
            sage: m.canonicalize_radical()
            [              6 log(x) + log(y)]
            [ sin(1/(x + 1))               1]"""
    @overload
    def canonicalize_radical(self) -> Any:
        """Matrix_symbolic_sparse.canonicalize_radical(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 807)

        Choose a canonical branch of each entry of ``self`` by calling
        :meth:`Expression.canonicalize_radical()` componentwise.

        EXAMPLES::

            sage: var('x','y')
            (x, y)
            sage: l1 = [sqrt(2)*sqrt(3)*sqrt(6) , log(x*y)]
            sage: l2 = [sin(x/(x^2 + x)) , 1]
            sage: m = matrix([l1, l2], sparse=True)
            sage: m
            [sqrt(6)*sqrt(3)*sqrt(2)                log(x*y)]
            [       sin(x/(x^2 + x))                       1]
            sage: m.canonicalize_radical()
            [              6 log(x) + log(y)]
            [ sin(1/(x + 1))               1]"""
    @overload
    def canonicalize_radical(self) -> Any:
        """Matrix_symbolic_sparse.canonicalize_radical(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 807)

        Choose a canonical branch of each entry of ``self`` by calling
        :meth:`Expression.canonicalize_radical()` componentwise.

        EXAMPLES::

            sage: var('x','y')
            (x, y)
            sage: l1 = [sqrt(2)*sqrt(3)*sqrt(6) , log(x*y)]
            sage: l2 = [sin(x/(x^2 + x)) , 1]
            sage: m = matrix([l1, l2], sparse=True)
            sage: m
            [sqrt(6)*sqrt(3)*sqrt(2)                log(x*y)]
            [       sin(x/(x^2 + x))                       1]
            sage: m.canonicalize_radical()
            [              6 log(x) + log(y)]
            [ sin(1/(x + 1))               1]"""
    def charpoly(self, var=..., algorithm=...) -> Any:
        """Matrix_symbolic_sparse.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 478)

        Compute the characteristic polynomial of ``self``, using maxima.

        .. NOTE::

            The characteristic polynomial is defined as `\\det(xI-A)`.

        INPUT:

        - ``var`` -- (default: ``'x'``) name of variable of charpoly

        EXAMPLES::

            sage: M = matrix(SR, 2, 2, var('a,b,c,d'), sparse=True)
            sage: M.charpoly('t')
            t^2 + (-a - d)*t - b*c + a*d
            sage: matrix(SR, 5, [1..5^2], sparse=True).charpoly()
            x^5 - 65*x^4 - 250*x^3

        TESTS:

        The cached polynomial should be independent of the ``var``
        argument (:issue:`12292`). We check (indirectly) that the
        second call uses the cached value by noting that its result is
        not cached::

            sage: M = MatrixSpace(SR, 2, sparse=True)
            sage: A = M(range(0, 2^2))
            sage: type(A)
            <class 'sage.matrix.matrix_symbolic_sparse.Matrix_symbolic_sparse'>
            sage: A.charpoly('x')
            x^2 - 3*x - 2
            sage: A.charpoly('y')
            y^2 - 3*y - 2
            sage: A._cache['charpoly']
            x^2 - 3*x - 2

        Ensure the variable name of the polynomial does not conflict
        with variables used within the matrix (:issue:`14403`)::

            sage: Matrix(SR, [[sqrt(x), x],[1,x]], sparse=True).charpoly().list()
            [x^(3/2) - x, -x - sqrt(x), 1]

        Test that :issue:`13711` is fixed::

            sage: matrix([[sqrt(2), -1], [pi, e^2]], sparse=True).charpoly()
            x^2 + (-sqrt(2) - e^2)*x + pi + sqrt(2)*e^2

        Test that :issue:`26427` is fixed::

            sage: M = matrix(SR, 7, 7, SR.var('a', 49), sparse=True)
            sage: M.charpoly().degree() # long time
            7"""
    @overload
    def echelonize(self, **kwds) -> Any:
        """Matrix_symbolic_sparse.echelonize(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 176)

        Echelonize using the classical algorithm.

        TESTS::

            sage: m = matrix([[cos(pi/5), sin(pi/5)], [-sin(pi/5), cos(pi/5)]], sparse=True)
            sage: m.echelonize(); m
            [1 0]
            [0 1]"""
    @overload
    def echelonize(self) -> Any:
        """Matrix_symbolic_sparse.echelonize(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 176)

        Echelonize using the classical algorithm.

        TESTS::

            sage: m = matrix([[cos(pi/5), sin(pi/5)], [-sin(pi/5), cos(pi/5)]], sparse=True)
            sage: m.echelonize(); m
            [1 0]
            [0 1]"""
    @overload
    def eigenvalues(self, extend=...) -> Any:
        """Matrix_symbolic_sparse.eigenvalues(self, extend=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 189)

        Compute the eigenvalues by solving the characteristic
        polynomial in maxima.

        The argument ``extend`` is ignored but kept for compatibility with
        other matrix classes.

        EXAMPLES::

            sage: a=matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.eigenvalues()
            [-1/2*sqrt(33) + 5/2, 1/2*sqrt(33) + 5/2]

        TESTS:

        Check for :issue:`31700`::

            sage: m = matrix([[cos(pi/5), sin(pi/5)], [-sin(pi/5), cos(pi/5)]], sparse=True)
            sage: t = linear_transformation(m)
            sage: t.eigenvalues()
            [1/4*sqrt(5) - 1/4*sqrt(2*sqrt(5) - 10) + 1/4,
             1/4*sqrt(5) + 1/4*sqrt(2*sqrt(5) - 10) + 1/4]"""
    @overload
    def eigenvalues(self) -> Any:
        """Matrix_symbolic_sparse.eigenvalues(self, extend=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 189)

        Compute the eigenvalues by solving the characteristic
        polynomial in maxima.

        The argument ``extend`` is ignored but kept for compatibility with
        other matrix classes.

        EXAMPLES::

            sage: a=matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.eigenvalues()
            [-1/2*sqrt(33) + 5/2, 1/2*sqrt(33) + 5/2]

        TESTS:

        Check for :issue:`31700`::

            sage: m = matrix([[cos(pi/5), sin(pi/5)], [-sin(pi/5), cos(pi/5)]], sparse=True)
            sage: t = linear_transformation(m)
            sage: t.eigenvalues()
            [1/4*sqrt(5) - 1/4*sqrt(2*sqrt(5) - 10) + 1/4,
             1/4*sqrt(5) + 1/4*sqrt(2*sqrt(5) - 10) + 1/4]"""
    @overload
    def eigenvalues(self) -> Any:
        """Matrix_symbolic_sparse.eigenvalues(self, extend=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 189)

        Compute the eigenvalues by solving the characteristic
        polynomial in maxima.

        The argument ``extend`` is ignored but kept for compatibility with
        other matrix classes.

        EXAMPLES::

            sage: a=matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.eigenvalues()
            [-1/2*sqrt(33) + 5/2, 1/2*sqrt(33) + 5/2]

        TESTS:

        Check for :issue:`31700`::

            sage: m = matrix([[cos(pi/5), sin(pi/5)], [-sin(pi/5), cos(pi/5)]], sparse=True)
            sage: t = linear_transformation(m)
            sage: t.eigenvalues()
            [1/4*sqrt(5) - 1/4*sqrt(2*sqrt(5) - 10) + 1/4,
             1/4*sqrt(5) + 1/4*sqrt(2*sqrt(5) - 10) + 1/4]"""
    @overload
    def eigenvectors_left(self, other=...) -> Any:
        '''Matrix_symbolic_sparse.eigenvectors_left(self, other=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 218)

        Compute the left eigenvectors of a matrix.

        INPUT:

        - ``other`` -- a square matrix `B` (default: ``None``) in a generalized
          eigenvalue problem; if ``None``, an ordinary eigenvalue problem is
          solved (currently supported only if the base ring of ``self`` is
          ``RDF`` or ``CDF``)

        OUTPUT:

        For each distinct eigenvalue, returns a list of the form (e,V,n)
        where e is the eigenvalue, V is a list of eigenvectors forming a
        basis for the corresponding left eigenspace, and n is the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: A = matrix(SR,3,3,range(9), sparse=True); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: es = A.eigenvectors_left(); es
            [(-3*sqrt(6) + 6, [(1, -1/5*sqrt(6) + 4/5, -2/5*sqrt(6) + 3/5)], 1),
             (3*sqrt(6) + 6, [(1, 1/5*sqrt(6) + 4/5, 2/5*sqrt(6) + 3/5)], 1),
             (0, [(1, -2, 1)], 1)]
            sage: eval, [evec], mult = es[0]
            sage: delta = eval*evec - evec*A
            sage: abs(abs(delta)) < 1e-10
            3/5*sqrt(((2*sqrt(6) - 3)*(sqrt(6) - 2) + 7*sqrt(6) - 18)^2 + ((sqrt(6) - 2)*(sqrt(6) - 4) + 6*sqrt(6) - 14)^2) < (1.00000000000000e-10)
            sage: abs(abs(delta)).n() < 1e-10
            True

        ::

            sage: A = matrix(SR, 2, 2, var(\'a,b,c,d\'), sparse=True)
            sage: A.eigenvectors_left()
            [(1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d + sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1), (1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d - sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1)]
            sage: es = A.eigenvectors_left(); es
            [(1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d + sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1), (1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d - sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1)]
            sage: eval, [evec], mult = es[0]
            sage: delta = eval*evec - evec*A
            sage: delta.apply_map(lambda x: x.full_simplify())
            (0, 0)

        This routine calls Maxima and can struggle with even small matrices
        with a few variables, such as a `3\\times 3` matrix with three variables.
        However, if the entries are integers or rationals it can produce exact
        values in a reasonable time.  These examples create 0-1 matrices from
        the adjacency matrices of graphs and illustrate how the format and type
        of the results differ when the base ring changes.  First for matrices
        over the rational numbers, then the same matrix but viewed as a symbolic
        matrix. ::

            sage: G=graphs.CycleGraph(5)
            sage: am = G.adjacency_matrix(sparse=True)
            sage: spectrum = am.eigenvectors_left()
            sage: qqbar_evalue = spectrum[2][0]
            sage: type(qqbar_evalue)
            <class \'sage.rings.qqbar.AlgebraicNumber\'>
            sage: qqbar_evalue
            0.618033988749895?

            sage: am = G.adjacency_matrix(sparse=True).change_ring(SR)
            sage: spectrum = am.eigenvectors_left()
            sage: symbolic_evalue = spectrum[2][0]
            sage: type(symbolic_evalue)
            <class \'sage.symbolic.expression.Expression\'>
            sage: symbolic_evalue
            1/2*sqrt(5) - 1/2

            sage: bool(qqbar_evalue == symbolic_evalue)
            True

        A slightly larger matrix with a "nice" spectrum. ::

            sage: G = graphs.CycleGraph(6)
            sage: am = G.adjacency_matrix(sparse=True).change_ring(SR)
            sage: am.eigenvectors_left()
            [(-1, [(1, 0, -1, 1, 0, -1), (0, 1, -1, 0, 1, -1)], 2), (1, [(1, 0, -1, -1, 0, 1), (0, 1, 1, 0, -1, -1)], 2), (-2, [(1, -1, 1, -1, 1, -1)], 1), (2, [(1, 1, 1, 1, 1, 1)], 1)]

        TESTS::

            sage: A = matrix(SR, [[1, 2], [3, 4]], sparse=True)
            sage: B = matrix(SR, [[1, 1], [0, 1]], sparse=True)
            sage: A.eigenvectors_left(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: generalized eigenvector decomposition is
            implemented for RDF and CDF, but not for Symbolic Ring

        Check that :issue:`23332` is fixed::

            sage: matrix([[x, x^2], [1, 0]], sparse=True).eigenvectors_left()
            [(-1/2*x*(sqrt(5) - 1), [(1, -1/2*x*(sqrt(5) + 1))], 1),
             (1/2*x*(sqrt(5) + 1), [(1, 1/2*x*(sqrt(5) - 1))], 1)]'''
    @overload
    def eigenvectors_left(self) -> Any:
        '''Matrix_symbolic_sparse.eigenvectors_left(self, other=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 218)

        Compute the left eigenvectors of a matrix.

        INPUT:

        - ``other`` -- a square matrix `B` (default: ``None``) in a generalized
          eigenvalue problem; if ``None``, an ordinary eigenvalue problem is
          solved (currently supported only if the base ring of ``self`` is
          ``RDF`` or ``CDF``)

        OUTPUT:

        For each distinct eigenvalue, returns a list of the form (e,V,n)
        where e is the eigenvalue, V is a list of eigenvectors forming a
        basis for the corresponding left eigenspace, and n is the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: A = matrix(SR,3,3,range(9), sparse=True); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: es = A.eigenvectors_left(); es
            [(-3*sqrt(6) + 6, [(1, -1/5*sqrt(6) + 4/5, -2/5*sqrt(6) + 3/5)], 1),
             (3*sqrt(6) + 6, [(1, 1/5*sqrt(6) + 4/5, 2/5*sqrt(6) + 3/5)], 1),
             (0, [(1, -2, 1)], 1)]
            sage: eval, [evec], mult = es[0]
            sage: delta = eval*evec - evec*A
            sage: abs(abs(delta)) < 1e-10
            3/5*sqrt(((2*sqrt(6) - 3)*(sqrt(6) - 2) + 7*sqrt(6) - 18)^2 + ((sqrt(6) - 2)*(sqrt(6) - 4) + 6*sqrt(6) - 14)^2) < (1.00000000000000e-10)
            sage: abs(abs(delta)).n() < 1e-10
            True

        ::

            sage: A = matrix(SR, 2, 2, var(\'a,b,c,d\'), sparse=True)
            sage: A.eigenvectors_left()
            [(1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d + sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1), (1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d - sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1)]
            sage: es = A.eigenvectors_left(); es
            [(1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d + sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1), (1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d - sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1)]
            sage: eval, [evec], mult = es[0]
            sage: delta = eval*evec - evec*A
            sage: delta.apply_map(lambda x: x.full_simplify())
            (0, 0)

        This routine calls Maxima and can struggle with even small matrices
        with a few variables, such as a `3\\times 3` matrix with three variables.
        However, if the entries are integers or rationals it can produce exact
        values in a reasonable time.  These examples create 0-1 matrices from
        the adjacency matrices of graphs and illustrate how the format and type
        of the results differ when the base ring changes.  First for matrices
        over the rational numbers, then the same matrix but viewed as a symbolic
        matrix. ::

            sage: G=graphs.CycleGraph(5)
            sage: am = G.adjacency_matrix(sparse=True)
            sage: spectrum = am.eigenvectors_left()
            sage: qqbar_evalue = spectrum[2][0]
            sage: type(qqbar_evalue)
            <class \'sage.rings.qqbar.AlgebraicNumber\'>
            sage: qqbar_evalue
            0.618033988749895?

            sage: am = G.adjacency_matrix(sparse=True).change_ring(SR)
            sage: spectrum = am.eigenvectors_left()
            sage: symbolic_evalue = spectrum[2][0]
            sage: type(symbolic_evalue)
            <class \'sage.symbolic.expression.Expression\'>
            sage: symbolic_evalue
            1/2*sqrt(5) - 1/2

            sage: bool(qqbar_evalue == symbolic_evalue)
            True

        A slightly larger matrix with a "nice" spectrum. ::

            sage: G = graphs.CycleGraph(6)
            sage: am = G.adjacency_matrix(sparse=True).change_ring(SR)
            sage: am.eigenvectors_left()
            [(-1, [(1, 0, -1, 1, 0, -1), (0, 1, -1, 0, 1, -1)], 2), (1, [(1, 0, -1, -1, 0, 1), (0, 1, 1, 0, -1, -1)], 2), (-2, [(1, -1, 1, -1, 1, -1)], 1), (2, [(1, 1, 1, 1, 1, 1)], 1)]

        TESTS::

            sage: A = matrix(SR, [[1, 2], [3, 4]], sparse=True)
            sage: B = matrix(SR, [[1, 1], [0, 1]], sparse=True)
            sage: A.eigenvectors_left(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: generalized eigenvector decomposition is
            implemented for RDF and CDF, but not for Symbolic Ring

        Check that :issue:`23332` is fixed::

            sage: matrix([[x, x^2], [1, 0]], sparse=True).eigenvectors_left()
            [(-1/2*x*(sqrt(5) - 1), [(1, -1/2*x*(sqrt(5) + 1))], 1),
             (1/2*x*(sqrt(5) + 1), [(1, 1/2*x*(sqrt(5) - 1))], 1)]'''
    @overload
    def eigenvectors_left(self) -> Any:
        '''Matrix_symbolic_sparse.eigenvectors_left(self, other=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 218)

        Compute the left eigenvectors of a matrix.

        INPUT:

        - ``other`` -- a square matrix `B` (default: ``None``) in a generalized
          eigenvalue problem; if ``None``, an ordinary eigenvalue problem is
          solved (currently supported only if the base ring of ``self`` is
          ``RDF`` or ``CDF``)

        OUTPUT:

        For each distinct eigenvalue, returns a list of the form (e,V,n)
        where e is the eigenvalue, V is a list of eigenvectors forming a
        basis for the corresponding left eigenspace, and n is the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: A = matrix(SR,3,3,range(9), sparse=True); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: es = A.eigenvectors_left(); es
            [(-3*sqrt(6) + 6, [(1, -1/5*sqrt(6) + 4/5, -2/5*sqrt(6) + 3/5)], 1),
             (3*sqrt(6) + 6, [(1, 1/5*sqrt(6) + 4/5, 2/5*sqrt(6) + 3/5)], 1),
             (0, [(1, -2, 1)], 1)]
            sage: eval, [evec], mult = es[0]
            sage: delta = eval*evec - evec*A
            sage: abs(abs(delta)) < 1e-10
            3/5*sqrt(((2*sqrt(6) - 3)*(sqrt(6) - 2) + 7*sqrt(6) - 18)^2 + ((sqrt(6) - 2)*(sqrt(6) - 4) + 6*sqrt(6) - 14)^2) < (1.00000000000000e-10)
            sage: abs(abs(delta)).n() < 1e-10
            True

        ::

            sage: A = matrix(SR, 2, 2, var(\'a,b,c,d\'), sparse=True)
            sage: A.eigenvectors_left()
            [(1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d + sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1), (1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d - sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1)]
            sage: es = A.eigenvectors_left(); es
            [(1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d + sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1), (1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d - sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1)]
            sage: eval, [evec], mult = es[0]
            sage: delta = eval*evec - evec*A
            sage: delta.apply_map(lambda x: x.full_simplify())
            (0, 0)

        This routine calls Maxima and can struggle with even small matrices
        with a few variables, such as a `3\\times 3` matrix with three variables.
        However, if the entries are integers or rationals it can produce exact
        values in a reasonable time.  These examples create 0-1 matrices from
        the adjacency matrices of graphs and illustrate how the format and type
        of the results differ when the base ring changes.  First for matrices
        over the rational numbers, then the same matrix but viewed as a symbolic
        matrix. ::

            sage: G=graphs.CycleGraph(5)
            sage: am = G.adjacency_matrix(sparse=True)
            sage: spectrum = am.eigenvectors_left()
            sage: qqbar_evalue = spectrum[2][0]
            sage: type(qqbar_evalue)
            <class \'sage.rings.qqbar.AlgebraicNumber\'>
            sage: qqbar_evalue
            0.618033988749895?

            sage: am = G.adjacency_matrix(sparse=True).change_ring(SR)
            sage: spectrum = am.eigenvectors_left()
            sage: symbolic_evalue = spectrum[2][0]
            sage: type(symbolic_evalue)
            <class \'sage.symbolic.expression.Expression\'>
            sage: symbolic_evalue
            1/2*sqrt(5) - 1/2

            sage: bool(qqbar_evalue == symbolic_evalue)
            True

        A slightly larger matrix with a "nice" spectrum. ::

            sage: G = graphs.CycleGraph(6)
            sage: am = G.adjacency_matrix(sparse=True).change_ring(SR)
            sage: am.eigenvectors_left()
            [(-1, [(1, 0, -1, 1, 0, -1), (0, 1, -1, 0, 1, -1)], 2), (1, [(1, 0, -1, -1, 0, 1), (0, 1, 1, 0, -1, -1)], 2), (-2, [(1, -1, 1, -1, 1, -1)], 1), (2, [(1, 1, 1, 1, 1, 1)], 1)]

        TESTS::

            sage: A = matrix(SR, [[1, 2], [3, 4]], sparse=True)
            sage: B = matrix(SR, [[1, 1], [0, 1]], sparse=True)
            sage: A.eigenvectors_left(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: generalized eigenvector decomposition is
            implemented for RDF and CDF, but not for Symbolic Ring

        Check that :issue:`23332` is fixed::

            sage: matrix([[x, x^2], [1, 0]], sparse=True).eigenvectors_left()
            [(-1/2*x*(sqrt(5) - 1), [(1, -1/2*x*(sqrt(5) + 1))], 1),
             (1/2*x*(sqrt(5) + 1), [(1, 1/2*x*(sqrt(5) - 1))], 1)]'''
    @overload
    def eigenvectors_left(self) -> Any:
        '''Matrix_symbolic_sparse.eigenvectors_left(self, other=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 218)

        Compute the left eigenvectors of a matrix.

        INPUT:

        - ``other`` -- a square matrix `B` (default: ``None``) in a generalized
          eigenvalue problem; if ``None``, an ordinary eigenvalue problem is
          solved (currently supported only if the base ring of ``self`` is
          ``RDF`` or ``CDF``)

        OUTPUT:

        For each distinct eigenvalue, returns a list of the form (e,V,n)
        where e is the eigenvalue, V is a list of eigenvectors forming a
        basis for the corresponding left eigenspace, and n is the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: A = matrix(SR,3,3,range(9), sparse=True); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: es = A.eigenvectors_left(); es
            [(-3*sqrt(6) + 6, [(1, -1/5*sqrt(6) + 4/5, -2/5*sqrt(6) + 3/5)], 1),
             (3*sqrt(6) + 6, [(1, 1/5*sqrt(6) + 4/5, 2/5*sqrt(6) + 3/5)], 1),
             (0, [(1, -2, 1)], 1)]
            sage: eval, [evec], mult = es[0]
            sage: delta = eval*evec - evec*A
            sage: abs(abs(delta)) < 1e-10
            3/5*sqrt(((2*sqrt(6) - 3)*(sqrt(6) - 2) + 7*sqrt(6) - 18)^2 + ((sqrt(6) - 2)*(sqrt(6) - 4) + 6*sqrt(6) - 14)^2) < (1.00000000000000e-10)
            sage: abs(abs(delta)).n() < 1e-10
            True

        ::

            sage: A = matrix(SR, 2, 2, var(\'a,b,c,d\'), sparse=True)
            sage: A.eigenvectors_left()
            [(1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d + sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1), (1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d - sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1)]
            sage: es = A.eigenvectors_left(); es
            [(1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d + sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1), (1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2), [(1, -1/2*(a - d - sqrt(a^2 + 4*b*c - 2*a*d + d^2))/c)], 1)]
            sage: eval, [evec], mult = es[0]
            sage: delta = eval*evec - evec*A
            sage: delta.apply_map(lambda x: x.full_simplify())
            (0, 0)

        This routine calls Maxima and can struggle with even small matrices
        with a few variables, such as a `3\\times 3` matrix with three variables.
        However, if the entries are integers or rationals it can produce exact
        values in a reasonable time.  These examples create 0-1 matrices from
        the adjacency matrices of graphs and illustrate how the format and type
        of the results differ when the base ring changes.  First for matrices
        over the rational numbers, then the same matrix but viewed as a symbolic
        matrix. ::

            sage: G=graphs.CycleGraph(5)
            sage: am = G.adjacency_matrix(sparse=True)
            sage: spectrum = am.eigenvectors_left()
            sage: qqbar_evalue = spectrum[2][0]
            sage: type(qqbar_evalue)
            <class \'sage.rings.qqbar.AlgebraicNumber\'>
            sage: qqbar_evalue
            0.618033988749895?

            sage: am = G.adjacency_matrix(sparse=True).change_ring(SR)
            sage: spectrum = am.eigenvectors_left()
            sage: symbolic_evalue = spectrum[2][0]
            sage: type(symbolic_evalue)
            <class \'sage.symbolic.expression.Expression\'>
            sage: symbolic_evalue
            1/2*sqrt(5) - 1/2

            sage: bool(qqbar_evalue == symbolic_evalue)
            True

        A slightly larger matrix with a "nice" spectrum. ::

            sage: G = graphs.CycleGraph(6)
            sage: am = G.adjacency_matrix(sparse=True).change_ring(SR)
            sage: am.eigenvectors_left()
            [(-1, [(1, 0, -1, 1, 0, -1), (0, 1, -1, 0, 1, -1)], 2), (1, [(1, 0, -1, -1, 0, 1), (0, 1, 1, 0, -1, -1)], 2), (-2, [(1, -1, 1, -1, 1, -1)], 1), (2, [(1, 1, 1, 1, 1, 1)], 1)]

        TESTS::

            sage: A = matrix(SR, [[1, 2], [3, 4]], sparse=True)
            sage: B = matrix(SR, [[1, 1], [0, 1]], sparse=True)
            sage: A.eigenvectors_left(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: generalized eigenvector decomposition is
            implemented for RDF and CDF, but not for Symbolic Ring

        Check that :issue:`23332` is fixed::

            sage: matrix([[x, x^2], [1, 0]], sparse=True).eigenvectors_left()
            [(-1/2*x*(sqrt(5) - 1), [(1, -1/2*x*(sqrt(5) + 1))], 1),
             (1/2*x*(sqrt(5) + 1), [(1, 1/2*x*(sqrt(5) - 1))], 1)]'''
    @overload
    def eigenvectors_right(self, other=...) -> Any:
        """Matrix_symbolic_sparse.eigenvectors_right(self, other=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 332)

        Compute the right eigenvectors of a matrix.

        INPUT:

        - ``other`` -- a square matrix `B` (default: ``None``) in a generalized
          eigenvalue problem; if ``None``, an ordinary eigenvalue problem is
          solved (currently supported only if the base ring of ``self`` is
          ``RDF`` or ``CDF``)

        OUTPUT:

        For each distinct eigenvalue, returns a list of the form (e,V,n)
        where e is the eigenvalue, V is a list of eigenvectors forming a
        basis for the corresponding right eigenspace, and n is the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: A = matrix(SR,2,2,range(4), sparse=True); A
            [0 1]
            [2 3]
            sage: right = A.eigenvectors_right(); right
            [(-1/2*sqrt(17) + 3/2, [(1, -1/2*sqrt(17) + 3/2)], 1), (1/2*sqrt(17) + 3/2, [(1, 1/2*sqrt(17) + 3/2)], 1)]

        The right eigenvectors are nothing but the left eigenvectors of the
        transpose matrix::

            sage: left  = A.transpose().eigenvectors_left(); left
            [(-1/2*sqrt(17) + 3/2, [(1, -1/2*sqrt(17) + 3/2)], 1), (1/2*sqrt(17) + 3/2, [(1, 1/2*sqrt(17) + 3/2)], 1)]
            sage: right[0][1] == left[0][1]
            True

        TESTS::

            sage: A = matrix(SR, [[1, 2], [3, 4]], sparse=True)
            sage: B = matrix(SR, [[1, 1], [0, 1]], sparse=True)
            sage: A.eigenvectors_right(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: generalized eigenvector decomposition is
            implemented for RDF and CDF, but not for Symbolic Ring

        Check that :issue:`23332` is fixed::

            sage: matrix([[x, x^2], [1, 0]], sparse=True).eigenvectors_right()
            [(-1/2*x*(sqrt(5) - 1), [(1, -1/2*(sqrt(5) + 1)/x)], 1),
             (1/2*x*(sqrt(5) + 1), [(1, 1/2*(sqrt(5) - 1)/x)], 1)]"""
    @overload
    def eigenvectors_right(self) -> Any:
        """Matrix_symbolic_sparse.eigenvectors_right(self, other=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 332)

        Compute the right eigenvectors of a matrix.

        INPUT:

        - ``other`` -- a square matrix `B` (default: ``None``) in a generalized
          eigenvalue problem; if ``None``, an ordinary eigenvalue problem is
          solved (currently supported only if the base ring of ``self`` is
          ``RDF`` or ``CDF``)

        OUTPUT:

        For each distinct eigenvalue, returns a list of the form (e,V,n)
        where e is the eigenvalue, V is a list of eigenvectors forming a
        basis for the corresponding right eigenspace, and n is the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: A = matrix(SR,2,2,range(4), sparse=True); A
            [0 1]
            [2 3]
            sage: right = A.eigenvectors_right(); right
            [(-1/2*sqrt(17) + 3/2, [(1, -1/2*sqrt(17) + 3/2)], 1), (1/2*sqrt(17) + 3/2, [(1, 1/2*sqrt(17) + 3/2)], 1)]

        The right eigenvectors are nothing but the left eigenvectors of the
        transpose matrix::

            sage: left  = A.transpose().eigenvectors_left(); left
            [(-1/2*sqrt(17) + 3/2, [(1, -1/2*sqrt(17) + 3/2)], 1), (1/2*sqrt(17) + 3/2, [(1, 1/2*sqrt(17) + 3/2)], 1)]
            sage: right[0][1] == left[0][1]
            True

        TESTS::

            sage: A = matrix(SR, [[1, 2], [3, 4]], sparse=True)
            sage: B = matrix(SR, [[1, 1], [0, 1]], sparse=True)
            sage: A.eigenvectors_right(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: generalized eigenvector decomposition is
            implemented for RDF and CDF, but not for Symbolic Ring

        Check that :issue:`23332` is fixed::

            sage: matrix([[x, x^2], [1, 0]], sparse=True).eigenvectors_right()
            [(-1/2*x*(sqrt(5) - 1), [(1, -1/2*(sqrt(5) + 1)/x)], 1),
             (1/2*x*(sqrt(5) + 1), [(1, 1/2*(sqrt(5) - 1)/x)], 1)]"""
    @overload
    def eigenvectors_right(self, B) -> Any:
        """Matrix_symbolic_sparse.eigenvectors_right(self, other=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 332)

        Compute the right eigenvectors of a matrix.

        INPUT:

        - ``other`` -- a square matrix `B` (default: ``None``) in a generalized
          eigenvalue problem; if ``None``, an ordinary eigenvalue problem is
          solved (currently supported only if the base ring of ``self`` is
          ``RDF`` or ``CDF``)

        OUTPUT:

        For each distinct eigenvalue, returns a list of the form (e,V,n)
        where e is the eigenvalue, V is a list of eigenvectors forming a
        basis for the corresponding right eigenspace, and n is the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: A = matrix(SR,2,2,range(4), sparse=True); A
            [0 1]
            [2 3]
            sage: right = A.eigenvectors_right(); right
            [(-1/2*sqrt(17) + 3/2, [(1, -1/2*sqrt(17) + 3/2)], 1), (1/2*sqrt(17) + 3/2, [(1, 1/2*sqrt(17) + 3/2)], 1)]

        The right eigenvectors are nothing but the left eigenvectors of the
        transpose matrix::

            sage: left  = A.transpose().eigenvectors_left(); left
            [(-1/2*sqrt(17) + 3/2, [(1, -1/2*sqrt(17) + 3/2)], 1), (1/2*sqrt(17) + 3/2, [(1, 1/2*sqrt(17) + 3/2)], 1)]
            sage: right[0][1] == left[0][1]
            True

        TESTS::

            sage: A = matrix(SR, [[1, 2], [3, 4]], sparse=True)
            sage: B = matrix(SR, [[1, 1], [0, 1]], sparse=True)
            sage: A.eigenvectors_right(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: generalized eigenvector decomposition is
            implemented for RDF and CDF, but not for Symbolic Ring

        Check that :issue:`23332` is fixed::

            sage: matrix([[x, x^2], [1, 0]], sparse=True).eigenvectors_right()
            [(-1/2*x*(sqrt(5) - 1), [(1, -1/2*(sqrt(5) + 1)/x)], 1),
             (1/2*x*(sqrt(5) + 1), [(1, 1/2*(sqrt(5) - 1)/x)], 1)]"""
    @overload
    def eigenvectors_right(self) -> Any:
        """Matrix_symbolic_sparse.eigenvectors_right(self, other=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 332)

        Compute the right eigenvectors of a matrix.

        INPUT:

        - ``other`` -- a square matrix `B` (default: ``None``) in a generalized
          eigenvalue problem; if ``None``, an ordinary eigenvalue problem is
          solved (currently supported only if the base ring of ``self`` is
          ``RDF`` or ``CDF``)

        OUTPUT:

        For each distinct eigenvalue, returns a list of the form (e,V,n)
        where e is the eigenvalue, V is a list of eigenvectors forming a
        basis for the corresponding right eigenspace, and n is the
        algebraic multiplicity of the eigenvalue.

        EXAMPLES::

            sage: A = matrix(SR,2,2,range(4), sparse=True); A
            [0 1]
            [2 3]
            sage: right = A.eigenvectors_right(); right
            [(-1/2*sqrt(17) + 3/2, [(1, -1/2*sqrt(17) + 3/2)], 1), (1/2*sqrt(17) + 3/2, [(1, 1/2*sqrt(17) + 3/2)], 1)]

        The right eigenvectors are nothing but the left eigenvectors of the
        transpose matrix::

            sage: left  = A.transpose().eigenvectors_left(); left
            [(-1/2*sqrt(17) + 3/2, [(1, -1/2*sqrt(17) + 3/2)], 1), (1/2*sqrt(17) + 3/2, [(1, 1/2*sqrt(17) + 3/2)], 1)]
            sage: right[0][1] == left[0][1]
            True

        TESTS::

            sage: A = matrix(SR, [[1, 2], [3, 4]], sparse=True)
            sage: B = matrix(SR, [[1, 1], [0, 1]], sparse=True)
            sage: A.eigenvectors_right(B)
            Traceback (most recent call last):
            ...
            NotImplementedError: generalized eigenvector decomposition is
            implemented for RDF and CDF, but not for Symbolic Ring

        Check that :issue:`23332` is fixed::

            sage: matrix([[x, x^2], [1, 0]], sparse=True).eigenvectors_right()
            [(-1/2*x*(sqrt(5) - 1), [(1, -1/2*(sqrt(5) + 1)/x)], 1),
             (1/2*x*(sqrt(5) + 1), [(1, 1/2*(sqrt(5) - 1)/x)], 1)]"""
    def exp(self) -> Any:
        """Matrix_symbolic_sparse.exp(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 384)

        Return the matrix exponential of this matrix `X`, which is the matrix

        .. MATH::

           e^X = \\sum_{k=0}^{\\infty} \\frac{X^k}{k!}.

        This function depends on maxima's matrix exponentiation
        function, which does not deal well with floating point
        numbers.  If the matrix has floating point numbers, they will
        be rounded automatically to rational numbers during the
        computation.

        EXAMPLES::

            sage: m = matrix(SR,2, [0,x,x,0], sparse=True); m
            [0 x]
            [x 0]
            sage: m.exp()
            [1/2*(e^(2*x) + 1)*e^(-x) 1/2*(e^(2*x) - 1)*e^(-x)]
            [1/2*(e^(2*x) - 1)*e^(-x) 1/2*(e^(2*x) + 1)*e^(-x)]
            sage: exp(m)
            [1/2*(e^(2*x) + 1)*e^(-x) 1/2*(e^(2*x) - 1)*e^(-x)]
            [1/2*(e^(2*x) - 1)*e^(-x) 1/2*(e^(2*x) + 1)*e^(-x)]

        Exponentiation works on 0x0 and 1x1 matrices, but the 1x1 example
        requires a patched version of maxima (:issue:`32898`) for now::

            sage: m = matrix(SR,0,[], sparse=True); m
            []
            sage: m.exp()
            []
            sage: m = matrix(SR,1,[2], sparse=True); m
            [2]
            sage: m.exp()  # not tested, requires patched maxima
            [e^2]

        Commuting matrices `m, n` have the property that
        `e^{m+n} = e^m e^n` (but non-commuting matrices need not)::

            sage: m = matrix(SR,2,[1..4], sparse=True); n = m^2
            sage: m*n
            [ 37  54]
            [ 81 118]
            sage: n*m
            [ 37  54]
            [ 81 118]

            sage: a = exp(m+n) - exp(m)*exp(n)
            sage: a.simplify_rational() == 0
            True

        The input matrix must be square::

            sage: m = matrix(SR,2,3,[1..6], sparse=True); exp(m)
            Traceback (most recent call last):
            ...
            ValueError: exp only defined on square matrices

        In this example we take the symbolic answer and make it
        numerical at the end::

            sage: exp(matrix(SR, [[1.2, 5.6], [3,4]], sparse=True)).change_ring(RDF)  # rel tol 1e-15
            [ 346.5574872980695  661.7345909344504]
            [354.50067371488416  677.4247827652946]

        Another example involving the reversed identity matrix, which
        we clumsily create::

            sage: m = identity_matrix(SR,4, sparse=True)
            sage: m = matrix(list(reversed(m.rows())), sparse=True) * x
            sage: exp(m)
            [1/2*(e^(2*x) + 1)*e^(-x)                        0                        0 1/2*(e^(2*x) - 1)*e^(-x)]
            [                       0 1/2*(e^(2*x) + 1)*e^(-x) 1/2*(e^(2*x) - 1)*e^(-x)                        0]
            [                       0 1/2*(e^(2*x) - 1)*e^(-x) 1/2*(e^(2*x) + 1)*e^(-x)                        0]
            [1/2*(e^(2*x) - 1)*e^(-x)                        0                        0 1/2*(e^(2*x) + 1)*e^(-x)]"""
    @overload
    def expand(self) -> Any:
        """Matrix_symbolic_sparse.expand(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 844)

        Operate point-wise on each element.

        EXAMPLES::

            sage: M = matrix(2, 2, range(4)) - var('x')
            sage: M*M
            [      x^2 + 2      -2*x + 3]
            [     -4*x + 6 (x - 3)^2 + 2]
            sage: (M*M).expand()
            [       x^2 + 2       -2*x + 3]
            [      -4*x + 6 x^2 - 6*x + 11]"""
    @overload
    def expand(self) -> Any:
        """Matrix_symbolic_sparse.expand(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 844)

        Operate point-wise on each element.

        EXAMPLES::

            sage: M = matrix(2, 2, range(4)) - var('x')
            sage: M*M
            [      x^2 + 2      -2*x + 3]
            [     -4*x + 6 (x - 3)^2 + 2]
            sage: (M*M).expand()
            [       x^2 + 2       -2*x + 3]
            [      -4*x + 6 x^2 - 6*x + 11]"""
    @overload
    def factor(self) -> Any:
        """Matrix_symbolic_sparse.factor(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 829)

        Operate point-wise on each element.

        EXAMPLES::

            sage: M = matrix(SR, 2, 2, x^2 - 2*x + 1, sparse=True); M
            [x^2 - 2*x + 1             0]
            [            0 x^2 - 2*x + 1]
            sage: M.factor()
            [(x - 1)^2         0]
            [        0 (x - 1)^2]"""
    @overload
    def factor(self) -> Any:
        """Matrix_symbolic_sparse.factor(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 829)

        Operate point-wise on each element.

        EXAMPLES::

            sage: M = matrix(SR, 2, 2, x^2 - 2*x + 1, sparse=True); M
            [x^2 - 2*x + 1             0]
            [            0 x^2 - 2*x + 1]
            sage: M.factor()
            [(x - 1)^2         0]
            [        0 (x - 1)^2]"""
    @overload
    def fcp(self, var=...) -> Any:
        """Matrix_symbolic_sparse.fcp(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 588)

        Return the factorization of the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- (default: ``'x'``) name of variable of charpoly

        EXAMPLES::

            sage: a = matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.fcp()
            x^2 - 5*x - 2
            sage: [i for i in a.fcp()]
            [(x^2 - 5*x - 2, 1)]
            sage: a = matrix(SR,[[1,0],[0,2]], sparse=True)
            sage: a.fcp()
            (x - 2) * (x - 1)
            sage: [i for i in a.fcp()]
            [(x - 2, 1), (x - 1, 1)]
            sage: a = matrix(SR, 5, [1..5^2], sparse=True)
            sage: a.fcp()
            (x^2 - 65*x - 250) * x^3
            sage: list(a.fcp())
            [(x^2 - 65*x - 250, 1), (x, 3)]"""
    @overload
    def fcp(self) -> Any:
        """Matrix_symbolic_sparse.fcp(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 588)

        Return the factorization of the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- (default: ``'x'``) name of variable of charpoly

        EXAMPLES::

            sage: a = matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.fcp()
            x^2 - 5*x - 2
            sage: [i for i in a.fcp()]
            [(x^2 - 5*x - 2, 1)]
            sage: a = matrix(SR,[[1,0],[0,2]], sparse=True)
            sage: a.fcp()
            (x - 2) * (x - 1)
            sage: [i for i in a.fcp()]
            [(x - 2, 1), (x - 1, 1)]
            sage: a = matrix(SR, 5, [1..5^2], sparse=True)
            sage: a.fcp()
            (x^2 - 65*x - 250) * x^3
            sage: list(a.fcp())
            [(x^2 - 65*x - 250, 1), (x, 3)]"""
    @overload
    def fcp(self) -> Any:
        """Matrix_symbolic_sparse.fcp(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 588)

        Return the factorization of the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- (default: ``'x'``) name of variable of charpoly

        EXAMPLES::

            sage: a = matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.fcp()
            x^2 - 5*x - 2
            sage: [i for i in a.fcp()]
            [(x^2 - 5*x - 2, 1)]
            sage: a = matrix(SR,[[1,0],[0,2]], sparse=True)
            sage: a.fcp()
            (x - 2) * (x - 1)
            sage: [i for i in a.fcp()]
            [(x - 2, 1), (x - 1, 1)]
            sage: a = matrix(SR, 5, [1..5^2], sparse=True)
            sage: a.fcp()
            (x^2 - 65*x - 250) * x^3
            sage: list(a.fcp())
            [(x^2 - 65*x - 250, 1), (x, 3)]"""
    @overload
    def fcp(self) -> Any:
        """Matrix_symbolic_sparse.fcp(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 588)

        Return the factorization of the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- (default: ``'x'``) name of variable of charpoly

        EXAMPLES::

            sage: a = matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.fcp()
            x^2 - 5*x - 2
            sage: [i for i in a.fcp()]
            [(x^2 - 5*x - 2, 1)]
            sage: a = matrix(SR,[[1,0],[0,2]], sparse=True)
            sage: a.fcp()
            (x - 2) * (x - 1)
            sage: [i for i in a.fcp()]
            [(x - 2, 1), (x - 1, 1)]
            sage: a = matrix(SR, 5, [1..5^2], sparse=True)
            sage: a.fcp()
            (x^2 - 65*x - 250) * x^3
            sage: list(a.fcp())
            [(x^2 - 65*x - 250, 1), (x, 3)]"""
    @overload
    def fcp(self) -> Any:
        """Matrix_symbolic_sparse.fcp(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 588)

        Return the factorization of the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- (default: ``'x'``) name of variable of charpoly

        EXAMPLES::

            sage: a = matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.fcp()
            x^2 - 5*x - 2
            sage: [i for i in a.fcp()]
            [(x^2 - 5*x - 2, 1)]
            sage: a = matrix(SR,[[1,0],[0,2]], sparse=True)
            sage: a.fcp()
            (x - 2) * (x - 1)
            sage: [i for i in a.fcp()]
            [(x - 2, 1), (x - 1, 1)]
            sage: a = matrix(SR, 5, [1..5^2], sparse=True)
            sage: a.fcp()
            (x^2 - 65*x - 250) * x^3
            sage: list(a.fcp())
            [(x^2 - 65*x - 250, 1), (x, 3)]"""
    @overload
    def fcp(self) -> Any:
        """Matrix_symbolic_sparse.fcp(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 588)

        Return the factorization of the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- (default: ``'x'``) name of variable of charpoly

        EXAMPLES::

            sage: a = matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.fcp()
            x^2 - 5*x - 2
            sage: [i for i in a.fcp()]
            [(x^2 - 5*x - 2, 1)]
            sage: a = matrix(SR,[[1,0],[0,2]], sparse=True)
            sage: a.fcp()
            (x - 2) * (x - 1)
            sage: [i for i in a.fcp()]
            [(x - 2, 1), (x - 1, 1)]
            sage: a = matrix(SR, 5, [1..5^2], sparse=True)
            sage: a.fcp()
            (x^2 - 65*x - 250) * x^3
            sage: list(a.fcp())
            [(x^2 - 65*x - 250, 1), (x, 3)]"""
    @overload
    def fcp(self) -> Any:
        """Matrix_symbolic_sparse.fcp(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 588)

        Return the factorization of the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- (default: ``'x'``) name of variable of charpoly

        EXAMPLES::

            sage: a = matrix(SR,[[1,2],[3,4]], sparse=True)
            sage: a.fcp()
            x^2 - 5*x - 2
            sage: [i for i in a.fcp()]
            [(x^2 - 5*x - 2, 1)]
            sage: a = matrix(SR,[[1,0],[0,2]], sparse=True)
            sage: a.fcp()
            (x - 2) * (x - 1)
            sage: [i for i in a.fcp()]
            [(x - 2, 1), (x - 1, 1)]
            sage: a = matrix(SR, 5, [1..5^2], sparse=True)
            sage: a.fcp()
            (x^2 - 65*x - 250) * x^3
            sage: list(a.fcp())
            [(x^2 - 65*x - 250, 1), (x, 3)]"""
    def function(self, *args) -> Any:
        """Matrix_symbolic_sparse.function(self, *args)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 1012)

        Return a matrix over a callable symbolic expression ring.

        EXAMPLES::

            sage: x, y = var('x,y')
            sage: v = matrix([[x,y],[x*sin(y), 0]], sparse=True)
            sage: w = v.function([x,y]); w
            [       (x, y) |--> x        (x, y) |--> y]
            [(x, y) |--> x*sin(y)        (x, y) |--> 0]
            sage: w.parent()
            Full MatrixSpace of 2 by 2 sparse matrices over Callable function ring with arguments (x, y)"""
    @overload
    def jordan_form(self, subdivide=..., transformation=...) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self, subdivide=...) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self, subdivide=...) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self, transformation=...) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self, transformation=...) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def jordan_form(self, subdivide=...) -> Any:
        """Matrix_symbolic_sparse.jordan_form(self, subdivide=True, transformation=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 618)

        Return a Jordan normal form of ``self``.

        INPUT:

        - ``self`` -- a square matrix

        - ``subdivide`` -- boolean (default: ``True``)

        - ``transformation`` -- boolean (default: ``False``)

        OUTPUT:

        If ``transformation`` is ``False``, only a Jordan normal form
        (unique up to the ordering of the Jordan blocks) is returned.
        Otherwise, a pair ``(J, P)`` is returned, where ``J`` is a
        Jordan normal form and ``P`` is an invertible matrix such that
        ``self`` equals ``P * J * P^(-1)``.

        If ``subdivide`` is ``True``, the Jordan blocks in the
        returned matrix ``J`` are indicated by a subdivision in
        the sense of :meth:`~sage.matrix.matrix2.subdivide`.

        EXAMPLES:

        We start with some examples of diagonalisable matrices::

            sage: a,b,c,d = var('a,b,c,d')
            sage: matrix([a], sparse=True).jordan_form()
            [a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=True)
            [d|0]
            [-+-]
            [0|a]
            sage: matrix([[a, 0], [1, d]], sparse=True).jordan_form(subdivide=False)
            [d 0]
            [0 a]
            sage: matrix([[a, x, x], [0, b, x], [0, 0, c]], sparse=True).jordan_form()
            [c|0|0]
            [-+-+-]
            [0|b|0]
            [-+-+-]
            [0|0|a]

        In the following examples, we compute Jordan forms of some
        non-diagonalisable matrices::

            sage: matrix([[a, a], [0, a]], sparse=True).jordan_form()
            [a 1]
            [0 a]
            sage: matrix([[a, 0, b], [0, c, 0], [0, 0, a]], sparse=True).jordan_form()
            [c|0 0]
            [-+---]
            [0|a 1]
            [0|0 a]

        The following examples illustrate the ``transformation`` flag.
        Note that symbolic expressions may need to be simplified to
        make consistency checks succeed::

            sage: A = matrix([[x - a*c, a^2], [-c^2, x + a*c]], sparse=True)
            sage: J, P = A.jordan_form(transformation=True)
            sage: J, P
            (
            [x 1]  [-a*c    1]
            [0 x], [-c^2    0]
            )
            sage: A1 = P * J * ~P; A1
            [             -a*c + x (a*c - x)*a/c + a*x/c]
            [                 -c^2               a*c + x]
            sage: A1.simplify_rational() == A
            True

            sage: B = matrix([[a, b, c], [0, a, d], [0, 0, a]], sparse=True)
            sage: J, T = B.jordan_form(transformation=True)
            sage: J, T
            (
            [a 1 0]  [b*d   c   0]
            [0 a 1]  [  0   d   0]
            [0 0 a], [  0   0   1]
            )
            sage: (B * T).simplify_rational() == T * J
            True

        Finally, some examples involving square roots::

            sage: matrix([[a, -b], [b, a]], sparse=True).jordan_form()
            [a - I*b|      0]
            [-------+-------]
            [      0|a + I*b]
            sage: matrix([[a, b], [c, d]], sparse=True).jordan_form(subdivide=False)
            [1/2*a + 1/2*d - 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)                                                   0]
            [                                                  0 1/2*a + 1/2*d + 1/2*sqrt(a^2 + 4*b*c - 2*a*d + d^2)]"""
    @overload
    def minpoly(self, var=...) -> Any:
        """Matrix_symbolic_sparse.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 556)

        Return the minimal polynomial of ``self``.

        EXAMPLES::

            sage: M = Matrix.identity(SR, 2, sparse=True)
            sage: M.minpoly()
            x - 1

            sage: t = var('t')
            sage: m = matrix(2, [1, 2, 4, t], sparse=True)
            sage: m.minimal_polynomial()
            x^2 + (-t - 1)*x + t - 8

        TESTS:

        Check that the variable `x` can occur in the matrix::

            sage: m = matrix([[x]], sparse=True)
            sage: m.minimal_polynomial('y')
            y - x"""
    @overload
    def minpoly(self) -> Any:
        """Matrix_symbolic_sparse.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 556)

        Return the minimal polynomial of ``self``.

        EXAMPLES::

            sage: M = Matrix.identity(SR, 2, sparse=True)
            sage: M.minpoly()
            x - 1

            sage: t = var('t')
            sage: m = matrix(2, [1, 2, 4, t], sparse=True)
            sage: m.minimal_polynomial()
            x^2 + (-t - 1)*x + t - 8

        TESTS:

        Check that the variable `x` can occur in the matrix::

            sage: m = matrix([[x]], sparse=True)
            sage: m.minimal_polynomial('y')
            y - x"""
    @overload
    def number_of_arguments(self) -> Any:
        """Matrix_symbolic_sparse.number_of_arguments(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 899)

        Return the number of arguments that ``self`` can take.

        EXAMPLES::

            sage: var('a,b,c,x,y')
            (a, b, c, x, y)
            sage: m = matrix([[a, (x+y)/(x+y)], [x^2, y^2+2]], sparse=True); m
            [      a       1]
            [    x^2 y^2 + 2]
            sage: m.number_of_arguments()
            3"""
    @overload
    def number_of_arguments(self) -> Any:
        """Matrix_symbolic_sparse.number_of_arguments(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 899)

        Return the number of arguments that ``self`` can take.

        EXAMPLES::

            sage: var('a,b,c,x,y')
            (a, b, c, x, y)
            sage: m = matrix([[a, (x+y)/(x+y)], [x^2, y^2+2]], sparse=True); m
            [      a       1]
            [    x^2 y^2 + 2]
            sage: m.number_of_arguments()
            3"""
    @overload
    def simplify(self) -> Any:
        """Matrix_symbolic_sparse.simplify(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 726)

        Simplify ``self``.

        EXAMPLES::

            sage: var('x,y,z')
            (x, y, z)
            sage: m = matrix([[z, (x+y)/(x+y)], [x^2, y^2+2]], sparse=True); m
            [      z       1]
            [    x^2 y^2 + 2]
            sage: m.simplify()
            [      z       1]
            [    x^2 y^2 + 2]"""
    @overload
    def simplify(self) -> Any:
        """Matrix_symbolic_sparse.simplify(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 726)

        Simplify ``self``.

        EXAMPLES::

            sage: var('x,y,z')
            (x, y, z)
            sage: m = matrix([[z, (x+y)/(x+y)], [x^2, y^2+2]], sparse=True); m
            [      z       1]
            [    x^2 y^2 + 2]
            sage: m.simplify()
            [      z       1]
            [    x^2 y^2 + 2]"""
    @overload
    def simplify_full(self) -> Any:
        """Matrix_symbolic_sparse.simplify_full(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 779)

        Simplify a symbolic matrix by calling
        :meth:`Expression.simplify_full()` componentwise.

        INPUT:

        - ``self`` -- the matrix whose entries we should simplify

        OUTPUT: a copy of ``self`` with all of its entries simplified

        EXAMPLES:

        Symbolic matrices will have their entries simplified::

            sage: a,n,k = SR.var('a,n,k')
            sage: f1 = sin(x)^2 + cos(x)^2
            sage: f2 = sin(x/(x^2 + x))
            sage: f3 = binomial(n,k)*factorial(k)*factorial(n-k)
            sage: f4 = x*sin(2)/(x^a)
            sage: A = matrix(SR, [[f1,f2],[f3,f4]], sparse=True)
            sage: A.simplify_full()
            [                1    sin(1/(x + 1))]
            [     factorial(n) x^(-a + 1)*sin(2)]"""
    @overload
    def simplify_full(self) -> Any:
        """Matrix_symbolic_sparse.simplify_full(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 779)

        Simplify a symbolic matrix by calling
        :meth:`Expression.simplify_full()` componentwise.

        INPUT:

        - ``self`` -- the matrix whose entries we should simplify

        OUTPUT: a copy of ``self`` with all of its entries simplified

        EXAMPLES:

        Symbolic matrices will have their entries simplified::

            sage: a,n,k = SR.var('a,n,k')
            sage: f1 = sin(x)^2 + cos(x)^2
            sage: f2 = sin(x/(x^2 + x))
            sage: f3 = binomial(n,k)*factorial(k)*factorial(n-k)
            sage: f4 = x*sin(2)/(x^a)
            sage: A = matrix(SR, [[f1,f2],[f3,f4]], sparse=True)
            sage: A.simplify_full()
            [                1    sin(1/(x + 1))]
            [     factorial(n) x^(-a + 1)*sin(2)]"""
    @overload
    def simplify_full(self) -> Any:
        """Matrix_symbolic_sparse.simplify_full(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 779)

        Simplify a symbolic matrix by calling
        :meth:`Expression.simplify_full()` componentwise.

        INPUT:

        - ``self`` -- the matrix whose entries we should simplify

        OUTPUT: a copy of ``self`` with all of its entries simplified

        EXAMPLES:

        Symbolic matrices will have their entries simplified::

            sage: a,n,k = SR.var('a,n,k')
            sage: f1 = sin(x)^2 + cos(x)^2
            sage: f2 = sin(x/(x^2 + x))
            sage: f3 = binomial(n,k)*factorial(k)*factorial(n-k)
            sage: f4 = x*sin(2)/(x^a)
            sage: A = matrix(SR, [[f1,f2],[f3,f4]], sparse=True)
            sage: A.simplify_full()
            [                1    sin(1/(x + 1))]
            [     factorial(n) x^(-a + 1)*sin(2)]"""
    @overload
    def simplify_rational(self) -> Any:
        """Matrix_symbolic_sparse.simplify_rational(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 758)

        EXAMPLES::

            sage: M = matrix(SR, 3, 3, range(9), sparse=True) - var('t')
            sage: (~M*M)[0,0]
            t*(3*(2/t + (6/t + 7)/((t - 3/t - 4)*t))*(2/t + (6/t + 5)/((t - 3/t
            - 4)*t))/(t - (6/t + 7)*(6/t + 5)/(t - 3/t - 4) - 12/t - 8) + 1/t +
            3/((t - 3/t - 4)*t^2)) - 6*(2/t + (6/t + 5)/((t - 3/t - 4)*t))/(t -
            (6/t + 7)*(6/t + 5)/(t - 3/t - 4) - 12/t - 8) - 3*(6/t + 7)*(2/t +
            (6/t + 5)/((t - 3/t - 4)*t))/((t - (6/t + 7)*(6/t + 5)/(t - 3/t -
            4) - 12/t - 8)*(t - 3/t - 4)) - 3/((t - 3/t - 4)*t)
            sage: expand((~M*M)[0,0])
            1
            sage: (~M * M).simplify_rational()
            [1 0 0]
            [0 1 0]
            [0 0 1]"""
    @overload
    def simplify_rational(self) -> Any:
        """Matrix_symbolic_sparse.simplify_rational(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 758)

        EXAMPLES::

            sage: M = matrix(SR, 3, 3, range(9), sparse=True) - var('t')
            sage: (~M*M)[0,0]
            t*(3*(2/t + (6/t + 7)/((t - 3/t - 4)*t))*(2/t + (6/t + 5)/((t - 3/t
            - 4)*t))/(t - (6/t + 7)*(6/t + 5)/(t - 3/t - 4) - 12/t - 8) + 1/t +
            3/((t - 3/t - 4)*t^2)) - 6*(2/t + (6/t + 5)/((t - 3/t - 4)*t))/(t -
            (6/t + 7)*(6/t + 5)/(t - 3/t - 4) - 12/t - 8) - 3*(6/t + 7)*(2/t +
            (6/t + 5)/((t - 3/t - 4)*t))/((t - (6/t + 7)*(6/t + 5)/(t - 3/t -
            4) - 12/t - 8)*(t - 3/t - 4)) - 3/((t - 3/t - 4)*t)
            sage: expand((~M*M)[0,0])
            1
            sage: (~M * M).simplify_rational()
            [1 0 0]
            [0 1 0]
            [0 0 1]"""
    @overload
    def simplify_trig(self) -> Any:
        """Matrix_symbolic_sparse.simplify_trig(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 743)

        EXAMPLES::

            sage: theta = var('theta')
            sage: M = matrix(SR, 2, 2, [cos(theta), sin(theta), -sin(theta), cos(theta)], sparse=True)
            sage: ~M
            [1/cos(theta) - sin(theta)^2/((sin(theta)^2/cos(theta) + cos(theta))*cos(theta)^2)                   -sin(theta)/((sin(theta)^2/cos(theta) + cos(theta))*cos(theta))]
            [                   sin(theta)/((sin(theta)^2/cos(theta) + cos(theta))*cos(theta))                                          1/(sin(theta)^2/cos(theta) + cos(theta))]
            sage: (~M).simplify_trig()
            [ cos(theta) -sin(theta)]
            [ sin(theta)  cos(theta)]"""
    @overload
    def simplify_trig(self) -> Any:
        """Matrix_symbolic_sparse.simplify_trig(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 743)

        EXAMPLES::

            sage: theta = var('theta')
            sage: M = matrix(SR, 2, 2, [cos(theta), sin(theta), -sin(theta), cos(theta)], sparse=True)
            sage: ~M
            [1/cos(theta) - sin(theta)^2/((sin(theta)^2/cos(theta) + cos(theta))*cos(theta)^2)                   -sin(theta)/((sin(theta)^2/cos(theta) + cos(theta))*cos(theta))]
            [                   sin(theta)/((sin(theta)^2/cos(theta) + cos(theta))*cos(theta))                                          1/(sin(theta)^2/cos(theta) + cos(theta))]
            sage: (~M).simplify_trig()
            [ cos(theta) -sin(theta)]
            [ sin(theta)  cos(theta)]"""
    @overload
    def variables(self) -> Any:
        """Matrix_symbolic_sparse.variables(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 861)

        Return the variables of ``self``.

        EXAMPLES::

            sage: var('a,b,c,x,y')
            (a, b, c, x, y)
            sage: m = matrix([[x, x+2], [x^2, x^2+2]], sparse=True); m
            [      x   x + 2]
            [    x^2 x^2 + 2]
            sage: m.variables()
            (x,)
            sage: m = matrix([[a, b+c], [x^2, y^2+2]], sparse=True); m
            [      a   b + c]
            [    x^2 y^2 + 2]
            sage: m.variables()
            (a, b, c, x, y)"""
    @overload
    def variables(self) -> Any:
        """Matrix_symbolic_sparse.variables(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 861)

        Return the variables of ``self``.

        EXAMPLES::

            sage: var('a,b,c,x,y')
            (a, b, c, x, y)
            sage: m = matrix([[x, x+2], [x^2, x^2+2]], sparse=True); m
            [      x   x + 2]
            [    x^2 x^2 + 2]
            sage: m.variables()
            (x,)
            sage: m = matrix([[a, b+c], [x^2, y^2+2]], sparse=True); m
            [      a   b + c]
            [    x^2 y^2 + 2]
            sage: m.variables()
            (a, b, c, x, y)"""
    @overload
    def variables(self) -> Any:
        """Matrix_symbolic_sparse.variables(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 861)

        Return the variables of ``self``.

        EXAMPLES::

            sage: var('a,b,c,x,y')
            (a, b, c, x, y)
            sage: m = matrix([[x, x+2], [x^2, x^2+2]], sparse=True); m
            [      x   x + 2]
            [    x^2 x^2 + 2]
            sage: m.variables()
            (x,)
            sage: m = matrix([[a, b+c], [x^2, y^2+2]], sparse=True); m
            [      a   b + c]
            [    x^2 y^2 + 2]
            sage: m.variables()
            (a, b, c, x, y)"""
    def __call__(self, *args, **kwargs) -> Any:
        """Matrix_symbolic_sparse.__call__(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_symbolic_sparse.pyx (starting at line 915)

        EXAMPLES::

            sage: var('x,y,z')
            (x, y, z)
            sage: M = MatrixSpace(SR,2,2, sparse=True)
            sage: h = M(sin(x)+cos(x))
            sage: h
            [cos(x) + sin(x)               0]
            [              0 cos(x) + sin(x)]
            sage: h(x=1)
            [cos(1) + sin(1)               0]
            [              0 cos(1) + sin(1)]
            sage: h(x=x)
            [cos(x) + sin(x)               0]
            [              0 cos(x) + sin(x)]

            sage: h = M((sin(x)+cos(x)).function(x))
            sage: h
            [cos(x) + sin(x)               0]
            [              0 cos(x) + sin(x)]

            sage: f = M([0,x,y,z]); f
            [0 x]
            [y z]
            sage: f.arguments()
            (x, y, z)
            sage: f()
            [0 x]
            [y z]
            sage: f(x=1)
            [0 1]
            [y z]
            sage: f(x=1,y=2)
            [0 1]
            [2 z]
            sage: f(x=1,y=2,z=3)
            [0 1]
            [2 3]
            sage: f({x:1,y:2,z:3})
            [0 1]
            [2 3]

        TESTS::

            sage: f(1, x=2)
            Traceback (most recent call last):
            ...
            ValueError: args and kwargs cannot both be specified
            sage: f(x=1,y=2,z=3,t=4)
            [0 1]
            [2 3]

            sage: h(1)
            Traceback (most recent call last):
            ...
            ValueError: use named arguments, like EXPR(x=..., y=...)"""
