import sage.numerical.backends.matrix_sdp_backend
from sage.matrix.constructor import Matrix as Matrix
from sage.numerical.sdp import SDPSolverException as SDPSolverException
from typing import Any, ClassVar, overload

class CVXOPTSDPBackend(sage.numerical.backends.matrix_sdp_backend.MatrixSDPBackend):
    """CVXOPTSDPBackend(maximization=True, base_ring=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, maximization=..., base_ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 32)

                Cython constructor.

                EXAMPLES::

                    sage: from sage.numerical.backends.generic_sdp_backend import get_solver
                    sage: p = get_solver(solver='CVXOPT')
        """
    def dual_variable(self, inti, sparse=...) -> Any:
        """CVXOPTSDPBackend.dual_variable(self, int i, sparse=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 255)

        The `i`-th dual variable.

        Available after ``self.solve()`` is called, otherwise the result is
        undefined.

        - ``index`` -- integer; the constraint's id

        OUTPUT: the matrix of the `i`-th dual variable

        EXAMPLES::

            sage: p = SemidefiniteProgram(maximization=False, solver='cvxopt')
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
            sage: p.solve()                                     # tol 1e-08
            -3.0
            sage: B = p.get_backend()
            sage: x = p.get_values(x).values()
            sage: -(a3*B.dual_variable(0)).trace() - (b3*B.dual_variable(1)).trace()     # tol 1e-07
            -3.0
            sage: g = sum((B.slack(j)*B.dual_variable(j)).trace() for j in range(2)); g  # tol 1.5e-08
            0.0


        TESTS::

            sage: B.dual_variable(7)
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
            sage: abs(g - B._get_answer()['gap'])   # tol 1e-22
            0.0"""
    @overload
    def get_objective_value(self) -> Any:
        """CVXOPTSDPBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 160)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.154
            sage: N(p.get_backend().get_objective_value(), digits=4)
            -3.154"""
    @overload
    def get_objective_value(self) -> Any:
        """CVXOPTSDPBackend.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 160)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.154
            sage: N(p.get_backend().get_objective_value(), digits=4)
            -3.154"""
    def get_variable_value(self, intvariable) -> Any:
        """CVXOPTSDPBackend.get_variable_value(self, int variable)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 221)

        Return the value of a variable given by the solver.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.154
            sage: N(p.get_backend().get_variable_value(0), digits=3)
            -0.368
            sage: N(p.get_backend().get_variable_value(1), digits=4)
            1.898
            sage: N(p.get_backend().get_variable_value(2), digits=3)
            -0.888"""
    def slack(self, inti, sparse=...) -> Any:
        """CVXOPTSDPBackend.slack(self, int i, sparse=False)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 303)

        Slack of the `i`-th constraint.

        Available after ``self.solve()`` is called, otherwise the result is
        undefined.

        - ``index`` -- integer; the constraint's id

        OUTPUT: the matrix of the slack of the `i`-th constraint

        EXAMPLES::

            sage: p = SemidefiniteProgram(maximization = False, solver='cvxopt')
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
            sage: p.solve()                         # tol 1e-08
            -3.0
            sage: B = p.get_backend()
            sage: B1 = B.slack(1); B1               # tol 1e-08
            [0.0 0.0]
            [0.0 0.0]
            sage: B1.is_positive_definite()
            True
            sage: x = sorted(p.get_values(x).values())
            sage: x[0]*b1 + x[1]*b2 - b3 + B1       # tol 1e-09
            [0.0 0.0]
            [0.0 0.0]

        TESTS::

            sage: B.slack(7)
            Traceback (most recent call last):
            ...
            IndexError: list index out of range"""
    @overload
    def solve(self) -> int:
        """CVXOPTSDPBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 57)

        Solve the problem.

        .. NOTE::

            This method raises :class:`SDPSolverException` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.225
            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.154"""
    @overload
    def solve(self) -> Any:
        """CVXOPTSDPBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 57)

        Solve the problem.

        .. NOTE::

            This method raises :class:`SDPSolverException` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.225
            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.154"""
    @overload
    def solve(self) -> Any:
        """CVXOPTSDPBackend.solve(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 57)

        Solve the problem.

        .. NOTE::

            This method raises :class:`SDPSolverException` exceptions when
            the solution cannot be computed for any reason (none
            exists, or the LP solver was not able to find it, etc...)

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.225
            sage: p = SemidefiniteProgram(solver='cvxopt', maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1] + x[2])
            sage: a1 = matrix([[-7., -11.], [-11., 3.]])
            sage: a2 = matrix([[7., -18.], [-18., 8.]])
            sage: a3 = matrix([[-2., -8.], [-8., 1.]])
            sage: a4 = matrix([[33., -9.], [-9., 26.]])
            sage: b1 = matrix([[-21., -11., 0.], [-11., 10., 8.], [0.,   8., 5.]])
            sage: b2 = matrix([[0.,  10.,  16.], [10., -10., -10.], [16., -10., 3.]])
            sage: b3 = matrix([[-5.,   2., -17.], [2.,  -6.,   8.], [-17.,  8., 6.]])
            sage: b4 = matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] + a3*x[2] <= a4)
            sage: p.add_constraint(b1*x[0] + b2*x[1] + b3*x[2] <= b4)
            sage: N(p.solve(), digits=4)
            -3.154"""
    def solver_parameter(self, name, value=...) -> Any:
        '''CVXOPTSDPBackend.solver_parameter(self, name, value=None)

        File: /build/sagemath/src/sage/src/sage/numerical/backends/cvxopt_sdp_backend.pyx (starting at line 352)

        Return or define a solver parameter.

        INPUT:

        - ``name`` -- string; the parameter

        - ``value`` -- the parameter\'s value if it is to be defined,
          or ``None`` (default) to obtain its current value

        .. NOTE::

           The list of available parameters is available at
           :meth:`~sage.numerical.sdp.SemidefiniteProgram.solver_parameter`.

        EXAMPLES::

            sage: from sage.numerical.backends.generic_sdp_backend import get_solver
            sage: p = get_solver(solver=\'CVXOPT\')
            sage: p.solver_parameter("show_progress")
            False
            sage: p.solver_parameter("show_progress", True)
            sage: p.solver_parameter("show_progress")
            True'''
