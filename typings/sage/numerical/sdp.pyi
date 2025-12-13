import sage.structure.element
import sage.structure.parent
import sage.structure.sage_object
from sage.matrix.constructor import matrix as matrix
from sage.numerical.linear_functions import LinearConstraint as LinearConstraint, LinearFunction as LinearFunction
from sage.structure.element import Matrix as Matrix, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict

class SDPSolverException(RuntimeError):
    '''File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1159)

        Exception raised when the solver fails.

        ``SDPSolverException`` is the exception raised when the solver fails.

        EXAMPLES::

            sage: from sage.numerical.sdp import SDPSolverException
            sage: SDPSolverException("Error")
            SDPSolverException(\'Error\'...)

        TESTS:

        No solution::

            sage: # needs cvxopt
            sage: p = SemidefiniteProgram(solver=\'cvxopt\')
            sage: x = p.new_variable()
            sage: p.set_objective(x[0])
            sage: a = matrix([[1,2],[2,4]])
            sage: b = matrix([[1,9],[9,4]])
            sage: p.add_constraint(a*x[0] == b)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            SDPSolverException: ...

        The value of the exception::

            sage: from sage.numerical.sdp import SDPSolverException
            sage: e = SDPSolverException("Error")
            sage: print(e)
            Error
    '''

class SDPVariable(sage.structure.element.Element):
    """SDPVariable(parent, sdp, name)

    File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1197)

    ``SDPVariable`` is a variable used by the class
    ``SemidefiniteProgram``.

    .. warning::

        You should not instantiate this class directly. Instead, use
        :meth:`SemidefiniteProgram.new_variable`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, sdp, name) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1208)

                Constructor for ``SDPVariable``.

                INPUT:

                - ``parent`` -- :class:`SDPVariableParent`; the parent of the
                  SDP variable

                - ``sdp`` -- :class:`SemidefiniteProgram`; the
                  underlying linear program

                - ``name`` -- a name for the ``SDPVariable``

                - ``lower_bound``, ``upper_bound`` -- lower bound and upper
                  bound on the variable. Set to ``None`` to indicate that the
                  variable is unbounded.

                For more informations, see the method
                ``SemidefiniteProgram.new_variable``.

                EXAMPLES::

                    sage: p = SemidefiniteProgram()
                    sage: p.new_variable()
                    SDPVariable
        """
    @overload
    def items(self) -> Any:
        """SDPVariable.items(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1292)

        Return the pairs (keys,value) contained in the dictionary.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: v = p.new_variable()
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.items())
            [(0, x_0), (1, x_1)]"""
    @overload
    def items(self) -> Any:
        """SDPVariable.items(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1292)

        Return the pairs (keys,value) contained in the dictionary.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: v = p.new_variable()
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.items())
            [(0, x_0), (1, x_1)]"""
    @overload
    def keys(self) -> Any:
        """SDPVariable.keys(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1278)

        Return the keys already defined in the dictionary.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: v = p.new_variable()
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.keys())
            [0, 1]"""
    @overload
    def keys(self) -> Any:
        """SDPVariable.keys(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1278)

        Return the keys already defined in the dictionary.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: v = p.new_variable()
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.keys())
            [0, 1]"""
    @overload
    def values(self) -> Any:
        """SDPVariable.values(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1306)

        Return the symbolic variables associated to the current dictionary.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: v = p.new_variable()
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.values(), key=str)
            [x_0, x_1]"""
    @overload
    def values(self) -> Any:
        """SDPVariable.values(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1306)

        Return the symbolic variables associated to the current dictionary.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: v = p.new_variable()
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.values(), key=str)
            [x_0, x_1]"""
    def __getitem__(self, i) -> Any:
        """SDPVariable.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1240)

        Return the symbolic variable corresponding to the key.

        Returns the element asked, otherwise creates it.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: v = p.new_variable()
            sage: p.set_objective(v[0] + v[1])
            sage: v[0]
            x_0"""

class SDPVariableParent(sage.structure.parent.Parent):
    """File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1367)

        Parent for :class:`SDPVariable`.

        .. warning::

            This class is for internal use. You should not instantiate it
            yourself. Use :meth:`SemidefiniteProgram.new_variable`
            to generate sdp variables.
    """

    class Element(sage.structure.element.Element):
        """SDPVariable(parent, sdp, name)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1197)

        ``SDPVariable`` is a variable used by the class
        ``SemidefiniteProgram``.

        .. warning::

            You should not instantiate this class directly. Instead, use
            :meth:`SemidefiniteProgram.new_variable`."""
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1208)

                    Constructor for ``SDPVariable``.

                    INPUT:

                    - ``parent`` -- :class:`SDPVariableParent`; the parent of the
                      SDP variable

                    - ``sdp`` -- :class:`SemidefiniteProgram`; the
                      underlying linear program

                    - ``name`` -- a name for the ``SDPVariable``

                    - ``lower_bound``, ``upper_bound`` -- lower bound and upper
                      bound on the variable. Set to ``None`` to indicate that the
                      variable is unbounded.

                    For more informations, see the method
                    ``SemidefiniteProgram.new_variable``.

                    EXAMPLES::

                        sage: p = SemidefiniteProgram()
                        sage: p.new_variable()
                        SDPVariable
        """
        @overload
        def items(self) -> Any:
            """SDPVariable.items(self)

            File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1292)

            Return the pairs (keys,value) contained in the dictionary.

            EXAMPLES::

                sage: p = SemidefiniteProgram()
                sage: v = p.new_variable()
                sage: p.set_objective(v[0] + v[1])
                sage: sorted(v.items())
                [(0, x_0), (1, x_1)]"""
        @overload
        def items(self) -> Any:
            """SDPVariable.items(self)

            File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1292)

            Return the pairs (keys,value) contained in the dictionary.

            EXAMPLES::

                sage: p = SemidefiniteProgram()
                sage: v = p.new_variable()
                sage: p.set_objective(v[0] + v[1])
                sage: sorted(v.items())
                [(0, x_0), (1, x_1)]"""
        @overload
        def keys(self) -> Any:
            """SDPVariable.keys(self)

            File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1278)

            Return the keys already defined in the dictionary.

            EXAMPLES::

                sage: p = SemidefiniteProgram()
                sage: v = p.new_variable()
                sage: p.set_objective(v[0] + v[1])
                sage: sorted(v.keys())
                [0, 1]"""
        @overload
        def keys(self) -> Any:
            """SDPVariable.keys(self)

            File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1278)

            Return the keys already defined in the dictionary.

            EXAMPLES::

                sage: p = SemidefiniteProgram()
                sage: v = p.new_variable()
                sage: p.set_objective(v[0] + v[1])
                sage: sorted(v.keys())
                [0, 1]"""
        @overload
        def values(self) -> Any:
            """SDPVariable.values(self)

            File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1306)

            Return the symbolic variables associated to the current dictionary.

            EXAMPLES::

                sage: p = SemidefiniteProgram()
                sage: v = p.new_variable()
                sage: p.set_objective(v[0] + v[1])
                sage: sorted(v.values(), key=str)
                [x_0, x_1]"""
        @overload
        def values(self) -> Any:
            """SDPVariable.values(self)

            File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1306)

            Return the symbolic variables associated to the current dictionary.

            EXAMPLES::

                sage: p = SemidefiniteProgram()
                sage: v = p.new_variable()
                sage: p.set_objective(v[0] + v[1])
                sage: sorted(v.values(), key=str)
                [x_0, x_1]"""
        def __getitem__(self, i) -> Any:
            """SDPVariable.__getitem__(self, i)

            File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1240)

            Return the symbolic variable corresponding to the key.

            Returns the element asked, otherwise creates it.

            EXAMPLES::

                sage: p = SemidefiniteProgram()
                sage: v = p.new_variable()
                sage: p.set_objective(v[0] + v[1])
                sage: v[0]
                x_0"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class SemidefiniteProgram(sage.structure.sage_object.SageObject):
    '''SemidefiniteProgram(solver=None, maximization=True, names=tuple(), **kwds)

    File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 241)

    The ``SemidefiniteProgram`` class is the link between Sage, semidefinite
    programming (SDP) and semidefinite programming solvers.

    A Semidefinite Programming (SDP) consists of variables, linear
    constraints on these variables, and an objective function which is to be
    maximised or minimised under these constraints.

    See the :wikipedia:`Semidefinite_programming` for further information on semidefinite
    programming, and the :mod:`SDP module <sage.numerical.sdp>` for its use in
    Sage.

    INPUT:

    - ``solver`` -- selects a solver:

      - CVXOPT (``solver="CVXOPT"``). See the `CVXOPT <http://www.cvxopt.org/>`_
        website.

      - If ``solver=None`` (default), the default solver is used (see
        :func:`default_sdp_solver`)

    - ``maximization``

      - When set to ``True`` (default), the ``SemidefiniteProgram``
        is defined as a maximization.

      - When set to ``False``, the ``SemidefiniteProgram`` is
        defined as a minimization.


    .. SEEALSO::

        - :func:`default_sdp_solver` -- returns/sets the default SDP solver

    EXAMPLES:

    Computation of a basic Semidefinite Program::

         sage: p = SemidefiniteProgram(maximization=False)
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
         sage: N(p.solve(), 2)                                                          # needs cvxopt
         -3.0'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, solver=..., maximization=..., names=..., **kwds) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 296)

                Constructor for the ``SemidefiniteProgram`` class.

                INPUT:

                - ``solver`` -- the following solvers should be available through this class:

                  - CVXOPT (``solver="CVXOPT"``). See the `CVXOPT <http://www.cvxopt.org/>`_
                      web site.

                  - If ``solver=None`` (default), the default solver is used (see
                   ``default_sdp_solver`` method.

                - ``maximization``

                  - When set to ``True`` (default), the ``SemidefiniteProgram``
                    is defined as a maximization.
                  - When set to ``False``, the ``SemidefiniteProgram`` is
                    defined as a minimization.

                - ``names`` -- list/tuple/iterable of string. Default names of
                  the SDP variables. Used to enable the ``sdp.<x> =
                  SemidefiniteProgram()`` syntax.

                - other keyword arguments are passed to the solver.

                .. SEEALSO::

                - :meth:`default_sdp_solver` -- returns/Sets the default SDP solver

                EXAMPLES::

                    sage: p = SemidefiniteProgram(maximization=True)
        '''
    @overload
    def __init__(self, maximization=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 296)

                Constructor for the ``SemidefiniteProgram`` class.

                INPUT:

                - ``solver`` -- the following solvers should be available through this class:

                  - CVXOPT (``solver="CVXOPT"``). See the `CVXOPT <http://www.cvxopt.org/>`_
                      web site.

                  - If ``solver=None`` (default), the default solver is used (see
                   ``default_sdp_solver`` method.

                - ``maximization``

                  - When set to ``True`` (default), the ``SemidefiniteProgram``
                    is defined as a maximization.
                  - When set to ``False``, the ``SemidefiniteProgram`` is
                    defined as a minimization.

                - ``names`` -- list/tuple/iterable of string. Default names of
                  the SDP variables. Used to enable the ``sdp.<x> =
                  SemidefiniteProgram()`` syntax.

                - other keyword arguments are passed to the solver.

                .. SEEALSO::

                - :meth:`default_sdp_solver` -- returns/Sets the default SDP solver

                EXAMPLES::

                    sage: p = SemidefiniteProgram(maximization=True)
        '''
    def add_constraint(self, linear_function, name=...) -> Any:
        """SemidefiniteProgram.add_constraint(self, linear_function, name=None)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 813)

        Add a constraint to the ``SemidefiniteProgram``.

        INPUT:

        - ``linear_function`` -- two different types of arguments are possible:

          - A linear function. In this case, arguments ``min`` or ``max``
            have to be specified.
          - A linear constraint of the form ``A <= B``, ``A >= B``,
            ``A <= B <= C``, ``A >= B >= C`` or ``A == B``. In this
            case, arguments ``min`` and ``max`` will be ignored.

        - ``name`` -- a name for the constraint

        EXAMPLES:

        Let's solve the following semidefinite program:

        .. MATH::

            \\begin{aligned}
                \\text{maximize} &\\qquad x + 5y  \\qquad \\\\\n                \\text{subject to} &\\qquad \\left( \\begin{array}{cc} 1 & 2  \\\\ 2 & 3  \\end{array} \\right) x +
                \\left( \\begin{array}{cc} 1 & 1  \\\\ 1 & 1  \\end{array} \\right) y \\preceq
                \\left( \\begin{array}{cc} 1 & -1  \\\\ -1 & 1  \\end{array} \\right)
            \\end{aligned}

        This SDP can be solved as follows::

            sage: p = SemidefiniteProgram(maximization=True)
            sage: x = p.new_variable()
            sage: p.set_objective(x[1] + 5*x[2])
            sage: a1 = matrix([[1,2],[2,3]])
            sage: a2 = matrix([[1,1],[1,1]])
            sage: a3 = matrix([[1,-1],[-1,1]])
            sage: p.add_constraint(a1*x[1] + a2*x[2] <= a3)
            sage: N(p.solve(), digits=3)                                                # needs cvxopt
            16.2

        One can also define double-bounds or equality using the symbol
        ``>=`` or ``==``::

            sage: p = SemidefiniteProgram(maximization=True)
            sage: x = p.new_variable()
            sage: p.set_objective(x[1] + 5*x[2])
            sage: a1 = matrix([[1,2],[2,3]])
            sage: a2 = matrix([[1,1],[1,1]])
            sage: a3 = matrix([[1,-1],[-1,1]])
            sage: p.add_constraint(a3 >= a1*x[1] + a2*x[2])
            sage: N(p.solve(), digits=3)                                                # needs cvxopt
            16.2

        TESTS:

        Complex constraints::

            sage: p = SemidefiniteProgram()
            sage: b = p.new_variable()
            sage: a1 = matrix([[1,2],[2,3]])
            sage: a2 = matrix([[1,-2],[-2,4]])
            sage: p.add_constraint(a1*b[8] - a1*b[15] <= a2*b[8])
            sage: p.show()
            Maximization:
            <BLANKLINE>
            Constraints:
                constraint_0: [ 0.0  4.0][ 4.0 -1.0]x_0 + [-1.0 -2.0][-2.0 -3.0]x_1 <=  [0 0][0 0]
            Variables:
              x_0, x_1

        Empty constraint::

            sage: p = SemidefiniteProgram()
            sage: p.add_constraint(sum([]))"""
    @overload
    def base_ring(self) -> Any:
        """SemidefiniteProgram.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 448)

        Return the base ring.

        OUTPUT: a ring. The coefficients that the chosen solver supports

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt')
            sage: p.base_ring()
            Real Double Field"""
    @overload
    def base_ring(self) -> Any:
        """SemidefiniteProgram.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 448)

        Return the base ring.

        OUTPUT: a ring. The coefficients that the chosen solver supports

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver='cvxopt')
            sage: p.base_ring()
            Real Double Field"""
    def dual_variable(self, inti, sparse=...) -> Any:
        """SemidefiniteProgram.dual_variable(self, int i, sparse=False)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 953)

        The `i`-th dual variable.

        Available after ``self.solve()`` is called, otherwise the result is
        undefined.

        INPUT:

        - ``index`` -- integer; the constraint's id

        OUTPUT: the matrix of the `i`-th dual variable

        EXAMPLES:

        Dual objective value is the same as the primal one::

            sage: p = SemidefiniteProgram(maximization=False)
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

            sage: # needs cvxopt
            sage: p.solve()                                                              # tol 1e-08
            -3.0
            sage: x = p.get_values(x).values()
            sage: -(a3*p.dual_variable(0)).trace() - (b3*p.dual_variable(1)).trace()     # tol 1e-07
            -3.0

        Dual variable is orthogonal to the slack ::

            sage: # needs cvxopt
            sage: g = sum((p.slack(j)*p.dual_variable(j)).trace() for j in range(2)); g  # tol 1.2e-08
            0.0

        TESTS::

            sage: p.dual_variable(7)                                                    # needs cvxopt
            Traceback (most recent call last):
            ...
            IndexError: list index out of range"""
    @overload
    def gen(self, i) -> Any:
        """SemidefiniteProgram.gen(self, i)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 552)

        Return the linear variable `x_i`.

        EXAMPLES::

            sage: sdp = SemidefiniteProgram()
            sage: sdp.gen(0)
            x_0
            sage: [sdp.gen(i) for i in range(10)]
            [x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9]"""
    @overload
    def gen(self, i) -> Any:
        """SemidefiniteProgram.gen(self, i)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 552)

        Return the linear variable `x_i`.

        EXAMPLES::

            sage: sdp = SemidefiniteProgram()
            sage: sdp.gen(0)
            x_0
            sage: [sdp.gen(i) for i in range(10)]
            [x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9]"""
    @overload
    def get_backend(self) -> Any:
        """SemidefiniteProgram.get_backend(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1133)

        Return the backend instance used.

        This might be useful when access to additional functions provided by
        the backend is needed.

        EXAMPLES:

        This example prints a matrix coefficient::

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
    def get_backend(self) -> Any:
        """SemidefiniteProgram.get_backend(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1133)

        Return the backend instance used.

        This might be useful when access to additional functions provided by
        the backend is needed.

        EXAMPLES:

        This example prints a matrix coefficient::

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
    def get_values(self, *lists) -> Any:
        '''SemidefiniteProgram.get_values(self, *lists)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 690)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - Any instance of :class:`SDPVariable` (or one of its elements),
          or lists of them.

        OUTPUT:

        - Each instance of :class:`SDPVariable` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a :class:`SDPVariable` is replaced
          by its corresponding numerical value.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver = "cvxopt", maximization = False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[3] - x[5])
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 5.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 2.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[3] + a2*x[5] <= a3)
            sage: p.add_constraint(b1*x[3] + b2*x[5] <= b3)
            sage: N(p.solve(), 3)                                                       # needs cvxopt
            -3.0

        To return  the optimal value of ``x[3]``::

            sage: N(p.get_values(x[3]),3)                                               # needs cvxopt
            -1.0

        To get a dictionary identical to ``x`` containing optimal
        values for the corresponding variables ::

            sage: x_sol = p.get_values(x)                                               # needs cvxopt
            sage: sorted(x_sol)                                                         # needs cvxopt
            [3, 5]'''
    @overload
    def get_values(self, x) -> Any:
        '''SemidefiniteProgram.get_values(self, *lists)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 690)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - Any instance of :class:`SDPVariable` (or one of its elements),
          or lists of them.

        OUTPUT:

        - Each instance of :class:`SDPVariable` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a :class:`SDPVariable` is replaced
          by its corresponding numerical value.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver = "cvxopt", maximization = False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[3] - x[5])
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 5.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 2.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[3] + a2*x[5] <= a3)
            sage: p.add_constraint(b1*x[3] + b2*x[5] <= b3)
            sage: N(p.solve(), 3)                                                       # needs cvxopt
            -3.0

        To return  the optimal value of ``x[3]``::

            sage: N(p.get_values(x[3]),3)                                               # needs cvxopt
            -1.0

        To get a dictionary identical to ``x`` containing optimal
        values for the corresponding variables ::

            sage: x_sol = p.get_values(x)                                               # needs cvxopt
            sage: sorted(x_sol)                                                         # needs cvxopt
            [3, 5]'''
    @overload
    def linear_constraints_parent(self) -> Any:
        """SemidefiniteProgram.linear_constraints_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 357)

        Return the parent for all linear constraints.

        See :mod:`~sage.numerical.linear_functions` for more
        details.

        EXAMPLES::

             sage: p = SemidefiniteProgram()
             sage: p.linear_constraints_parent()
             Linear constraints over Real Double Field"""
    @overload
    def linear_constraints_parent(self) -> Any:
        """SemidefiniteProgram.linear_constraints_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 357)

        Return the parent for all linear constraints.

        See :mod:`~sage.numerical.linear_functions` for more
        details.

        EXAMPLES::

             sage: p = SemidefiniteProgram()
             sage: p.linear_constraints_parent()
             Linear constraints over Real Double Field"""
    def linear_function(self, *args, **kwargs):
        """SemidefiniteProgram.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 376)

        Construct a new linear function.

        EXAMPLES::

             sage: p = SemidefiniteProgram()
             sage: p.linear_function({0:1})
             x_0"""
    @overload
    def linear_functions_parent(self) -> Any:
        """SemidefiniteProgram.linear_functions_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 341)

        Return the parent for all linear functions.

        EXAMPLES::

             sage: p = SemidefiniteProgram()
             sage: p.linear_functions_parent()
             Linear functions over Real Double Field"""
    @overload
    def linear_functions_parent(self) -> Any:
        """SemidefiniteProgram.linear_functions_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 341)

        Return the parent for all linear functions.

        EXAMPLES::

             sage: p = SemidefiniteProgram()
             sage: p.linear_functions_parent()
             Linear functions over Real Double Field"""
    @overload
    def new_variable(self, name=...) -> Any:
        '''SemidefiniteProgram.new_variable(self, name=\'\')

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 480)

        Return an instance of :class:`SDPVariable` associated
        to the current instance of :class:`SemidefiniteProgram`.

        A new variable ``x`` is defined by::

            sage: p = SemidefiniteProgram()
            sage: x = p.new_variable()

        It behaves exactly as an usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        INPUT:

        - ``dim`` -- integer; defines the dimension of the dictionary
          If ``x`` has dimension `2`, its fields will be of the form
          ``x[key1][key2]``. Deprecated.

        - ``name`` -- string; associates a name to the variable

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: x = p.new_variable()
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: p.add_constraint(a1*x[0] + a1*x[3] <= 0)
            sage: p.show()
            Maximization:
            <BLANKLINE>
            Constraints:
              constraint_0: [1.0 2.0][2.0 3.0]x_0 + [1.0 2.0][2.0 3.0]x_1 <=  [0 0][0 0]
            Variables:
               x_0,  x_1'''
    @overload
    def new_variable(self) -> Any:
        '''SemidefiniteProgram.new_variable(self, name=\'\')

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 480)

        Return an instance of :class:`SDPVariable` associated
        to the current instance of :class:`SemidefiniteProgram`.

        A new variable ``x`` is defined by::

            sage: p = SemidefiniteProgram()
            sage: x = p.new_variable()

        It behaves exactly as an usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        INPUT:

        - ``dim`` -- integer; defines the dimension of the dictionary
          If ``x`` has dimension `2`, its fields will be of the form
          ``x[key1][key2]``. Deprecated.

        - ``name`` -- string; associates a name to the variable

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: x = p.new_variable()
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: p.add_constraint(a1*x[0] + a1*x[3] <= 0)
            sage: p.show()
            Maximization:
            <BLANKLINE>
            Constraints:
              constraint_0: [1.0 2.0][2.0 3.0]x_0 + [1.0 2.0][2.0 3.0]x_1 <=  [0 0][0 0]
            Variables:
               x_0,  x_1'''
    @overload
    def new_variable(self) -> Any:
        '''SemidefiniteProgram.new_variable(self, name=\'\')

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 480)

        Return an instance of :class:`SDPVariable` associated
        to the current instance of :class:`SemidefiniteProgram`.

        A new variable ``x`` is defined by::

            sage: p = SemidefiniteProgram()
            sage: x = p.new_variable()

        It behaves exactly as an usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        INPUT:

        - ``dim`` -- integer; defines the dimension of the dictionary
          If ``x`` has dimension `2`, its fields will be of the form
          ``x[key1][key2]``. Deprecated.

        - ``name`` -- string; associates a name to the variable

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: x = p.new_variable()
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: p.add_constraint(a1*x[0] + a1*x[3] <= 0)
            sage: p.show()
            Maximization:
            <BLANKLINE>
            Constraints:
              constraint_0: [1.0 2.0][2.0 3.0]x_0 + [1.0 2.0][2.0 3.0]x_1 <=  [0 0][0 0]
            Variables:
               x_0,  x_1'''
    @overload
    def number_of_constraints(self) -> int:
        '''SemidefiniteProgram.number_of_constraints(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 566)

        Return the number of constraints assigned so far.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver = "cvxopt")
            sage: x = p.new_variable()
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 5.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 2.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a3)
            sage: p.add_constraint(b1*x[0] + b2*x[1] <= b3)
            sage: p.add_constraint(b1*x[0] + a2*x[1] <= b3)
            sage: p.number_of_constraints()
            3'''
    @overload
    def number_of_constraints(self) -> Any:
        '''SemidefiniteProgram.number_of_constraints(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 566)

        Return the number of constraints assigned so far.

        EXAMPLES::

            sage: p = SemidefiniteProgram(solver = "cvxopt")
            sage: x = p.new_variable()
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 5.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 2.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a3)
            sage: p.add_constraint(b1*x[0] + b2*x[1] <= b3)
            sage: p.add_constraint(b1*x[0] + a2*x[1] <= b3)
            sage: p.number_of_constraints()
            3'''
    @overload
    def number_of_variables(self) -> int:
        """SemidefiniteProgram.number_of_variables(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 588)

        Return the number of variables used so far.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: a = matrix([[1, 2.], [2., 3.]])
            sage: p.add_constraint(a*p[0] - a*p[2] <=  2*a*p[4]  )
            sage: p.number_of_variables()
            3"""
    @overload
    def number_of_variables(self) -> Any:
        """SemidefiniteProgram.number_of_variables(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 588)

        Return the number of variables used so far.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: a = matrix([[1, 2.], [2., 3.]])
            sage: p.add_constraint(a*p[0] - a*p[2] <=  2*a*p[4]  )
            sage: p.number_of_variables()
            3"""
    def set_objective(self, obj) -> Any:
        """SemidefiniteProgram.set_objective(self, obj)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 758)

        Set the objective of the :class:`SemidefiniteProgram`.

        INPUT:

        - ``obj`` -- a semidefinite function to be optimized
          (can also be set to ``None`` or ``0`` when just
          looking for a feasible solution)

        EXAMPLES:

        Let's solve the following semidefinite program:

        .. MATH::

            \\begin{aligned}
                \\text{maximize} &\\qquad x + 5y  \\qquad \\\\\n                \\text{subject to} &\\qquad \\left( \\begin{array}{cc} 1 & 2  \\\\ 2 & 3  \\end{array} \\right) x +
                \\left( \\begin{array}{cc} 1 & 1  \\\\ 1 & 1  \\end{array} \\right) y \\preceq
                \\left( \\begin{array}{cc} 1 & -1  \\\\ -1 & 1  \\end{array} \\right)
            \\end{aligned}

        This SDP can be solved as follows::

            sage: p = SemidefiniteProgram(maximization=True)
            sage: x = p.new_variable()
            sage: p.set_objective(x[1] + 5*x[2])
            sage: a1 = matrix([[1,2],[2,3]])
            sage: a2 = matrix([[1,1],[1,1]])
            sage: a3 = matrix([[1,-1],[-1,1]])
            sage: p.add_constraint(a1*x[1] + a2*x[2] <= a3)
            sage: N(p.solve(), digits=3)                                                # needs cvxopt
            16.2
            sage: p.set_objective(None)
            sage: _ = p.solve()                                                         # needs cvxopt"""
    def set_problem_name(self, name) -> Any:
        '''SemidefiniteProgram.set_problem_name(self, name)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 462)

        Set the name of the ``SemidefiniteProgram``.

        INPUT:

        - ``name`` -- string representing the name of the
          ``SemidefiniteProgram``

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: p.set_problem_name("Test program")
            sage: p
            Semidefinite Program "Test program" ( maximization, 0 variables, 0 constraints )'''
    @overload
    def show(self) -> Any:
        """SemidefiniteProgram.show(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 602)

        Display the :class:`SemidefiniteProgram` in a human-readable way.

        EXAMPLES:

        When constraints and variables have names ::

              sage: p = SemidefiniteProgram()
              sage: x = p.new_variable(name='hihi')
              sage: a1 = matrix([[1,2],[2,3]])
              sage: a2 = matrix([[2,3],[3,4]])
              sage: a3 = matrix([[3,4],[4,5]])
              sage: p.set_objective(x[0] - x[1])
              sage: p.add_constraint(a1*x[0] + a2*x[1]<= a3)
              sage: p.show()
              Maximization:
                hihi[0] - hihi[1]
              Constraints:
                constraint_0: [1.0 2.0][2.0 3.0]hihi[0] + [2.0 3.0][3.0 4.0]hihi[1] <=  [3.0 4.0][4.0 5.0]
              Variables:
                 hihi[0],  hihi[1]"""
    @overload
    def show(self) -> Any:
        """SemidefiniteProgram.show(self)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 602)

        Display the :class:`SemidefiniteProgram` in a human-readable way.

        EXAMPLES:

        When constraints and variables have names ::

              sage: p = SemidefiniteProgram()
              sage: x = p.new_variable(name='hihi')
              sage: a1 = matrix([[1,2],[2,3]])
              sage: a2 = matrix([[2,3],[3,4]])
              sage: a3 = matrix([[3,4],[4,5]])
              sage: p.set_objective(x[0] - x[1])
              sage: p.add_constraint(a1*x[0] + a2*x[1]<= a3)
              sage: p.show()
              Maximization:
                hihi[0] - hihi[1]
              Constraints:
                constraint_0: [1.0 2.0][2.0 3.0]hihi[0] + [2.0 3.0][3.0 4.0]hihi[1] <=  [3.0 4.0][4.0 5.0]
              Variables:
                 hihi[0],  hihi[1]"""
    def slack(self, inti, sparse=...) -> Any:
        """SemidefiniteProgram.slack(self, int i, sparse=False)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1004)

        Slack of the `i`-th constraint.

        Available after ``self.solve()`` is called, otherwise the result is
        undefined.

        INPUT:

        - ``index`` -- integer; the constraint's id

        OUTPUT: the matrix of the slack of the `i`-th constraint

        EXAMPLES::

            sage: p = SemidefiniteProgram(maximization = False)
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

            sage: # needs cvxopt
            sage: p.solve()                         # tol 1e-08
            -3.0
            sage: B1 = p.slack(1); B1               # tol 1e-08
            [0.0 0.0]
            [0.0 0.0]
            sage: B1.is_positive_definite()
            True
            sage: x = sorted(p.get_values(x).values())
            sage: x[0]*b1 + x[1]*b2 - b3 + B1       # tol 1e-09
            [0.0 0.0]
            [0.0 0.0]

        TESTS::

            sage: p.slack(7)                                                            # needs cvxopt
            Traceback (most recent call last):
            ...
            IndexError: list index out of range"""
    @overload
    def solve(self, objective_only=...) -> Any:
        """SemidefiniteProgram.solve(self, objective_only=False)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 911)

        Solve the :class:`SemidefiniteProgram`.

        INPUT:

        - ``objective_only`` -- boolean:

          - when set to ``True``, only the objective function is returned
          - when set to ``False`` (default), the optimal numerical values
            are stored (takes computational time)

        OUTPUT: the optimal value taken by the objective function

        TESTS:

        The SDP from the header of this module::

            sage: p = SemidefiniteProgram(maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1])
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 2.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 1.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a3)
            sage: p.add_constraint(b1*x[0] + b2*x[1] <= b3)

            sage: # needs cvxopt
            sage: N(p.solve(), 4)
            -11.
            sage: x = p.get_values(x)
            sage: N(x[0],4)
            -8.0
            sage: N(x[1],4)
            3.0"""
    @overload
    def solve(self) -> Any:
        """SemidefiniteProgram.solve(self, objective_only=False)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 911)

        Solve the :class:`SemidefiniteProgram`.

        INPUT:

        - ``objective_only`` -- boolean:

          - when set to ``True``, only the objective function is returned
          - when set to ``False`` (default), the optimal numerical values
            are stored (takes computational time)

        OUTPUT: the optimal value taken by the objective function

        TESTS:

        The SDP from the header of this module::

            sage: p = SemidefiniteProgram(maximization=False)
            sage: x = p.new_variable()
            sage: p.set_objective(x[0] - x[1])
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 2.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 1.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a3)
            sage: p.add_constraint(b1*x[0] + b2*x[1] <= b3)

            sage: # needs cvxopt
            sage: N(p.solve(), 4)
            -11.
            sage: x = p.get_values(x)
            sage: N(x[0],4)
            -8.0
            sage: N(x[1],4)
            3.0"""
    def solver_parameter(self, name, value=...) -> Any:
        '''SemidefiniteProgram.solver_parameter(self, name, value=None)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1053)

        Return or define a solver parameter.

        The solver parameters are by essence solver-specific, which
        means their meaning heavily depends on the solver used.

        (If you do not know which solver you are using, then you are
        using CVXOPT).

        INPUT:

        - ``name`` -- string; the parameter

        - ``value`` -- the parameter\'s value if it is to be defined,
          or ``None`` (default) to obtain its current value

        EXAMPLES::

            sage: # needs cvxopt
            sage: p.<x> = SemidefiniteProgram(solver=\'cvxopt\',
            ....:                             maximization=False)
            sage: p.solver_parameter("show_progress", True)
            sage: p.solver_parameter("show_progress")
            True
            sage: p.set_objective(x[0] - x[1])
            sage: a1 = matrix([[1, 2.], [2., 3.]])
            sage: a2 = matrix([[3, 4.], [4., 2.]])
            sage: a3 = matrix([[5, 6.], [6., 7.]])
            sage: b1 = matrix([[1, 1.], [1., 1.]])
            sage: b2 = matrix([[2, 2.], [2., 1.]])
            sage: b3 = matrix([[3, 3.], [3., 3.]])
            sage: p.add_constraint(a1*x[0] + a2*x[1] <= a3)
            sage: p.add_constraint(b1*x[0] + b2*x[1] <= b3)
            sage: N(p.solve(), 4)
                 pcost       dcost       gap    pres   dres   k/t
             0:  1...
            ...
            Optimal solution found.
            -11.'''
    def sum(self, L) -> Any:
        """SemidefiniteProgram.sum(self, L)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 1099)

        Efficiently compute the sum of a sequence of
        :class:`~sage.numerical.linear_functions.LinearFunction` elements.

        INPUT:

        - ``L`` -- list of
          :class:`~sage.numerical.linear_functions.LinearFunction` instances

        .. NOTE::

            The use of the regular ``sum`` function is not recommended
            as it is much less efficient than this one.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: v = p.new_variable()

        The following command::

            sage: s = p.sum(v[i] for i in range(90))

        is much more efficient than::

            sage: s = sum(v[i] for i in range(90))"""
    def __call__(self, x) -> Any:
        """SemidefiniteProgram.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 376)

        Construct a new linear function.

        EXAMPLES::

             sage: p = SemidefiniteProgram()
             sage: p.linear_function({0:1})
             x_0"""
    def __getitem__(self, v) -> Any:
        """SemidefiniteProgram.__getitem__(self, v)

        File: /build/sagemath/src/sage/src/sage/numerical/sdp.pyx (starting at line 423)

        Return the symbolic variable corresponding to the key
        from a default dictionary.

        It returns the element asked, and otherwise creates it.
        If necessary, it also creates the default dictionary.

        This method lets the user define LinearProgram without having to
        define independent dictionaries when it is not necessary for him.

        EXAMPLES::

            sage: p = SemidefiniteProgram()
            sage: p.set_objective(p['x'] + p['z'])
            sage: p['x']
            x_0"""
