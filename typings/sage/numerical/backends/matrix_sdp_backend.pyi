import sage.numerical.backends.generic_sdp_backend
from sage.matrix.constructor import matrix as matrix
from typing import Any, ClassVar, overload

class MatrixSDPBackend(sage.numerical.backends.generic_sdp_backend.GenericSDPBackend):
    """MatrixSDPBackend(maximization=True, base_ring=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, maximization=..., base_ring=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 27)

                Cython constructor.

                EXAMPLES::

                    sage: from sage.numerical.backends.generic_sdp_backend import get_solver
                    sage: p = get_solver(solver = "CVXOPT")
        '''
    def add_linear_constraint(self, coefficients, name=...) -> Any:
        '''MatrixSDPBackend.add_linear_constraint(self, coefficients, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 247)

        Add a linear constraint.

        INPUT:

        - ``coefficients`` an iterable with ``(c,v)`` pairs where ``c``
          is a variable index (integer) and ``v`` is a value (matrix).
          The pairs come sorted by indices. If c is -1 it
          represents the constant coefficient.

        - ``name`` -- an optional name for this row (default: ``None``)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint(  [(0, matrix([[33., -9.], [-9., 26.]])) , (1,  matrix([[-7., -11.] ,[ -11., 3.]]) )])
            sage: p.row(0)
            ([0, 1],
             [
            [ 33.0000000000000 -9.00000000000000]
            [-9.00000000000000  26.0000000000000],
            <BLANKLINE>
            [-7.00000000000000 -11.0000000000000]
            [-11.0000000000000  3.00000000000000]
            ])
            sage: p.add_linear_constraint(  [(0, matrix([[33., -9.], [-9., 26.]])) , (1,  matrix([[-7., -11.] ,[ -11., 3.]]) )],name=\'fun\')
            sage: p.row_name(-1)
            \'fun\''''
    def add_linear_constraints(self, intnumber, names=...) -> Any:
        '''MatrixSDPBackend.add_linear_constraints(self, int number, names=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 294)

        Add constraints.

        INPUT:

        - ``number`` -- integer; the number of constraints to add

        - ``names`` -- an optional list of names (default: ``None``)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(5)
            sage: p.row(4)
            ([], [])'''
    @overload
    def add_variable(self, obj=..., name=...) -> int:
        '''MatrixSDPBackend.add_variable(self, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 88)

        Add a variable.

        This amounts to adding a new column of matrices to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``obj`` -- (optional) coefficient of this variable in the objective
          function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default:
          ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(name=\'x\',obj=1.0)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            1.00000000000000'''
    @overload
    def add_variable(self) -> Any:
        '''MatrixSDPBackend.add_variable(self, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 88)

        Add a variable.

        This amounts to adding a new column of matrices to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``obj`` -- (optional) coefficient of this variable in the objective
          function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default:
          ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(name=\'x\',obj=1.0)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            1.00000000000000'''
    @overload
    def add_variable(self) -> Any:
        '''MatrixSDPBackend.add_variable(self, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 88)

        Add a variable.

        This amounts to adding a new column of matrices to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``obj`` -- (optional) coefficient of this variable in the objective
          function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default:
          ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(name=\'x\',obj=1.0)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            1.00000000000000'''
    @overload
    def add_variable(self, name=..., obj=...) -> Any:
        '''MatrixSDPBackend.add_variable(self, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 88)

        Add a variable.

        This amounts to adding a new column of matrices to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``obj`` -- (optional) coefficient of this variable in the objective
          function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default:
          ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(name=\'x\',obj=1.0)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            1.00000000000000'''
    def add_variables(self, intn, names=...) -> int:
        '''MatrixSDPBackend.add_variables(self, int n, names=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 135)

        Add ``n`` variables.

        This amounts to adding new columns to the matrix. By default,
        the variables are both positive and real.

        INPUT:

        - ``n`` -- the number of new variables (must be > 0)

        - ``names`` -- list of names (default: ``None``)

        OUTPUT: the index of the variable created last

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.ncols()
            0
            sage: p.add_variables(5)
            4
            sage: p.ncols()
            5
            sage: p.add_variables(2, names=[\'a\',\'b\'])
            6'''
    @overload
    def base_ring(self) -> Any:
        """MatrixSDPBackend.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 56)

        The base ring.

        TESTS::

            sage: from sage.numerical.backends.matrix_sdp_backend import MatrixSDPBackend
            sage: MatrixSDPBackend(base_ring=QQ).base_ring()
            Rational Field"""
    @overload
    def base_ring(self) -> Any:
        """MatrixSDPBackend.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 56)

        The base ring.

        TESTS::

            sage: from sage.numerical.backends.matrix_sdp_backend import MatrixSDPBackend
            sage: MatrixSDPBackend(base_ring=QQ).base_ring()
            Rational Field"""
    def col_name(self, intindex) -> Any:
        '''MatrixSDPBackend.col_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 455)

        Return the ``index``-th col name.

        INPUT:

        - ``index`` -- integer; the col\'s id

        - ``name`` -- (``char *``) its name; when set to ``NULL``
          (default), the method returns the current name

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.add_variable(name="I am a variable")
            0
            sage: p.col_name(0)
            \'I am a variable\''''
    @overload
    def get_matrix(self) -> Any:
        """MatrixSDPBackend.get_matrix(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 68)

        Get a block of a matrix coefficient.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt')
            sage: x = p.new_variable()
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 5.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a1)
            sage: b = p.get_backend()
            sage: b.get_matrix()[0][0]
            (
                [-1.0 -2.0]
            -1, [-2.0 -3.0]
            )"""
    @overload
    def get_matrix(self) -> Any:
        """MatrixSDPBackend.get_matrix(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 68)

        Get a block of a matrix coefficient.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt')
            sage: x = p.new_variable()
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 5.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a1)
            sage: b = p.get_backend()
            sage: b.get_matrix()[0][0]
            (
                [-1.0 -2.0]
            -1, [-2.0 -3.0]
            )"""
    @overload
    def is_maximization(self) -> bool:
        '''MatrixSDPBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 354)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''MatrixSDPBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 354)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''MatrixSDPBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 354)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def ncols(self) -> int:
        '''MatrixSDPBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 318)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''MatrixSDPBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 318)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''MatrixSDPBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 318)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def nrows(self) -> int:
        '''MatrixSDPBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 336)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.nrows()
            0
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(2)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''MatrixSDPBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 336)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.nrows()
            0
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(2)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''MatrixSDPBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 336)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.nrows()
            0
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(2)
            sage: p.nrows()
            2'''
    def objective_coefficient(self, intvariable, coeff=...) -> Any:
        '''MatrixSDPBackend.objective_coefficient(self, int variable, coeff=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 193)

        Set or get the coefficient of a variable in the objective
        function

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``coeff`` -- double; its coefficient

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.add_variable()
            0
            sage: p.objective_coefficient(0)
            0.0
            sage: p.objective_coefficient(0,2)
            sage: p.objective_coefficient(0)
            2.0'''
    def problem_name(self, name=...) -> Any:
        '''MatrixSDPBackend.problem_name(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 373)

        Return or define the problem\'s name.

        INPUT:

        - ``name`` -- string; the problem\'s name. When set to
          ``NULL`` (default), the method returns the problem\'s name.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.problem_name("There once was a french fry")
            sage: print(p.problem_name())
            There once was a french fry'''
    def row(self, inti) -> Any:
        '''MatrixSDPBackend.row(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 395)

        Return a row.

        INPUT:

        - ``index`` -- integer; the constraint\'s id

        OUTPUT:

        A pair ``(indices, coeffs)`` where ``indices`` lists the
        entries whose coefficient is nonzero, and to which ``coeffs``
        associates their coefficient on the model of the
        ``add_linear_constraint`` method.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(  [(0, matrix([[33., -9.], [-9., 26.]])) , (1,  matrix([[-7., -11.] ,[ -11., 3.]]) )])
            sage: p.row(0)
            ([0, 1],
             [
            [ 33.0000000000000 -9.00000000000000]
            [-9.00000000000000  26.0000000000000],
            <BLANKLINE>
            [-7.00000000000000 -11.0000000000000]
            [-11.0000000000000  3.00000000000000]
            ])'''
    def row_name(self, intindex) -> Any:
        '''MatrixSDPBackend.row_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 435)

        Return the ``index``-th row name.

        INPUT:

        - ``index`` -- integer; the row\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.add_linear_constraints(1, names=\'A\')
            sage: p.row_name(0)
            \'A\''''
    def set_objective(self, listcoeff, d=...) -> Any:
        '''MatrixSDPBackend.set_objective(self, list coeff, d=0.0)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 221)

        Set the objective function.

        INPUT:

        - ``coeff`` -- list of real values, whose i-th element is the
          coefficient of the i-th variable in the objective function

        - ``d`` -- double; the constant term in the linear function (set to `0`
          by default)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.add_variables(5)
            4
            sage: p.set_objective([1, 1, 2, 1, 3])
            sage: [p.objective_coefficient(x) for x in range(5)]
            [1, 1, 2, 1, 3]'''
    def set_sense(self, intsense) -> Any:
        '''MatrixSDPBackend.set_sense(self, int sense)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/matrix_sdp_backend.pyx (starting at line 167)

        Set the direction (maximization/minimization).

        INPUT:

        - ``sense`` -- integer:

            * +1 => Maximization
            * -1 => Minimization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver = "CVXOPT")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
