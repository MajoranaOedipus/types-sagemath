import _cython_3_2_1
import sage.structure.sage_object
from typing import Any, ClassVar, overload

__pyx_capi__: dict
default_mip_solver: _cython_3_2_1.cython_function_or_method
default_solver: None
get_solver: _cython_3_2_1.cython_function_or_method

class GenericBackend(sage.structure.sage_object.SageObject):
    _test_add_col: ClassVar[method] = ...
    _test_add_linear_constraint_vector: ClassVar[method] = ...
    _test_add_linear_constraints: ClassVar[method] = ...
    _test_add_variables: ClassVar[method] = ...
    _test_copy_some_mips: ClassVar[method] = ...
    _test_sense: ClassVar[method] = ...
    _test_solve: ClassVar[method] = ...
    _test_solve_trac_18572: ClassVar[method] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_col(self, indices, coeffs) -> Any:
        '''GenericBackend.add_col(self, indices, coeffs)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 564)

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

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.nrows()
            5'''
    def add_linear_constraint(self, coefficients, lower_bound, upper_bound, name=...) -> Any:
        '''GenericBackend.add_linear_constraint(self, coefficients, lower_bound, upper_bound, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 448)

        Add a linear constraint.

        INPUT:

        - ``coefficients`` -- an iterable of pairs ``(i, v)``. In each
          pair, ``i`` is a variable index (integer) and ``v`` is a
          value (element of :meth:`base_ring`).

        - ``lower_bound`` -- element of :meth:`base_ring` or
          ``None``; the lower bound

        - ``upper_bound`` -- element of :meth:`base_ring` or
          ``None``; the upper bound

        - ``name`` -- string or ``None``; optional name for this row

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint( zip(range(5), range(5)), 2.0, 2.0)
            sage: p.row(0)
            ([0, 1, 2, 3, 4], [0.0, 1.0, 2.0, 3.0, 4.0])
            sage: p.row_bounds(0)
            (2.0, 2.0)
            sage: p.add_linear_constraint( zip(range(5), range(5)), 1.0, 1.0, name=\'foo\')
            sage: p.row_name(1)
            \'foo\''''
    def add_linear_constraint_vector(self, degree, coefficients, lower_bound, upper_bound, name=...) -> Any:
        '''GenericBackend.add_linear_constraint_vector(self, degree, coefficients, lower_bound, upper_bound, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 484)

        Add a vector-valued linear constraint.

        .. NOTE::

            This is the generic implementation, which will split the
            vector-valued constraint into components and add these
            individually. Backends are encouraged to replace it with
            their own optimized implementation.

        INPUT:

        - ``degree`` -- integer; the vector degree, that is, the
          number of new scalar constraints

        - ``coefficients`` -- an iterable of pairs ``(i, v)``. In each
          pair, ``i`` is a variable index (integer) and ``v`` is a
          vector (real and of length ``degree``).

        - ``lower_bound`` -- either a vector or ``None``; the
          component-wise lower bound

        - ``upper_bound`` -- either a vector or ``None``; the
          component-wise upper bound

        - ``name`` -- string or ``None``; an optional name for all new
          rows

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: coeffs = ([0, vector([1, 2])], [1, vector([2, 3])])
            sage: upper = vector([5, 5])
            sage: lower = vector([0, 0])
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint_vector(2, coeffs, lower, upper, \'foo\')'''
    def add_linear_constraints(self, intnumber, lower_bound, upper_bound, names=...) -> Any:
        '''GenericBackend.add_linear_constraints(self, int number, lower_bound, upper_bound, names=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 624)

        Add ``\'number`` linear constraints.

        INPUT:

        - ``number`` -- integer; the number of constraints to add

        - ``lower_bound`` -- a lower bound, either a real value or ``None``

        - ``upper_bound`` -- an upper bound, either a real value or ``None``

        - ``names`` -- an optional list of names (default: ``None``)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            5
            sage: p.add_linear_constraints(5, None, 2)
            sage: p.row(4)
            ([], [])
            sage: p.row_bounds(4)
            (None, 2.0)'''
    @overload
    def add_variable(self, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., name=...) -> int:
        '''GenericBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 42)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(binary=True)
            1
            sage: p.add_variable(lower_bound=-2.0, integer=True)
            2
            sage: p.add_variable(continuous=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    @overload
    def add_variable(self) -> Any:
        '''GenericBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 42)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(binary=True)
            1
            sage: p.add_variable(lower_bound=-2.0, integer=True)
            2
            sage: p.add_variable(continuous=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    @overload
    def add_variable(self, binary=...) -> Any:
        '''GenericBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 42)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(binary=True)
            1
            sage: p.add_variable(lower_bound=-2.0, integer=True)
            2
            sage: p.add_variable(continuous=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    @overload
    def add_variable(self, lower_bound=..., integer=...) -> Any:
        '''GenericBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 42)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(binary=True)
            1
            sage: p.add_variable(lower_bound=-2.0, integer=True)
            2
            sage: p.add_variable(continuous=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    @overload
    def add_variable(self, continuous=..., integer=...) -> Any:
        '''GenericBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 42)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(binary=True)
            1
            sage: p.add_variable(lower_bound=-2.0, integer=True)
            2
            sage: p.add_variable(continuous=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    @overload
    def add_variable(self, name=..., obj=...) -> Any:
        '''GenericBackend.add_variable(self, lower_bound=0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 42)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integral (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable(binary=True)
            1
            sage: p.add_variable(lower_bound=-2.0, integer=True)
            2
            sage: p.add_variable(continuous=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.add_variable(name=\'x\', obj=1.0)
            3
            sage: p.col_name(3)
            \'x\'
            sage: p.objective_coefficient(3)
            1.0'''
    def add_variables(self, intn, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., names=...) -> int:
        '''GenericBackend.add_variables(self, int n, lower_bound=False, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, names=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 97)

        Add ``n`` variables.

        This amounts to adding new columns to the matrix. By default,
        the variables are both nonnegative and real.

        INPUT:

        - ``n`` -- the number of new variables (must be > 0)

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is binary (default: ``True``)

        - ``integer`` -- ``True`` if the variable is binary (default: ``False``)

        - ``obj`` -- coefficient of all variables in the objective function (default: 0.0)

        - ``names`` -- list of names (default: ``None``)

        OUTPUT: the index of the variable created last

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variables(5)
            4
            sage: p.ncols()
            5
            sage: p.add_variables(2, lower_bound=-2.0, integer=True, names=[\'a\',\'b\'])
            6

        TESTS:

        Check that arguments are used::

            sage: # optional - nonexistent_lp_solver
            sage: p.col_bounds(5)               # tol 1e-8
            (-2.0, None)
            sage: p.is_variable_integer(5)
            True
            sage: p.col_name(5)
            \'a\'
            sage: p.objective_coefficient(5)    # tol 1e-8
            42.0'''
    def base_ring(self) -> Any:
        """GenericBackend.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 35)"""
    @overload
    def best_known_objective_bound(self) -> Any:
        '''GenericBackend.best_known_objective_bound(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 778)

        Return the value of the currently best known bound.

        This method returns the current best upper (resp. lower) bound on the
        optimal value of the objective function in a maximization
        (resp. minimization) problem. It is equal to the output of
        :meth:`get_objective_value` if the MILP found an optimal solution, but
        it can differ if it was interrupted manually or after a time limit (cf
        :meth:`solver_parameter`).

        .. NOTE::

           Has no meaning unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(solver="Nonexistent_LP_solver")
            sage: b = p.new_variable(binary=True)
            sage: for u,v in graphs.CycleGraph(5).edges(labels=False):
            ....:     p.add_constraint(b[u]+b[v]<=1)
            sage: p.set_objective(p.sum(b[x] for x in range(5)))
            sage: p.solve()
            2.0
            sage: pb = p.get_backend()
            sage: pb.get_objective_value()
            2.0
            sage: pb.best_known_objective_bound()
            2.0'''
    @overload
    def best_known_objective_bound(self) -> Any:
        '''GenericBackend.best_known_objective_bound(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 778)

        Return the value of the currently best known bound.

        This method returns the current best upper (resp. lower) bound on the
        optimal value of the objective function in a maximization
        (resp. minimization) problem. It is equal to the output of
        :meth:`get_objective_value` if the MILP found an optimal solution, but
        it can differ if it was interrupted manually or after a time limit (cf
        :meth:`solver_parameter`).

        .. NOTE::

           Has no meaning unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(solver="Nonexistent_LP_solver")
            sage: b = p.new_variable(binary=True)
            sage: for u,v in graphs.CycleGraph(5).edges(labels=False):
            ....:     p.add_constraint(b[u]+b[v]<=1)
            sage: p.set_objective(p.sum(b[x] for x in range(5)))
            sage: p.solve()
            2.0
            sage: pb = p.get_backend()
            sage: pb.get_objective_value()
            2.0
            sage: pb.best_known_objective_bound()
            2.0'''
    def col_bounds(self, intindex) -> Any:
        '''GenericBackend.col_bounds(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1120)

        Return the bounds of a specific variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        OUTPUT:

        A pair ``(lower_bound, upper_bound)``. Each of them can be set
        to ``None`` if the variable is not bounded in the
        corresponding direction, and is a real value otherwise.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_upper_bound(0, 5)
            sage: p.col_bounds(0)
            (0.0, 5.0)'''
    def col_name(self, intindex) -> Any:
        '''GenericBackend.col_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1239)

        Return the ``index``-th column name.

        INPUT:

        - ``index`` -- integer; the column id

        - ``name`` -- (``char *``) its name; when set to ``NULL``
          (default), the method returns the current name

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variable(name="I am a variable")
            1
            sage: p.col_name(0)
            \'I am a variable\''''
    @overload
    def copy(self) -> Any:
        '''GenericBackend.copy(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1003)

        Return a copy of ``self``.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = MixedIntegerLinearProgram(solver="Nonexistent_LP_solver")
            sage: b = p.new_variable()
            sage: p.add_constraint(b[1] + b[2] <= 6)
            sage: p.set_objective(b[1] + b[2])
            sage: copy(p).solve()
            6.0'''
    @overload
    def copy(self, p) -> Any:
        '''GenericBackend.copy(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1003)

        Return a copy of ``self``.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = MixedIntegerLinearProgram(solver="Nonexistent_LP_solver")
            sage: b = p.new_variable()
            sage: p.add_constraint(b[1] + b[2] <= 6)
            sage: p.set_objective(b[1] + b[2])
            sage: copy(p).solve()
            6.0'''
    @overload
    def get_objective_value(self) -> Any:
        '''GenericBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 749)

        Return the value of the objective function.

        .. NOTE::

           Behavior is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            1
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
        '''GenericBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 749)

        Return the value of the objective function.

        .. NOTE::

           Behavior is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            1
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
    def get_relative_objective_gap(self) -> Any:
        '''GenericBackend.get_relative_objective_gap(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 811)

        Return the relative objective gap of the best known solution.

        For a minimization problem, this value is computed by
        `(\\texttt{bestinteger} - \\texttt{bestobjective}) / (1e-10 +
        |\\texttt{bestobjective}|)`, where ``bestinteger`` is the value returned
        by :meth:`~MixedIntegerLinearProgram.get_objective_value` and
        ``bestobjective`` is the value returned by
        :meth:`~MixedIntegerLinearProgram.best_known_objective_bound`. For a
        maximization problem, the value is computed by `(\\texttt{bestobjective}
        - \\texttt{bestinteger}) / (1e-10 + |\\texttt{bestobjective}|)`.

        .. NOTE::

           Has no meaning unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(solver="Nonexistent_LP_solver")
            sage: b = p.new_variable(binary=True)
            sage: for u,v in graphs.CycleGraph(5).edges(labels=False):
            ....:     p.add_constraint(b[u]+b[v]<=1)
            sage: p.set_objective(p.sum(b[x] for x in range(5)))
            sage: p.solve()
            2.0
            sage: pb = p.get_backend()
            sage: pb.get_objective_value()
            2.0
            sage: pb.get_relative_objective_gap()
            0.0'''
    def get_variable_value(self, intvariable) -> Any:
        '''GenericBackend.get_variable_value(self, int variable)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 846)

        Return the value of a variable given by the solver.

        .. NOTE::

           Behavior is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            1
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
        '''GenericBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 920)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''GenericBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 920)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''GenericBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 920)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    def is_slack_variable_basic(self, intindex) -> bool:
        '''GenericBackend.is_slack_variable_basic(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1485)

        Test whether the slack variable of the given row is basic.

        This assumes that the problem has been solved with the simplex method
        and a basis is available.  Otherwise an exception will be raised.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(maximization=True,
            ....:                               solver="Nonexistent_LP_solver")
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(-x[0] + x[1] <= 2)
            sage: p.add_constraint(8 * x[0] + 2 * x[1] <= 17)
            sage: p.set_objective(5.5 * x[0] - 3 * x[1])
            sage: b = p.get_backend()
            sage: # Backend-specific commands to instruct solver to use simplex method here
            sage: b.solve()
            0
            sage: b.is_slack_variable_basic(0)
            True
            sage: b.is_slack_variable_basic(1)
            False'''
    def is_slack_variable_nonbasic_at_lower_bound(self, intindex) -> bool:
        '''GenericBackend.is_slack_variable_nonbasic_at_lower_bound(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1516)

        Test whether the given variable is nonbasic at lower bound.

        This assumes that the problem has been solved with the simplex method
        and a basis is available.  Otherwise an exception will be raised.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(maximization=True,
            ....:                               solver="Nonexistent_LP_solver")
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(-x[0] + x[1] <= 2)
            sage: p.add_constraint(8 * x[0] + 2 * x[1] <= 17)
            sage: p.set_objective(5.5 * x[0] - 3 * x[1])
            sage: b = p.get_backend()
            sage: # Backend-specific commands to instruct solver to use simplex method here
            sage: b.solve()
            0
            sage: b.is_slack_variable_nonbasic_at_lower_bound(0)
            False
            sage: b.is_slack_variable_nonbasic_at_lower_bound(1)
            True'''
    def is_variable_basic(self, intindex) -> bool:
        '''GenericBackend.is_variable_basic(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1423)

        Test whether the given variable is basic.

        This assumes that the problem has been solved with the simplex method
        and a basis is available.  Otherwise an exception will be raised.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(maximization=True,
            ....:                               solver="Nonexistent_LP_solver")
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(-x[0] + x[1] <= 2)
            sage: p.add_constraint(8 * x[0] + 2 * x[1] <= 17)
            sage: p.set_objective(5.5 * x[0] - 3 * x[1])
            sage: b = p.get_backend()
            sage: # Backend-specific commands to instruct solver to use simplex method here
            sage: b.solve()
            0
            sage: b.is_variable_basic(0)
            True
            sage: b.is_variable_basic(1)
            False'''
    def is_variable_binary(self, intindex) -> bool:
        '''GenericBackend.is_variable_binary(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1149)

        Test whether the given variable is of binary type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.set_variable_type(0,0)
            sage: p.is_variable_binary(0)
            True'''
    def is_variable_continuous(self, intindex) -> bool:
        '''GenericBackend.is_variable_continuous(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1195)

        Test whether the given variable is of continuous/real type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.is_variable_continuous(0)
            True
            sage: p.set_variable_type(0,1)
            sage: p.is_variable_continuous(0)
            False'''
    def is_variable_integer(self, intindex) -> bool:
        '''GenericBackend.is_variable_integer(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1172)

        Test whether the given variable is of integer type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.set_variable_type(0,1)
            sage: p.is_variable_integer(0)
            True'''
    def is_variable_nonbasic_at_lower_bound(self, intindex) -> bool:
        '''GenericBackend.is_variable_nonbasic_at_lower_bound(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1454)

        Test whether the given variable is nonbasic at lower bound.

        This assumes that the problem has been solved with the simplex method
        and a basis is available.  Otherwise an exception will be raised.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(maximization=True,
            ....:                               solver="Nonexistent_LP_solver")
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(-x[0] + x[1] <= 2)
            sage: p.add_constraint(8 * x[0] + 2 * x[1] <= 17)
            sage: p.set_objective(5.5 * x[0] - 3 * x[1])
            sage: b = p.get_backend()
            sage: # Backend-specific commands to instruct solver to use simplex method here
            sage: b.solve()
            0
            sage: b.is_variable_nonbasic_at_lower_bound(0)
            False
            sage: b.is_variable_nonbasic_at_lower_bound(1)
            True'''
    @overload
    def ncols(self) -> int:
        '''GenericBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 875)

        Return the number of columns/variables.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''GenericBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 875)

        Return the number of columns/variables.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''GenericBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 875)

        Return the number of columns/variables.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def nrows(self) -> int:
        '''GenericBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 902)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''GenericBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 902)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''GenericBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 902)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2'''
    def objective_coefficient(self, intvariable, coeff=...) -> Any:
        '''GenericBackend.objective_coefficient(self, int variable, coeff=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 286)

        Set or get the coefficient of a variable in the objective
        function

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``coeff`` -- double; its coefficient

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variable()
            0
            sage: p.objective_coefficient(0)
            0.0
            sage: p.objective_coefficient(0,2)
            sage: p.objective_coefficient(0)
            2.0'''
    @overload
    def objective_constant_term(self, d=...) -> Any:
        '''GenericBackend.objective_constant_term(self, d=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 312)

        Set or get the constant term in the objective function.

        INPUT:

        - ``d`` -- double; its coefficient.  If ``None`` (default), return the
          current value.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.objective_constant_term()
            0.0
            sage: p.objective_constant_term(42)
            sage: p.objective_constant_term()
            42.0'''
    @overload
    def objective_constant_term(self) -> Any:
        '''GenericBackend.objective_constant_term(self, d=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 312)

        Set or get the constant term in the objective function.

        INPUT:

        - ``d`` -- double; its coefficient.  If ``None`` (default), return the
          current value.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.objective_constant_term()
            0.0
            sage: p.objective_constant_term(42)
            sage: p.objective_constant_term()
            42.0'''
    @overload
    def objective_constant_term(self) -> Any:
        '''GenericBackend.objective_constant_term(self, d=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 312)

        Set or get the constant term in the objective function.

        INPUT:

        - ``d`` -- double; its coefficient.  If ``None`` (default), return the
          current value.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.objective_constant_term()
            0.0
            sage: p.objective_constant_term(42)
            sage: p.objective_constant_term()
            42.0'''
    def problem_name(self, name=...) -> Any:
        '''GenericBackend.problem_name(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 937)

        Return or define the problem\'s name.

        INPUT:

        - ``name`` -- string; the problem\'s name. When set to
          ``None`` (default), the method returns the problem\'s name.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")   # optional - Nonexistent_LP_solver
            sage: p.problem_name("There once was a french fry") # optional - Nonexistent_LP_solver
            sage: print(p.problem_name())                       # optional - Nonexistent_LP_solver
            There once was a french fry'''
    def remove_constraint(self, inti) -> Any:
        '''GenericBackend.remove_constraint(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 390)

        Remove a constraint.

        INPUT:

        - ``i`` -- index of the constraint to remove

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(solver="Nonexistent_LP_solver")
            sage: v = p.new_variable(nonnegative=True)
            sage: x,y = v[0], v[1]
            sage: p.add_constraint(2*x + 3*y, max=6)
            sage: p.add_constraint(3*x + 2*y, max=6)
            sage: p.set_objective(x + y + 7)
            sage: p.set_integer(x); p.set_integer(y)
            sage: p.solve()
            9.0
            sage: p.remove_constraint(0)
            sage: p.solve()
            10.0
            sage: p.get_values([x,y])
            [0.0, 3.0]'''
    def remove_constraints(self, constraints) -> Any:
        '''GenericBackend.remove_constraints(self, constraints)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 418)

        Remove several constraints.

        INPUT:

        - ``constraints`` -- an iterable containing the indices of the rows to remove

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([(0, 2), (1, 3)], None, 6)
            sage: p.add_linear_constraint([(0, 3), (1, 2)], None, 6)
            sage: p.remove_constraints([0, 1])'''
    def row(self, inti) -> Any:
        '''GenericBackend.row(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1061)

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
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(zip(range(5), range(5)), 2, 2)
            sage: p.row(0)
            ([4, 3, 2, 1], [4.0, 3.0, 2.0, 1.0]) ## FIXME: Why backwards?
            sage: p.row_bounds(0)
            (2.0, 2.0)'''
    def row_bounds(self, intindex) -> Any:
        '''GenericBackend.row_bounds(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1091)

        Return the bounds of a specific constraint.

        INPUT:

        - ``index`` -- integer; the constraint\'s id

        OUTPUT:

        A pair ``(lower_bound, upper_bound)``. Each of them can be set
        to ``None`` if the constraint is not bounded in the
        corresponding direction, and is a real value otherwise.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(list(range(5)), list(range(5)), 2, 2)
            sage: p.row(0)
            ([4, 3, 2, 1], [4.0, 3.0, 2.0, 1.0]) ## FIXME: Why backwards?
            sage: p.row_bounds(0)
            (2.0, 2.0)'''
    def row_name(self, intindex) -> Any:
        '''GenericBackend.row_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1220)

        Return the ``index``-th row name.

        INPUT:

        - ``index`` -- integer; the row\'s id

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_linear_constraints(1, 2, None, names=[\'Empty constraint 1\'])
            sage: p.row_name(0)
            \'Empty constraint 1\''''
    def set_objective(self, listcoeff, d=...) -> Any:
        '''GenericBackend.set_objective(self, list coeff, d=0.0)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 337)

        Set the objective function.

        INPUT:

        - ``coeff`` -- list of real values, whose i-th element is the
          coefficient of the i-th variable in the objective function

        - ``d`` -- double; the constant term in the linear function (set to `0`
          by default)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(5)
            4
            sage: p.set_objective([1, 1, 2, 1, 3])
            sage: [p.objective_coefficient(x) for x in range(5)]
            [1.0, 1.0, 2.0, 1.0, 3.0]

        Constants in the objective function are respected::

            sage: # optional - nonexistent_lp_solver
            sage: p = MixedIntegerLinearProgram(solver=\'Nonexistent_LP_solver\')
            sage: x,y = p[0], p[1]
            sage: p.add_constraint(2*x + 3*y, max=6)
            sage: p.add_constraint(3*x + 2*y, max=6)
            sage: p.set_objective(x + y + 7)
            sage: p.set_integer(x); p.set_integer(y)
            sage: p.solve()
            9.0'''
    def set_sense(self, intsense) -> Any:
        '''GenericBackend.set_sense(self, int sense)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 241)

        Set the direction (maximization/minimization).

        INPUT:

        - ``sense`` -- integer:

            * +1 => Maximization
            * -1 => Minimization

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    def set_variable_type(self, intvariable, intvtype) -> Any:
        '''GenericBackend.set_variable_type(self, int variable, int vtype)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 212)

        Set the type of a variable.

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``vtype`` -- integer:

          *  `1`  Integer
          *  `0`  Binary
          *  `-1`  Continuous

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.set_variable_type(0,1)
            sage: p.is_variable_integer(0)
            True'''
    def set_verbosity(self, intlevel) -> Any:
        '''GenericBackend.set_verbosity(self, int level)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 374)

        Set the log (verbosity) level.

        INPUT:

        - ``level`` -- integer; from 0 (no verbosity) to 3

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")  # optional - Nonexistent_LP_solver
            sage: p.set_verbosity(2)                                # optional - Nonexistent_LP_solver'''
    @overload
    def solve(self) -> int:
        '''GenericBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 693)

        Solve the problem.

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.solve()
            0
            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: ...'''
    @overload
    def solve(self) -> Any:
        '''GenericBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 693)

        Solve the problem.

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.solve()
            0
            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: ...'''
    @overload
    def solve(self) -> Any:
        '''GenericBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 693)

        Solve the problem.

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(list(range(5)), list(range(5)))
            sage: p.solve()
            0
            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: ...'''
    def solver_parameter(self, name, value=...) -> Any:
        '''GenericBackend.solver_parameter(self, name, value=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1396)

        Return or define a solver parameter.

        INPUT:

        - ``name`` -- string; the parameter

        - ``value`` -- the parameter\'s value if it is to be defined,
          or ``None`` (default) to obtain its current value

        .. NOTE::

           The list of available parameters is available at
           :meth:`~sage.numerical.mip.MixedIntegerLinearProgram.solver_parameter`.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.solver_parameter("timelimit")
            sage: p.solver_parameter("timelimit", 60)
            sage: p.solver_parameter("timelimit")'''
    def variable_lower_bound(self, intindex, value=...) -> Any:
        '''GenericBackend.variable_lower_bound(self, int index, value=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1369)

        Return or define the lower bound on a variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        - ``value`` -- real value, or ``None`` to mean that the
          variable has not lower bound. When set to ``False``
          (default), the method returns the current value.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_lower_bound(0, 5)
            sage: p.col_bounds(0)
            (5.0, None)'''
    def variable_upper_bound(self, intindex, value=...) -> Any:
        '''GenericBackend.variable_upper_bound(self, int index, value=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1342)

        Return or define the upper bound on a variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        - ``value`` -- real value, or ``None`` to mean that the
          variable has not upper bound. When set to ``False``
          (default), the method returns the current value.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_upper_bound(0, 5)
            sage: p.col_bounds(0)
            (0.0, 5.0)'''
    def write_lp(self, name) -> Any:
        '''GenericBackend.write_lp(self, name)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 957)

        Write the problem to a ``.lp`` file.

        INPUT:

        - ``filename`` -- string

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            2
            sage: p.add_linear_constraint([(0, 1], (1, 2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: from tempfile import NamedTemporaryFile
            sage: with NamedTemporaryFile(suffix=\'.lp\') as f:
            ....:     p.write_lp(f.name)'''
    def write_mps(self, name, intmodern) -> Any:
        '''GenericBackend.write_mps(self, name, int modern)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 980)

        Write the problem to a ``.mps`` file.

        INPUT:

        - ``filename`` -- string

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver="Nonexistent_LP_solver")
            sage: p.add_variables(2)
            2
            sage: p.add_linear_constraint([(0, 1), (1, 2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: from tempfile import NamedTemporaryFile
            sage: with NamedTemporaryFile(suffix=\'.lp\') as f:
            ....:     p.write_lp(f.name)'''
    def zero(self) -> Any:
        """GenericBackend.zero(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 39)"""
    def __copy__(self) -> Any:
        '''GenericBackend.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1021)

        Return a copy of ``self``.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = MixedIntegerLinearProgram(solver="Nonexistent_LP_solver")
            sage: b = p.new_variable()
            sage: p.add_constraint(b[1] + b[2] <= 6)
            sage: p.set_objective(b[1] + b[2])
            sage: cp = copy(p.get_backend())
            sage: cp.solve()
            0
            sage: cp.get_objective_value()
            6.0'''
    def __deepcopy__(self, memo=...) -> Any:
        '''GenericBackend.__deepcopy__(self, memo={})

        File: /build/sagemath/src/sage/src/sage/numerical/backends/generic_backend.pyx (starting at line 1041)

        Return a deep copy of ``self``.

        EXAMPLES::

            sage: # optional - nonexistent_lp_solver
            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = MixedIntegerLinearProgram(solver="Nonexistent_LP_solver")
            sage: b = p.new_variable()
            sage: p.add_constraint(b[1] + b[2] <= 6)
            sage: p.set_objective(b[1] + b[2])
            sage: cp = deepcopy(p.get_backend())
            sage: cp.solve()
            0
            sage: cp.get_objective_value()
            6.0'''
