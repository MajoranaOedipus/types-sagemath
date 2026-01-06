r"""
Generic Backend for SDP solvers

This class only lists the methods that should be defined by any
interface with a SDP Solver. All these methods immediately raise
:exc:`NotImplementedError` exceptions when called, and are obviously
meant to be replaced by the solver-specific method. This file can also
be used as a template to create a new interface : one would only need
to replace the occurrences of ``"Nonexistent_SDP_solver"`` by the
solver's name, and replace ``GenericSDPBackend`` by
``SolverName(GenericSDPBackend)`` so that the new solver extends this
class.

AUTHORS:

- Ingolfur Edvardsson (2014-07): initial implementation
"""
from collections.abc import Iterable
from typing import Any, Literal, overload
from typings_sagemath import Int, RealInexact
from sage.structure.element import RingElement, Matrix
from sage.rings.ring import Ring

@overload
def default_sdp_solver() -> str | type[GenericSDPBackend]: ...
@overload
def default_sdp_solver(solver: Literal["SVXOPT"] | type[GenericSDPBackend]) -> None:
    """
    Return/set the default SDP solver used by Sage.

    INPUT:

    - ``solver`` -- one of the following:

      - the string ``'CVXOPT'``, to make the use of the CVXOPT solver
        (see the `CVXOPT <http://cvxopt.org/>`_ web site) the default;

      - a subclass of
        :class:`sage.numerical.backends.generic_sdp_backend.GenericSDPBackend`,
        to make it the default; or

      - ``None`` -- (default) in which case the current default solver
        (a string or a class) is returned

    OUTPUT:

    This function returns the current default solver (a string or a
    class) if ``solver = None`` (default). Otherwise, it sets the
    default solver to the one given. If this solver does not exist, or
    is not available, a :exc:`ValueError` exception is raised.

    EXAMPLES::

        sage: former_solver = default_sdp_solver()
        sage: default_sdp_solver("Cvxopt")
        sage: default_sdp_solver()
        'Cvxopt'
        sage: default_sdp_solver("Yeahhhhhhhhhhh")
        Traceback (most recent call last):
        ...
        ValueError: 'solver' should be set to ...
        sage: default_sdp_solver(former_solver)
        sage: from sage.numerical.backends.generic_sdp_backend import GenericSDPBackend
        sage: class my_sdp_solver(GenericSDPBackend): pass
        sage: default_sdp_solver(my_sdp_solver)
        sage: default_sdp_solver() is my_sdp_solver
        True
    """
default_solver: None | str | type[GenericSDPBackend]
def get_solver(solver: Literal["SVXOPT"] | type[GenericSDPBackend] | None = None, base_ring: Ring | None = None) -> GenericSDPBackend:
    """
    Return a solver according to the given preferences.

    INPUT:

    - ``solver`` -- one of the following:

      - the string ``'CVXOPT'``, designating the use of the CVXOPT solver
        (see the `CVXOPT <http://cvxopt.org/>`_ web site);

      - a subclass of
        :class:`sage.numerical.backends.generic_sdp_backend.GenericSDPBackend`

      - ``None`` -- (default) in which case the default solver is used (see
        :func:`default_sdp_solver`)

    .. SEEALSO::

        - :func:`default_sdp_solver` -- returns/sets the default SDP solver

    EXAMPLES::

        sage: from sage.numerical.backends.generic_sdp_backend import get_solver
        sage: p = get_solver()

    Passing a class::

        sage: from sage.numerical.backends.generic_sdp_backend import GenericSDPBackend
        sage: class MockSDPBackend(GenericSDPBackend):
        ....:     def solve(self):
        ....:         raise RuntimeError("SDP is too slow")
        sage: P = SemidefiniteProgram(solver=MockSDPBackend)
        sage: P.solve()
        Traceback (most recent call last):
        ...
        RuntimeError: SDP is too slow
    """

class GenericSDPBackend:
    
    def add_linear_constraint(self, coefficients: Iterable[tuple[Int, RealInexact]], name: str | None = None):
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
    def add_linear_constraints(self, number: Int, names: str | None = None):
        '''
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
    def add_variable(self, obj=0.0, name: str | None = None) -> int:
        '''
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
    def add_variables(self, n: Int, names: Iterable[str] | None = None) -> int:
        '''
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
    def base_ring(self) -> Ring:
        """
        The base ring.

        TESTS::

            sage: from sage.numerical.backends.generic_sdp_backend import GenericSDPBackend
            sage: GenericSDPBackend().base_ring()
            Real Double Field"""
    def col_name(self, index: Int) -> str:
        '''
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
    def dual_variable(self, i: Int, sparse: bool = False) -> Matrix:
        '''
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
    def get_objective_value(self):
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
    def get_variable_value(self, variable: Int):
        '''
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
    def is_maximization(self) -> bool:
        '''
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
    def ncols(self) -> int:
        '''
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
    def nrows(self) -> int:
        '''
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
    def objective_coefficient(self, variable: int, coeff: RealInexact | None = None):
        '''
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
    @overload
    def problem_name(self) -> str: ...
    @overload
    def problem_name(self, name: str) -> None:
        '''
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
    def row(self, i: Int) -> tuple:
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
    def row_name(self, index: Int) -> str:
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
    def set_objective(self, coeff: list[RealInexact], d: RealInexact =0.0) -> None:
        '''
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
    def set_sense(self, sense: Literal[+1, -1]) -> None:
        '''
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
    def slack(self, i: Int, sparse: bool = False) -> Matrix:
        '''
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
    def solve(self) -> int:
        '''
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
    def solver_parameter(self, name: str, value) -> None: ...
    @overload
    def solver_parameter(self, name: str) -> Any:
        '''
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
    def zero(self) -> RingElement:
        """
        Zero of the base ring.

        TESTS::

            sage: from sage.numerical.backends.generic_sdp_backend import GenericSDPBackend
            sage: GenericSDPBackend().zero()
            0.0"""
