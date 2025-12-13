import sage.numerical.backends.generic_backend
from sage.numerical.mip import MIPSolverException as MIPSolverException
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class PPLBackend(sage.numerical.backends.generic_backend.GenericBackend):
    """File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 31)

        MIP Backend that uses the exact MIP solver from the Parma Polyhedra Library.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_col(self, indices, coeffs) -> Any:
        '''PPLBackend.add_col(self, indices, coeffs)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 595)

        Add a column.

        INPUT:

        - ``indices`` -- list of integers; this list contains the
          indices of the constraints in which the variable\'s
          coefficient is nonzero

        - ``coeffs`` -- list of real values; associates a coefficient
          to the variable in each of the constraints in which it
          appears. Namely, the i-th entry of ``coeffs`` corresponds to
          the coefficient of the variable in the constraint
          represented by the i-th entry in ``indices``.

        .. NOTE::

            ``indices`` and ``coeffs`` are expected to be of the same
            length.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.nrows()
            5'''
    def add_linear_constraint(self, coefficients, lower_bound, upper_bound, name=...) -> Any:
        '''PPLBackend.add_linear_constraint(self, coefficients, lower_bound, upper_bound, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 539)

        Add a linear constraint.

        INPUT:

        - ``coefficients`` -- an iterable with ``(c,v)`` pairs where ``c``
          is a variable index (integer) and ``v`` is a value (real
          value).

        - ``lower_bound`` -- a lower bound, either a real value or ``None``

        - ``upper_bound`` -- an upper bound, either a real value or ``None``

        - ``name`` -- an optional name for this row (default: ``None``)

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0]/2 + x[1]/3 <= 2/5)
            sage: p.set_objective(x[1])
            sage: p.solve()
            6/5
            sage: p.add_constraint(x[0] - x[1] >= 1/10)
            sage: p.solve()
            21/50
            sage: p.set_max(x[0], 1/2)
            sage: p.set_min(x[1], 3/8)
            sage: p.solve()
            2/5

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(zip(range(5), range(5)), 2.0, 2.0)
            sage: p.row(0)
            ([1, 2, 3, 4], [1, 2, 3, 4])
            sage: p.row_bounds(0)
            (2.00000000000000, 2.00000000000000)
            sage: p.add_linear_constraint( zip(range(5), range(5)), 1.0, 1.0, name=\'foo\')
            sage: p.row_name(-1)
            \'foo\''''
    def add_linear_constraints(self, intnumber, lower_bound, upper_bound, names=...) -> Any:
        '''PPLBackend.add_linear_constraints(self, int number, lower_bound, upper_bound, names=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 639)

        Add constraints.

        INPUT:

        - ``number`` -- integer; the number of constraints to add

        - ``lower_bound`` -- a lower bound, either a real value or ``None``

        - ``upper_bound`` -- an upper bound, either a real value or ``None``

        - ``names`` -- an optional list of names (default: ``None``)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(5, None, 2)
            sage: p.row(4)
            ([], [])
            sage: p.row_bounds(4)
            (None, 2)'''
    @overload
    def add_variable(self, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., name=...) -> int:
        '''PPLBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 243)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        It has not been implemented for selecting the variable type yet.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(lower_bound=-2)
            1
            sage: p.add_variable(name=\'x\',obj=2/3)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            2/3
            sage: p.add_variable(integer=True)
            3'''
    @overload
    def add_variable(self) -> Any:
        '''PPLBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 243)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        It has not been implemented for selecting the variable type yet.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(lower_bound=-2)
            1
            sage: p.add_variable(name=\'x\',obj=2/3)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            2/3
            sage: p.add_variable(integer=True)
            3'''
    @overload
    def add_variable(self, lower_bound=...) -> Any:
        '''PPLBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 243)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        It has not been implemented for selecting the variable type yet.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(lower_bound=-2)
            1
            sage: p.add_variable(name=\'x\',obj=2/3)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            2/3
            sage: p.add_variable(integer=True)
            3'''
    @overload
    def add_variable(self, name=..., obj=...) -> Any:
        '''PPLBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 243)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        It has not been implemented for selecting the variable type yet.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(lower_bound=-2)
            1
            sage: p.add_variable(name=\'x\',obj=2/3)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            2/3
            sage: p.add_variable(integer=True)
            3'''
    @overload
    def add_variable(self, integer=...) -> Any:
        '''PPLBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 243)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        It has not been implemented for selecting the variable type yet.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(lower_bound=-2)
            1
            sage: p.add_variable(name=\'x\',obj=2/3)
            2
            sage: p.col_name(2)
            \'x\'
            sage: p.objective_coefficient(2)
            2/3
            sage: p.add_variable(integer=True)
            3'''
    def add_variables(self, intn, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., names=...) -> int:
        '''PPLBackend.add_variables(self, int n, lower_bound=0, upper_bound=None, binary=False, continuous=True, integer=False, obj=0, names=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 312)

        Add ``n`` variables.

        This amounts to adding new columns to the matrix. By default,
        the variables are both positive and real.

        It has not been implemented for selecting the variable type yet.

        INPUT:

        - ``n`` -- the number of new variables (must be > 0)

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- coefficient of all variables in the objective function (default: 0)

        - ``names`` -- list of names (default: ``None``)

        OUTPUT: the index of the variable created last

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variables(5)
            4
            sage: p.ncols()
            5
            sage: p.add_variables(2, lower_bound=-2.0, obj=42.0, names=[\'a\',\'b\'])
            6

        TESTS:

        Check that arguments are used::

            sage: p.col_bounds(5) # tol 1e-8
            (-2.0, None)
            sage: p.col_name(5)
            \'a\'
            sage: p.objective_coefficient(5) # tol 1e-8
            42.0'''
    def base_ring(self) -> Any:
        """PPLBackend.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 93)"""
    def col_bounds(self, intindex) -> Any:
        '''PPLBackend.col_bounds(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 928)

        Return the bounds of a specific variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        OUTPUT:

        A pair ``(lower_bound, upper_bound)``. Each of them can be set
        to ``None`` if the variable is not bounded in the
        corresponding direction, and is a real value otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0, None)
            sage: p.variable_upper_bound(0, 5)
            sage: p.col_bounds(0)
            (0, 5)'''
    def col_name(self, intindex) -> Any:
        '''PPLBackend.col_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 1039)

        Return the ``index``-th col name.

        INPUT:

        - ``index`` -- integer; the col\'s id

        - ``name`` -- (``char *``) its name; when set to ``NULL``
          (default), the method returns the current name

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variable(name="I am a variable")
            0
            sage: p.col_name(0)
            \'I am a variable\''''
    @overload
    def get_objective_value(self) -> Any:
        '''PPLBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 729)

        Return the exact value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(5/13*x[0] + x[1]/2 == 8/7)
            sage: p.set_objective(5/13*x[0] + x[1]/2)
            sage: p.solve()
            8/7

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([(0,1), (1,2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            15/2
            sage: p.get_variable_value(0)
            0
            sage: p.get_variable_value(1)
            3/2'''
    @overload
    def get_objective_value(self) -> Any:
        '''PPLBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 729)

        Return the exact value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(5/13*x[0] + x[1]/2 == 8/7)
            sage: p.set_objective(5/13*x[0] + x[1]/2)
            sage: p.solve()
            8/7

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([(0,1), (1,2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            15/2
            sage: p.get_variable_value(0)
            0
            sage: p.get_variable_value(1)
            3/2'''
    def get_variable_value(self, intvariable) -> Any:
        '''PPLBackend.get_variable_value(self, int variable)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 764)

        Return the value of a variable given by the solver.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([(0,1), (1, 2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            15/2
            sage: p.get_variable_value(0)
            0
            sage: p.get_variable_value(1)
            3/2'''
    @overload
    def init_mip(self) -> Any:
        """PPLBackend.init_mip(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 133)

        Converting the matrix form of the MIP Problem to PPL MIP_Problem.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='PPL')
            sage: p.base_ring()
            Rational Field
            sage: type(p.zero())
            <class 'sage.rings.rational.Rational'>
            sage: p.init_mip()"""
    @overload
    def init_mip(self) -> Any:
        """PPLBackend.init_mip(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 133)

        Converting the matrix form of the MIP Problem to PPL MIP_Problem.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='PPL')
            sage: p.base_ring()
            Rational Field
            sage: type(p.zero())
            <class 'sage.rings.rational.Rational'>
            sage: p.init_mip()"""
    @overload
    def is_maximization(self) -> bool:
        '''PPLBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 825)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''PPLBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 825)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''PPLBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 825)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    def is_variable_binary(self, intindex) -> bool:
        '''PPLBackend.is_variable_binary(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 956)

        Test whether the given variable is of binary type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.is_variable_binary(0)
            False'''
    def is_variable_continuous(self, intindex) -> bool:
        '''PPLBackend.is_variable_continuous(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 998)

        Test whether the given variable is of continuous/real type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.is_variable_continuous(0)
            True'''
    def is_variable_integer(self, intindex) -> bool:
        '''PPLBackend.is_variable_integer(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 977)

        Test whether the given variable is of integer type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.is_variable_integer(0)
            False'''
    @overload
    def ncols(self) -> int:
        '''PPLBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 792)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''PPLBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 792)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''PPLBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 792)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def nrows(self) -> int:
        '''PPLBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 809)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''PPLBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 809)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''PPLBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 809)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    def objective_coefficient(self, intvariable, coeff=...) -> Any:
        '''PPLBackend.objective_coefficient(self, int variable, coeff=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 458)

        Set or get the coefficient of a variable in the objective
        function

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``coeff`` -- integer; its coefficient

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variable()
            0
            sage: p.objective_coefficient(0)
            0
            sage: p.objective_coefficient(0,2)
            sage: p.objective_coefficient(0)
            2'''
    def problem_name(self, name=...) -> Any:
        '''PPLBackend.problem_name(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 844)

        Return or define the problem\'s name.

        INPUT:

        - ``name`` -- string; the problem\'s name. When set to
          ``None`` (default), the method returns the problem\'s name.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.problem_name("There once was a french fry")
            sage: print(p.problem_name())
            There once was a french fry'''
    def row(self, inti) -> Any:
        '''PPLBackend.row(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 865)

        Return a row.

        INPUT:

        - ``index`` -- integer; the constraint\'s id

        OUTPUT:

        A pair ``(indices, coeffs)`` where ``indices`` lists the
        entries whose coefficient is nonzero, and to which ``coeffs``
        associates their coefficient on the model of the
        ``add_linear_constraint`` method.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(zip(range(5), range(5)), 2, 2)
            sage: p.row(0)
            ([1, 2, 3, 4], [1, 2, 3, 4])
            sage: p.row_bounds(0)
            (2, 2)'''
    def row_bounds(self, intindex) -> Any:
        '''PPLBackend.row_bounds(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 900)

        Return the bounds of a specific constraint.

        INPUT:

        - ``index`` -- integer; the constraint\'s id

        OUTPUT:

        A pair ``(lower_bound, upper_bound)``. Each of them can be set
        to ``None`` if the constraint is not bounded in the
        corresponding direction, and is a real value otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(zip(range(5), range(5)), 2, 2)
            sage: p.row(0)
            ([1, 2, 3, 4], [1, 2, 3, 4])
            sage: p.row_bounds(0)
            (2, 2)'''
    def row_name(self, intindex) -> Any:
        '''PPLBackend.row_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 1019)

        Return the ``index``-th row name.

        INPUT:

        - ``index`` -- integer; the row\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_linear_constraints(1, 2, None, names=["Empty constraint 1"])
            sage: p.row_name(0)
            \'Empty constraint 1\''''
    def set_objective(self, listcoeff, d=...) -> Any:
        '''PPLBackend.set_objective(self, list coeff, d=0)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 486)

        Set the objective function.

        INPUT:

        - ``coeff`` -- list of real values, whose i-th element is the
          coefficient of the i-th variable in the objective function

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0]*5 + x[1]/11 <= 6)
            sage: p.set_objective(x[0])
            sage: p.solve()
            6/5
            sage: p.set_objective(x[0]/2 + 1)
            sage: p.show()
            Maximization:
              1/2 x_0 + 1
            <BLANKLINE>
            Constraints:
              constraint_0: 5 x_0 + 1/11 x_1 <= 6
            Variables:
              x_0 is a continuous variable (min=0, max=+oo)
              x_1 is a continuous variable (min=0, max=+oo)
            sage: p.solve()
            8/5

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(5)
            4
            sage: p.set_objective([1, 1, 2, 1, 3])
            sage: [p.objective_coefficient(x) for x in range(5)]
            [1, 1, 2, 1, 3]'''
    def set_sense(self, intsense) -> Any:
        '''PPLBackend.set_sense(self, int sense)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 432)

        Set the direction (maximization/minimization).

        INPUT:

        - ``sense`` -- integer:

            * +1 => Maximization
            * -1 => Minimization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    def set_variable_type(self, intvariable, intvtype) -> Any:
        '''PPLBackend.set_variable_type(self, int variable, int vtype)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 379)

        Set the type of a variable.

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``vtype`` -- integer:

            *  1  Integer
            *  0  Binary
            *  -1  Continuous

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variables(5)
            4
            sage: p.set_variable_type(0,1)
            sage: p.is_variable_integer(0)
            True
            sage: p.set_variable_type(3,0)
            sage: p.is_variable_integer(3) or p.is_variable_binary(3)
            True
            sage: p.col_bounds(3) # tol 1e-6
            (0, 1)
            sage: p.set_variable_type(3, -1)
            sage: p.is_variable_continuous(3)
            True

        TESTS:

        Test that an exception is raised when an invalid type is passed::

            sage: p.set_variable_type(3, -2)
            Traceback (most recent call last):
            ...
            ValueError: ...'''
    def set_verbosity(self, intlevel) -> Any:
        '''PPLBackend.set_verbosity(self, int level)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 528)

        Set the log (verbosity) level. Not Implemented.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.set_verbosity(0)'''
    @overload
    def solve(self) -> int:
        '''PPLBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 676)

        Solve the problem.

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the solver was not able to find it, etc...)

        EXAMPLES:

        A linear optimization problem::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.solve()
            0

        An unbounded problem::

            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: ...

        An integer optimization problem::

            sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
            sage: x = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(2*x[0] + 3*x[1], max = 6)
            sage: p.add_constraint(3*x[0] + 2*x[1], max = 6)
            sage: p.set_objective(x[0] + x[1] + 7)
            sage: p.solve()
            9'''
    @overload
    def solve(self) -> Any:
        '''PPLBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 676)

        Solve the problem.

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the solver was not able to find it, etc...)

        EXAMPLES:

        A linear optimization problem::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.solve()
            0

        An unbounded problem::

            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: ...

        An integer optimization problem::

            sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
            sage: x = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(2*x[0] + 3*x[1], max = 6)
            sage: p.add_constraint(3*x[0] + 2*x[1], max = 6)
            sage: p.set_objective(x[0] + x[1] + 7)
            sage: p.solve()
            9'''
    @overload
    def solve(self) -> Any:
        '''PPLBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 676)

        Solve the problem.

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the solver was not able to find it, etc...)

        EXAMPLES:

        A linear optimization problem::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.solve()
            0

        An unbounded problem::

            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: ...

        An integer optimization problem::

            sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
            sage: x = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(2*x[0] + 3*x[1], max = 6)
            sage: p.add_constraint(3*x[0] + 2*x[1], max = 6)
            sage: p.set_objective(x[0] + x[1] + 7)
            sage: p.solve()
            9'''
    @overload
    def solve(self) -> Any:
        '''PPLBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 676)

        Solve the problem.

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the solver was not able to find it, etc...)

        EXAMPLES:

        A linear optimization problem::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.solve()
            0

        An unbounded problem::

            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: ...

        An integer optimization problem::

            sage: p = MixedIntegerLinearProgram(solver=\'PPL\')
            sage: x = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(2*x[0] + 3*x[1], max = 6)
            sage: p.add_constraint(3*x[0] + 2*x[1], max = 6)
            sage: p.set_objective(x[0] + x[1] + 7)
            sage: p.solve()
            9'''
    def variable_lower_bound(self, intindex, value=...) -> Any:
        '''PPLBackend.variable_lower_bound(self, int index, value=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 1095)

        Return or define the lower bound on a variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        - ``value`` -- real value, or ``None`` to mean that the
          variable has not lower bound. When set to ``False``
          (default), the method returns the current value.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0, None)
            sage: p.variable_lower_bound(0, 5)
            sage: p.col_bounds(0)
            (5, None)
            sage: p.variable_lower_bound(0, None)
            sage: p.col_bounds(0)
            (None, None)'''
    def variable_upper_bound(self, intindex, value=...) -> Any:
        '''PPLBackend.variable_upper_bound(self, int index, value=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 1063)

        Return or define the upper bound on a variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        - ``value`` -- real value, or ``None`` to mean that the
          variable has not upper bound. When set to ``False``
          (default), the method returns the current value.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "PPL")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0, None)
            sage: p.variable_upper_bound(0, 5)
            sage: p.col_bounds(0)
            (0, 5)
            sage: p.variable_upper_bound(0, None)
            sage: p.col_bounds(0)
            (0, None)'''
    def zero(self) -> Any:
        """PPLBackend.zero(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 97)"""
    def __copy__(self) -> Any:
        '''PPLBackend.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/ppl_backend.pyx (starting at line 100)

        Return a copy of ``self``.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = MixedIntegerLinearProgram(solver = "PPL")
            sage: b = p.new_variable()
            sage: p.add_constraint(b[1] + b[2] <= 6)
            sage: p.set_objective(b[1] + b[2])
            sage: cp = copy(p.get_backend())
            sage: cp.solve()
            0
            sage: cp.get_objective_value()
            6'''
