import _cython_3_2_1
from typing import Any, ClassVar, overload

__pyx_capi__: dict
default_sdp_solver: _cython_3_2_1.cython_function_or_method
default_solver: None
get_solver: _cython_3_2_1.cython_function_or_method

class GenericSDPBackend:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_linear_constraint(self, coefficients, name=...) -> Any:
        '''GenericSDPBackend.add_linear_constraint(self, coefficients, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 203)

        Add a linear constraint.

        INPUT:

        - ``coefficients`` an iterable with ``(c,v)`` pairs where ``c``
          is a variable index (integer) and ``v`` is a value (real
          value).

        - ``lower_bound`` -- a lower bound, either a real value or ``None``

        - ``upper_bound`` -- an upper bound, either a real value or ``None``

        - ``name`` -- an optional name for this row (default: ``None``)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(zip(range(5), range(5)), 2.0, 2.0)
            sage: p.row(0)
            ([4, 3, 2, 1], [4.0, 3.0, 2.0, 1.0])                   # optional - Nonexistent_LP_solver
            sage: p.row_bounds(0)
            (2.0, 2.0)
            sage: p.add_linear_constraint( zip(range(5), range(5)), 1.0, 1.0, name=\'foo\')
            sage: p.row_name(-1)
            "foo"'''
    def add_linear_constraints(self, intnumber, names=...) -> Any:
        '''GenericSDPBackend.add_linear_constraints(self, int number, names=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 237)

        Add constraints.

        INPUT:

        - ``number`` -- integer; the number of constraints to add

        - ``lower_bound`` -- a lower bound, either a real value or ``None``

        - ``upper_bound`` -- an upper bound, either a real value or ``None``

        - ``names`` -- an optional list of names (default: ``None``)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            5
            sage: p.add_linear_constraints(5, None, 2)
            sage: p.row(4)
            ([], [])
            sage: p.row_bounds(4)
            (None, 2.0)'''
    @overload
    def add_variable(self, obj=..., name=...) -> int:
        '''GenericSDPBackend.add_variable(self, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 56)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``obj`` -- (optional) coefficient of this variable in the objective
          function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default:
          ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    @overload
    def add_variable(self) -> Any:
        '''GenericSDPBackend.add_variable(self, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 56)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``obj`` -- (optional) coefficient of this variable in the objective
          function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default:
          ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    @overload
    def add_variable(self, name=..., obj=...) -> Any:
        '''GenericSDPBackend.add_variable(self, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 56)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``obj`` -- (optional) coefficient of this variable in the objective
          function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default:
          ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    def add_variables(self, intn, names=...) -> int:
        '''GenericSDPBackend.add_variables(self, int n, names=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 93)

        Add ``n`` variables.

        This amounts to adding new columns to the matrix. By default,
        the variables are both positive and real.

        INPUT:

        - ``n`` -- the number of new variables (must be > 0)

        - ``obj`` -- coefficient of all variables in the objective function (default: 0.0)

        - ``names`` -- list of names (default: ``None``)

        OUTPUT: the index of the variable created last

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variables(5)
            4
            sage: p.ncols()
            5
            sage: p.add_variables(2, lower_bound=-2.0, integer=True, names=[\'a\',\'b\'])
            6'''
    @overload
    def base_ring(self) -> Any:
        """GenericSDPBackend.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 31)

        The base ring.

        TESTS::

            sage: from sage.numerical.backends.generic_sdp_backend import GenericSDPBackend
            sage: GenericSDPBackend().base_ring()
            Real Double Field"""
    @overload
    def base_ring(self) -> Any:
        """GenericSDPBackend.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 31)

        The base ring.

        TESTS::

            sage: from sage.numerical.backends.generic_sdp_backend import GenericSDPBackend
            sage: GenericSDPBackend().base_ring()
            Real Double Field"""
    def col_name(self, intindex) -> Any:
        '''GenericSDPBackend.col_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 473)

        Return the ``index``-th col name.

        INPUT:

        - ``index`` -- integer; the col\'s id

        - ``name`` -- (``char *``) its name; when set to ``NULL``
          (default), the method returns the current name

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variable(name="I am a variable")
            1
            sage: p.col_name(0)
            \'I am a variable\''''
    def dual_variable(self, inti, sparse=...) -> Any:
        '''GenericSDPBackend.dual_variable(self, int i, sparse=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 496)

        The `i`-th dual variable.

        Available after ``self.solve()`` is called, otherwise the result is undefined

        - ``index`` -- integer; the constraint\'s id

        OUTPUT: the matrix of the `i`-th dual variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = SemidefiniteProgram(maximization=False, solver="Nonexistent_LP_solver")
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1])
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 5.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 2.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a3)
            sage: p.add_constraint(b1*x[0] + b2*x[1] <= b3)
            sage: p.solve()
            -3.0
            sage: B = p.get_backend()
            sage: x = p.get_values(x).values()
            sage: -(a3*B.dual_variable(0)).trace()-(b3*B.dual_variable(1)).trace()
            -3.0
            sage: g = sum((B.slack(j)*B.dual_variable(j)).trace() for j in range(2)); g
            0.0

        TESTS::

            sage: B.dual_variable(7)  # optional - Nonexistent_LP_solver
            ...
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
            sage: abs(g - B._get_answer()[\'gap\'])  # optional - Nonexistent_LP_solver # tol 1e-22
            0.0'''
    @overload
    def get_objective_value(self) -> Any:
        '''GenericSDPBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 293)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            2
            sage: p.add_linear_constraint([(0,1), (1,2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            7.5
            sage: p.get_variable_value(0)
            0.0
            sage: p.get_variable_value(1)
            1.5'''
    @overload
    def get_objective_value(self) -> Any:
        '''GenericSDPBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 293)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            2
            sage: p.add_linear_constraint([(0,1), (1,2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            7.5
            sage: p.get_variable_value(0)
            0.0
            sage: p.get_variable_value(1)
            1.5'''
    def get_variable_value(self, intvariable) -> Any:
        '''GenericSDPBackend.get_variable_value(self, int variable)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 321)

        Return the value of a variable given by the solver.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            2
            sage: p.add_linear_constraint([(0,1), (1, 2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            7.5
            sage: p.get_variable_value(0)
            0.0
            sage: p.get_variable_value(1)
            1.5'''
    @overload
    def is_maximization(self) -> bool:
        '''GenericSDPBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 386)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''GenericSDPBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 386)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''GenericSDPBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 386)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def ncols(self) -> int:
        '''GenericSDPBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 350)

        Return the number of columns/variables.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            2
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''GenericSDPBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 350)

        Return the number of columns/variables.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            2
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''GenericSDPBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 350)

        Return the number of columns/variables.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            2
            sage: p.ncols()
            2'''
    @overload
    def nrows(self) -> int:
        '''GenericSDPBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 369)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''GenericSDPBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 369)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''GenericSDPBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 369)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    def objective_coefficient(self, intvariable, coeff=...) -> Any:
        '''GenericSDPBackend.objective_coefficient(self, int variable, coeff=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 150)

        Set or get the coefficient of a variable in the objective
        function

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``coeff`` -- double; its coefficient

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variable()
            1
            sage: p.objective_coefficient(0)
            0.0
            sage: p.objective_coefficient(0,2)
            sage: p.objective_coefficient(0)
            2.0'''
    def problem_name(self, name=...) -> Any:
        '''GenericSDPBackend.problem_name(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 403)

        Return or define the problem\'s name.

        INPUT:

        - ``name`` -- string; the problem\'s name. When set to
          ``NULL`` (default), the method returns the problem\'s name.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.problem_name("There once was a french fry")
            sage: print(p.problem_name())
            There once was a french fry'''
    def row(self, inti) -> Any:
        '''GenericSDPBackend.row(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 424)

        Return a row.

        INPUT:

        - ``index`` -- integer; the constraint\'s id

        OUTPUT:

        A pair ``(indices, coeffs)`` where ``indices`` lists the
        entries whose coefficient is nonzero, and to which ``coeffs``
        associates their coefficient on the model of the
        ``add_linear_constraint`` method.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            5
            sage: p.add_linear_constraint(zip(range(5), range(5)), 2, 2)
            sage: p.row(0)
            ([4, 3, 2, 1], [4.0, 3.0, 2.0, 1.0])
            sage: p.row_bounds(0)
            (2.0, 2.0)'''
    def row_name(self, intindex) -> Any:
        '''GenericSDPBackend.row_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 454)

        Return the ``index``-th row name.

        INPUT:

        - ``index`` -- integer; the row\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_linear_constraints(1, 2, None, name="Empty constraint 1")
            sage: p.row_name(0)
            \'Empty constraint 1\''''
    def set_objective(self, listcoeff, d=...) -> Any:
        '''GenericSDPBackend.set_objective(self, list coeff, d=0.0)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 176)

        Set the objective function.

        INPUT:

        - ``coeff`` -- list of real values, whose i-th element is the
          coefficient of the i-th variable in the objective function

        - ``d`` -- double; the constant term in the linear function (set to `0`
          by default)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            5
            sage: p.set_objective([1, 1, 2, 1, 3])
            sage: [p.objective_coefficient(x) for x in range(5)]
            [1.0, 1.0, 2.0, 1.0, 3.0]

        Constants in the objective function are respected.'''
    def set_sense(self, intsense) -> Any:
        '''GenericSDPBackend.set_sense(self, int sense)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 126)

        Set the direction (maximization/minimization).

        INPUT:

        - ``sense`` -- integer:

          * `+1` => Maximization
          * `-1` => Minimization

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    def slack(self, inti, sparse=...) -> Any:
        '''GenericSDPBackend.slack(self, int i, sparse=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 541)

        Slack of the `i`-th constraint.

        Available after ``self.solve()`` is called, otherwise the result is
        undefined.

        - ``index`` -- integer; the constraint\'s id

        OUTPUT: the matrix of the slack of the `i`-th constraint

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = SemidefiniteProgram(maximization=False, solver="Nonexistent_LP_solver")
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1])
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 5.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 2.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a3)
            sage: p.add_constraint(b1*x[0] + b2*x[1] <= b3)
            sage: p.solve()
            -3.0
            sage: B = p.get_backend()
            sage: B1 = B.slack(1); B1
            [0.0 0.0]
            [0.0 0.0]
            sage: B1.is_positive_definite()
            True
            sage: x = p.get_values(x).values()
            sage: x[0]*b1 + x[1]*b2 - b3 + B1
            [0.0 0.0]
            [0.0 0.0]

        TESTS::

            sage: B.slack(7)  # optional - Nonexistent_LP_solver
            ...
            Traceback (most recent call last):
            ...
            IndexError: list index out of range'''
    @overload
    def solve(self) -> int:
        '''GenericSDPBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 266)

        Solve the problem.

        .. NOTE::

            This method raises :class:`SDPSolverException` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(range(5), range(5))
            sage: p.solve()
            0
            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            SDPSolverException: ...'''
    @overload
    def solve(self) -> Any:
        '''GenericSDPBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 266)

        Solve the problem.

        .. NOTE::

            This method raises :class:`SDPSolverException` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(range(5), range(5))
            sage: p.solve()
            0
            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            SDPSolverException: ...'''
    @overload
    def solve(self) -> Any:
        '''GenericSDPBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 266)

        Solve the problem.

        .. NOTE::

            This method raises :class:`SDPSolverException` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(range(5), range(5))
            sage: p.solve()
            0
            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            SDPSolverException: ...'''
    def solver_parameter(self, name, value=...) -> Any:
        '''GenericSDPBackend.solver_parameter(self, name, value=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 589)

        Return or define a solver parameter.

        INPUT:

        - ``name`` -- string; the parameter

        - ``value`` -- the parameter\'s value if it is to be defined,
          or ``None`` (default) to obtain its current value

        .. NOTE::

           The list of available parameters is available at
           :meth:`~sage.numerical.sdp.SemidefiniteProgram.solver_parameter`.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.solver_parameter("timelimit")
            sage: p.solver_parameter("timelimit", 60)
            sage: p.solver_parameter("timelimit")'''
    @overload
    def zero(self) -> Any:
        """GenericSDPBackend.zero(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 44)

        Zero of the base ring.

        TESTS::

            sage: from sage.numerical.backends.generic_sdp_backend import GenericSDPBackend
            sage: GenericSDPBackend().zero()
            0.0"""
    @overload
    def zero(self) -> Any:
        """GenericSDPBackend.zero(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_sdp_backend.pyx (starting at line 44)

        Zero of the base ring.

        TESTS::

            sage: from sage.numerical.backends.generic_sdp_backend import GenericSDPBackend
            sage: GenericSDPBackend().zero()
            0.0"""
