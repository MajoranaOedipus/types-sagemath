import sage.numerical.backends.generic_backend
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.numerical.mip import MIPSolverException as MIPSolverException
from typing import Any, ClassVar, overload

FS_ENCODING: str
dbl_max: float
glp_absolute_tolerance: int
glp_backtracking: int
glp_binarize: int
glp_br_dth: int
glp_br_ffv: int
glp_br_lfv: int
glp_br_mfv: int
glp_br_pch: int
glp_br_tech: int
glp_branching: int
glp_bs: int
glp_bt_bfs: int
glp_bt_blb: int
glp_bt_bph: int
glp_bt_dfs: int
glp_bt_tech: int
glp_bv: int
glp_clique_cuts: int
glp_clq_cuts: int
glp_cov_cuts: int
glp_cv: int
glp_db: int
glp_dual: int
glp_dualp: int
glp_exact_simplex_only: int
glp_feas: int
glp_feasibility_pump: int
glp_fp_heur: int
glp_fr: int
glp_fx: int
glp_gmi_cuts: int
glp_gomory_cuts: int
glp_intopt_only: int
glp_it_lim: int
glp_iteration_limit: int
glp_iv: int
glp_lo: int
glp_max: int
glp_meth: int
glp_min: int
glp_mip_gap: int
glp_mip_gap_tolerance: int
glp_mir_cuts: int
glp_mixed_cover_cuts: int
glp_mixed_int_rounding_cuts: int
glp_mps_deck: int
glp_mps_file: int
glp_msg_all: int
glp_msg_dbg: int
glp_msg_err: int
glp_msg_lev_intopt: int
glp_msg_lev_simplex: int
glp_msg_off: int
glp_msg_on: int
glp_nf: int
glp_nl: int
glp_nofeas: int
glp_nu: int
glp_obj_ll: int
glp_obj_lower_limit: int
glp_obj_ul: int
glp_obj_upper_limit: int
glp_off: int
glp_on: int
glp_opt: int
glp_out_dly_intopt: int
glp_out_dly_simplex: int
glp_out_frq_intopt: int
glp_out_frq_simplex: int
glp_output_delay_intopt: int
glp_output_delay_simplex: int
glp_output_frequency_intopt: int
glp_pp_all: int
glp_pp_none: int
glp_pp_root: int
glp_pp_tech: int
glp_preprocessing: int
glp_presolve_intopt: int
glp_presolve_simplex: int
glp_pricing: int
glp_primal: int
glp_primal_v_dual: int
glp_pt_pse: int
glp_pt_std: int
glp_r_test: int
glp_ratio_test: int
glp_relative_tolerance: int
glp_rt_har: int
glp_rt_std: int
glp_simplex_only: int
glp_simplex_or_intopt: int
glp_simplex_then_intopt: int
glp_tm_lim_intopt: int
glp_tm_lim_simplex: int
glp_tol_bnd: int
glp_tol_dj: int
glp_tol_int: int
glp_tol_obj: int
glp_tol_piv: int
glp_tolerance_dual: int
glp_tolerance_pivot: int
glp_tolerance_primal: int
glp_undef: int
glp_up: int
glp_verbosity_intopt: int
glp_verbosity_simplex: int
int_max: int
solver_parameter_names_dict: dict
solver_parameter_values: dict

class GLPKBackend(sage.numerical.backends.generic_backend.GenericBackend):
    """File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 35)

        MIP Backend that uses the GLPK solver.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_col(self, indices, coeffs) -> Any:
        '''GLPKBackend.add_col(self, indices, coeffs)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 856)

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
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(range(5), range(5))
            sage: p.nrows()
            5'''
    def add_linear_constraint(self, coefficients, lower_bound, upper_bound, name=...) -> Any:
        '''GLPKBackend.add_linear_constraint(self, coefficients, lower_bound, upper_bound, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 563)

        Add a linear constraint.

        INPUT:

        - ``coefficients`` an iterable with ``(c,v)`` pairs where ``c``
          is a variable index (integer) and ``v`` is a value (real
          value).

        - ``lower_bound`` -- a lower bound, either a real value or ``None``

        - ``upper_bound`` -- an upper bound, either a real value or ``None``

        - ``name`` -- an optional name for this row (default: ``None``)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(zip(range(5), range(5)), 2.0, 2.0)
            sage: p.row(0)
            ([4, 3, 2, 1], [4.0, 3.0, 2.0, 1.0])
            sage: p.row_bounds(0)
            (2.0, 2.0)
            sage: p.add_linear_constraint(zip(range(5), range(5)), 1.0, 1.0, name=\'foo\')
            sage: p.row_name(1)
            \'foo\'

        TESTS:

        This used to crash Sage, but was fixed in :issue:`19525`::

            sage: p = MixedIntegerLinearProgram(solver=\'glpk\')
            sage: q = MixedIntegerLinearProgram(solver=\'glpk\')
            sage: q.add_constraint(p.new_variable()[0] <= 1)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index 0'''
    def add_linear_constraints(self, intnumber, lower_bound, upper_bound, names=...) -> Any:
        '''GLPKBackend.add_linear_constraints(self, int number, lower_bound, upper_bound, names=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 649)

        Add ``\'number`` linear constraints.

        INPUT:

        - ``number`` -- integer; the number of constraints to add

        - ``lower_bound`` -- a lower bound, either a real value or ``None``

        - ``upper_bound`` -- an upper bound, either a real value or ``None``

        - ``names`` -- an optional list of names (default: ``None``)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(5, None, 2)
            sage: p.row(4)
            ([], [])
            sage: p.row_bounds(4)
            (None, 2.0)
            sage: p.add_linear_constraints(2, None, 2, names=[\'foo\',\'bar\'])'''
    @overload
    def add_variable(self, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., name=...) -> int:
        '''GLPKBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 66)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive, real and the coefficient in the
        objective function is 0.0.

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

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
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
        '''GLPKBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 66)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive, real and the coefficient in the
        objective function is 0.0.

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

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
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
        '''GLPKBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 66)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive, real and the coefficient in the
        objective function is 0.0.

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

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
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
        '''GLPKBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 66)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive, real and the coefficient in the
        objective function is 0.0.

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

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
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
        '''GLPKBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 66)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive, real and the coefficient in the
        objective function is 0.0.

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

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
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
        '''GLPKBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 66)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive, real and the coefficient in the
        objective function is 0.0.

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

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
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
    def add_variables(self, intnumber, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., names=...) -> int:
        '''GLPKBackend.add_variables(self, int number, lower_bound=0.0, upper_bound=None, binary=False, continuous=False, integer=False, obj=0.0, names=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 144)

        Add ``number`` new variables.

        This amounts to adding new columns to the matrix. By default,
        the variables are both positive, real and their coefficient in
        the objective function is 0.0.

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

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.add_variables(5)
            4
            sage: p.ncols()
            5
            sage: p.add_variables(2, lower_bound=-2.0, integer=True, obj=42.0, names=[\'a\',\'b\'])
            6

        TESTS:

        Check that arguments are used::

            sage: p.col_bounds(5) # tol 1e-8
            (-2.0, None)
            sage: p.is_variable_integer(5)
            True
            sage: p.col_name(5)
            \'a\'
            sage: p.objective_coefficient(5)
            42.0'''
    @overload
    def best_known_objective_bound(self) -> Any:
        '''GLPKBackend.best_known_objective_bound(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1178)

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

            sage: # needs sage.graphs
            sage: g = graphs.CubeGraph(9)
            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.solver_parameter("mip_gap_tolerance",100)
            sage: b = p.new_variable(binary=True)
            sage: p.set_objective(p.sum(b[v] for v in g))
            sage: for v in g:
            ....:     p.add_constraint(b[v]+p.sum(b[u] for u in g.neighbors(v)) <= 1)
            sage: p.add_constraint(b[v] == 1) # Force an easy non-0 solution
            sage: p.solve() # rel tol 100
            1.0
            sage: backend = p.get_backend()
            sage: backend.best_known_objective_bound() # random
            48.0'''
    @overload
    def best_known_objective_bound(self) -> Any:
        '''GLPKBackend.best_known_objective_bound(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1178)

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

            sage: # needs sage.graphs
            sage: g = graphs.CubeGraph(9)
            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.solver_parameter("mip_gap_tolerance",100)
            sage: b = p.new_variable(binary=True)
            sage: p.set_objective(p.sum(b[v] for v in g))
            sage: for v in g:
            ....:     p.add_constraint(b[v]+p.sum(b[u] for u in g.neighbors(v)) <= 1)
            sage: p.add_constraint(b[v] == 1) # Force an easy non-0 solution
            sage: p.solve() # rel tol 100
            1.0
            sage: backend = p.get_backend()
            sage: backend.best_known_objective_bound() # random
            48.0'''
    def col_bounds(self, intindex) -> Any:
        '''GLPKBackend.col_bounds(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 804)

        Return the bounds of a specific variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        OUTPUT:

        A pair ``(lower_bound, upper_bound)``. Each of them can be set
        to ``None`` if the variable is not bounded in the
        corresponding direction, and is a real value otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_upper_bound(0, 5)
            sage: p.col_bounds(0)
            (0.0, 5.0)

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.col_bounds(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid column index 2'''
    def col_name(self, intindex) -> Any:
        '''GLPKBackend.col_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1381)

        Return the ``index``-th col name.

        INPUT:

        - ``index`` -- integer; the col\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variable(name=\'I am a variable\')
            0
            sage: p.col_name(0)
            \'I am a variable\'

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.col_name(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid column index 2'''
    def eval_tab_col(self, intk) -> Any:
        '''GLPKBackend.eval_tab_col(self, int k)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2988)

        Compute a column of the current simplex tableau.

        A (column) corresponds to some non-basic variable specified by the
        parameter ``k`` as follows:

        - if `0 \\leq k \\leq m-1`, the non-basic variable is `k`-th auxiliary
          variable,

        - if `m \\leq k \\leq m+n-1`, the non-basic variable is `(k-m)`-th
          structural variable,

        where `m` is the number of rows and `n` is the number of columns
        in the specified problem object.

        .. NOTE::

            The basis factorization must exist and the variable with
            index ``k`` must not be basic. Otherwise, a :exc:`ValueError` is
            be raised.

        INPUT:

        - ``k`` -- integer; the id of the non-basic variable

        OUTPUT:

        A pair ``(indices, coeffs)`` where ``indices`` lists the
        entries whose coefficient is nonzero, and to which ``coeffs``
        associates their coefficient in the computed column
        of the current simplex tableau.

        .. NOTE::

            Elements in ``indices`` have the same sense as index `k`.
            All these variables are basic by definition.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.eval_tab_col(1)
            Traceback (most recent call last):
            ...
            ValueError: basis factorization does not exist
            sage: lp.solve()
            0
            sage: lp.eval_tab_col(1)
            ([0, 5, 3], [-2.0, 2.0, -0.5])
            sage: lp.eval_tab_col(2)
            ([0, 5, 3], [8.0, -4.0, 1.5])
            sage: lp.eval_tab_col(4)
            ([0, 5, 3], [-2.0, 2.0, -1.25])
            sage: lp.eval_tab_col(0)
            Traceback (most recent call last):
            ...
            ValueError: slack variable 0 is basic
            sage: lp.eval_tab_col(-1)
            Traceback (most recent call last):
            ...
            ValueError: ...'''
    def eval_tab_row(self, intk) -> Any:
        '''GLPKBackend.eval_tab_row(self, int k)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2890)

        Compute a row of the current simplex tableau.

        A row corresponds to some basic variable specified by the parameter
        ``k`` as follows:

        - if `0 \\leq k \\leq m-1`, the basic variable is `k`-th auxiliary
          variable,

        - if `m \\leq k \\leq m+n-1`, the basic variable is `(k-m)`-th structural
          variable,

        where `m` is the number of rows and `n` is the number of columns in the
        specified problem object.

        .. NOTE::

            The basis factorization must exist and the variable with
            index ``k`` must be basic. Otherwise, a :exc:`ValueError` is
            be raised.

        INPUT:

        - ``k`` -- integer; the id of the basic variable

        OUTPUT:

        A pair ``(indices, coeffs)`` where ``indices`` lists the
        entries whose coefficient is nonzero, and to which ``coeffs``
        associates their coefficient in the computed row
        of the current simplex tableau.

        .. NOTE::

            Elements in ``indices`` have the same sense as index ``k``.
            All these variables are non-basic by definition.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.eval_tab_row(0)
            Traceback (most recent call last):
            ...
            ValueError: basis factorization does not exist
            sage: lp.solve()
            0
            sage: lp.eval_tab_row(0)
            ([1, 2, 4], [-2.0, 8.0, -2.0])
            sage: lp.eval_tab_row(3)
            ([1, 2, 4], [-0.5, 1.5, -1.25])
            sage: lp.eval_tab_row(5)
            ([1, 2, 4], [2.0, -4.0, 2.0])
            sage: lp.eval_tab_row(1)
            Traceback (most recent call last):
            ...
            ValueError: slack variable 1 is not basic
            sage: lp.eval_tab_row(-1)
            Traceback (most recent call last):
            ...
            ValueError: ...'''
    def get_col_dual(self, intvariable) -> double:
        '''GLPKBackend.get_col_dual(self, int variable) -> double

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2639)

        Return the dual value (reduced cost) of a variable

        The dual value is the reduced cost of a variable.
        The reduced cost is the amount by which the objective coefficient
        of a non basic variable has to change to become a basic variable.

        INPUT:

        - ``variable`` -- the number of the variable

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.
           If the simplex algorithm has not been used for solving just a
           0.0 will be returned.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(3)
            2
            sage: p.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: p.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: p.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: p.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: p.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: p.solve()
            0
            sage: p.get_col_dual(1)
            -5.0

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.get_col_dual(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid column index 2'''
    def get_col_stat(self, intj) -> int:
        '''GLPKBackend.get_col_stat(self, int j) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2739)

        Retrieve the status of a variable.

        INPUT:

        - ``j`` -- the index of the variable

        OUTPUT:

        Current status assigned to the structural variable associated
        with j-th column:

            * GLP_BS = 1     basic variable
            * GLP_NL = 2     non-basic variable on lower bound
            * GLP_NU = 3     non-basic variable on upper bound
            * GLP_NF = 4     non-basic free (unbounded) variable
            * GLP_NS = 5     non-basic fixed variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            0
            sage: lp.get_col_stat(0)
            1
            sage: lp.get_col_stat(1)
            2
            sage: lp.get_col_stat(100)
            Traceback (most recent call last):
            ...
            ValueError: The variable\'s index j must satisfy 0 <= j < number_of_variables'''
    @overload
    def get_objective_value(self) -> Any:
        '''GLPKBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1147)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([[0, 1], [1, 2]], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            7.5
            sage: p.get_variable_value(0) # abs tol 1e-15
            0.0
            sage: p.get_variable_value(1)
            1.5'''
    @overload
    def get_objective_value(self) -> Any:
        '''GLPKBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1147)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([[0, 1], [1, 2]], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            7.5
            sage: p.get_variable_value(0) # abs tol 1e-15
            0.0
            sage: p.get_variable_value(1)
            1.5'''
    def get_relative_objective_gap(self) -> Any:
        '''GLPKBackend.get_relative_objective_gap(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1212)

        Return the relative objective gap of the best known solution.

        For a minimization problem, this value is computed by
        `(\\texttt{bestinteger} - \\texttt{bestobjective}) / (1e-10 +
        |\\texttt{bestobjective}|)`, where ``bestinteger`` is the value returned
        by :meth:`get_objective_value` and ``bestobjective`` is the value
        returned by :meth:`best_known_objective_bound`. For a maximization
        problem, the value is computed by `(\\texttt{bestobjective} -
        \\texttt{bestinteger}) / (1e-10 + |\\texttt{bestobjective}|)`.

        .. NOTE::

           Has no meaning unless ``solve`` has been called before.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: g = graphs.CubeGraph(9)
            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.solver_parameter("mip_gap_tolerance",100)
            sage: b = p.new_variable(binary=True)
            sage: p.set_objective(p.sum(b[v] for v in g))
            sage: for v in g:
            ....:     p.add_constraint(b[v]+p.sum(b[u] for u in g.neighbors(v)) <= 1)
            sage: p.add_constraint(b[v] == 1) # Force an easy non-0 solution
            sage: p.solve() # rel tol 100
            1.0
            sage: backend = p.get_backend()
            sage: backend.get_relative_objective_gap() # random
            46.99999999999999

        TESTS:

        Just make sure that the variable *has* been defined, and is not just
        undefined::

            sage: backend.get_relative_objective_gap() > 1                              # needs sage.graphs
            True'''
    def get_row_dual(self, intvariable) -> double:
        '''GLPKBackend.get_row_dual(self, int variable) -> double

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2592)

        Return the dual value of a constraint.

        The dual value of the i-th row is also the value of the i-th variable
        of the dual problem.

        The dual value of a constraint is the shadow price of the constraint.
        The shadow price is the amount by which the objective value will change
        if the constraints bounds change by one unit under the precondition
        that the basis remains the same.

        INPUT:

        - ``variable`` -- the number of the constraint

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.
           If the simplex algorithm has not been used for solving 0.0 will
           be returned.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            0
            sage: lp.get_row_dual(0)   # tolerance 0.00001
            0.0
            sage: lp.get_row_dual(1)   # tolerance 0.00001
            10.0'''
    def get_row_prim(self, inti) -> Any:
        '''GLPKBackend.get_row_prim(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1300)

        Return the value of the auxiliary variable associated with i-th row.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            0
            sage: lp.get_objective_value()
            280.0
            sage: lp.get_row_prim(0)
            24.0
            sage: lp.get_row_prim(1)
            20.0
            sage: lp.get_row_prim(2)
            8.0

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.get_row_prim(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid row index 2'''
    def get_row_stat(self, inti) -> int:
        '''GLPKBackend.get_row_stat(self, int i) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2693)

        Retrieve the status of a constraint.

        INPUT:

        - ``i`` -- the index of the constraint

        OUTPUT:

        Current status assigned to the auxiliary variable associated with i-th
        row:

            * GLP_BS = 1     basic variable
            * GLP_NL = 2     non-basic variable on lower bound
            * GLP_NU = 3     non-basic variable on upper bound
            * GLP_NF = 4     non-basic free (unbounded) variable
            * GLP_NS = 5     non-basic fixed variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            0
            sage: lp.get_row_stat(0)
            1
            sage: lp.get_row_stat(1)
            3
            sage: lp.get_row_stat(-1)
            Traceback (most recent call last):
            ...
            ValueError: The constraint\'s index i must satisfy 0 <= i < number_of_constraints'''
    def get_variable_value(self, intvariable) -> Any:
        '''GLPKBackend.get_variable_value(self, int variable)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1255)

        Return the value of a variable given by the solver.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([[0, 1], [1, 2]], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: p.get_objective_value()
            7.5
            sage: p.get_variable_value(0) # abs tol 1e-15
            0.0
            sage: p.get_variable_value(1)
            1.5

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.get_variable_value(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index 2'''
    @overload
    def is_maximization(self) -> bool:
        '''GLPKBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1572)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''GLPKBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1572)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    @overload
    def is_maximization(self) -> Any:
        '''GLPKBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1572)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    def is_slack_variable_basic(self, intindex) -> bool:
        """GLPKBackend.is_slack_variable_basic(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2449)

        Test whether the slack variable of the given row is basic.

        This assumes that the problem has been solved with the simplex method
        and a basis is available.  Otherwise an exception will be raised.

        INPUT:

        - ``index`` -- integer; the variable's id

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(maximization=True,            ....:                               solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(-x[0] + x[1] <= 2)
            sage: p.add_constraint(8 * x[0] + 2 * x[1] <= 17)
            sage: p.set_objective(5.5 * x[0] - 3 * x[1])
            sage: b = p.get_backend()
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: b.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: b.solve()
            0
            sage: b.is_slack_variable_basic(0)
            True
            sage: b.is_slack_variable_basic(1)
            False"""
    def is_slack_variable_nonbasic_at_lower_bound(self, intindex) -> bool:
        """GLPKBackend.is_slack_variable_nonbasic_at_lower_bound(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2480)

        Test whether the slack variable of the given row is nonbasic at lower bound.

        This assumes that the problem has been solved with the simplex method
        and a basis is available.  Otherwise an exception will be raised.

        INPUT:

        - ``index`` -- integer; the variable's id

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(maximization=True,            ....:                               solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(-x[0] + x[1] <= 2)
            sage: p.add_constraint(8 * x[0] + 2 * x[1] <= 17)
            sage: p.set_objective(5.5 * x[0] - 3 * x[1])
            sage: b = p.get_backend()
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: b.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: b.solve()
            0
            sage: b.is_slack_variable_nonbasic_at_lower_bound(0)
            False
            sage: b.is_slack_variable_nonbasic_at_lower_bound(1)
            True"""
    def is_variable_basic(self, intindex) -> bool:
        """GLPKBackend.is_variable_basic(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2388)

        Test whether the given variable is basic.

        This assumes that the problem has been solved with the simplex method
        and a basis is available.  Otherwise an exception will be raised.

        INPUT:

        - ``index`` -- integer; the variable's id

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(maximization=True,            ....:                               solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(-x[0] + x[1] <= 2)
            sage: p.add_constraint(8 * x[0] + 2 * x[1] <= 17)
            sage: p.set_objective(5.5 * x[0] - 3 * x[1])
            sage: b = p.get_backend()
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: b.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: b.solve()
            0
            sage: b.is_variable_basic(0)
            True
            sage: b.is_variable_basic(1)
            False"""
    def is_variable_binary(self, intindex) -> bool:
        '''GLPKBackend.is_variable_binary(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1462)

        Test whether the given variable is of binary type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.set_variable_type(0,0)
            sage: p.is_variable_binary(0)
            True

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.is_variable_binary(2)
            False'''
    def is_variable_continuous(self, intindex) -> bool:
        '''GLPKBackend.is_variable_continuous(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1534)

        Test whether the given variable is of continuous/real type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.is_variable_continuous(0)
            True
            sage: p.set_variable_type(0,1)
            sage: p.is_variable_continuous(0)
            False

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.is_variable_continuous(2)
            False'''
    def is_variable_integer(self, intindex) -> bool:
        '''GLPKBackend.is_variable_integer(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1498)

        Test whether the given variable is of integer type.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.set_variable_type(0,1)
            sage: p.is_variable_integer(0)
            True

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.is_variable_integer(2)
            False'''
    def is_variable_nonbasic_at_lower_bound(self, intindex) -> bool:
        """GLPKBackend.is_variable_nonbasic_at_lower_bound(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2419)

        Test whether the given variable is nonbasic at lower bound.
        This assumes that the problem has been solved with the simplex method
        and a basis is available.  Otherwise an exception will be raised.

        INPUT:

        - ``index`` -- integer; the variable's id

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(maximization=True,            ....:                               solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(-x[0] + x[1] <= 2)
            sage: p.add_constraint(8 * x[0] + 2 * x[1] <= 17)
            sage: p.set_objective(5.5 * x[0] - 3 * x[1])
            sage: b = p.get_backend()
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: b.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: b.solve()
            0
            sage: b.is_variable_nonbasic_at_lower_bound(0)
            False
            sage: b.is_variable_nonbasic_at_lower_bound(1)
            True"""
    @overload
    def ncols(self) -> int:
        '''GLPKBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1347)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''GLPKBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1347)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def ncols(self) -> Any:
        '''GLPKBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1347)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2'''
    @overload
    def nrows(self) -> int:
        '''GLPKBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1364)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2, None)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''GLPKBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1364)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2, None)
            sage: p.nrows()
            2'''
    @overload
    def nrows(self) -> Any:
        '''GLPKBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1364)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(2, 2, None)
            sage: p.nrows()
            2'''
    def objective_coefficient(self, intvariable, coeff=...) -> Any:
        '''GLPKBackend.objective_coefficient(self, int variable, coeff=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 305)

        Set or get the coefficient of a variable in the objective function.

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``coeff`` -- double; its coefficient or ``None`` for
          reading (default: ``None``)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variable()
            0
            sage: p.objective_coefficient(0)
            0.0
            sage: p.objective_coefficient(0,2)
            sage: p.objective_coefficient(0)
            2.0

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.objective_coefficient(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index 2'''
    @overload
    def print_ranges(self, filename=...) -> int:
        '''GLPKBackend.print_ranges(self, filename=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2511)

        Print results of a sensitivity analysis

        If no filename is given as an input the results of the
        sensitivity analysis are displayed on the screen. If a
        filename is given they are written to a file.

        INPUT:

        - ``filename`` -- (optional) name of the file

        OUTPUT: zero if the operations was successful otherwise nonzero

        .. NOTE::

            This method is only effective if an optimal solution has been found
            for the lp using the simplex algorithm. In all other cases an error
            message is printed.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint(list(zip([0, 1], [1, 2])), None, 3)
            sage: p.set_objective([2, 5])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: p.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: p.print_ranges()
            glp_print_ranges: optimal basic solution required
            1
            sage: p.solve()
            0
            sage: from tempfile import NamedTemporaryFile
            sage: with NamedTemporaryFile(mode=\'r+t\', suffix=\'.tmp\') as f:
            ....:     p.print_ranges(f.name)
            ....:     for ll in f.readlines():
            ....:         if ll: print(ll)
            ...
            GLPK ... - SENSITIVITY ANALYSIS REPORT                                                                         Page   1
            Problem:
            Objective:  7.5 (MAXimum)
               No. Row name     St      Activity         Slack   Lower bound       Activity      Obj coef  Obj value at Limiting
                                                      Marginal   Upper bound          range         range   break point variable
            ------ ------------ -- ------------- ------------- -------------  ------------- ------------- ------------- ------------
                 1              NU       3.00000        .               -Inf         .           -2.50000        .
                                                       2.50000       3.00000           +Inf          +Inf          +Inf
            GLPK ... - SENSITIVITY ANALYSIS REPORT                                                                         Page   2
            Problem:
            Objective:  7.5 (MAXimum)
               No. Column name  St      Activity      Obj coef   Lower bound       Activity      Obj coef  Obj value at Limiting
                                                      Marginal   Upper bound          range         range   break point variable
            ------ ------------ -- ------------- ------------- -------------  ------------- ------------- ------------- ------------
                 1              NL        .            2.00000        .                -Inf          -Inf          +Inf
                                                       -.50000          +Inf        3.00000       2.50000       6.00000
                 2              BS       1.50000       5.00000        .                -Inf       4.00000       6.00000
                                                        .               +Inf        1.50000          +Inf          +Inf
            End of report'''
    @overload
    def print_ranges(self) -> Any:
        '''GLPKBackend.print_ranges(self, filename=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2511)

        Print results of a sensitivity analysis

        If no filename is given as an input the results of the
        sensitivity analysis are displayed on the screen. If a
        filename is given they are written to a file.

        INPUT:

        - ``filename`` -- (optional) name of the file

        OUTPUT: zero if the operations was successful otherwise nonzero

        .. NOTE::

            This method is only effective if an optimal solution has been found
            for the lp using the simplex algorithm. In all other cases an error
            message is printed.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint(list(zip([0, 1], [1, 2])), None, 3)
            sage: p.set_objective([2, 5])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: p.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: p.print_ranges()
            glp_print_ranges: optimal basic solution required
            1
            sage: p.solve()
            0
            sage: from tempfile import NamedTemporaryFile
            sage: with NamedTemporaryFile(mode=\'r+t\', suffix=\'.tmp\') as f:
            ....:     p.print_ranges(f.name)
            ....:     for ll in f.readlines():
            ....:         if ll: print(ll)
            ...
            GLPK ... - SENSITIVITY ANALYSIS REPORT                                                                         Page   1
            Problem:
            Objective:  7.5 (MAXimum)
               No. Row name     St      Activity         Slack   Lower bound       Activity      Obj coef  Obj value at Limiting
                                                      Marginal   Upper bound          range         range   break point variable
            ------ ------------ -- ------------- ------------- -------------  ------------- ------------- ------------- ------------
                 1              NU       3.00000        .               -Inf         .           -2.50000        .
                                                       2.50000       3.00000           +Inf          +Inf          +Inf
            GLPK ... - SENSITIVITY ANALYSIS REPORT                                                                         Page   2
            Problem:
            Objective:  7.5 (MAXimum)
               No. Column name  St      Activity      Obj coef   Lower bound       Activity      Obj coef  Obj value at Limiting
                                                      Marginal   Upper bound          range         range   break point variable
            ------ ------------ -- ------------- ------------- -------------  ------------- ------------- ------------- ------------
                 1              NL        .            2.00000        .                -Inf          -Inf          +Inf
                                                       -.50000          +Inf        3.00000       2.50000       6.00000
                 2              BS       1.50000       5.00000        .                -Inf       4.00000       6.00000
                                                        .               +Inf        1.50000          +Inf          +Inf
            End of report'''
    def problem_name(self, name=...) -> Any:
        '''GLPKBackend.problem_name(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 347)

        Return or define the problem\'s name.

        INPUT:

        - ``name`` -- string; the problem\'s name. When set to
          ``None`` (default), the method returns the problem\'s name.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.problem_name("There once was a french fry")
            sage: print(p.problem_name())
            There once was a french fry'''
    def remove_constraint(self, inti) -> Any:
        '''GLPKBackend.remove_constraint(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 472)

        Remove a constraint from ``self``.

        INPUT:

        - ``i`` -- index of the constraint to remove

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x, y = p[\'x\'], p[\'y\']
            sage: p.add_constraint(2*x + 3*y <= 6)
            sage: p.add_constraint(3*x + 2*y <= 6)
            sage: p.add_constraint(x >= 0)
            sage: p.set_objective(x + y + 7)
            sage: p.set_integer(x); p.set_integer(y)
            sage: p.solve()
            9.0
            sage: p.remove_constraint(0)
            sage: p.solve()
            10.0

        Removing fancy constraints does not make Sage crash::

            sage: MixedIntegerLinearProgram(solver = "GLPK").remove_constraint(-2)
            Traceback (most recent call last):
            ...
            ValueError: The constraint\'s index i must satisfy 0 <= i < number_of_constraints'''
    def remove_constraints(self, constraints) -> Any:
        '''GLPKBackend.remove_constraints(self, constraints)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 511)

        Remove several constraints.

        INPUT:

        - ``constraints`` -- an iterable containing the indices of the rows to remove

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x, y = p[\'x\'], p[\'y\']
            sage: p.add_constraint(2*x + 3*y <= 6)
            sage: p.add_constraint(3*x + 2*y <= 6)
            sage: p.add_constraint(x >= 0)
            sage: p.set_objective(x + y + 7)
            sage: p.set_integer(x); p.set_integer(y)
            sage: p.solve()
            9.0
            sage: p.remove_constraints([0])
            sage: p.solve()
            10.0
            sage: p.get_values([x,y])
            [0.0, 3.0]

        TESTS:

        Removing fancy constraints does not make Sage crash::

            sage: MixedIntegerLinearProgram(solver="GLPK").remove_constraints([0, -2])
            Traceback (most recent call last):
            ...
            ValueError: The constraint\'s index i must satisfy 0 <= i < number_of_constraints'''
    def row(self, intindex) -> Any:
        '''GLPKBackend.row(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 697)

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
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(list(zip(range(5), range(5))), 2, 2)
            sage: p.row(0)
            ([4, 3, 2, 1], [4.0, 3.0, 2.0, 1.0])
            sage: p.row_bounds(0)
            (2.0, 2.0)

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.row(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid row index 2'''
    def row_bounds(self, intindex) -> Any:
        '''GLPKBackend.row_bounds(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 753)

        Return the bounds of a specific constraint.

        INPUT:

        - ``index`` -- integer; the constraint\'s id

        OUTPUT:

        A pair ``(lower_bound, upper_bound)``. Each of them can be set
        to ``None`` if the constraint is not bounded in the
        corresponding direction, and is a real value otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(list(zip(range(5), range(5))), 2, 2)
            sage: p.row(0)
            ([4, 3, 2, 1], [4.0, 3.0, 2.0, 1.0])
            sage: p.row_bounds(0)
            (2.0, 2.0)

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.row_bounds(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid row index 2'''
    def row_name(self, intindex) -> Any:
        '''GLPKBackend.row_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1422)

        Return the ``index``-th row name.

        INPUT:

        - ``index`` -- integer; the row\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_linear_constraints(1, 2, None, names=[\'Empty constraint 1\'])
            sage: p.row_name(0)
            \'Empty constraint 1\'

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.row_name(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid row index 2'''
    def set_col_stat(self, intj, intstat) -> Any:
        '''GLPKBackend.set_col_stat(self, int j, int stat)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2821)

        Set the status of a variable.

        INPUT:

        - ``j`` -- the index of the constraint

        - ``stat`` -- the status to set to

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            0
            sage: lp.get_col_stat(0)
            1
            sage: lp.set_col_stat(0, 2)
            sage: lp.get_col_stat(0)
            2'''
    def set_objective(self, listcoeff, d=...) -> Any:
        '''GLPKBackend.set_objective(self, list coeff, d=0.0)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 379)

        Set the objective function.

        INPUT:

        - ``coeff`` -- list of real values, whose i-th element is the
          coefficient of the i-th variable in the objective function

        - ``d`` -- double; the constant term in the linear function (set to `0`
          by default)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(5)
            4
            sage: p.set_objective([1, 1, 2, 1, 3])
            sage: [p.objective_coefficient(x) for x in range(5)]
            [1.0, 1.0, 2.0, 1.0, 3.0]'''
    def set_row_stat(self, inti, intstat) -> Any:
        '''GLPKBackend.set_row_stat(self, int i, int stat)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2786)

        Set the status of a constraint.

        INPUT:

        - ``i`` -- the index of the constraint

        - ``stat`` -- the status to set to

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            0
            sage: lp.get_row_stat(0)
            1
            sage: lp.set_row_stat(0, 3)
            sage: lp.get_row_stat(0)
            3'''
    def set_sense(self, intsense) -> Any:
        '''GLPKBackend.set_sense(self, int sense)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 279)

        Set the direction (maximization/minimization).

        INPUT:

        - ``sense`` -- integer:

            * +1 => Maximization
            * -1 => Minimization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False'''
    def set_variable_type(self, intvariable, intvtype) -> Any:
        '''GLPKBackend.set_variable_type(self, int variable, int vtype)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 230)

        Set the type of a variable.

        INPUT:

        - ``variable`` -- integer; the variable\'s id

        - ``vtype`` -- integer:

            *  1  Integer
            *  0  Binary
            * -1 Real

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.set_variable_type(0,1)
            sage: p.is_variable_integer(0)
            True

        TESTS:

        We sanity check the input that will be passed to GLPK::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'GLPK\')
            sage: p.set_variable_type(2,0)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index 2'''
    def set_verbosity(self, intlevel) -> Any:
        '''GLPKBackend.set_verbosity(self, int level)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 410)

        Set the verbosity level.

        INPUT:

        - ``level`` -- integer; from 0 (no verbosity) to 3

        EXAMPLES::

            sage: p.<x> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.add_constraint(10 * x[0] <= 1)
            sage: p.add_constraint(5 * x[1] <= 1)
            sage: p.set_objective(x[0] + x[1])
            sage: p.solve()
            0.30000000000000004
            sage: p.get_backend().set_verbosity(3)
            sage: p.solver_parameter("simplex_or_intopt", "intopt_only")
            sage: p.solve()
            GLPK Integer Optimizer...
            2 rows, 2 columns, 2 non-zeros
            0 integer variables, none of which are binary
            Preprocessing...
            Objective value =   3.000000000e-01
            INTEGER OPTIMAL SOLUTION FOUND BY MIP PREPROCESSOR
            0.30000000000000004

        ::

            sage: p.<x> = MixedIntegerLinearProgram(solver=\'GLPK/exact\')
            sage: p.add_constraint(10 * x[0] <= 1)
            sage: p.add_constraint(5 * x[1] <= 1)
            sage: p.set_objective(x[0] + x[1])
            sage: p.solve() # tol 1e-14
            0.3
            sage: p.get_backend().set_verbosity(2)
            sage: p.solve() # tol 1e-14
            *     2:   objval =                    0.3   (0)
            *     2:   objval =                    0.3   (0)
            0.3
            sage: p.get_backend().set_verbosity(3)
            sage: p.solve() # tol 1e-14
            glp_exact: 2 rows, 2 columns, 2 non-zeros
            ...
            *     2:   objval =                    0.3   (0)
            *     2:   objval =                    0.3   (0)
            OPTIMAL SOLUTION FOUND
            0.3'''
    def solve(self) -> int:
        '''GLPKBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 910)

        Solve the problem.

        Sage uses GLPK\'s implementation of the branch-and-cut
        algorithm (``glp_intopt``) to solve the mixed-integer linear
        program.  This algorithm can be requested explicitly by
        setting the solver parameter "simplex_or_intopt" to
        "intopt_only". By default, the simplex method will be used
        first to detect pathological problems that the integer solver
        cannot handle. If all variables are continuous, the integer
        algorithm reduces to solving the linear program by the simplex
        method.

        EXAMPLES::

            sage: lp = MixedIntegerLinearProgram(solver = \'GLPK\', maximization = False)
            sage: x, y = lp[0], lp[1]
            sage: lp.add_constraint(-2*x + y <= 1)
            sage: lp.add_constraint(x - y <= 1)
            sage: lp.add_constraint(x + y >= 2)
            sage: lp.set_objective(x + y)
            sage: lp.set_integer(x)
            sage: lp.set_integer(y)
            sage: lp.solve()
            2.0
            sage: lp.get_values([x, y])
            [1.0, 1.0]

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(range(5), range(5))
            sage: p.solve()
            0
            sage: p.objective_coefficient(0,1)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: ...

        .. WARNING::

            GLPK\'s ``glp_intopt`` sometimes fails catastrophically
            when given a system it cannot solve (:issue:`12309`). It
            can loop indefinitely, or just plain segfault. Upstream
            considers this behavior "essentially innate" to the
            current design, and suggests preprocessing with
            ``glp_simplex``, which is what SageMath does by default.
            Set the ``simplex_or_intopt`` solver parameter to
            ``glp_intopt_only`` at your own risk.

        EXAMPLES::

            sage: lp = MixedIntegerLinearProgram(solver = "GLPK")
            sage: v = lp.new_variable(nonnegative=True)
            sage: lp.add_constraint(v[1] +v[2] -2.0 *v[3], max=-1.0)
            sage: lp.add_constraint(v[0] -4.0/3 *v[1] +1.0/3 *v[2], max=-1.0/3)
            sage: lp.add_constraint(v[0] +0.5 *v[1] -0.5 *v[2] +0.25 *v[3], max=-0.25)
            sage: lp.solve()
            0.0
            sage: lp.add_constraint(v[0] +4.0 *v[1] -v[2] +v[3], max=-1.0)
            sage: lp.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: Problem has no feasible solution

        If we switch to "simplex_only", the integrality constraints are ignored,
        and we get an optimal solution to the continuous relaxation.

        EXAMPLES::

            sage: lp = MixedIntegerLinearProgram(solver = \'GLPK\', maximization = False)
            sage: x, y = lp[0], lp[1]
            sage: lp.add_constraint(-2*x + y <= 1)
            sage: lp.add_constraint(x - y <= 1)
            sage: lp.add_constraint(x + y >= 2)
            sage: lp.set_objective(x + y)
            sage: lp.set_integer(x)
            sage: lp.set_integer(y)
            sage: lp.solver_parameter("simplex_or_intopt", "simplex_only") # use simplex only
            sage: lp.solve()
            2.0
            sage: lp.get_values([x, y])
            [1.5, 0.5]

        If one solves a linear program and wishes to access dual information
        (`get_col_dual` etc.) or tableau data (`get_row_stat` etc.),
        one needs to switch to "simplex_only" before solving.

        GLPK also has an exact rational simplex solver.  The only access
        to data is via double-precision floats, which means that
        rationals in the input data may be rounded before the exact
        solver sees them. Thus, it is unreasonable to expect that
        arbitrary LPs with rational coefficients are solved exactly.
        Once the LP has been read into the backend, it reconstructs
        rationals from doubles and does solve exactly over the rationals,
        but results are returned as as doubles.

        EXAMPLES::

            sage: lp.solver_parameter("simplex_or_intopt", "exact_simplex_only") # use exact simplex only
            sage: lp.solve()
            2.0
            sage: lp.get_values([x, y])
            [1.5, 0.5]

        If you need the rational solution, you need to retrieve the
        basis information via ``get_col_stat`` and ``get_row_stat``
        and calculate the corresponding basic solution.  Below we only
        test that the basis information is indeed available.
        Calculating the corresponding basic solution is left as an
        exercise.

        EXAMPLES::

            sage: lp.get_backend().get_row_stat(0)
            1
            sage: lp.get_backend().get_col_stat(0)
            1

        Below we test that integers that can be exactly represented by
        IEEE 754 double-precision floating point numbers survive the
        rational reconstruction done by ``glp_exact`` and the subsequent
        conversion to double-precision floating point numbers.

        EXAMPLES::

            sage: lp = MixedIntegerLinearProgram(solver = \'GLPK\', maximization = True)
            sage: test = 2^53 - 43
            sage: lp.solver_parameter("simplex_or_intopt", "exact_simplex_only") # use exact simplex only
            sage: x = lp[0]
            sage: lp.add_constraint(x <= test)
            sage: lp.set_objective(x)
            sage: lp.solve() == test # yes, we want an exact comparison here
            True
            sage: lp.get_values(x) == test # yes, we want an exact comparison here
            True

        Below we test that GLPK backend can detect unboundedness in
        "simplex_only" mode (:issue:`18838`).

        EXAMPLES::

            sage: lp = MixedIntegerLinearProgram(maximization=True, solver = "GLPK")
            sage: lp.set_objective(lp[0])
            sage: lp.solver_parameter("simplex_or_intopt", "simplex_only")
            sage: lp.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: Problem has unbounded solution
            sage: lp.set_objective(lp[1])
            sage: lp.solver_parameter("primal_v_dual", "GLP_DUAL")
            sage: lp.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: Problem has unbounded solution
            sage: lp.solver_parameter("simplex_or_intopt", "simplex_then_intopt")
            sage: lp.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: The LP (relaxation) problem has no dual feasible solution
            sage: lp.solver_parameter("simplex_or_intopt", "intopt_only")
            sage: lp.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: The LP (relaxation) problem has no dual feasible solution
            sage: lp.set_max(lp[1],5)
            sage: lp.solve()
            5.0

        Solving a LP within the acceptable gap. No exception is raised, even if
        the result is not optimal. To do this, we try to compute the maximum
        number of disjoint balls (of diameter 1) in a hypercube::

            sage: # needs sage.graphs
            sage: g = graphs.CubeGraph(9)
            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.solver_parameter("mip_gap_tolerance",100)
            sage: b = p.new_variable(binary=True)
            sage: p.set_objective(p.sum(b[v] for v in g))
            sage: for v in g:
            ....:     p.add_constraint(b[v]+p.sum(b[u] for u in g.neighbors(v)) <= 1)
            sage: p.add_constraint(b[v] == 1) # Force an easy non-0 solution
            sage: p.solve() # rel tol 100
            1

        Same, now with a time limit::

            sage: # needs sage.graphs
            sage: p.solver_parameter("mip_gap_tolerance",1)
            sage: p.solver_parameter("timelimit",3.0)
            sage: p.solve() # rel tol 100
            1'''
    def solver_parameter(self, name, value=...) -> Any:
        '''GLPKBackend.solver_parameter(self, name, value=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1862)

        Return or define a solver parameter.

        INPUT:

        - ``name`` -- string; the parameter

        - ``value`` -- the parameter\'s value if it is to be defined,
          or ``None`` (default) to obtain its current value

        You can supply the name of a parameter and its value using either a
        string or a ``glp_`` constant (which are defined as Cython variables of
        this module).

        In most cases, you can use the same name for a parameter as that given
        in the GLPK documentation, which is available by downloading GLPK from
        <http://www.gnu.org/software/glpk/>. The exceptions relate to parameters
        common to both methods; these require you to append ``_simplex`` or
        ``_intopt`` to the name to resolve ambiguity, since the interface allows
        access to both.

        We have also provided more meaningful names, to assist readability.

        Parameter **names** are specified in lower case.
        To use a constant instead of a string, prepend ``glp_`` to the name.
        For example, both ``glp_gmi_cuts`` or ``\'gmi_cuts\'`` control whether
        to solve using Gomory cuts.

        Parameter **values** are specified as strings in upper case,
        or as constants in lower case. For example, both ``glp_on`` and ``"GLP_ON"``
        specify the same thing.

        Naturally, you can use ``True`` and ``False`` in cases where ``glp_on`` and ``glp_off``
        would be used.

        A list of parameter names, with their possible values:

        **General-purpose parameters:**

        .. list-table::
         :widths: 30 70

         * - ``timelimit``

           - specify the time limit IN SECONDS.  This affects both simplex
             and intopt.

         * - ``timelimit_simplex`` and ``timelimit_intopt``

           - specify the time limit IN MILLISECONDS. (This is glpk\'s
             default.)

         * - ``simplex_or_intopt``

           - specify which solution routines in GLPK to use. Set this
             to either ``simplex_only``, ``exact_simplex_only``,
             ``intopt_only``, or ``simplex_then_intopt`` (the
             default). The ``simplex_then_intopt`` option does some
             extra work, but avoids hangs/crashes in GLPK on problems
             with no solution; SageMath will try simplex first, then
             perform integer optimization only if a solution of the LP
             relaxation exists. If you know that your system is not
             pathological, one of the other options will be faster.

         * - ``verbosity_intopt`` and ``verbosity_simplex``

           - one of ``GLP_MSG_OFF``, ``GLP_MSG_ERR``, ``GLP_MSG_ON``, or
             ``GLP_MSG_ALL``. The default is ``GLP_MSG_OFF``.

         * - ``output_frequency_intopt`` and ``output_frequency_simplex``

           - the output frequency, in milliseconds. Default is 5000.

         * - ``output_delay_intopt`` and ``output_delay_simplex``

           - the output delay, in milliseconds, regarding the use of the
             simplex method on the LP relaxation. Default is 10000.


        **intopt-specific parameters:**

        .. list-table::
         :widths: 30 70

         * - ``branching``
           - - ``GLP_BR_FFV``  first fractional variable
             - ``GLP_BR_LFV``  last fractional variable
             - ``GLP_BR_MFV``  most fractional variable
             - ``GLP_BR_DTH``  Driebeck-Tomlin heuristic (default)
             - ``GLP_BR_PCH``  hybrid pseudocost heuristic

         * - ``backtracking``
           - - ``GLP_BT_DFS``  depth first search
             - ``GLP_BT_BFS``  breadth first search
             - ``GLP_BT_BLB``  best local bound (default)
             - ``GLP_BT_BPH``  best projection heuristic

         * - ``preprocessing``
           - - ``GLP_PP_NONE``
             - ``GLP_PP_ROOT``  preprocessing only at root level
             - ``GLP_PP_ALL``   (default)


         * - ``feasibility_pump``

           - ``GLP_ON`` or ``GLP_OFF`` (default)

         * - ``gomory_cuts``

           - ``GLP_ON`` or ``GLP_OFF`` (default)

         * - ``mixed_int_rounding_cuts``

           - ``GLP_ON`` or ``GLP_OFF`` (default)

         * - ``mixed_cover_cuts``

           - ``GLP_ON`` or ``GLP_OFF`` (default)

         * - ``clique_cuts``

           - ``GLP_ON`` or ``GLP_OFF`` (default)

         * - ``absolute_tolerance``

           - (double) used to check if optimal solution to LP relaxation is
             integer feasible. GLPK manual advises, "do not change... without
             detailed understanding of its purpose."

         * - ``relative_tolerance``

           - (double) used to check if objective value in LP relaxation is not
             better than best known integer solution. GLPK manual advises, "do
             not change... without detailed understanding of its purpose."

         * - ``mip_gap_tolerance``

           - (double) relative mip gap tolerance. Default is 0.0.

         * - ``presolve_intopt``

           - ``GLP_ON`` (default) or ``GLP_OFF``

         * - ``binarize``

           - ``GLP_ON`` or ``GLP_OFF`` (default)


        **simplex-specific parameters:**

        .. list-table::
         :widths: 30 70

         * - ``primal_v_dual``

           - - ``GLP_PRIMAL``  (default)
             - ``GLP_DUAL``
             - ``GLP_DUALP``

         * - ``pricing``

           - - ``GLP_PT_STD``    standard (textbook)
             - ``GLP_PT_PSE``    projected steepest edge (default)

         * - ``ratio_test``

           - - ``GLP_RT_STD``  standard (textbook)
             - ``GLP_RT_HAR``  Harris\' two-pass ratio test (default)

         * - ``tolerance_primal``

           - (double) tolerance used to check if basic solution is primal
             feasible. GLPK manual advises, "do not change... without
             detailed understanding of its purpose."

         * - ``tolerance_dual``

           - (double) tolerance used to check if basic solution is dual
             feasible. GLPK manual advises, "do not change... without
             detailed understanding of its purpose."

         * - ``tolerance_pivot``

           - (double) tolerance used to choose pivot. GLPK manual advises,
             "do not change... without detailed understanding of its
             purpose."

         * - ``obj_lower_limit``

           - (double) lower limit of the objective function.  The default is
             ``-DBL_MAX``.

         * - ``obj_upper_limit``

           - (double) upper limit of the objective function.  The default is
             ``DBL_MAX``.

         * - ``iteration_limit``

           - (int) iteration limit of the simplex algorithm.  The default is
             ``INT_MAX``.

         * - ``presolve_simplex``

           - ``GLP_ON`` or ``GLP_OFF`` (default).

        .. NOTE::

            The coverage for GLPK\'s control parameters for simplex and integer optimization
            is nearly complete. The only thing lacking is a wrapper for callback routines.

            To date, no attempt has been made to expose the interior point methods.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.solver_parameter("timelimit", 60)
            sage: p.solver_parameter("timelimit")
            60.0

        - Don\'t forget the difference between ``timelimit`` and ``timelimit_intopt``

        ::

            sage: p.solver_parameter("timelimit_intopt")
            60000

        If you don\'t care for an integer answer, you can ask for an LP
        relaxation instead.  The default solver performs integer optimization,
        but you can switch to the standard simplex algorithm through the
        ``glp_simplex_or_intopt`` parameter.

        EXAMPLES::

            sage: lp = MixedIntegerLinearProgram(solver = \'GLPK\', maximization = False)
            sage: x, y = lp[0], lp[1]
            sage: lp.add_constraint(-2*x + y <= 1)
            sage: lp.add_constraint(x - y <= 1)
            sage: lp.add_constraint(x + y >= 2)
            sage: lp.set_integer(x); lp.set_integer(y)
            sage: lp.set_objective(x + y)
            sage: lp.solve()
            2.0
            sage: lp.get_values([x,y])
            [1.0, 1.0]
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            2.0
            sage: lp.get_values([x,y])
            [1.5, 0.5]

        You can get GLPK to spout all sorts of information at you.
        The default is to turn this off, but sometimes (debugging) it\'s very useful::

            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_then_intopt)
            sage: lp.solver_parameter(backend.glp_mir_cuts, backend.glp_on)
            sage: lp.solver_parameter(backend.glp_msg_lev_intopt, backend.glp_msg_all)
            sage: lp.solver_parameter(backend.glp_mir_cuts)
            1

        If you actually try to solve ``lp``, you will get a lot of detailed information.'''
    def variable_lower_bound(self, intindex, value=...) -> Any:
        '''GLPKBackend.variable_lower_bound(self, int index, value=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1688)

        Return or define the lower bound on a variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        - ``value`` -- real value, or ``None`` to mean that the
          variable has not lower bound. When set to ``False``
          (default), the method returns the current value.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_lower_bound(0, 5)
            sage: p.col_bounds(0)
            (5.0, None)

        TESTS:

        :issue:`14581`::

            sage: P = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = P["x"]
            sage: P.set_min(x, 5)
            sage: P.set_min(x, 0)
            sage: P.get_min(x)
            0.0

        Check that :issue:`10232` is fixed::

            sage: p = get_solver(solver=\'GLPK\')
            sage: p.variable_lower_bound(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index 2

            sage: p.variable_lower_bound(-1)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index -1

            sage: p.variable_lower_bound(3, 5)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index 3

            sage: p.add_variable()
            0
            sage: p.variable_lower_bound(0, \'hey!\')
            Traceback (most recent call last):
            ...
            TypeError: must be real number, not str'''
    def variable_upper_bound(self, intindex, value=...) -> Any:
        '''GLPKBackend.variable_upper_bound(self, int index, value=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1589)

        Return or define the upper bound on a variable.

        INPUT:

        - ``index`` -- integer; the variable\'s id

        - ``value`` -- real value, or ``None`` to mean that the
          variable has not upper bound. When set to ``False``
          (default), the method returns the current value.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_upper_bound(0, 5)
            sage: p.col_bounds(0)
            (0.0, 5.0)

        TESTS:

        :issue:`14581`::

            sage: P = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = P["x"]
            sage: P.set_max(x, 0)
            sage: P.get_max(x)
            0.0

        Check that :issue:`10232` is fixed::

            sage: p = get_solver(solver=\'GLPK\')
            sage: p.variable_upper_bound(2)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index 2

            sage: p.variable_upper_bound(-1)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index -1

            sage: p.variable_upper_bound(3, 5)
            Traceback (most recent call last):
            ...
            ValueError: invalid variable index 3

            sage: p.add_variable()
            0
            sage: p.variable_upper_bound(0, \'hey!\')
            Traceback (most recent call last):
            ...
            TypeError: must be real number, not str'''
    @overload
    def warm_up(self) -> int:
        '''GLPKBackend.warm_up(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2856)

        Warm up the basis using current statuses assigned to rows and cols.

        OUTPUT: the warming up status

            * 0             The operation has been successfully performed.
            * GLP_EBADB     The basis matrix is invalid.
            * GLP_ESING     The basis matrix is singular within the working precision.
            * GLP_ECOND     The basis matrix is ill-conditioned.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            0
            sage: lp.get_objective_value()
            280.0
            sage: lp.set_row_stat(0,3)
            sage: lp.set_col_stat(1,1)
            sage: lp.warm_up()
            0'''
    @overload
    def warm_up(self) -> Any:
        '''GLPKBackend.warm_up(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 2856)

        Warm up the basis using current statuses assigned to rows and cols.

        OUTPUT: the warming up status

            * 0             The operation has been successfully performed.
            * GLP_EBADB     The basis matrix is invalid.
            * GLP_ESING     The basis matrix is singular within the working precision.
            * GLP_ECOND     The basis matrix is ill-conditioned.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: lp = get_solver(solver = "GLPK")
            sage: lp.add_variables(3)
            2
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [8, 6, 1])), None, 48)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [4, 2, 1.5])), None, 20)
            sage: lp.add_linear_constraint(list(zip([0, 1, 2], [2, 1.5, 0.5])), None, 8)
            sage: lp.set_objective([60, 30, 20])
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: lp.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: lp.solve()
            0
            sage: lp.get_objective_value()
            280.0
            sage: lp.set_row_stat(0,3)
            sage: lp.set_col_stat(1,1)
            sage: lp.warm_up()
            0'''
    def write_lp(self, filename) -> Any:
        '''GLPKBackend.write_lp(self, filename)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1788)

        Write the problem to a ``.lp`` file.

        INPUT:

        - ``filename`` -- string

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([[0, 1], [1, 2]], None, 3)
            sage: p.set_objective([2, 5])
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix=\'.lp\') as f:
            ....:     _ = p.write_lp(f.name)
            ....:     len(f.readlines())
            ...
            9 lines were written
            9'''
    def write_mps(self, filename, intmodern) -> Any:
        '''GLPKBackend.write_mps(self, filename, int modern)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1815)

        Write the problem to a ``.mps`` file.

        INPUT:

        - ``filename`` -- string

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver = "GLPK")
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([[0, 1], [1, 2]], None, 3)
            sage: p.set_objective([2, 5])
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix=\'mps\') as f:
            ....:     _ = p.write_mps(f.name, 2)
            ....:     len(f.readlines())
            ...
            17 records were written
            17'''
    def __copy__(self) -> Any:
        '''GLPKBackend.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/glpk_backend.pyx (starting at line 1842)

        Return a copy of ``self``.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = MixedIntegerLinearProgram(solver = "GLPK")
            sage: b = p.new_variable()
            sage: p.add_constraint(b[1] + b[2] <= 6)
            sage: p.set_objective(b[1] + b[2])
            sage: copy(p).solve()
            6.0'''
