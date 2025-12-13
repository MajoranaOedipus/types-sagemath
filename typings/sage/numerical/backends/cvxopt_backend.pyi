import sage.numerical.backends.generic_backend
from sage.numerical.mip import MIPSolverException as MIPSolverException
from typing import Any, ClassVar, overload

class CVXOPTBackend(sage.numerical.backends.generic_backend.GenericBackend):
    """File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 25)

        MIP Backend that uses the CVXOPT solver.

        There is no support for integer variables.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='CVXOPT')

        TESTS:

        :issue:`20332`::

            sage: p
            Mixed Integer Program (no objective, 0 variables, 0 constraints)
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_col(self, indices, coeffs) -> Any:
        """CVXOPTBackend.add_col(self, indices, coeffs)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 311)

        Add a column.

        INPUT:

        - ``indices`` -- list of integers; this list contains the
          indices of the constraints in which the variable's
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
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.nrows()
            0
            sage: p.add_linear_constraints(5, 0, None)
            sage: p.add_col(range(5), range(5))
            sage: p.nrows()
            5"""
    def add_linear_constraint(self, coefficients, lower_bound, upper_bound, name=...) -> Any:
        """CVXOPTBackend.add_linear_constraint(self, coefficients, lower_bound, upper_bound, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 359)

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
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(zip(range(5), range(5)), 2.0, 2.0)
            sage: p.row(0)
            ([1, 2, 3, 4], [1, 2, 3, 4])
            sage: p.row_bounds(0)
            (2.00000000000000, 2.00000000000000)
            sage: p.add_linear_constraint(zip(range(5), range(5)), 1.0, 1.0, name='foo')
            sage: p.row_name(-1)
            'foo'"""
    @overload
    def add_variable(self, lower_bound=..., upper_bound=..., binary=..., continuous=..., integer=..., obj=..., name=...) -> int:
        """CVXOPTBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 132)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.
        Variable types are always continuous, and thus the parameters
        ``binary``, ``integer``, and ``continuous`` have no effect.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name='x',obj=1.0)
            4
            sage: p.col_name(3)
            'x_3'
            sage: p.col_name(4)
            'x'
            sage: p.objective_coefficient(4)
            1.00000000000000

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables"""
    @overload
    def add_variable(self) -> Any:
        """CVXOPTBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 132)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.
        Variable types are always continuous, and thus the parameters
        ``binary``, ``integer``, and ``continuous`` have no effect.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name='x',obj=1.0)
            4
            sage: p.col_name(3)
            'x_3'
            sage: p.col_name(4)
            'x'
            sage: p.objective_coefficient(4)
            1.00000000000000

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables"""
    @overload
    def add_variable(self) -> Any:
        """CVXOPTBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 132)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.
        Variable types are always continuous, and thus the parameters
        ``binary``, ``integer``, and ``continuous`` have no effect.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name='x',obj=1.0)
            4
            sage: p.col_name(3)
            'x_3'
            sage: p.col_name(4)
            'x'
            sage: p.objective_coefficient(4)
            1.00000000000000

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables"""
    @overload
    def add_variable(self, lower_bound=...) -> Any:
        """CVXOPTBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 132)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.
        Variable types are always continuous, and thus the parameters
        ``binary``, ``integer``, and ``continuous`` have no effect.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name='x',obj=1.0)
            4
            sage: p.col_name(3)
            'x_3'
            sage: p.col_name(4)
            'x'
            sage: p.objective_coefficient(4)
            1.00000000000000

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables"""
    @overload
    def add_variable(self, continuous=...) -> Any:
        """CVXOPTBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 132)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.
        Variable types are always continuous, and thus the parameters
        ``binary``, ``integer``, and ``continuous`` have no effect.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name='x',obj=1.0)
            4
            sage: p.col_name(3)
            'x_3'
            sage: p.col_name(4)
            'x'
            sage: p.objective_coefficient(4)
            1.00000000000000

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables"""
    @overload
    def add_variable(self, name=..., obj=...) -> Any:
        """CVXOPTBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 132)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.
        Variable types are always continuous, and thus the parameters
        ``binary``, ``integer``, and ``continuous`` have no effect.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name='x',obj=1.0)
            4
            sage: p.col_name(3)
            'x_3'
            sage: p.col_name(4)
            'x'
            sage: p.objective_coefficient(4)
            1.00000000000000

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables"""
    @overload
    def add_variable(self, integer=...) -> Any:
        """CVXOPTBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 132)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.
        Variable types are always continuous, and thus the parameters
        ``binary``, ``integer``, and ``continuous`` have no effect.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name='x',obj=1.0)
            4
            sage: p.col_name(3)
            'x_3'
            sage: p.col_name(4)
            'x'
            sage: p.objective_coefficient(4)
            1.00000000000000

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables"""
    @overload
    def add_variable(self, binary=...) -> Any:
        """CVXOPTBackend.add_variable(self, lower_bound=0.0, upper_bound=None, binary=False, continuous=True, integer=False, obj=None, name=None) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 132)

        Add a variable.

        This amounts to adding a new column to the matrix. By default,
        the variable is both positive and real.
        Variable types are always continuous, and thus the parameters
        ``binary``, ``integer``, and ``continuous`` have no effect.

        INPUT:

        - ``lower_bound`` -- the lower bound of the variable (default: 0)

        - ``upper_bound`` -- the upper bound of the variable (default: ``None``)

        - ``binary`` -- ``True`` if the variable is binary (default: ``False``)

        - ``continuous`` -- ``True`` if the variable is continuous (default: ``True``)

        - ``integer`` -- ``True`` if the variable is integer (default: ``False``)

        - ``obj`` -- (optional) coefficient of this variable in the objective function (default: 0.0)

        - ``name`` -- an optional name for the newly added variable (default: ``None``)

        OUTPUT: the index of the newly created variable

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.ncols()
            1
            sage: p.add_variable()
            1
            sage: p.add_variable(lower_bound=-2.0)
            2
            sage: p.add_variable(continuous=True)
            3
            sage: p.add_variable(name='x',obj=1.0)
            4
            sage: p.col_name(3)
            'x_3'
            sage: p.col_name(4)
            'x'
            sage: p.objective_coefficient(4)
            1.00000000000000

        TESTS::

            sage: p.add_variable(integer=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables
            sage: p.add_variable(binary=True)
            Traceback (most recent call last):
            ...
            RuntimeError: CVXOPT only supports continuous variables"""
    def col_bounds(self, intindex) -> Any:
        """CVXOPTBackend.col_bounds(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 765)

        Return the bounds of a specific variable.

        INPUT:

        - ``index`` -- integer; the variable's id

        OUTPUT:

        A pair ``(lower_bound, upper_bound)``. Each of them can be set
        to ``None`` if the variable is not bounded in the
        corresponding direction, and is a real value otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_upper_bound(0, 5)
            sage: p.col_bounds(0)
            (0.0, 5)"""
    def col_name(self, intindex) -> Any:
        '''CVXOPTBackend.col_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 894)

        Return the ``index``-th col name.

        INPUT:

        - ``index`` -- integer; the col\'s id

        - ``name`` -- (``char *``) its name; when set to ``NULL``
          (default), the method returns the current name

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'CVXOPT\')
            sage: p.add_variable(name="I am a variable")
            0
            sage: p.col_name(0)
            \'I am a variable\''''
    @overload
    def get_objective_value(self) -> Any:
        """CVXOPTBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 563)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='cvxopt')
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([(0,1), (1,2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: N(p.get_objective_value(),4)
            7.5
            sage: N(p.get_variable_value(0),4)
            3.6e-7
            sage: N(p.get_variable_value(1),4)
            1.5"""
    @overload
    def get_objective_value(self) -> Any:
        """CVXOPTBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 563)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='cvxopt')
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([(0,1), (1,2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: N(p.get_objective_value(),4)
            7.5
            sage: N(p.get_variable_value(0),4)
            3.6e-7
            sage: N(p.get_variable_value(1),4)
            1.5"""
    def get_variable_value(self, intvariable) -> Any:
        """CVXOPTBackend.get_variable_value(self, int variable)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 595)

        Return the value of a variable given by the solver.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variables(2)
            1
            sage: p.add_linear_constraint([(0,1), (1, 2)], None, 3)
            sage: p.set_objective([2, 5])
            sage: p.solve()
            0
            sage: N(p.get_objective_value(),4)
            7.5
            sage: N(p.get_variable_value(0),4)
            3.6e-7
            sage: N(p.get_variable_value(1),4)
            1.5"""
    @overload
    def is_maximization(self) -> bool:
        """CVXOPTBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 658)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False"""
    @overload
    def is_maximization(self) -> Any:
        """CVXOPTBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 658)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False"""
    @overload
    def is_maximization(self) -> Any:
        """CVXOPTBackend.is_maximization(self) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 658)

        Test whether the problem is a maximization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False"""
    def is_variable_binary(self, intindex) -> bool:
        """CVXOPTBackend.is_variable_binary(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 793)

        Test whether the given variable is of binary type.
        CVXOPT does not allow integer variables, so this is a bit moot.

        INPUT:

        - ``index`` -- integer; the variable's id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.set_variable_type(0,0)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.is_variable_binary(0)
            False"""
    def is_variable_continuous(self, intindex) -> bool:
        """CVXOPTBackend.is_variable_continuous(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 846)

        Test whether the given variable is of continuous/real type.
        CVXOPT does not allow integer variables, so this is a bit moot.

        INPUT:

        - ``index`` -- integer; the variable's id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.is_variable_continuous(0)
            True
            sage: p.set_variable_type(0,1)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.is_variable_continuous(0)
            True"""
    def is_variable_integer(self, intindex) -> bool:
        """CVXOPTBackend.is_variable_integer(self, int index) -> bool

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 819)

        Test whether the given variable is of integer type.
        CVXOPT does not allow integer variables, so this is a bit moot.

        INPUT:

        - ``index`` -- integer; the variable's id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variable()
            0
            sage: p.set_variable_type(0,-1)
            sage: p.set_variable_type(0,1)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: p.is_variable_integer(0)
            False"""
    @overload
    def ncols(self) -> int:
        """CVXOPTBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 622)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2"""
    @overload
    def ncols(self) -> Any:
        """CVXOPTBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 622)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2"""
    @overload
    def ncols(self) -> Any:
        """CVXOPTBackend.ncols(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 622)

        Return the number of columns/variables.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.ncols()
            0
            sage: p.add_variables(2)
            1
            sage: p.ncols()
            2"""
    @overload
    def nrows(self) -> int:
        """CVXOPTBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 640)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.nrows()
            0
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2"""
    @overload
    def nrows(self) -> Any:
        """CVXOPTBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 640)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.nrows()
            0
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2"""
    @overload
    def nrows(self) -> Any:
        """CVXOPTBackend.nrows(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 640)

        Return the number of rows/constraints.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.nrows()
            0
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraints(2, 2.0, None)
            sage: p.nrows()
            2"""
    def objective_coefficient(self, intvariable, coeff=...) -> Any:
        """CVXOPTBackend.objective_coefficient(self, int variable, coeff=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 251)

        Set or get the coefficient of a variable in the objective
        function

        INPUT:

        - ``variable`` -- integer; the variable's id

        - ``coeff`` -- double; its coefficient

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variable()
            0
            sage: p.objective_coefficient(0)
            0.0
            sage: p.objective_coefficient(0,2)
            sage: p.objective_coefficient(0)
            2.0"""
    def problem_name(self, name=...) -> Any:
        '''CVXOPTBackend.problem_name(self, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 677)

        Return or define the problem\'s name.

        INPUT:

        - ``name`` -- string; the problem\'s name. When set to
          ``None`` (default), the method returns the problem\'s name.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'CVXOPT\')
            sage: p.problem_name()
            \'\'
            sage: p.problem_name("There once was a french fry")
            sage: print(p.problem_name())
            There once was a french fry'''
    def row(self, inti) -> Any:
        """CVXOPTBackend.row(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 700)

        Return a row.

        INPUT:

        - ``index`` -- integer; the constraint's id

        OUTPUT:

        A pair ``(indices, coeffs)`` where ``indices`` lists the
        entries whose coefficient is nonzero, and to which ``coeffs``
        associates their coefficient on the model of the
        ``add_linear_constraint`` method.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(list(zip(range(5), range(5))), 2, 2)
            sage: p.row(0)
            ([1, 2, 3, 4], [1, 2, 3, 4])
            sage: p.row_bounds(0)
            (2, 2)"""
    def row_bounds(self, intindex) -> Any:
        """CVXOPTBackend.row_bounds(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 737)

        Return the bounds of a specific constraint.

        INPUT:

        - ``index`` -- integer; the constraint's id

        OUTPUT:

        A pair ``(lower_bound, upper_bound)``. Each of them can be set
        to ``None`` if the constraint is not bounded in the
        corresponding direction, and is a real value otherwise.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variables(5)
            4
            sage: p.add_linear_constraint(list(zip(range(5), range(5))), 2, 2)
            sage: p.row(0)
            ([1, 2, 3, 4], [1, 2, 3, 4])
            sage: p.row_bounds(0)
            (2, 2)"""
    def row_name(self, intindex) -> Any:
        '''CVXOPTBackend.row_name(self, int index)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 874)

        Return the ``index``-th row name.

        INPUT:

        - ``index`` -- integer; the row\'s id

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'CVXOPT\')
            sage: p.add_linear_constraints(1, 2, None, names=["Empty constraint 1"])
            sage: p.row_name(0)
            \'Empty constraint 1\''''
    def set_objective(self, listcoeff, d=...) -> Any:
        """CVXOPTBackend.set_objective(self, list coeff, d=0.0)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 279)

        Set the objective function.

        INPUT:

        - ``coeff`` -- list of real values, whose i-th element is the
          coefficient of the i-th variable in the objective function

        - ``d`` -- double; the constant term in the linear function (set to `0`
          by default)

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variables(5)
            4
            sage: p.set_objective([1, 1, 2, 1, 3])
            sage: [p.objective_coefficient(x) for x in range(5)]
            [1, 1, 2, 1, 3]"""
    def set_sense(self, intsense) -> Any:
        """CVXOPTBackend.set_sense(self, int sense)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 225)

        Set the direction (maximization/minimization).

        INPUT:

        - ``sense`` -- integer:

          * `+1` => Maximization
          * `-1` => Minimization

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.is_maximization()
            True
            sage: p.set_sense(-1)
            sage: p.is_maximization()
            False"""
    def set_variable_type(self, intvariable, intvtype) -> Any:
        """CVXOPTBackend.set_variable_type(self, int variable, int vtype)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 206)

        Set the type of a variable.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='cvxopt')
            sage: p.add_variables(5)
            4
            sage: p.set_variable_type(3, -1)
            sage: p.set_variable_type(3, -2)
            Traceback (most recent call last):
            ...
            ValueError: ..."""
    def set_verbosity(self, intlevel) -> Any:
        """CVXOPTBackend.set_verbosity(self, int level)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 305)

        Do not apply for the cvxopt solver."""
    def solve(self, *args, **kwargs):
        '''CVXOPTBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 403)

        Solve the problem.

        .. NOTE::

            This method raises ``MIPSolverException`` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'cvxopt\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(-4*x[0] - 5*x[1])
            sage: p.add_constraint(2*x[0] + x[1] <= 3)
            sage: p.add_constraint(2*x[1] + x[0] <= 3)
            sage: N(p.solve(), digits=2)
            -9.0

            sage: p = MixedIntegerLinearProgram(solver=\'cvxopt\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 2*x[1])
            sage: p.add_constraint(-5*x[0] + x[1] <= 7)
            sage: p.add_constraint(-5*x[0] + x[1] >= 7)
            sage: p.add_constraint(x[0] + x[1] >= 26)
            sage: p.add_constraint(x[0] >= 3)
            sage: p.add_constraint(x[1] >= 4)
            sage: N(p.solve(), digits=4)
            48.83

            sage: p = MixedIntegerLinearProgram(solver=\'cvxopt\')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + x[1] + 3*x[2])
            sage: p.solver_parameter("show_progress",True)
            sage: p.add_constraint(x[0] + 2*x[1] <= 4)
            sage: p.add_constraint(5*x[2] - x[1] <= 8)
            sage: N(p.solve(), digits=2)
                     pcost       dcost       gap    pres   dres   k/t
                 ...
                8.8

        When the optimal solution is not unique, CVXOPT as an interior point solver
        gives a different type of solution compared to the solvers that use the
        simplex method.

        In the following example, the top face of the cube is optimal, and CVXOPT
        gives the center point of the top face, whereas the other tested solvers
        return a vertex::

            sage: c = MixedIntegerLinearProgram(solver=\'cvxopt\')
            sage: p = MixedIntegerLinearProgram(solver=\'ppl\')
            sage: g = MixedIntegerLinearProgram()
            sage: xc = c.new_variable(nonnegative=True)
            sage: xp = p.new_variable(nonnegative=True)
            sage: xg = g.new_variable(nonnegative=True)
            sage: c.set_objective(xc[2])
            sage: p.set_objective(xp[2])
            sage: g.set_objective(xg[2])
            sage: c.add_constraint(xc[0] <= 100)
            sage: c.add_constraint(xc[1] <= 100)
            sage: c.add_constraint(xc[2] <= 100)
            sage: p.add_constraint(xp[0] <= 100)
            sage: p.add_constraint(xp[1] <= 100)
            sage: p.add_constraint(xp[2] <= 100)
            sage: g.add_constraint(xg[0] <= 100)
            sage: g.add_constraint(xg[1] <= 100)
            sage: g.add_constraint(xg[2] <= 100)
            sage: N(c.solve(), digits=4)
            100.0
            sage: N(c.get_values(xc[0]), digits=3)
            50.0
            sage: N(c.get_values(xc[1]), digits=3)
            50.0
            sage: N(c.get_values(xc[2]), digits=4)
            100.0
            sage: N(p.solve(), digits=4)
            100.0
            sage: N(p.get_values(xp[0]), 2)
            0.00
            sage: N(p.get_values(xp[1]), 2)
            0.00
            sage: N(p.get_values(xp[2]), digits=4)
            100.0
            sage: N(g.solve(), digits=4)
            100.0
            sage: N(g.get_values(xg[0]), 2)       # abstol 1e-15
            0.00
            sage: N(g.get_values(xg[1]), 2)       # abstol 1e-15
            0.00
            sage: N(g.get_values(xg[2]), digits=4)
            100.0'''
    def solver_parameter(self, name, value=...) -> Any:
        '''CVXOPTBackend.solver_parameter(self, name, value=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 976)

        Return or define a solver parameter.

        INPUT:

        - ``name`` -- string; the parameter

        - ``value`` -- the parameter\'s value if it is to be defined,
          or ``None`` (default) to obtain its current value

        .. NOTE::

           The list of available parameters is available at
           :meth:`~sage.numerical.mip.MixedIntegerLinearProgram.solver_parameter`.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver=\'CVXOPT\')
            sage: p.solver_parameter("show_progress")
            False
            sage: p.solver_parameter("show_progress", True)
            sage: p.solver_parameter("show_progress")
            True'''
    def variable_lower_bound(self, intindex, value=...) -> Any:
        """CVXOPTBackend.variable_lower_bound(self, int index, value=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 947)

        Return or define the lower bound on a variable.

        INPUT:

        - ``index`` -- integer; the variable's id

        - ``value`` -- real value, or ``None`` to mean that the
          variable has not lower bound. When set to ``False``
          (default), the method returns the current value.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_lower_bound(0, 5)
            sage: p.col_bounds(0)
            (5, None)"""
    def variable_upper_bound(self, intindex, value=...) -> Any:
        """CVXOPTBackend.variable_upper_bound(self, int index, value=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 918)

        Return or define the upper bound on a variable.

        INPUT:

        - ``index`` -- integer; the variable's id

        - ``value`` -- real value, or ``None`` to mean that the
          variable has not upper bound. When set to ``False``
          (default), the method returns the current value.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = get_solver(solver='CVXOPT')
            sage: p.add_variable()
            0
            sage: p.col_bounds(0)
            (0.0, None)
            sage: p.variable_upper_bound(0, 5)
            sage: p.col_bounds(0)
            (0.0, 5)"""
    def __copy__(self) -> Any:
        """CVXOPTBackend.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_backend.pyx (starting at line 94)

        Return a copy of ``self``.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_backend import get_solver
            sage: p = MixedIntegerLinearProgram(solver='CVXOPT')
            sage: b = p.new_variable()
            sage: p.add_constraint(b[1] + b[2] <= 6)
            sage: p.add_constraint(b[2] <= 5)
            sage: p.set_objective(b[1] + b[2])
            sage: cp = copy(p.get_backend())
            sage: cp.solve()
            0
            sage: cp.get_objective_value()
            6.0"""
