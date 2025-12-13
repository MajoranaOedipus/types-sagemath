import sage.sets.family
import sage.structure.sage_object
from sage.categories.category import ZZ as ZZ
from sage.structure.element import Matrix as Matrix
from typing import Any, ClassVar, overload

class MIPSolverException(RuntimeError):
    '''File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3173)

        Exception raised when the solver fails.

        EXAMPLES::

            sage: from sage.numerical.mip import MIPSolverException
            sage: e = MIPSolverException("Error")
            sage: e
            MIPSolverException(\'Error\'...)
            sage: print(e)
            Error

        TESTS:

        No continuous solution::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(v[0], max=5.5)
            sage: p.add_constraint(v[0], min=7.6)
            sage: p.set_objective(v[0])

        Tests of GLPK\'s Exceptions::

            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: Problem has no feasible solution

        No integer solution::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(v[0], max=5.6)
            sage: p.add_constraint(v[0], min=5.2)
            sage: p.set_objective(v[0])
            sage: p.set_integer(v)

        Tests of GLPK\'s Exceptions::

            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: Problem has no feasible solution
    '''

class MIPVariable(sage.sets.family.FiniteFamily):
    """MIPVariable(mip, vtype, name='', lower_bound=0, upper_bound=None, indices=None)

    File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3222)

    ``MIPVariable`` is a variable used by the class
    ``MixedIntegerLinearProgram``.

    .. WARNING::

        You should not instantiate this class directly. Instead, use
        :meth:`MixedIntegerLinearProgram.new_variable`."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, mip, vtype, name=..., lower_bound=..., upper_bound=..., indices=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3232)

                Constructor for ``MIPVariable``.

                INPUT:

                - ``parent`` -- :class:`MIPVariableParent`; the parent of the
                  MIP variable

                - ``mip`` -- :class:`MixedIntegerLinearProgram`; the
                  underlying linear program

                - ``vtype`` -- integer; defines the type of the variables
                  (default: ``REAL``, i.e., ``vtype=-1``)

                - ``name`` -- a name for the ``MIPVariable``

                - ``lower_bound``, ``upper_bound`` -- lower bound and upper
                  bound on the variable. Set to ``None`` to indicate that the
                  variable is unbounded.

                - ``indices`` -- (optional) an iterable of keys; components
                  corresponding to these keys are created in order,
                  and access to components with other keys will raise an
                  error; otherwise components of this variable can be
                  indexed by arbitrary keys and are created dynamically
                  on access

                For more information, see the method
                ``MixedIntegerLinearProgram.new_variable``.

                EXAMPLES::

                    sage: p = MixedIntegerLinearProgram(solver='GLPK')
                    sage: p.new_variable(nonnegative=True)
                    MIPVariable with 0 real components, >= 0
        """
    @overload
    def copy_for_mip(self, mip) -> Any:
        """MIPVariable.copy_for_mip(self, mip)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3400)

        Return a copy of ``self`` suitable for a new :class:`MixedIntegerLinearProgram`
        instance ``mip``.

        For this to make sense, ``mip`` should have been obtained as a copy of
        ``self.mip()``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: pv = p.new_variable(nonnegative=True)
            sage: pv[0]
            x_0
            sage: q = copy(p)
            sage: qv = pv.copy_for_mip(q)
            sage: pv[77]
            x_1
            sage: p.number_of_variables()
            2
            sage: q.number_of_variables()
            1
            sage: qv[33]
            x_1
            sage: p.number_of_variables()
            2
            sage: q.number_of_variables()
            2

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: pv = p.new_variable(indices=[3, 7])
            sage: q = copy(p)
            sage: qv = pv.copy_for_mip(q)
            sage: qv[3]
            x_0
            sage: qv[5]
            Traceback (most recent call last):
            ...
            IndexError: 5 does not index a component of MIPVariable with 2 real components"""
    @overload
    def copy_for_mip(self, q) -> Any:
        """MIPVariable.copy_for_mip(self, mip)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3400)

        Return a copy of ``self`` suitable for a new :class:`MixedIntegerLinearProgram`
        instance ``mip``.

        For this to make sense, ``mip`` should have been obtained as a copy of
        ``self.mip()``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: pv = p.new_variable(nonnegative=True)
            sage: pv[0]
            x_0
            sage: q = copy(p)
            sage: qv = pv.copy_for_mip(q)
            sage: pv[77]
            x_1
            sage: p.number_of_variables()
            2
            sage: q.number_of_variables()
            1
            sage: qv[33]
            x_1
            sage: p.number_of_variables()
            2
            sage: q.number_of_variables()
            2

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: pv = p.new_variable(indices=[3, 7])
            sage: q = copy(p)
            sage: qv = pv.copy_for_mip(q)
            sage: qv[3]
            x_0
            sage: qv[5]
            Traceback (most recent call last):
            ...
            IndexError: 5 does not index a component of MIPVariable with 2 real components"""
    @overload
    def copy_for_mip(self, q) -> Any:
        """MIPVariable.copy_for_mip(self, mip)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3400)

        Return a copy of ``self`` suitable for a new :class:`MixedIntegerLinearProgram`
        instance ``mip``.

        For this to make sense, ``mip`` should have been obtained as a copy of
        ``self.mip()``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: pv = p.new_variable(nonnegative=True)
            sage: pv[0]
            x_0
            sage: q = copy(p)
            sage: qv = pv.copy_for_mip(q)
            sage: pv[77]
            x_1
            sage: p.number_of_variables()
            2
            sage: q.number_of_variables()
            1
            sage: qv[33]
            x_1
            sage: p.number_of_variables()
            2
            sage: q.number_of_variables()
            2

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: pv = p.new_variable(indices=[3, 7])
            sage: q = copy(p)
            sage: qv = pv.copy_for_mip(q)
            sage: qv[3]
            x_0
            sage: qv[5]
            Traceback (most recent call last):
            ...
            IndexError: 5 does not index a component of MIPVariable with 2 real components"""
    @overload
    def items(self) -> Any:
        """MIPVariable.items(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3573)

        Return the pairs (keys, value) contained in the dictionary.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.items())
            [(0, x_0), (1, x_1)]"""
    @overload
    def items(self) -> Any:
        """MIPVariable.items(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3573)

        Return the pairs (keys, value) contained in the dictionary.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.items())
            [(0, x_0), (1, x_1)]"""
    @overload
    def keys(self) -> Any:
        """MIPVariable.keys(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3559)

        Return the keys already defined in the dictionary.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.keys())
            [0, 1]"""
    @overload
    def keys(self) -> Any:
        """MIPVariable.keys(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3559)

        Return the keys already defined in the dictionary.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.keys())
            [0, 1]"""
    @overload
    def mip(self) -> Any:
        """MIPVariable.mip(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3601)

        Return the :class:`MixedIntegerLinearProgram` in which ``self`` is a variable.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p == v.mip()
            True"""
    @overload
    def mip(self) -> Any:
        """MIPVariable.mip(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3601)

        Return the :class:`MixedIntegerLinearProgram` in which ``self`` is a variable.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p == v.mip()
            True"""
    def set_max(self, max) -> Any:
        """MIPVariable.set_max(self, max)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3484)

        Set an upper bound on the variable.

        INPUT:

        - ``max`` -- an upper bound, or ``None`` to mean that the variable is
          unbounded

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(real=True, nonnegative=True)
            sage: p.get_max(v)
            sage: p.get_max(v[0])
            sage: p.set_max(v,4)
            sage: p.get_max(v)
            4
            sage: p.get_max(v[0])
            4.0

        TESTS:

        Test that :issue:`20462` is fixed::

            sage: p.<x,y> = MixedIntegerLinearProgram()
            sage: x[0], y[0]
            (x_0, x_1)
            sage: x.set_max(42)
            sage: p.get_max(y[0]) is None
            True"""
    def set_min(self, min) -> Any:
        """MIPVariable.set_min(self, min)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3446)

        Set a lower bound on the variable.

        INPUT:

        - ``min`` -- a lower bound, or ``None`` to mean that the variable is
          unbounded

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(real=True, nonnegative=True)
            sage: p.get_min(v)
            0
            sage: p.get_min(v[0])
            0.0
            sage: p.set_min(v,4)
            sage: p.get_min(v)
            4
            sage: p.get_min(v[0])
            4.0

        TESTS:

        Test that :issue:`20462` is fixed::

            sage: p.<x,y> = MixedIntegerLinearProgram()
            sage: x[0], y[0]
            (x_0, x_1)
            sage: x.set_min(42)
            sage: p.get_min(y[0]) is None
            True"""
    @overload
    def values(self) -> Any:
        """MIPVariable.values(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3587)

        Return the symbolic variables associated to the current dictionary.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.values(), key=str)
            [x_0, x_1]"""
    @overload
    def values(self) -> Any:
        """MIPVariable.values(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3587)

        Return the symbolic variables associated to the current dictionary.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[0] + v[1])
            sage: sorted(v.values(), key=str)
            [x_0, x_1]"""
    def __copy__(self) -> Any:
        """MIPVariable.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3281)

        Return a copy of ``self``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: pv = p.new_variable(nonnegative=True)
            sage: pv[0]
            x_0
            sage: pvc = copy(pv)
            sage: pvc[0]
            x_0
            sage: pv[1]
            x_1
            sage: pvc[1]
            x_2
            sage: p.number_of_variables()
            3"""
    def __deepcopy__(self, memo=...) -> Any:
        """MIPVariable.__deepcopy__(self, memo={})

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3303)

        Return a copy of ``self``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: pv = p.new_variable(nonnegative=True)
            sage: pv[0]
            x_0
            sage: pvc = deepcopy(pv)
            sage: pvc[0]
            x_0
            sage: pv[1]
            x_1
            sage: pvc[1]
            x_2
            sage: p.number_of_variables()
            3"""
    def __getitem__(self, i) -> Any:
        """MIPVariable.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3325)

        Return the variable component corresponding to the key.

        Returns the component asked.

        Otherwise, if ``self`` was created with indices=None,
        creates the component.

        EXAMPLES:

        Dynamic indices::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[0] + v[1])
            sage: v[0]
            x_0

        Static indices::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable(indices=range(7))
            sage: p.number_of_variables()
            7
            sage: x[3]
            x_3
            sage: x[11]
            Traceback (most recent call last):
            ...
            IndexError: 11 does not index a component of MIPVariable with 7 real components

        Indices can be more than just integers::

            sage: p = MixedIntegerLinearProgram()
            sage: indices = ( (i,j) for i in range(6) for j in range(4) )
            sage: x = p.new_variable(indices=indices)
            sage: p.number_of_variables()
            24
            sage: x[(2, 3)]
            x_11

        TESTS:

        An empty list of static indices gives an error on every component access;
        it is different from passing ``indices=None`` (the default) on init. ::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable(indices=[])
            sage: x[0]
            Traceback (most recent call last):
            ...
            IndexError: 0 does not index a component of MIPVariable with 0 real components"""
    def __mul__(self, left, right) -> Any:
        """MIPVariable.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3614)

        Multiply ``left`` with ``right``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable()
            sage: m = matrix([[1,2], [3,4]])
            sage: v * m
            (1.0, 2.0)*x_0 + (3.0, 4.0)*x_1
            sage: m * v
            (1.0, 3.0)*x_0 + (2.0, 4.0)*x_1

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: v = p.new_variable()
            sage: m = matrix([[1,1/2], [2/3,3/4]])
            sage: v * m
            (1, 1/2)*x_0 + (2/3, 3/4)*x_1
            sage: m * v
            (1, 2/3)*x_0 + (1/2, 3/4)*x_1

            sage: c = vector([1, 2])
            sage: v * c
            x_0 + 2*x_1
            sage: c * v
            x_0 + 2*x_1"""
    def __rmul__(self, other):
        """Return value*self."""

class MixedIntegerLinearProgram(sage.structure.sage_object.SageObject):
    '''MixedIntegerLinearProgram(solver=None, maximization=True, constraint_generation=False, check_redundant=False, names=tuple(), base_ring=None)

    File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 267)

    The ``MixedIntegerLinearProgram`` class is the link between Sage, linear
    programming (LP) and mixed integer programming (MIP) solvers.

    A Mixed Integer Linear Program (MILP) consists of variables, linear
    constraints on these variables, and an objective function which is to be
    maximised or minimised under these constraints.

    See the thematic tutorial on `Linear Programming (Mixed Integer)
    <../../../../thematic_tutorials/linear_programming.html>`_
    or :wikipedia:`Linear_programming` for further information on linear
    programming, and the :mod:`MILP module <sage.numerical.mip>` for its use in
    Sage.

    INPUT:

    - ``solver`` -- selects a solver; see `Solvers (backends)
      <../../../../thematic_tutorials/linear_programming.html#solvers-backends>`_
      for more information and installation instructions for optional
      solvers.

      - ``solver="GLPK"``: the `GNU Linear Programming Kit
        <http://www.gnu.org/software/glpk/>`_.

      - ``solver="GLPK/exact"``: GLPK\'s implementation of an exact rational simplex
        method.

      - ``solver="Coin"``: the `COIN-OR CBC (COIN Branch and Cut) solver
        <http://www.coin-or.org>`_.

      - ``solver="CPLEX"``: provided by the proprietary `IBM ILOG CPLEX
        Optimization Studio <https://www.ibm.com/products/ilog-cplex-optimization-studio/>`_.

      - ``solver="Gurobi"``: the proprietary `Gurobi solver <http://www.gurobi.com/>`_.

      - ``solver="CVXOPT"``: see the `CVXOPT <http://www.cvxopt.org/>`_ web site.

      - ``solver="PPL"``: an exact rational solver (for small scale instances)
        provided by the `Parma Polyhedra Library (PPL) <http://bugseng.com/products/ppl>`_.

      - ``solver="InteractiveLP"``: a didactical
        implementation of the revised simplex method in Sage.  It works over
        any exact ordered field, the default is ``QQ``.

      - If ``solver=None`` (default), the default solver is used (see
        :func:`default_mip_solver`).

      - ``solver`` can also be a callable (such as a class),
        see :func:`sage.numerical.backends.generic_backend.get_solver` for
        examples.

    - ``maximization``

      - When set to ``True`` (default), the ``MixedIntegerLinearProgram``
        is defined as a maximization.

      - When set to ``False``, the ``MixedIntegerLinearProgram`` is
        defined as a minimization.

    - ``constraint_generation`` -- only used when ``solver=None``

      - When set to ``True``, after solving the ``MixedIntegerLinearProgram``,
        it is possible to add a constraint, and then solve it again.
        The effect is that solvers that do not support this feature will not be
        used.

      - Defaults to ``False``.

    .. SEEALSO::

     - :func:`default_mip_solver` -- returns/sets the default MIP solver

    EXAMPLES:

    Computation of a maximum stable set in Petersen\'s graph::

         sage: # needs sage.graphs
         sage: g = graphs.PetersenGraph()
         sage: p = MixedIntegerLinearProgram(maximization=True, solver=\'GLPK\')
         sage: b = p.new_variable(binary=True)
         sage: p.set_objective(sum([b[v] for v in g]))
         sage: for (u,v) in g.edges(sort=False, labels=None):
         ....:     p.add_constraint(b[u] + b[v], max=1)
         sage: p.solve(objective_only=True)
         4.0

    TESTS:

    Check that :issue:`16497` is fixed::

        sage: for type in ["binary", "integer"]:
        ....:     k = 3
        ....:     items = [1/5, 1/3, 2/3, 3/4, 5/7]
        ....:     maximum = 1
        ....:     p = MixedIntegerLinearProgram(solver=\'GLPK\')
        ....:     box = p.new_variable(nonnegative=True, **{type: True})
        ....:     for b in range(k):
        ....:         p.add_constraint(p.sum([items[i]*box[i,b] for i in range(len(items))]) <= maximum)
        ....:     for i in range(len(items)):
        ....:         p.add_constraint(p.sum([box[i,b] for b in range(k)]) == 1)
        ....:     p.set_objective(None)
        ....:     _ = p.solve()
        ....:     box = p.get_values(box)
        ....:     print(all(v in ZZ for v in box.values()))
        True
        True'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, solver=..., maximization=..., constraint_generation=..., check_redundant=..., names=..., base_ring=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 376)

                Constructor for the ``MixedIntegerLinearProgram`` class.

                INPUT:

                - ``solver`` -- one of the following:

                  - a string indicating one of the available solvers
                    (see :class:`MixedIntegerLinearProgram`)

                  - ``None`` -- (default) the default solver is used, see
                    :func:`default_mip_solver`

                  - or a callable (such as a class), see
                    :func:`sage.numerical.backends.generic_backend.get_solver`
                    for examples

                - ``maximization``

                  - When set to ``True`` (default), the ``MixedIntegerLinearProgram``
                    is defined as a maximization.
                  - When set to ``False``, the ``MixedIntegerLinearProgram`` is
                    defined as a minimization.

                - ``constraint_generation`` -- only used when ``solver=None``:

                  - When set to ``True``, after solving the
                    ``MixedIntegerLinearProgram``, it is possible to add a constraint,
                    and then solve it again. The effect is that solvers that do not
                    support this feature will not be used.

                  - Defaults to ``False``.

                - ``check_redundant`` -- whether to check that constraints added to the
                  program are redundant with constraints already in the program.
                  Only obvious redundancies are checked: to be considered redundant,
                  either a constraint is equal to another constraint in the program,
                  or it is a constant multiple of the other. To make this search
                  effective and efficient, constraints are normalized; thus, the
                  constraint `-x_1 < 0` will be stored as `x_1 > 0`.

                - ``names`` -- list/tuple/iterable of string. Default names of
                  the MIP variables. Used to enable the ``MIP.<x> =
                  MixedIntegerLinearProgram()`` syntax.

                .. SEEALSO::

                - :meth:`default_mip_solver` -- returns/sets the default MIP solver

                EXAMPLES::

                    sage: p = MixedIntegerLinearProgram(maximization=True)

                TESTS:

                Checks that the objects are deallocated without invoking the cyclic garbage
                collector (cf. :issue:`12616`)::

                    sage: del p
                    sage: def just_create_variables():
                    ....:     p = MixedIntegerLinearProgram(solver='GLPK')
                    ....:     b = p.new_variable(nonnegative=True)
                    ....:     p.add_constraint(b[3] + b[6] <= 2)
                    ....:     p.solve()
                    sage: C = sage.numerical.mip.MixedIntegerLinearProgram
                    sage: import gc
                    sage: _ = gc.collect()  # avoid side effects of other doc tests
                    sage: sum([1 for x in gc.get_objects() if isinstance(x,C)])
                    0

                We now disable the cyclic garbage collector. Since :issue:`12616` avoids
                a reference cycle, the mixed integer linear program created in
                ``just_create_variables()`` is removed even without the cyclic garbage
                collection::

                    sage: gc.disable()
                    sage: just_create_variables()
                    sage: sum([1 for x in gc.get_objects() if isinstance(x,C)])
                    0
                    sage: gc.enable()
        """
    @overload
    def add_constraint(self, linear_function, max=..., min=..., name=..., return_indices=...) -> Any:
        """MixedIntegerLinearProgram.add_constraint(self, linear_function, max=None, min=None, name=None, return_indices=False)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1873)

        Add a constraint to the ``MixedIntegerLinearProgram``.

        INPUT:

        - ``linear_function`` -- four different types of arguments are
          admissible:

            - A linear function. In this case, one of the arguments
              ``min`` or ``max`` has to be specified.

            - A linear constraint of the form ``A <= B``, ``A >= B``,
              ``A <= B <= C``, ``A >= B >= C`` or ``A == B``.

            - A vector-valued linear function, see
              :mod:`~sage.numerical.linear_tensor`. In this case, one
              of the arguments ``min`` or ``max`` has to be specified.

            - An (in)equality of vector-valued linear functions, that
              is, elements of the space of linear functions tensored
              with a vector space. See
              :mod:`~sage.numerical.linear_tensor_constraints` for
              details.

        - ``max`` -- constant or ``None`` (default). An upper bound on
          the linear function. This must be a numerical value for
          scalar linear functions, or a vector for vector-valued
          linear functions. Not allowed if the ``linear_function``
          argument is a symbolic (in)-equality.

        - ``min`` -- constant or ``None`` (default). A lower bound on
          the linear function. This must be a numerical value for
          scalar linear functions, or a vector for vector-valued
          linear functions. Not allowed if the ``linear_function``
          argument is a symbolic (in)-equality.

        - ``name`` -- a name for the constraint

        - ``return_indices`` -- boolean (default: ``False``),
          whether to return the indices of the added constraints

        OUTPUT:

        The row indices of the constraints added, if
        ``return_indices`` is true and the backend guarantees that
        removing them again yields the original MIP, ``None``
        otherwise.

        To set a lower and/or upper bound on the variables use the methods
        ``set_min`` and/or ``set_max`` of ``MixedIntegerLinearProgram``.

        EXAMPLES:

        Consider the following linear program::

            Maximize:
              x + 5 * y
            Constraints:
              x + 0.2 y       <= 4
              1.5 * x + 3 * y <= 4
            Variables:
              x is Real (min = 0, max = None)
              y is Real (min = 0, max = None)

        It can be solved as follows::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(x[0] + 0.2*x[1], max=4)
            sage: p.add_constraint(1.5*x[0] + 3*x[1], max=4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        There are two different ways to add the constraint
        ``x[5] + 3*x[7] <= x[6] + 3`` to a ``MixedIntegerLinearProgram``.

        The first one consists in giving ``add_constraint`` this
        very expression::

            sage: p.add_constraint(x[5] + 3*x[7] <= x[6] + 3)

        The second (slightly more efficient) one is to use the
        arguments ``min`` or ``max``, which can only be numerical
        values::

            sage: p.add_constraint(x[5] + 3*x[7] - x[6], max=3)

        One can also define double-bounds or equality using symbols
        ``<=``, ``>=`` and ``==``::

            sage: p.add_constraint(x[5] + 3*x[7] == x[6] + 3)
            sage: p.add_constraint(x[5] + 3*x[7] <= x[6] + 3 <= x[8] + 27)

        Using this notation, the previous program can be written as::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(x[0] + 0.2*x[1] <= 4)
            sage: p.add_constraint(1.5*x[0] + 3*x[1] <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        The two constraints can also be combined into a single
        vector-valued constraint::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: f_vec = vector([1, 1.5]) * x[0] + vector([0.2, 3]) * x[1];  f_vec
            (1.0, 1.5)*x_0 + (0.2, 3.0)*x_1
            sage: p.add_constraint(f_vec, max=vector([4, 4]))
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        Instead of specifying the maximum in the optional ``max``
        argument, we can also use (in)equality notation for
        vector-valued linear functions::

            sage: f_vec <= 4    # constant rhs becomes vector
            (1.0, 1.5)*x_0 + (0.2, 3.0)*x_1 <= (4.0, 4.0)
            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(f_vec <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        Finally, one can use the matrix * :class:`MIPVariable`
        notation to write vector-valued linear functions::

            sage: m = matrix([[1.0, 0.2], [1.5, 3.0]]);  m
            [ 1.00000000000000 0.200000000000000]
            [ 1.50000000000000  3.00000000000000]
            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(m * x <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        TESTS:

        Complex constraints::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: b = p.new_variable(nonnegative=True)
            sage: p.add_constraint(b[8] - b[15] <= 3*b[8] + 9)
            sage: p.show()
            Constraints:
              -2.0 x_0 - x_1 <= 9.0
            Variables:
              x_0 is a continuous variable (min=0.0, max=+oo)
              x_1 is a continuous variable (min=0.0, max=+oo)

        Trivially true empty constraint:

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(sum([]), max=2)
            sage: p.solve()
            0.0

        Infeasible empty constraint::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(sum([]), min=2)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: Problem has no feasible solution

        Min/Max are numerical ::

            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(v[3] + v[5], min = v[6])
            Traceback (most recent call last):
            ...
            ValueError: min and max arguments are required to be constants
            sage: p.add_constraint(v[3] + v[5], max = v[6])
            Traceback (most recent call last):
            ...
            ValueError: min and max arguments are required to be constants

        Do not add redundant elements (notice only one copy of each constraint is added)::

            sage: lp = MixedIntegerLinearProgram(solver='GLPK', check_redundant=True)
            sage: for each in range(10):
            ....:     lp.add_constraint(lp[0]-lp[1], min=1)
            sage: lp.show()
            Constraints:
              1.0 <= x_0 - x_1
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)

        We check for constant multiples of constraints as well::

            sage: for each in range(10):
            ....:     lp.add_constraint(2*lp[0] - 2*lp[1], min=2)
            sage: lp.show()
            Constraints:
              1.0 <= x_0 - x_1
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)

        But if the constant multiple is negative, we should add it anyway (once)::

              sage: for each in range(10):
              ....:     lp.add_constraint(-2*lp[0] + 2*lp[1], min=-2)
              sage: lp.show()
              Constraints:
                1.0 <= x_0 - x_1
                -2.0 <= -2.0 x_0 + 2.0 x_1
              Variables:
                x_0 is a continuous variable (min=-oo, max=+oo)
                x_1 is a continuous variable (min=-oo, max=+oo)

        Catch ``True`` / ``False`` as INPUT (:issue:`13646`)::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(True)
            Traceback (most recent call last):
            ...
            ValueError: argument must be a linear function or constraint, got True

        Check that adding and removing constraints works::

            sage: p = MixedIntegerLinearProgram(check_redundant=True)
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0] + x[1] <= 3)
            sage: p.set_objective(x[0] + 2*x[1])
            sage: p.solve()
            6.0

        We add (non-trivially) redundant constraints::

            sage: c1 = p.add_constraint(0 <= x[0] <= 3, return_indices=True); c1
            [1, 2]
            sage: p.solve()
            6.0

        We add a non-redundant constraint::

            sage: c2 = p.add_constraint(1 <= x[1] <= 2, return_indices=True); c2
            [3, 4]
            sage: p.solve()
            5.0

        We remove the redundant constraints `1` and `2`, keep in mind
        that indices change when removing constraints::

            sage: p.remove_constraint(1)
            sage: p.remove_constraint(1)
            sage: p.solve()
            5.0

        We remove another constraint::

            sage: p.remove_constraint(2)
            sage: p.solve()
            6.0"""
    @overload
    def add_constraint(self, f_vec, max=...) -> Any:
        """MixedIntegerLinearProgram.add_constraint(self, linear_function, max=None, min=None, name=None, return_indices=False)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1873)

        Add a constraint to the ``MixedIntegerLinearProgram``.

        INPUT:

        - ``linear_function`` -- four different types of arguments are
          admissible:

            - A linear function. In this case, one of the arguments
              ``min`` or ``max`` has to be specified.

            - A linear constraint of the form ``A <= B``, ``A >= B``,
              ``A <= B <= C``, ``A >= B >= C`` or ``A == B``.

            - A vector-valued linear function, see
              :mod:`~sage.numerical.linear_tensor`. In this case, one
              of the arguments ``min`` or ``max`` has to be specified.

            - An (in)equality of vector-valued linear functions, that
              is, elements of the space of linear functions tensored
              with a vector space. See
              :mod:`~sage.numerical.linear_tensor_constraints` for
              details.

        - ``max`` -- constant or ``None`` (default). An upper bound on
          the linear function. This must be a numerical value for
          scalar linear functions, or a vector for vector-valued
          linear functions. Not allowed if the ``linear_function``
          argument is a symbolic (in)-equality.

        - ``min`` -- constant or ``None`` (default). A lower bound on
          the linear function. This must be a numerical value for
          scalar linear functions, or a vector for vector-valued
          linear functions. Not allowed if the ``linear_function``
          argument is a symbolic (in)-equality.

        - ``name`` -- a name for the constraint

        - ``return_indices`` -- boolean (default: ``False``),
          whether to return the indices of the added constraints

        OUTPUT:

        The row indices of the constraints added, if
        ``return_indices`` is true and the backend guarantees that
        removing them again yields the original MIP, ``None``
        otherwise.

        To set a lower and/or upper bound on the variables use the methods
        ``set_min`` and/or ``set_max`` of ``MixedIntegerLinearProgram``.

        EXAMPLES:

        Consider the following linear program::

            Maximize:
              x + 5 * y
            Constraints:
              x + 0.2 y       <= 4
              1.5 * x + 3 * y <= 4
            Variables:
              x is Real (min = 0, max = None)
              y is Real (min = 0, max = None)

        It can be solved as follows::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(x[0] + 0.2*x[1], max=4)
            sage: p.add_constraint(1.5*x[0] + 3*x[1], max=4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        There are two different ways to add the constraint
        ``x[5] + 3*x[7] <= x[6] + 3`` to a ``MixedIntegerLinearProgram``.

        The first one consists in giving ``add_constraint`` this
        very expression::

            sage: p.add_constraint(x[5] + 3*x[7] <= x[6] + 3)

        The second (slightly more efficient) one is to use the
        arguments ``min`` or ``max``, which can only be numerical
        values::

            sage: p.add_constraint(x[5] + 3*x[7] - x[6], max=3)

        One can also define double-bounds or equality using symbols
        ``<=``, ``>=`` and ``==``::

            sage: p.add_constraint(x[5] + 3*x[7] == x[6] + 3)
            sage: p.add_constraint(x[5] + 3*x[7] <= x[6] + 3 <= x[8] + 27)

        Using this notation, the previous program can be written as::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(x[0] + 0.2*x[1] <= 4)
            sage: p.add_constraint(1.5*x[0] + 3*x[1] <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        The two constraints can also be combined into a single
        vector-valued constraint::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: f_vec = vector([1, 1.5]) * x[0] + vector([0.2, 3]) * x[1];  f_vec
            (1.0, 1.5)*x_0 + (0.2, 3.0)*x_1
            sage: p.add_constraint(f_vec, max=vector([4, 4]))
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        Instead of specifying the maximum in the optional ``max``
        argument, we can also use (in)equality notation for
        vector-valued linear functions::

            sage: f_vec <= 4    # constant rhs becomes vector
            (1.0, 1.5)*x_0 + (0.2, 3.0)*x_1 <= (4.0, 4.0)
            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(f_vec <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        Finally, one can use the matrix * :class:`MIPVariable`
        notation to write vector-valued linear functions::

            sage: m = matrix([[1.0, 0.2], [1.5, 3.0]]);  m
            [ 1.00000000000000 0.200000000000000]
            [ 1.50000000000000  3.00000000000000]
            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(m * x <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        TESTS:

        Complex constraints::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: b = p.new_variable(nonnegative=True)
            sage: p.add_constraint(b[8] - b[15] <= 3*b[8] + 9)
            sage: p.show()
            Constraints:
              -2.0 x_0 - x_1 <= 9.0
            Variables:
              x_0 is a continuous variable (min=0.0, max=+oo)
              x_1 is a continuous variable (min=0.0, max=+oo)

        Trivially true empty constraint:

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(sum([]), max=2)
            sage: p.solve()
            0.0

        Infeasible empty constraint::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(sum([]), min=2)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: Problem has no feasible solution

        Min/Max are numerical ::

            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(v[3] + v[5], min = v[6])
            Traceback (most recent call last):
            ...
            ValueError: min and max arguments are required to be constants
            sage: p.add_constraint(v[3] + v[5], max = v[6])
            Traceback (most recent call last):
            ...
            ValueError: min and max arguments are required to be constants

        Do not add redundant elements (notice only one copy of each constraint is added)::

            sage: lp = MixedIntegerLinearProgram(solver='GLPK', check_redundant=True)
            sage: for each in range(10):
            ....:     lp.add_constraint(lp[0]-lp[1], min=1)
            sage: lp.show()
            Constraints:
              1.0 <= x_0 - x_1
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)

        We check for constant multiples of constraints as well::

            sage: for each in range(10):
            ....:     lp.add_constraint(2*lp[0] - 2*lp[1], min=2)
            sage: lp.show()
            Constraints:
              1.0 <= x_0 - x_1
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)

        But if the constant multiple is negative, we should add it anyway (once)::

              sage: for each in range(10):
              ....:     lp.add_constraint(-2*lp[0] + 2*lp[1], min=-2)
              sage: lp.show()
              Constraints:
                1.0 <= x_0 - x_1
                -2.0 <= -2.0 x_0 + 2.0 x_1
              Variables:
                x_0 is a continuous variable (min=-oo, max=+oo)
                x_1 is a continuous variable (min=-oo, max=+oo)

        Catch ``True`` / ``False`` as INPUT (:issue:`13646`)::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(True)
            Traceback (most recent call last):
            ...
            ValueError: argument must be a linear function or constraint, got True

        Check that adding and removing constraints works::

            sage: p = MixedIntegerLinearProgram(check_redundant=True)
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0] + x[1] <= 3)
            sage: p.set_objective(x[0] + 2*x[1])
            sage: p.solve()
            6.0

        We add (non-trivially) redundant constraints::

            sage: c1 = p.add_constraint(0 <= x[0] <= 3, return_indices=True); c1
            [1, 2]
            sage: p.solve()
            6.0

        We add a non-redundant constraint::

            sage: c2 = p.add_constraint(1 <= x[1] <= 2, return_indices=True); c2
            [3, 4]
            sage: p.solve()
            5.0

        We remove the redundant constraints `1` and `2`, keep in mind
        that indices change when removing constraints::

            sage: p.remove_constraint(1)
            sage: p.remove_constraint(1)
            sage: p.solve()
            5.0

        We remove another constraint::

            sage: p.remove_constraint(2)
            sage: p.solve()
            6.0"""
    @overload
    def add_constraint(self, _True) -> Any:
        """MixedIntegerLinearProgram.add_constraint(self, linear_function, max=None, min=None, name=None, return_indices=False)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1873)

        Add a constraint to the ``MixedIntegerLinearProgram``.

        INPUT:

        - ``linear_function`` -- four different types of arguments are
          admissible:

            - A linear function. In this case, one of the arguments
              ``min`` or ``max`` has to be specified.

            - A linear constraint of the form ``A <= B``, ``A >= B``,
              ``A <= B <= C``, ``A >= B >= C`` or ``A == B``.

            - A vector-valued linear function, see
              :mod:`~sage.numerical.linear_tensor`. In this case, one
              of the arguments ``min`` or ``max`` has to be specified.

            - An (in)equality of vector-valued linear functions, that
              is, elements of the space of linear functions tensored
              with a vector space. See
              :mod:`~sage.numerical.linear_tensor_constraints` for
              details.

        - ``max`` -- constant or ``None`` (default). An upper bound on
          the linear function. This must be a numerical value for
          scalar linear functions, or a vector for vector-valued
          linear functions. Not allowed if the ``linear_function``
          argument is a symbolic (in)-equality.

        - ``min`` -- constant or ``None`` (default). A lower bound on
          the linear function. This must be a numerical value for
          scalar linear functions, or a vector for vector-valued
          linear functions. Not allowed if the ``linear_function``
          argument is a symbolic (in)-equality.

        - ``name`` -- a name for the constraint

        - ``return_indices`` -- boolean (default: ``False``),
          whether to return the indices of the added constraints

        OUTPUT:

        The row indices of the constraints added, if
        ``return_indices`` is true and the backend guarantees that
        removing them again yields the original MIP, ``None``
        otherwise.

        To set a lower and/or upper bound on the variables use the methods
        ``set_min`` and/or ``set_max`` of ``MixedIntegerLinearProgram``.

        EXAMPLES:

        Consider the following linear program::

            Maximize:
              x + 5 * y
            Constraints:
              x + 0.2 y       <= 4
              1.5 * x + 3 * y <= 4
            Variables:
              x is Real (min = 0, max = None)
              y is Real (min = 0, max = None)

        It can be solved as follows::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(x[0] + 0.2*x[1], max=4)
            sage: p.add_constraint(1.5*x[0] + 3*x[1], max=4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        There are two different ways to add the constraint
        ``x[5] + 3*x[7] <= x[6] + 3`` to a ``MixedIntegerLinearProgram``.

        The first one consists in giving ``add_constraint`` this
        very expression::

            sage: p.add_constraint(x[5] + 3*x[7] <= x[6] + 3)

        The second (slightly more efficient) one is to use the
        arguments ``min`` or ``max``, which can only be numerical
        values::

            sage: p.add_constraint(x[5] + 3*x[7] - x[6], max=3)

        One can also define double-bounds or equality using symbols
        ``<=``, ``>=`` and ``==``::

            sage: p.add_constraint(x[5] + 3*x[7] == x[6] + 3)
            sage: p.add_constraint(x[5] + 3*x[7] <= x[6] + 3 <= x[8] + 27)

        Using this notation, the previous program can be written as::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(x[0] + 0.2*x[1] <= 4)
            sage: p.add_constraint(1.5*x[0] + 3*x[1] <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        The two constraints can also be combined into a single
        vector-valued constraint::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: f_vec = vector([1, 1.5]) * x[0] + vector([0.2, 3]) * x[1];  f_vec
            (1.0, 1.5)*x_0 + (0.2, 3.0)*x_1
            sage: p.add_constraint(f_vec, max=vector([4, 4]))
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        Instead of specifying the maximum in the optional ``max``
        argument, we can also use (in)equality notation for
        vector-valued linear functions::

            sage: f_vec <= 4    # constant rhs becomes vector
            (1.0, 1.5)*x_0 + (0.2, 3.0)*x_1 <= (4.0, 4.0)
            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(f_vec <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        Finally, one can use the matrix * :class:`MIPVariable`
        notation to write vector-valued linear functions::

            sage: m = matrix([[1.0, 0.2], [1.5, 3.0]]);  m
            [ 1.00000000000000 0.200000000000000]
            [ 1.50000000000000  3.00000000000000]
            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 5*x[1])
            sage: p.add_constraint(m * x <= 4)
            sage: p.solve()     # rel tol 1e-15
            6.666666666666666

        TESTS:

        Complex constraints::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: b = p.new_variable(nonnegative=True)
            sage: p.add_constraint(b[8] - b[15] <= 3*b[8] + 9)
            sage: p.show()
            Constraints:
              -2.0 x_0 - x_1 <= 9.0
            Variables:
              x_0 is a continuous variable (min=0.0, max=+oo)
              x_1 is a continuous variable (min=0.0, max=+oo)

        Trivially true empty constraint:

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(sum([]), max=2)
            sage: p.solve()
            0.0

        Infeasible empty constraint::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(sum([]), min=2)
            sage: p.solve()
            Traceback (most recent call last):
            ...
            MIPSolverException: GLPK: Problem has no feasible solution

        Min/Max are numerical ::

            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(v[3] + v[5], min = v[6])
            Traceback (most recent call last):
            ...
            ValueError: min and max arguments are required to be constants
            sage: p.add_constraint(v[3] + v[5], max = v[6])
            Traceback (most recent call last):
            ...
            ValueError: min and max arguments are required to be constants

        Do not add redundant elements (notice only one copy of each constraint is added)::

            sage: lp = MixedIntegerLinearProgram(solver='GLPK', check_redundant=True)
            sage: for each in range(10):
            ....:     lp.add_constraint(lp[0]-lp[1], min=1)
            sage: lp.show()
            Constraints:
              1.0 <= x_0 - x_1
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)

        We check for constant multiples of constraints as well::

            sage: for each in range(10):
            ....:     lp.add_constraint(2*lp[0] - 2*lp[1], min=2)
            sage: lp.show()
            Constraints:
              1.0 <= x_0 - x_1
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)

        But if the constant multiple is negative, we should add it anyway (once)::

              sage: for each in range(10):
              ....:     lp.add_constraint(-2*lp[0] + 2*lp[1], min=-2)
              sage: lp.show()
              Constraints:
                1.0 <= x_0 - x_1
                -2.0 <= -2.0 x_0 + 2.0 x_1
              Variables:
                x_0 is a continuous variable (min=-oo, max=+oo)
                x_1 is a continuous variable (min=-oo, max=+oo)

        Catch ``True`` / ``False`` as INPUT (:issue:`13646`)::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(True)
            Traceback (most recent call last):
            ...
            ValueError: argument must be a linear function or constraint, got True

        Check that adding and removing constraints works::

            sage: p = MixedIntegerLinearProgram(check_redundant=True)
            sage: x = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0] + x[1] <= 3)
            sage: p.set_objective(x[0] + 2*x[1])
            sage: p.solve()
            6.0

        We add (non-trivially) redundant constraints::

            sage: c1 = p.add_constraint(0 <= x[0] <= 3, return_indices=True); c1
            [1, 2]
            sage: p.solve()
            6.0

        We add a non-redundant constraint::

            sage: c2 = p.add_constraint(1 <= x[1] <= 2, return_indices=True); c2
            [3, 4]
            sage: p.solve()
            5.0

        We remove the redundant constraints `1` and `2`, keep in mind
        that indices change when removing constraints::

            sage: p.remove_constraint(1)
            sage: p.remove_constraint(1)
            sage: p.solve()
            5.0

        We remove another constraint::

            sage: p.remove_constraint(2)
            sage: p.solve()
            6.0"""
    @overload
    def base_ring(self) -> Any:
        """MixedIntegerLinearProgram.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 672)

        Return the base ring.

        OUTPUT: a ring. The coefficients that the chosen solver supports

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.base_ring()
            Real Double Field
            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: p.base_ring()
            Rational Field
            sage: from sage.rings.qqbar import AA                                       # needs sage.rings.number_field
            sage: p = MixedIntegerLinearProgram(solver='InteractiveLP', base_ring=AA)   # needs sage.rings.number_field
            sage: p.base_ring()                                                         # needs sage.rings.number_field
            Algebraic Real Field

            sage: # needs sage.groups sage.rings.number_field
            sage: d = polytopes.dodecahedron()
            sage: p = MixedIntegerLinearProgram(base_ring=d.base_ring())
            sage: p.base_ring()
            Number Field in sqrt5 with defining polynomial x^2 - 5 with sqrt5 = 2.236067977499790?"""
    @overload
    def base_ring(self) -> Any:
        """MixedIntegerLinearProgram.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 672)

        Return the base ring.

        OUTPUT: a ring. The coefficients that the chosen solver supports

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.base_ring()
            Real Double Field
            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: p.base_ring()
            Rational Field
            sage: from sage.rings.qqbar import AA                                       # needs sage.rings.number_field
            sage: p = MixedIntegerLinearProgram(solver='InteractiveLP', base_ring=AA)   # needs sage.rings.number_field
            sage: p.base_ring()                                                         # needs sage.rings.number_field
            Algebraic Real Field

            sage: # needs sage.groups sage.rings.number_field
            sage: d = polytopes.dodecahedron()
            sage: p = MixedIntegerLinearProgram(base_ring=d.base_ring())
            sage: p.base_ring()
            Number Field in sqrt5 with defining polynomial x^2 - 5 with sqrt5 = 2.236067977499790?"""
    @overload
    def base_ring(self) -> Any:
        """MixedIntegerLinearProgram.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 672)

        Return the base ring.

        OUTPUT: a ring. The coefficients that the chosen solver supports

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.base_ring()
            Real Double Field
            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: p.base_ring()
            Rational Field
            sage: from sage.rings.qqbar import AA                                       # needs sage.rings.number_field
            sage: p = MixedIntegerLinearProgram(solver='InteractiveLP', base_ring=AA)   # needs sage.rings.number_field
            sage: p.base_ring()                                                         # needs sage.rings.number_field
            Algebraic Real Field

            sage: # needs sage.groups sage.rings.number_field
            sage: d = polytopes.dodecahedron()
            sage: p = MixedIntegerLinearProgram(base_ring=d.base_ring())
            sage: p.base_ring()
            Number Field in sqrt5 with defining polynomial x^2 - 5 with sqrt5 = 2.236067977499790?"""
    @overload
    def base_ring(self) -> Any:
        """MixedIntegerLinearProgram.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 672)

        Return the base ring.

        OUTPUT: a ring. The coefficients that the chosen solver supports

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.base_ring()
            Real Double Field
            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: p.base_ring()
            Rational Field
            sage: from sage.rings.qqbar import AA                                       # needs sage.rings.number_field
            sage: p = MixedIntegerLinearProgram(solver='InteractiveLP', base_ring=AA)   # needs sage.rings.number_field
            sage: p.base_ring()                                                         # needs sage.rings.number_field
            Algebraic Real Field

            sage: # needs sage.groups sage.rings.number_field
            sage: d = polytopes.dodecahedron()
            sage: p = MixedIntegerLinearProgram(base_ring=d.base_ring())
            sage: p.base_ring()
            Number Field in sqrt5 with defining polynomial x^2 - 5 with sqrt5 = 2.236067977499790?"""
    @overload
    def base_ring(self) -> Any:
        """MixedIntegerLinearProgram.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 672)

        Return the base ring.

        OUTPUT: a ring. The coefficients that the chosen solver supports

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.base_ring()
            Real Double Field
            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: p.base_ring()
            Rational Field
            sage: from sage.rings.qqbar import AA                                       # needs sage.rings.number_field
            sage: p = MixedIntegerLinearProgram(solver='InteractiveLP', base_ring=AA)   # needs sage.rings.number_field
            sage: p.base_ring()                                                         # needs sage.rings.number_field
            Algebraic Real Field

            sage: # needs sage.groups sage.rings.number_field
            sage: d = polytopes.dodecahedron()
            sage: p = MixedIntegerLinearProgram(base_ring=d.base_ring())
            sage: p.base_ring()
            Number Field in sqrt5 with defining polynomial x^2 - 5 with sqrt5 = 2.236067977499790?"""
    @overload
    def base_ring(self) -> Any:
        """MixedIntegerLinearProgram.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 672)

        Return the base ring.

        OUTPUT: a ring. The coefficients that the chosen solver supports

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.base_ring()
            Real Double Field
            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: p.base_ring()
            Rational Field
            sage: from sage.rings.qqbar import AA                                       # needs sage.rings.number_field
            sage: p = MixedIntegerLinearProgram(solver='InteractiveLP', base_ring=AA)   # needs sage.rings.number_field
            sage: p.base_ring()                                                         # needs sage.rings.number_field
            Algebraic Real Field

            sage: # needs sage.groups sage.rings.number_field
            sage: d = polytopes.dodecahedron()
            sage: p = MixedIntegerLinearProgram(base_ring=d.base_ring())
            sage: p.base_ring()
            Number Field in sqrt5 with defining polynomial x^2 - 5 with sqrt5 = 2.236067977499790?"""
    @overload
    def best_known_objective_bound(self) -> Any:
        '''MixedIntegerLinearProgram.best_known_objective_bound(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2956)

        Return the value of the currently best known bound.

        This method returns the current best upper (resp. lower) bound
        on the optimal value of the objective function in a
        maximization (resp. minimization) problem. It is equal to the
        output of :meth:`get_objective_value` if the MILP found an
        optimal solution, but it can differ if it was interrupted
        manually or after a time limit (cf :meth:`solver_parameter`).

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
            ....:     p.add_constraint(b[v] + p.sum(b[u] for u in g.neighbors(v)) <= 1)
            sage: p.add_constraint(b[v] == 1)  # Force an easy non-0 solution
            sage: p.solve() # rel tol 100
            1.0
            sage: p.best_known_objective_bound()  # random
            48.0'''
    @overload
    def best_known_objective_bound(self) -> Any:
        '''MixedIntegerLinearProgram.best_known_objective_bound(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2956)

        Return the value of the currently best known bound.

        This method returns the current best upper (resp. lower) bound
        on the optimal value of the objective function in a
        maximization (resp. minimization) problem. It is equal to the
        output of :meth:`get_objective_value` if the MILP found an
        optimal solution, but it can differ if it was interrupted
        manually or after a time limit (cf :meth:`solver_parameter`).

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
            ....:     p.add_constraint(b[v] + p.sum(b[u] for u in g.neighbors(v)) <= 1)
            sage: p.add_constraint(b[v] == 1)  # Force an easy non-0 solution
            sage: p.solve() # rel tol 100
            1.0
            sage: p.best_known_objective_bound()  # random
            48.0'''
    @overload
    def constraints(self, indices=...) -> Any:
        """MixedIntegerLinearProgram.constraints(self, indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 937)

        Return a list of constraints, as 3-tuples.

        INPUT:

        - ``indices`` -- select which constraint(s) to return

            - If ``indices = None``, the method returns the list of all the
              constraints.

            - If ``indices`` is an integer `i`, the method returns constraint
              `i`.

            - If ``indices`` is a list of integers, the method returns the list
              of the corresponding constraints.

        OUTPUT:

        Each constraint is returned as a triple ``lower_bound, (indices,
        coefficients), upper_bound``.  For each of those entries, the
        corresponding linear function is the one associating to variable
        ``indices[i]`` the coefficient ``coefficients[i]``, and `0` to all the
        others.

        ``lower_bound`` and ``upper_bound`` are numerical values.

        EXAMPLES:

        First, let us define a small LP::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.add_constraint(p[0] - 2*p[1], min=1)

        To obtain the list of all constraints::

            sage: p.constraints()          # not tested
            [(1.0, ([1, 0], [-1.0, 1.0]), 4.0), (1.0, ([2, 0], [-2.0, 1.0]), None)]

        Or constraint `0` only::

            sage: p.constraints(0)         # not tested
            (1.0, ([1, 0], [-1.0, 1.0]), 4.0)

        A list of constraints containing only `1`::

            sage: p.constraints([1])       # not tested
            [(1.0, ([2, 0], [-2.0, 1.0]), None)]

        TESTS:

        As the ordering of the variables in each constraint depends on the
        solver used, we define a short function reordering it before it is
        printed. The output would look the same without this function applied::

            sage: def reorder_constraint(lb, indcoef, ub):
            ....:    ind, coef = indcoef
            ....:    d = dict(zip(ind, coef))
            ....:    ind.sort()
            ....:    return (lb, (ind, [d[i] for i in ind]), ub)

        Running the examples from above, reordering applied::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.add_constraint(p[0] - 2*p[1], min=1)
            sage: sorted(reorder_constraint(*c) for c in p.constraints())
            [(1.0, ([0, 1], [1.0, -1.0]), 4.0), (1.0, ([0, 2], [1.0, -2.0]), None)]
            sage: reorder_constraint(*p.constraints(0))
            (1.0, ([0, 1], [1.0, -1.0]), 4.0)
            sage: sorted(reorder_constraint(*c) for c in p.constraints([1]))
            [(1.0, ([0, 2], [1.0, -2.0]), None)]"""
    @overload
    def constraints(self) -> Any:
        """MixedIntegerLinearProgram.constraints(self, indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 937)

        Return a list of constraints, as 3-tuples.

        INPUT:

        - ``indices`` -- select which constraint(s) to return

            - If ``indices = None``, the method returns the list of all the
              constraints.

            - If ``indices`` is an integer `i`, the method returns constraint
              `i`.

            - If ``indices`` is a list of integers, the method returns the list
              of the corresponding constraints.

        OUTPUT:

        Each constraint is returned as a triple ``lower_bound, (indices,
        coefficients), upper_bound``.  For each of those entries, the
        corresponding linear function is the one associating to variable
        ``indices[i]`` the coefficient ``coefficients[i]``, and `0` to all the
        others.

        ``lower_bound`` and ``upper_bound`` are numerical values.

        EXAMPLES:

        First, let us define a small LP::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.add_constraint(p[0] - 2*p[1], min=1)

        To obtain the list of all constraints::

            sage: p.constraints()          # not tested
            [(1.0, ([1, 0], [-1.0, 1.0]), 4.0), (1.0, ([2, 0], [-2.0, 1.0]), None)]

        Or constraint `0` only::

            sage: p.constraints(0)         # not tested
            (1.0, ([1, 0], [-1.0, 1.0]), 4.0)

        A list of constraints containing only `1`::

            sage: p.constraints([1])       # not tested
            [(1.0, ([2, 0], [-2.0, 1.0]), None)]

        TESTS:

        As the ordering of the variables in each constraint depends on the
        solver used, we define a short function reordering it before it is
        printed. The output would look the same without this function applied::

            sage: def reorder_constraint(lb, indcoef, ub):
            ....:    ind, coef = indcoef
            ....:    d = dict(zip(ind, coef))
            ....:    ind.sort()
            ....:    return (lb, (ind, [d[i] for i in ind]), ub)

        Running the examples from above, reordering applied::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.add_constraint(p[0] - 2*p[1], min=1)
            sage: sorted(reorder_constraint(*c) for c in p.constraints())
            [(1.0, ([0, 1], [1.0, -1.0]), 4.0), (1.0, ([0, 2], [1.0, -2.0]), None)]
            sage: reorder_constraint(*p.constraints(0))
            (1.0, ([0, 1], [1.0, -1.0]), 4.0)
            sage: sorted(reorder_constraint(*c) for c in p.constraints([1]))
            [(1.0, ([0, 2], [1.0, -2.0]), None)]"""
    @overload
    def constraints(self) -> Any:
        """MixedIntegerLinearProgram.constraints(self, indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 937)

        Return a list of constraints, as 3-tuples.

        INPUT:

        - ``indices`` -- select which constraint(s) to return

            - If ``indices = None``, the method returns the list of all the
              constraints.

            - If ``indices`` is an integer `i`, the method returns constraint
              `i`.

            - If ``indices`` is a list of integers, the method returns the list
              of the corresponding constraints.

        OUTPUT:

        Each constraint is returned as a triple ``lower_bound, (indices,
        coefficients), upper_bound``.  For each of those entries, the
        corresponding linear function is the one associating to variable
        ``indices[i]`` the coefficient ``coefficients[i]``, and `0` to all the
        others.

        ``lower_bound`` and ``upper_bound`` are numerical values.

        EXAMPLES:

        First, let us define a small LP::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.add_constraint(p[0] - 2*p[1], min=1)

        To obtain the list of all constraints::

            sage: p.constraints()          # not tested
            [(1.0, ([1, 0], [-1.0, 1.0]), 4.0), (1.0, ([2, 0], [-2.0, 1.0]), None)]

        Or constraint `0` only::

            sage: p.constraints(0)         # not tested
            (1.0, ([1, 0], [-1.0, 1.0]), 4.0)

        A list of constraints containing only `1`::

            sage: p.constraints([1])       # not tested
            [(1.0, ([2, 0], [-2.0, 1.0]), None)]

        TESTS:

        As the ordering of the variables in each constraint depends on the
        solver used, we define a short function reordering it before it is
        printed. The output would look the same without this function applied::

            sage: def reorder_constraint(lb, indcoef, ub):
            ....:    ind, coef = indcoef
            ....:    d = dict(zip(ind, coef))
            ....:    ind.sort()
            ....:    return (lb, (ind, [d[i] for i in ind]), ub)

        Running the examples from above, reordering applied::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.add_constraint(p[0] - 2*p[1], min=1)
            sage: sorted(reorder_constraint(*c) for c in p.constraints())
            [(1.0, ([0, 1], [1.0, -1.0]), 4.0), (1.0, ([0, 2], [1.0, -2.0]), None)]
            sage: reorder_constraint(*p.constraints(0))
            (1.0, ([0, 1], [1.0, -1.0]), 4.0)
            sage: sorted(reorder_constraint(*c) for c in p.constraints([1]))
            [(1.0, ([0, 2], [1.0, -2.0]), None)]"""
    @overload
    def default_variable(self) -> Any:
        """MixedIntegerLinearProgram.default_variable(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 849)

        Return the default :class:`MIPVariable` of ``self``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.default_variable()
            MIPVariable with 0 real components"""
    @overload
    def default_variable(self) -> Any:
        """MixedIntegerLinearProgram.default_variable(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 849)

        Return the default :class:`MIPVariable` of ``self``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.default_variable()
            MIPVariable with 0 real components"""
    @overload
    def get_backend(self) -> Any:
        '''MixedIntegerLinearProgram.get_backend(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2904)

        Return the backend instance used.

        This might be useful when access to additional functions provided by
        the backend is needed.

        EXAMPLES:

        This example uses the simplex algorithm and prints information::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x, y = p[0], p[1]
            sage: p.add_constraint(2*x + 3*y, max=6)
            sage: p.add_constraint(3*x + 2*y, max=6)
            sage: p.set_objective(x + y + 7)
            sage: b = p.get_backend()
            sage: b.solver_parameter("simplex_or_intopt", "simplex_only")
            sage: b.solver_parameter("verbosity_simplex", "GLP_MSG_ALL")
            sage: ans = p.solve()
            GLPK Simplex Optimizer...
            2 rows, 2 columns, 4 non-zeros
            *     0: obj =   7.000000000e+00 inf =   0.000e+00 (2)
            *     2: obj =   9.400000000e+00 inf =   0.000e+00 (0)
            OPTIMAL LP SOLUTION FOUND
            sage: ans # rel tol 1e-5
            9.4'''
    @overload
    def get_backend(self) -> Any:
        '''MixedIntegerLinearProgram.get_backend(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2904)

        Return the backend instance used.

        This might be useful when access to additional functions provided by
        the backend is needed.

        EXAMPLES:

        This example uses the simplex algorithm and prints information::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x, y = p[0], p[1]
            sage: p.add_constraint(2*x + 3*y, max=6)
            sage: p.add_constraint(3*x + 2*y, max=6)
            sage: p.set_objective(x + y + 7)
            sage: b = p.get_backend()
            sage: b.solver_parameter("simplex_or_intopt", "simplex_only")
            sage: b.solver_parameter("verbosity_simplex", "GLP_MSG_ALL")
            sage: ans = p.solve()
            GLPK Simplex Optimizer...
            2 rows, 2 columns, 4 non-zeros
            *     0: obj =   7.000000000e+00 inf =   0.000e+00 (2)
            *     2: obj =   9.400000000e+00 inf =   0.000e+00 (0)
            OPTIMAL LP SOLUTION FOUND
            sage: ans # rel tol 1e-5
            9.4'''
    def get_max(self, v) -> Any:
        """MixedIntegerLinearProgram.get_max(self, v)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2756)

        Return the maximum value of a variable.

        INPUT:

        - ``v`` -- a variable

        OUTPUT:

        Maximum value of the variable, or ``None`` if the variable has no upper
        bound.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[1])
            sage: p.get_max(v[1])
            sage: p.set_max(v[1],6)
            sage: p.get_max(v[1])
            6.0"""
    def get_min(self, v) -> Any:
        """MixedIntegerLinearProgram.get_min(self, v)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2725)

        Return the minimum value of a variable.

        INPUT:

        - ``v`` -- a variable

        OUTPUT:

        Minimum value of the variable, or ``None`` if the variable has no lower
        bound.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[1])
            sage: p.get_min(v[1])
            0.0
            sage: p.set_min(v[1],6)
            sage: p.get_min(v[1])
            6.0
            sage: p.set_min(v[1], None)
            sage: p.get_min(v[1])"""
    @overload
    def get_objective_value(self) -> Any:
        """MixedIntegerLinearProgram.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2934)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p[0], p[1]
            sage: p.add_constraint(2*x + 3*y, max=6)
            sage: p.add_constraint(3*x + 2*y, max=6)
            sage: p.set_objective(x + y + 7)
            sage: p.solve()  # rel tol 1e-5
            9.4
            sage: p.get_objective_value()  # rel tol 1e-5
            9.4"""
    @overload
    def get_objective_value(self) -> Any:
        """MixedIntegerLinearProgram.get_objective_value(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2934)

        Return the value of the objective function.

        .. NOTE::

           Behaviour is undefined unless ``solve`` has been called before.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p[0], p[1]
            sage: p.add_constraint(2*x + 3*y, max=6)
            sage: p.add_constraint(3*x + 2*y, max=6)
            sage: p.set_objective(x + y + 7)
            sage: p.solve()  # rel tol 1e-5
            9.4
            sage: p.get_objective_value()  # rel tol 1e-5
            9.4"""
    def get_relative_objective_gap(self) -> Any:
        '''MixedIntegerLinearProgram.get_relative_objective_gap(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2989)

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

            sage: # needs sage.graphs
            sage: g = graphs.CubeGraph(9)
            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.solver_parameter("mip_gap_tolerance",100)
            sage: b = p.new_variable(binary=True)
            sage: p.set_objective(p.sum(b[v] for v in g))
            sage: for v in g:
            ....:     p.add_constraint(b[v] + p.sum(b[u] for u in g.neighbors(v)) <= 1)
            sage: p.add_constraint(b[v] == 1)  # Force an easy non-0 solution
            sage: p.solve() # rel tol 100
            1.0
            sage: p.get_relative_objective_gap()  # random
            46.99999999999999

        TESTS:

        Just make sure that the variable *has* been defined, and is not just
        undefined::

            sage: p.get_relative_objective_gap() > 1                                    # needs sage.graphs
            True'''
    @overload
    def get_values(self, *lists, convert=..., tolerance=...) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, x) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, y) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, x, y) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, x) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, x, convert=..., tolerance=...) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, x, convert=..., tolerance=...) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, x) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, x, convert=..., tolerance=...) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, x) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, y) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, tolerance=...) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, convert=..., tolerance=...) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, convert=...) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def get_values(self, convert=..., tolerance=...) -> Any:
        '''MixedIntegerLinearProgram.get_values(self, *lists, convert=None, tolerance=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1541)

        Return values found by the previous call to ``solve()``.

        INPUT:

        - ``*lists`` -- any instance of ``MIPVariable`` (or one of its
          elements), or lists of them

        - ``convert`` -- (default: ``None``) ``ZZ``, ``bool``, or ``True``:

          - if ``convert=None`` (default), return all variable values as the
            backend provides them, i.e., as an element of :meth:`base_ring` or a
            ``float``.

          - if ``convert=ZZ``, convert all variable values from the
            :meth:`base_ring` by rounding to the nearest integer.

          - if ``convert=bool``, convert all variable values from the
            :meth:`base_ring` by rounding to 0/1 and converting to ``bool``.

          - if ``convert=True``, use ``ZZ`` for MIP variables declared integer
            or binary, and convert the values of all other variables to the
            :meth:`base_ring`.

        - ``tolerance`` -- ``None``, a positive real number, or ``0`` (if
          :meth:`base_ring` is an exact ring).  Required if ``convert`` is not
          ``None`` and any integer conversion is to be done.  If the variable
          value differs from the nearest integer by more than ``tolerance``,
          raise a :exc:`RuntimeError`.

        OUTPUT:

        - Each instance of ``MIPVariable`` is replaced by a dictionary
          containing the numerical values found for each
          corresponding variable in the instance.
        - Each element of an instance of a ``MIPVariable`` is replaced
          by its corresponding numerical value.

        .. NOTE::

            While a variable may be declared as binary or integer, its value is
            an element of the :meth:`base_ring`, or for the numerical solvers,
            a ``float``.

            For the numerical solvers, :meth:`base_ring` is ``RDF``, an inexact
            ring.  Code using ``get_values`` should always account for possible
            numerical errors.

            Even for variables declared as binary or integer, or known to be an
            integer because of the mathematical properties of the model, the
            returned values cannot be expected to be exact integers.  This is
            normal behavior of the numerical solvers.

            For correct operation, any user code needs to avoid exact
            comparisons (``==``, ``!=``) and instead allow for numerical
            tolerances.  The magnitude of the numerical tolerances depends on
            both the model and the solver.

            The arguments ``convert`` and ``tolerance`` facilitate writing
            correct code.  See examples below.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[3] + 3*y[2,9] + x[5])
            sage: p.add_constraint(x[3] + y[2,9] + 2*x[5], max=2)
            sage: p.solve()
            6.0

        To return the value of ``y[2,9]`` in the optimal solution::

            sage: p.get_values(y[2,9])
            2.0
            sage: type(_)
            <class \'float\'>

        To convert the value to the :meth:`base_ring`::

            sage: p.get_values(y[2,9], convert=True)
            2.0
            sage: _.parent()
            Real Double Field

        To get a dictionary identical to ``x`` containing the
        values for the corresponding variables in the optimal solution::

            sage: x_sol = p.get_values(x)
            sage: sorted(x_sol)
            [3, 5]

        Obviously, it also works with variables of higher dimension::

            sage: y_sol = p.get_values(y)

        We could also have tried ::

            sage: [x_sol, y_sol] = p.get_values(x, y)

        Or::

            sage: [x_sol, y_sol] = p.get_values([x, y])

        Using ``convert`` and ``tolerance``.  First, a binary knapsack::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(binary=True)
            sage: p.set_objective(3*x[1] + 4*x[2] + 5*x[3])
            sage: p.add_constraint(2*x[1] + 3*x[2] + 4*x[3] <= 6)
            sage: p.solve()
            8.0
            sage: x_opt = p.get_values(x); x_opt
            {1: 1.0, 2: 0.0, 3: 1.0}
            sage: type(x_opt[1])
            <class \'float\'>
            sage: x_opt_ZZ = p.get_values(x, convert=True, tolerance=1e-6); x_opt_ZZ
            {1: 1, 2: 0, 3: 1}
            sage: x_opt_ZZ[1].parent()
            Integer Ring
            sage: x_opt_bool = p.get_values(x, convert=bool, tolerance=1e-6); x_opt_bool
            {1: True, 2: False, 3: True}

        Thanks to total unimodularity, single-commodity network flow problems
        with integer capacities and integer supplies/demands have integer vertex
        solutions.  Hence the integrality of solutions is mathematically
        guaranteed in an optimal solution if we use the simplex algorithm.  A
        numerical LP solver based on the simplex method such as GLPK will return
        an integer solution only up to a numerical error.  Hence, for correct
        operation, we should use ``tolerance``::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\', maximization=False)
            sage: x = p.new_variable(nonnegative=True)
            sage: x.set_max(1)
            sage: p.add_constraint(x[\'sa\'] + x[\'sb\'] == 1)
            sage: p.add_constraint(x[\'sa\'] + x[\'ba\'] - x[\'ab\'] - x[\'at\'] == 0)
            sage: p.add_constraint(x[\'sb\'] + x[\'ab\'] - x[\'ba\'] - x[\'bt\'] == 0)
            sage: p.set_objective(10*x[\'sa\'] + 10*x[\'bt\'])
            sage: p.solve()
            0.0
            sage: x_opt = p.get_values(x); x_opt
            {\'ab\': 0.0, \'at\': 1.0, \'ba\': 1.0, \'bt\': -0.0, \'sa\': 0.0, \'sb\': 1.0}
            sage: x_opt_ZZ = p.get_values(x, convert=ZZ, tolerance=1e-6); x_opt_ZZ
            {\'ab\': 0, \'at\': 1, \'ba\': 1, \'bt\': 0, \'sa\': 0, \'sb\': 1}

        TESTS:

        Test that an error is reported when we try to get the value
        of something that is not a variable in this problem::

            sage: p.get_values("Something strange")
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: p.get_values("Something stranger", 4711)
            Traceback (most recent call last):
            ...
            TypeError: Not a MIPVariable: ...
            sage: M1 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: M2 = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M1.new_variable()
            sage: y = M1.new_variable()
            sage: z = M2.new_variable()
            sage: M2.add_constraint(z[0] <= 5)
            sage: M2.solve()
            0.0
            sage: M2.get_values(x)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: M2.get_values(y)
            Traceback (most recent call last):
            ...
            ValueError: ...

        Test input validation for ``convert`` and ``tolerance``::

            sage: M_inexact = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = M_inexact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_inexact.solve()
            0.0
            sage: M_inexact.get_values(tolerance=0.01)
            Traceback (most recent call last):
            ...
            TypeError: cannot use tolerance if convert is None
            sage: M_inexact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_inexact.get_values(convert=True, tolerance=0)
            Traceback (most recent call last):
            ...
            ValueError: for an inexact base_ring, tolerance must be positive

            sage: M_exact =  MixedIntegerLinearProgram(solver=\'ppl\')
            sage: x = M_exact.new_variable(binary=True)
            sage: x[1]
            x_0
            sage: M_exact.solve()
            0
            sage: M_exact.get_values(convert=True)
            []
            sage: M_exact.get_values(x[1], convert=True)
            Traceback (most recent call last):
            ...
            TypeError: for converting to integers, a tolerance must be provided
            sage: M_exact.get_values(x[1], convert=True, tolerance=0)
            0
            sage: M_exact.get_values(convert=True, tolerance=-0.2)
            Traceback (most recent call last):
            ...
            ValueError: for an exact base_ring, tolerance must be nonnegative'''
    @overload
    def interactive_lp_problem(self, form=...) -> Any:
        """MixedIntegerLinearProgram.interactive_lp_problem(self, form='standard')

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3032)

        Return an InteractiveLPProblem and, if available, a basis.

        INPUT:

        - ``form`` -- (default: ``'standard'``) a string specifying return type: either
          ``None``, or ``'std'`` or ``'standard'``, respectively returns an instance of
          :class:`InteractiveLPProblem` or of :class:`InteractiveLPProblemStandardForm`

        OUTPUT:

        A 2-tuple consists of an instance of class :class:`InteractiveLPProblem` or
        :class:`InteractiveLPProblemStandardForm` that is constructed based on a given
        :class:`MixedIntegerLinearProgram`, and a list of basic
        variables (the basis) if standard form is chosen (by default), otherwise ``None``.

        All variables must have 0 as lower bound and no upper bound.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(names=['m'], solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True, name='n')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0] + x[1] - 7*y[0] + v[0] <= 2, name='K')
            sage: p.add_constraint(x[1] + 2*y[0] - v[0] <= 3)
            sage: p.add_constraint(5*x[0] + y[0] <= 21, name='L')
            sage: p.set_objective(2*x[0] + 3*x[1] + 4*y[0] + 5*v[0])
            sage: lp, basis = p.interactive_lp_problem()
            sage: basis
            ['K', 'w_1', 'L']
            sage: lp.constraint_coefficients()
            [ 1.0  1.0 -7.0  1.0]
            [ 0.0  1.0  2.0 -1.0]
            [ 5.0  0.0  1.0  0.0]
            sage: lp.b()
            (2.0, 3.0, 21.0)
            sage: lp.objective_coefficients()
            (2.0, 3.0, 4.0, 5.0)
            sage: lp.decision_variables()
            (m_0, m_1, n_0, x_3)
            sage: view(lp) #not tested
            sage: d = lp.dictionary(*basis)
            sage: view(d) #not tested

        TESTS::

            sage: b = p.get_backend()
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: b.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: b.solve()
            0
            sage: lp2, basis2 = p.interactive_lp_problem()
            sage: set(basis2)
            {'n_0', 'w_1', 'x_3'}
            sage: d2 = lp2.dictionary(*basis2)
            sage: d2.is_optimal()
            True
            sage: view(d2) #not tested

            sage: lp3, _ = p.interactive_lp_problem(form=None)
            sage: lp3.constraint_coefficients()
            [ 1.0  1.0 -7.0  1.0]
            [ 0.0  1.0  2.0 -1.0]
            [ 5.0  0.0  1.0  0.0]
            sage: lp3.b()
            (2.0, 3.0, 21.0)
            sage: lp3.objective_coefficients()
            (2.0, 3.0, 4.0, 5.0)
            sage: lp3.decision_variables()
            (m_0, m_1, n_0, x_3)
            sage: view(lp3) #not tested"""
    @overload
    def interactive_lp_problem(self) -> Any:
        """MixedIntegerLinearProgram.interactive_lp_problem(self, form='standard')

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3032)

        Return an InteractiveLPProblem and, if available, a basis.

        INPUT:

        - ``form`` -- (default: ``'standard'``) a string specifying return type: either
          ``None``, or ``'std'`` or ``'standard'``, respectively returns an instance of
          :class:`InteractiveLPProblem` or of :class:`InteractiveLPProblemStandardForm`

        OUTPUT:

        A 2-tuple consists of an instance of class :class:`InteractiveLPProblem` or
        :class:`InteractiveLPProblemStandardForm` that is constructed based on a given
        :class:`MixedIntegerLinearProgram`, and a list of basic
        variables (the basis) if standard form is chosen (by default), otherwise ``None``.

        All variables must have 0 as lower bound and no upper bound.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(names=['m'], solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True, name='n')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0] + x[1] - 7*y[0] + v[0] <= 2, name='K')
            sage: p.add_constraint(x[1] + 2*y[0] - v[0] <= 3)
            sage: p.add_constraint(5*x[0] + y[0] <= 21, name='L')
            sage: p.set_objective(2*x[0] + 3*x[1] + 4*y[0] + 5*v[0])
            sage: lp, basis = p.interactive_lp_problem()
            sage: basis
            ['K', 'w_1', 'L']
            sage: lp.constraint_coefficients()
            [ 1.0  1.0 -7.0  1.0]
            [ 0.0  1.0  2.0 -1.0]
            [ 5.0  0.0  1.0  0.0]
            sage: lp.b()
            (2.0, 3.0, 21.0)
            sage: lp.objective_coefficients()
            (2.0, 3.0, 4.0, 5.0)
            sage: lp.decision_variables()
            (m_0, m_1, n_0, x_3)
            sage: view(lp) #not tested
            sage: d = lp.dictionary(*basis)
            sage: view(d) #not tested

        TESTS::

            sage: b = p.get_backend()
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: b.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: b.solve()
            0
            sage: lp2, basis2 = p.interactive_lp_problem()
            sage: set(basis2)
            {'n_0', 'w_1', 'x_3'}
            sage: d2 = lp2.dictionary(*basis2)
            sage: d2.is_optimal()
            True
            sage: view(d2) #not tested

            sage: lp3, _ = p.interactive_lp_problem(form=None)
            sage: lp3.constraint_coefficients()
            [ 1.0  1.0 -7.0  1.0]
            [ 0.0  1.0  2.0 -1.0]
            [ 5.0  0.0  1.0  0.0]
            sage: lp3.b()
            (2.0, 3.0, 21.0)
            sage: lp3.objective_coefficients()
            (2.0, 3.0, 4.0, 5.0)
            sage: lp3.decision_variables()
            (m_0, m_1, n_0, x_3)
            sage: view(lp3) #not tested"""
    @overload
    def interactive_lp_problem(self) -> Any:
        """MixedIntegerLinearProgram.interactive_lp_problem(self, form='standard')

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3032)

        Return an InteractiveLPProblem and, if available, a basis.

        INPUT:

        - ``form`` -- (default: ``'standard'``) a string specifying return type: either
          ``None``, or ``'std'`` or ``'standard'``, respectively returns an instance of
          :class:`InteractiveLPProblem` or of :class:`InteractiveLPProblemStandardForm`

        OUTPUT:

        A 2-tuple consists of an instance of class :class:`InteractiveLPProblem` or
        :class:`InteractiveLPProblemStandardForm` that is constructed based on a given
        :class:`MixedIntegerLinearProgram`, and a list of basic
        variables (the basis) if standard form is chosen (by default), otherwise ``None``.

        All variables must have 0 as lower bound and no upper bound.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(names=['m'], solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True, name='n')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0] + x[1] - 7*y[0] + v[0] <= 2, name='K')
            sage: p.add_constraint(x[1] + 2*y[0] - v[0] <= 3)
            sage: p.add_constraint(5*x[0] + y[0] <= 21, name='L')
            sage: p.set_objective(2*x[0] + 3*x[1] + 4*y[0] + 5*v[0])
            sage: lp, basis = p.interactive_lp_problem()
            sage: basis
            ['K', 'w_1', 'L']
            sage: lp.constraint_coefficients()
            [ 1.0  1.0 -7.0  1.0]
            [ 0.0  1.0  2.0 -1.0]
            [ 5.0  0.0  1.0  0.0]
            sage: lp.b()
            (2.0, 3.0, 21.0)
            sage: lp.objective_coefficients()
            (2.0, 3.0, 4.0, 5.0)
            sage: lp.decision_variables()
            (m_0, m_1, n_0, x_3)
            sage: view(lp) #not tested
            sage: d = lp.dictionary(*basis)
            sage: view(d) #not tested

        TESTS::

            sage: b = p.get_backend()
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: b.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: b.solve()
            0
            sage: lp2, basis2 = p.interactive_lp_problem()
            sage: set(basis2)
            {'n_0', 'w_1', 'x_3'}
            sage: d2 = lp2.dictionary(*basis2)
            sage: d2.is_optimal()
            True
            sage: view(d2) #not tested

            sage: lp3, _ = p.interactive_lp_problem(form=None)
            sage: lp3.constraint_coefficients()
            [ 1.0  1.0 -7.0  1.0]
            [ 0.0  1.0  2.0 -1.0]
            [ 5.0  0.0  1.0  0.0]
            sage: lp3.b()
            (2.0, 3.0, 21.0)
            sage: lp3.objective_coefficients()
            (2.0, 3.0, 4.0, 5.0)
            sage: lp3.decision_variables()
            (m_0, m_1, n_0, x_3)
            sage: view(lp3) #not tested"""
    @overload
    def interactive_lp_problem(self, form=...) -> Any:
        """MixedIntegerLinearProgram.interactive_lp_problem(self, form='standard')

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 3032)

        Return an InteractiveLPProblem and, if available, a basis.

        INPUT:

        - ``form`` -- (default: ``'standard'``) a string specifying return type: either
          ``None``, or ``'std'`` or ``'standard'``, respectively returns an instance of
          :class:`InteractiveLPProblem` or of :class:`InteractiveLPProblemStandardForm`

        OUTPUT:

        A 2-tuple consists of an instance of class :class:`InteractiveLPProblem` or
        :class:`InteractiveLPProblemStandardForm` that is constructed based on a given
        :class:`MixedIntegerLinearProgram`, and a list of basic
        variables (the basis) if standard form is chosen (by default), otherwise ``None``.

        All variables must have 0 as lower bound and no upper bound.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(names=['m'], solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: y = p.new_variable(nonnegative=True, name='n')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(x[0] + x[1] - 7*y[0] + v[0] <= 2, name='K')
            sage: p.add_constraint(x[1] + 2*y[0] - v[0] <= 3)
            sage: p.add_constraint(5*x[0] + y[0] <= 21, name='L')
            sage: p.set_objective(2*x[0] + 3*x[1] + 4*y[0] + 5*v[0])
            sage: lp, basis = p.interactive_lp_problem()
            sage: basis
            ['K', 'w_1', 'L']
            sage: lp.constraint_coefficients()
            [ 1.0  1.0 -7.0  1.0]
            [ 0.0  1.0  2.0 -1.0]
            [ 5.0  0.0  1.0  0.0]
            sage: lp.b()
            (2.0, 3.0, 21.0)
            sage: lp.objective_coefficients()
            (2.0, 3.0, 4.0, 5.0)
            sage: lp.decision_variables()
            (m_0, m_1, n_0, x_3)
            sage: view(lp) #not tested
            sage: d = lp.dictionary(*basis)
            sage: view(d) #not tested

        TESTS::

            sage: b = p.get_backend()
            sage: import sage.numerical.backends.glpk_backend as backend
            sage: b.solver_parameter(backend.glp_simplex_or_intopt, backend.glp_simplex_only)
            sage: b.solve()
            0
            sage: lp2, basis2 = p.interactive_lp_problem()
            sage: set(basis2)
            {'n_0', 'w_1', 'x_3'}
            sage: d2 = lp2.dictionary(*basis2)
            sage: d2.is_optimal()
            True
            sage: view(d2) #not tested

            sage: lp3, _ = p.interactive_lp_problem(form=None)
            sage: lp3.constraint_coefficients()
            [ 1.0  1.0 -7.0  1.0]
            [ 0.0  1.0  2.0 -1.0]
            [ 5.0  0.0  1.0  0.0]
            sage: lp3.b()
            (2.0, 3.0, 21.0)
            sage: lp3.objective_coefficients()
            (2.0, 3.0, 4.0, 5.0)
            sage: lp3.decision_variables()
            (m_0, m_1, n_0, x_3)
            sage: view(lp3) #not tested"""
    def is_binary(self, e) -> Any:
        """MixedIntegerLinearProgram.is_binary(self, e)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2412)

        Test whether the variable ``e`` is binary. Variables are real by
        default.

        INPUT:

        - ``e`` -- a variable (not a ``MIPVariable``, but one of its elements)

        OUTPUT: ``True`` if the variable ``e`` is binary; ``False`` otherwise

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[1])
            sage: p.is_binary(v[1])
            False
            sage: p.set_binary(v[1])
            sage: p.is_binary(v[1])
            True"""
    def is_integer(self, e) -> Any:
        """MixedIntegerLinearProgram.is_integer(self, e)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2474)

        Test whether the variable is an integer. Variables are real by
        default.

        INPUT:

        - ``e`` -- a variable (not a ``MIPVariable``, but one of its elements)

        OUTPUT: ``True`` if the variable ``e`` is an integer; ``False`` otherwise

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[1])
            sage: p.is_integer(v[1])
            False
            sage: p.set_integer(v[1])
            sage: p.is_integer(v[1])
            True"""
    def is_real(self, e) -> Any:
        """MixedIntegerLinearProgram.is_real(self, e)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2538)

        Test whether the variable is real.

        INPUT:

        - ``e`` -- a variable (not a ``MIPVariable``, but one of its elements)

        OUTPUT: ``True`` if the variable is real; ``False`` otherwise

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[1])
            sage: p.is_real(v[1])
            True
            sage: p.set_binary(v[1])
            sage: p.is_real(v[1])
            False
            sage: p.set_real(v[1])
            sage: p.is_real(v[1])
            True"""
    @overload
    def linear_constraints_parent(self) -> Any:
        """MixedIntegerLinearProgram.linear_constraints_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 495)

        Return the parent for all linear constraints.

        See :mod:`~sage.numerical.linear_functions` for more
        details.

        EXAMPLES::

             sage: p = MixedIntegerLinearProgram(solver='GLPK')
             sage: p.linear_constraints_parent()
             Linear constraints over Real Double Field"""
    @overload
    def linear_constraints_parent(self) -> Any:
        """MixedIntegerLinearProgram.linear_constraints_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 495)

        Return the parent for all linear constraints.

        See :mod:`~sage.numerical.linear_functions` for more
        details.

        EXAMPLES::

             sage: p = MixedIntegerLinearProgram(solver='GLPK')
             sage: p.linear_constraints_parent()
             Linear constraints over Real Double Field"""
    @overload
    def linear_functions_parent(self) -> Any:
        """MixedIntegerLinearProgram.linear_functions_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 479)

        Return the parent for all linear functions.

        EXAMPLES::

             sage: p = MixedIntegerLinearProgram(solver='GLPK')
             sage: p.linear_functions_parent()
             Linear functions over Real Double Field"""
    @overload
    def linear_functions_parent(self) -> Any:
        """MixedIntegerLinearProgram.linear_functions_parent(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 479)

        Return the parent for all linear functions.

        EXAMPLES::

             sage: p = MixedIntegerLinearProgram(solver='GLPK')
             sage: p.linear_functions_parent()
             Linear functions over Real Double Field"""
    @overload
    def new_variable(self, real=..., binary=..., integer=..., nonnegative=..., name=..., indices=...) -> Any:
        '''MixedIntegerLinearProgram.new_variable(self, real=False, binary=False, integer=False, nonnegative=False, name=\'\', indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 717)

        Return a new :class:`MIPVariable` instance.

        A new variable ``x`` is defined by::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)

        It behaves exactly as a usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        .. SEEALSO::

            - :meth:`set_min`, :meth:`get_min` -- set/get the lower bound of a
              variable

            - :meth:`set_max`, :meth:`get_max` -- set/get the upper bound of a
              variable

        INPUT:

        - ``binary``, ``integer``, ``real`` -- boolean. Set one of these
          arguments to ``True`` to ensure that the variable gets the
          corresponding type.

        - ``nonnegative`` -- boolean (default: ``False``); whether the
          variable should be assumed to be nonnegative. Rather useless
          for the binary type

        - ``name`` -- string; associates a name to the variable. This
          is only useful when exporting the linear program to a file
          using ``write_mps`` or ``write_lp``, and has no other
          effect.

        - ``indices`` -- (optional) an iterable of keys; components
          corresponding to these keys are created in order,
          and access to components with other keys will raise an
          error; otherwise components of this variable can be
          indexed by arbitrary keys and are created dynamically
          on access

        OUTPUT:

        A new instance of :class:`MIPVariable` associated to the
        current :class:`MixedIntegerLinearProgram`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(); x
            MIPVariable with 0 real components
            sage: x0 = x[0]; x0
            x_0

        By default, variables are unbounded::

            sage: print(p.get_min(x0))
            None
            sage: print(p.get_max(x0))
            None

        To define two dictionaries of variables, the first being
        of real type, and the second of integer type ::

            sage: x = p.new_variable(real=True, nonnegative=True)
            sage: y = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(x[2] + y[3,5], max=2)
            sage: p.is_integer(x[2])
            False
            sage: p.is_integer(y[3,5])
            True

        An exception is raised when two types are supplied ::

            sage: z = p.new_variable(real=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: Exactly one of the available types has to be True

        Unbounded variables::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(real=True)
            sage: y = p.new_variable(integer=True)
            sage: p.add_constraint(x[0] + x[3] <= 8)
            sage: p.add_constraint(y[0] >= y[1])
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 8.0
              - x_2 + x_3 <= 0.0
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)
              x_2 is an integer variable (min=-oo, max=+oo)
              x_3 is an integer variable (min=-oo, max=+oo)

        On the Sage command line, generator syntax is accepted as a
        shorthand for generating new variables with default settings::

            sage: mip.<x, y, z> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: mip.add_constraint(x[0] + y[1] + z[2] <= 10)
            sage: mip.show()
            Constraints:
              x[0] + y[1] + z[2] <= 10.0
            Variables:
              x[0] = x_0 is a continuous variable (min=-oo, max=+oo)
              y[1] = x_1 is a continuous variable (min=-oo, max=+oo)
              z[2] = x_2 is a continuous variable (min=-oo, max=+oo)'''
    @overload
    def new_variable(self, nonnegative=...) -> Any:
        '''MixedIntegerLinearProgram.new_variable(self, real=False, binary=False, integer=False, nonnegative=False, name=\'\', indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 717)

        Return a new :class:`MIPVariable` instance.

        A new variable ``x`` is defined by::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)

        It behaves exactly as a usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        .. SEEALSO::

            - :meth:`set_min`, :meth:`get_min` -- set/get the lower bound of a
              variable

            - :meth:`set_max`, :meth:`get_max` -- set/get the upper bound of a
              variable

        INPUT:

        - ``binary``, ``integer``, ``real`` -- boolean. Set one of these
          arguments to ``True`` to ensure that the variable gets the
          corresponding type.

        - ``nonnegative`` -- boolean (default: ``False``); whether the
          variable should be assumed to be nonnegative. Rather useless
          for the binary type

        - ``name`` -- string; associates a name to the variable. This
          is only useful when exporting the linear program to a file
          using ``write_mps`` or ``write_lp``, and has no other
          effect.

        - ``indices`` -- (optional) an iterable of keys; components
          corresponding to these keys are created in order,
          and access to components with other keys will raise an
          error; otherwise components of this variable can be
          indexed by arbitrary keys and are created dynamically
          on access

        OUTPUT:

        A new instance of :class:`MIPVariable` associated to the
        current :class:`MixedIntegerLinearProgram`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(); x
            MIPVariable with 0 real components
            sage: x0 = x[0]; x0
            x_0

        By default, variables are unbounded::

            sage: print(p.get_min(x0))
            None
            sage: print(p.get_max(x0))
            None

        To define two dictionaries of variables, the first being
        of real type, and the second of integer type ::

            sage: x = p.new_variable(real=True, nonnegative=True)
            sage: y = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(x[2] + y[3,5], max=2)
            sage: p.is_integer(x[2])
            False
            sage: p.is_integer(y[3,5])
            True

        An exception is raised when two types are supplied ::

            sage: z = p.new_variable(real=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: Exactly one of the available types has to be True

        Unbounded variables::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(real=True)
            sage: y = p.new_variable(integer=True)
            sage: p.add_constraint(x[0] + x[3] <= 8)
            sage: p.add_constraint(y[0] >= y[1])
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 8.0
              - x_2 + x_3 <= 0.0
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)
              x_2 is an integer variable (min=-oo, max=+oo)
              x_3 is an integer variable (min=-oo, max=+oo)

        On the Sage command line, generator syntax is accepted as a
        shorthand for generating new variables with default settings::

            sage: mip.<x, y, z> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: mip.add_constraint(x[0] + y[1] + z[2] <= 10)
            sage: mip.show()
            Constraints:
              x[0] + y[1] + z[2] <= 10.0
            Variables:
              x[0] = x_0 is a continuous variable (min=-oo, max=+oo)
              y[1] = x_1 is a continuous variable (min=-oo, max=+oo)
              z[2] = x_2 is a continuous variable (min=-oo, max=+oo)'''
    @overload
    def new_variable(self) -> Any:
        '''MixedIntegerLinearProgram.new_variable(self, real=False, binary=False, integer=False, nonnegative=False, name=\'\', indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 717)

        Return a new :class:`MIPVariable` instance.

        A new variable ``x`` is defined by::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)

        It behaves exactly as a usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        .. SEEALSO::

            - :meth:`set_min`, :meth:`get_min` -- set/get the lower bound of a
              variable

            - :meth:`set_max`, :meth:`get_max` -- set/get the upper bound of a
              variable

        INPUT:

        - ``binary``, ``integer``, ``real`` -- boolean. Set one of these
          arguments to ``True`` to ensure that the variable gets the
          corresponding type.

        - ``nonnegative`` -- boolean (default: ``False``); whether the
          variable should be assumed to be nonnegative. Rather useless
          for the binary type

        - ``name`` -- string; associates a name to the variable. This
          is only useful when exporting the linear program to a file
          using ``write_mps`` or ``write_lp``, and has no other
          effect.

        - ``indices`` -- (optional) an iterable of keys; components
          corresponding to these keys are created in order,
          and access to components with other keys will raise an
          error; otherwise components of this variable can be
          indexed by arbitrary keys and are created dynamically
          on access

        OUTPUT:

        A new instance of :class:`MIPVariable` associated to the
        current :class:`MixedIntegerLinearProgram`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(); x
            MIPVariable with 0 real components
            sage: x0 = x[0]; x0
            x_0

        By default, variables are unbounded::

            sage: print(p.get_min(x0))
            None
            sage: print(p.get_max(x0))
            None

        To define two dictionaries of variables, the first being
        of real type, and the second of integer type ::

            sage: x = p.new_variable(real=True, nonnegative=True)
            sage: y = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(x[2] + y[3,5], max=2)
            sage: p.is_integer(x[2])
            False
            sage: p.is_integer(y[3,5])
            True

        An exception is raised when two types are supplied ::

            sage: z = p.new_variable(real=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: Exactly one of the available types has to be True

        Unbounded variables::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(real=True)
            sage: y = p.new_variable(integer=True)
            sage: p.add_constraint(x[0] + x[3] <= 8)
            sage: p.add_constraint(y[0] >= y[1])
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 8.0
              - x_2 + x_3 <= 0.0
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)
              x_2 is an integer variable (min=-oo, max=+oo)
              x_3 is an integer variable (min=-oo, max=+oo)

        On the Sage command line, generator syntax is accepted as a
        shorthand for generating new variables with default settings::

            sage: mip.<x, y, z> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: mip.add_constraint(x[0] + y[1] + z[2] <= 10)
            sage: mip.show()
            Constraints:
              x[0] + y[1] + z[2] <= 10.0
            Variables:
              x[0] = x_0 is a continuous variable (min=-oo, max=+oo)
              y[1] = x_1 is a continuous variable (min=-oo, max=+oo)
              z[2] = x_2 is a continuous variable (min=-oo, max=+oo)'''
    @overload
    def new_variable(self, real=..., nonnegative=...) -> Any:
        '''MixedIntegerLinearProgram.new_variable(self, real=False, binary=False, integer=False, nonnegative=False, name=\'\', indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 717)

        Return a new :class:`MIPVariable` instance.

        A new variable ``x`` is defined by::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)

        It behaves exactly as a usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        .. SEEALSO::

            - :meth:`set_min`, :meth:`get_min` -- set/get the lower bound of a
              variable

            - :meth:`set_max`, :meth:`get_max` -- set/get the upper bound of a
              variable

        INPUT:

        - ``binary``, ``integer``, ``real`` -- boolean. Set one of these
          arguments to ``True`` to ensure that the variable gets the
          corresponding type.

        - ``nonnegative`` -- boolean (default: ``False``); whether the
          variable should be assumed to be nonnegative. Rather useless
          for the binary type

        - ``name`` -- string; associates a name to the variable. This
          is only useful when exporting the linear program to a file
          using ``write_mps`` or ``write_lp``, and has no other
          effect.

        - ``indices`` -- (optional) an iterable of keys; components
          corresponding to these keys are created in order,
          and access to components with other keys will raise an
          error; otherwise components of this variable can be
          indexed by arbitrary keys and are created dynamically
          on access

        OUTPUT:

        A new instance of :class:`MIPVariable` associated to the
        current :class:`MixedIntegerLinearProgram`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(); x
            MIPVariable with 0 real components
            sage: x0 = x[0]; x0
            x_0

        By default, variables are unbounded::

            sage: print(p.get_min(x0))
            None
            sage: print(p.get_max(x0))
            None

        To define two dictionaries of variables, the first being
        of real type, and the second of integer type ::

            sage: x = p.new_variable(real=True, nonnegative=True)
            sage: y = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(x[2] + y[3,5], max=2)
            sage: p.is_integer(x[2])
            False
            sage: p.is_integer(y[3,5])
            True

        An exception is raised when two types are supplied ::

            sage: z = p.new_variable(real=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: Exactly one of the available types has to be True

        Unbounded variables::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(real=True)
            sage: y = p.new_variable(integer=True)
            sage: p.add_constraint(x[0] + x[3] <= 8)
            sage: p.add_constraint(y[0] >= y[1])
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 8.0
              - x_2 + x_3 <= 0.0
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)
              x_2 is an integer variable (min=-oo, max=+oo)
              x_3 is an integer variable (min=-oo, max=+oo)

        On the Sage command line, generator syntax is accepted as a
        shorthand for generating new variables with default settings::

            sage: mip.<x, y, z> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: mip.add_constraint(x[0] + y[1] + z[2] <= 10)
            sage: mip.show()
            Constraints:
              x[0] + y[1] + z[2] <= 10.0
            Variables:
              x[0] = x_0 is a continuous variable (min=-oo, max=+oo)
              y[1] = x_1 is a continuous variable (min=-oo, max=+oo)
              z[2] = x_2 is a continuous variable (min=-oo, max=+oo)'''
    @overload
    def new_variable(self, integer=..., nonnegative=...) -> Any:
        '''MixedIntegerLinearProgram.new_variable(self, real=False, binary=False, integer=False, nonnegative=False, name=\'\', indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 717)

        Return a new :class:`MIPVariable` instance.

        A new variable ``x`` is defined by::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)

        It behaves exactly as a usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        .. SEEALSO::

            - :meth:`set_min`, :meth:`get_min` -- set/get the lower bound of a
              variable

            - :meth:`set_max`, :meth:`get_max` -- set/get the upper bound of a
              variable

        INPUT:

        - ``binary``, ``integer``, ``real`` -- boolean. Set one of these
          arguments to ``True`` to ensure that the variable gets the
          corresponding type.

        - ``nonnegative`` -- boolean (default: ``False``); whether the
          variable should be assumed to be nonnegative. Rather useless
          for the binary type

        - ``name`` -- string; associates a name to the variable. This
          is only useful when exporting the linear program to a file
          using ``write_mps`` or ``write_lp``, and has no other
          effect.

        - ``indices`` -- (optional) an iterable of keys; components
          corresponding to these keys are created in order,
          and access to components with other keys will raise an
          error; otherwise components of this variable can be
          indexed by arbitrary keys and are created dynamically
          on access

        OUTPUT:

        A new instance of :class:`MIPVariable` associated to the
        current :class:`MixedIntegerLinearProgram`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(); x
            MIPVariable with 0 real components
            sage: x0 = x[0]; x0
            x_0

        By default, variables are unbounded::

            sage: print(p.get_min(x0))
            None
            sage: print(p.get_max(x0))
            None

        To define two dictionaries of variables, the first being
        of real type, and the second of integer type ::

            sage: x = p.new_variable(real=True, nonnegative=True)
            sage: y = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(x[2] + y[3,5], max=2)
            sage: p.is_integer(x[2])
            False
            sage: p.is_integer(y[3,5])
            True

        An exception is raised when two types are supplied ::

            sage: z = p.new_variable(real=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: Exactly one of the available types has to be True

        Unbounded variables::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(real=True)
            sage: y = p.new_variable(integer=True)
            sage: p.add_constraint(x[0] + x[3] <= 8)
            sage: p.add_constraint(y[0] >= y[1])
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 8.0
              - x_2 + x_3 <= 0.0
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)
              x_2 is an integer variable (min=-oo, max=+oo)
              x_3 is an integer variable (min=-oo, max=+oo)

        On the Sage command line, generator syntax is accepted as a
        shorthand for generating new variables with default settings::

            sage: mip.<x, y, z> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: mip.add_constraint(x[0] + y[1] + z[2] <= 10)
            sage: mip.show()
            Constraints:
              x[0] + y[1] + z[2] <= 10.0
            Variables:
              x[0] = x_0 is a continuous variable (min=-oo, max=+oo)
              y[1] = x_1 is a continuous variable (min=-oo, max=+oo)
              z[2] = x_2 is a continuous variable (min=-oo, max=+oo)'''
    @overload
    def new_variable(self, real=..., integer=...) -> Any:
        '''MixedIntegerLinearProgram.new_variable(self, real=False, binary=False, integer=False, nonnegative=False, name=\'\', indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 717)

        Return a new :class:`MIPVariable` instance.

        A new variable ``x`` is defined by::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)

        It behaves exactly as a usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        .. SEEALSO::

            - :meth:`set_min`, :meth:`get_min` -- set/get the lower bound of a
              variable

            - :meth:`set_max`, :meth:`get_max` -- set/get the upper bound of a
              variable

        INPUT:

        - ``binary``, ``integer``, ``real`` -- boolean. Set one of these
          arguments to ``True`` to ensure that the variable gets the
          corresponding type.

        - ``nonnegative`` -- boolean (default: ``False``); whether the
          variable should be assumed to be nonnegative. Rather useless
          for the binary type

        - ``name`` -- string; associates a name to the variable. This
          is only useful when exporting the linear program to a file
          using ``write_mps`` or ``write_lp``, and has no other
          effect.

        - ``indices`` -- (optional) an iterable of keys; components
          corresponding to these keys are created in order,
          and access to components with other keys will raise an
          error; otherwise components of this variable can be
          indexed by arbitrary keys and are created dynamically
          on access

        OUTPUT:

        A new instance of :class:`MIPVariable` associated to the
        current :class:`MixedIntegerLinearProgram`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(); x
            MIPVariable with 0 real components
            sage: x0 = x[0]; x0
            x_0

        By default, variables are unbounded::

            sage: print(p.get_min(x0))
            None
            sage: print(p.get_max(x0))
            None

        To define two dictionaries of variables, the first being
        of real type, and the second of integer type ::

            sage: x = p.new_variable(real=True, nonnegative=True)
            sage: y = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(x[2] + y[3,5], max=2)
            sage: p.is_integer(x[2])
            False
            sage: p.is_integer(y[3,5])
            True

        An exception is raised when two types are supplied ::

            sage: z = p.new_variable(real=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: Exactly one of the available types has to be True

        Unbounded variables::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(real=True)
            sage: y = p.new_variable(integer=True)
            sage: p.add_constraint(x[0] + x[3] <= 8)
            sage: p.add_constraint(y[0] >= y[1])
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 8.0
              - x_2 + x_3 <= 0.0
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)
              x_2 is an integer variable (min=-oo, max=+oo)
              x_3 is an integer variable (min=-oo, max=+oo)

        On the Sage command line, generator syntax is accepted as a
        shorthand for generating new variables with default settings::

            sage: mip.<x, y, z> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: mip.add_constraint(x[0] + y[1] + z[2] <= 10)
            sage: mip.show()
            Constraints:
              x[0] + y[1] + z[2] <= 10.0
            Variables:
              x[0] = x_0 is a continuous variable (min=-oo, max=+oo)
              y[1] = x_1 is a continuous variable (min=-oo, max=+oo)
              z[2] = x_2 is a continuous variable (min=-oo, max=+oo)'''
    @overload
    def new_variable(self, real=...) -> Any:
        '''MixedIntegerLinearProgram.new_variable(self, real=False, binary=False, integer=False, nonnegative=False, name=\'\', indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 717)

        Return a new :class:`MIPVariable` instance.

        A new variable ``x`` is defined by::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)

        It behaves exactly as a usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        .. SEEALSO::

            - :meth:`set_min`, :meth:`get_min` -- set/get the lower bound of a
              variable

            - :meth:`set_max`, :meth:`get_max` -- set/get the upper bound of a
              variable

        INPUT:

        - ``binary``, ``integer``, ``real`` -- boolean. Set one of these
          arguments to ``True`` to ensure that the variable gets the
          corresponding type.

        - ``nonnegative`` -- boolean (default: ``False``); whether the
          variable should be assumed to be nonnegative. Rather useless
          for the binary type

        - ``name`` -- string; associates a name to the variable. This
          is only useful when exporting the linear program to a file
          using ``write_mps`` or ``write_lp``, and has no other
          effect.

        - ``indices`` -- (optional) an iterable of keys; components
          corresponding to these keys are created in order,
          and access to components with other keys will raise an
          error; otherwise components of this variable can be
          indexed by arbitrary keys and are created dynamically
          on access

        OUTPUT:

        A new instance of :class:`MIPVariable` associated to the
        current :class:`MixedIntegerLinearProgram`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(); x
            MIPVariable with 0 real components
            sage: x0 = x[0]; x0
            x_0

        By default, variables are unbounded::

            sage: print(p.get_min(x0))
            None
            sage: print(p.get_max(x0))
            None

        To define two dictionaries of variables, the first being
        of real type, and the second of integer type ::

            sage: x = p.new_variable(real=True, nonnegative=True)
            sage: y = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(x[2] + y[3,5], max=2)
            sage: p.is_integer(x[2])
            False
            sage: p.is_integer(y[3,5])
            True

        An exception is raised when two types are supplied ::

            sage: z = p.new_variable(real=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: Exactly one of the available types has to be True

        Unbounded variables::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(real=True)
            sage: y = p.new_variable(integer=True)
            sage: p.add_constraint(x[0] + x[3] <= 8)
            sage: p.add_constraint(y[0] >= y[1])
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 8.0
              - x_2 + x_3 <= 0.0
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)
              x_2 is an integer variable (min=-oo, max=+oo)
              x_3 is an integer variable (min=-oo, max=+oo)

        On the Sage command line, generator syntax is accepted as a
        shorthand for generating new variables with default settings::

            sage: mip.<x, y, z> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: mip.add_constraint(x[0] + y[1] + z[2] <= 10)
            sage: mip.show()
            Constraints:
              x[0] + y[1] + z[2] <= 10.0
            Variables:
              x[0] = x_0 is a continuous variable (min=-oo, max=+oo)
              y[1] = x_1 is a continuous variable (min=-oo, max=+oo)
              z[2] = x_2 is a continuous variable (min=-oo, max=+oo)'''
    @overload
    def new_variable(self, integer=...) -> Any:
        '''MixedIntegerLinearProgram.new_variable(self, real=False, binary=False, integer=False, nonnegative=False, name=\'\', indices=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 717)

        Return a new :class:`MIPVariable` instance.

        A new variable ``x`` is defined by::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(nonnegative=True)

        It behaves exactly as a usual dictionary would. It can use any key
        argument you may like, as ``x[5]`` or ``x["b"]``, and has methods
        ``items()`` and ``keys()``.

        .. SEEALSO::

            - :meth:`set_min`, :meth:`get_min` -- set/get the lower bound of a
              variable

            - :meth:`set_max`, :meth:`get_max` -- set/get the upper bound of a
              variable

        INPUT:

        - ``binary``, ``integer``, ``real`` -- boolean. Set one of these
          arguments to ``True`` to ensure that the variable gets the
          corresponding type.

        - ``nonnegative`` -- boolean (default: ``False``); whether the
          variable should be assumed to be nonnegative. Rather useless
          for the binary type

        - ``name`` -- string; associates a name to the variable. This
          is only useful when exporting the linear program to a file
          using ``write_mps`` or ``write_lp``, and has no other
          effect.

        - ``indices`` -- (optional) an iterable of keys; components
          corresponding to these keys are created in order,
          and access to components with other keys will raise an
          error; otherwise components of this variable can be
          indexed by arbitrary keys and are created dynamically
          on access

        OUTPUT:

        A new instance of :class:`MIPVariable` associated to the
        current :class:`MixedIntegerLinearProgram`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(); x
            MIPVariable with 0 real components
            sage: x0 = x[0]; x0
            x_0

        By default, variables are unbounded::

            sage: print(p.get_min(x0))
            None
            sage: print(p.get_max(x0))
            None

        To define two dictionaries of variables, the first being
        of real type, and the second of integer type ::

            sage: x = p.new_variable(real=True, nonnegative=True)
            sage: y = p.new_variable(integer=True, nonnegative=True)
            sage: p.add_constraint(x[2] + y[3,5], max=2)
            sage: p.is_integer(x[2])
            False
            sage: p.is_integer(y[3,5])
            True

        An exception is raised when two types are supplied ::

            sage: z = p.new_variable(real=True, integer=True)
            Traceback (most recent call last):
            ...
            ValueError: Exactly one of the available types has to be True

        Unbounded variables::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: x = p.new_variable(real=True)
            sage: y = p.new_variable(integer=True)
            sage: p.add_constraint(x[0] + x[3] <= 8)
            sage: p.add_constraint(y[0] >= y[1])
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 8.0
              - x_2 + x_3 <= 0.0
            Variables:
              x_0 is a continuous variable (min=-oo, max=+oo)
              x_1 is a continuous variable (min=-oo, max=+oo)
              x_2 is an integer variable (min=-oo, max=+oo)
              x_3 is an integer variable (min=-oo, max=+oo)

        On the Sage command line, generator syntax is accepted as a
        shorthand for generating new variables with default settings::

            sage: mip.<x, y, z> = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: mip.add_constraint(x[0] + y[1] + z[2] <= 10)
            sage: mip.show()
            Constraints:
              x[0] + y[1] + z[2] <= 10.0
            Variables:
              x[0] = x_0 is a continuous variable (min=-oo, max=+oo)
              y[1] = x_1 is a continuous variable (min=-oo, max=+oo)
              z[2] = x_2 is a continuous variable (min=-oo, max=+oo)'''
    @overload
    def number_of_constraints(self) -> int:
        """MixedIntegerLinearProgram.number_of_constraints(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 892)

        Return the number of constraints assigned so far.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.add_constraint(p[0] - 2*p[1], min=1)
            sage: p.number_of_constraints()
            2"""
    @overload
    def number_of_constraints(self) -> Any:
        """MixedIntegerLinearProgram.number_of_constraints(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 892)

        Return the number of constraints assigned so far.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.add_constraint(p[0] - 2*p[1], min=1)
            sage: p.number_of_constraints()
            2"""
    def number_of_variables(self) -> int:
        """MixedIntegerLinearProgram.number_of_variables(self) -> int

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 906)

        Return the number of variables used so far.

        Note that this is backend-dependent, i.e. we count solver's
        variables rather than user's variables. An example of the latter
        can be seen below: Gurobi converts double inequalities,
        i.e. inequalities like `m <= c^T x <= M`, with `m<M`, into
        equations, by adding extra variables: `c^T x + y = M`, `0 <= y
        <= M-m`.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(p[0] - p[2], max=4)
            sage: p.number_of_variables()
            2
            sage: p.add_constraint(p[0] - 2*p[1], min=1)
            sage: p.number_of_variables()
            3
            sage: p = MixedIntegerLinearProgram(solver='glpk')
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)
            sage: p.number_of_variables()
            2
            sage: p = MixedIntegerLinearProgram(solver='gurobi')   # optional - Gurobi
            sage: p.add_constraint(p[0] - p[2], min=1, max=4)      # optional - Gurobi
            sage: p.number_of_variables()                          # optional - Gurobi
            3"""
    @overload
    def polyhedron(self, **kwds) -> Any:
        """MixedIntegerLinearProgram.polyhedron(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1037)

        Return the polyhedron defined by the Linear Program.

        INPUT:

        All arguments given to this method are forwarded to the constructor of
        the :func:`Polyhedron` class.

        OUTPUT:

        A :func:`Polyhedron` object whose `i`-th variable represents the `i`-th
        variable of ``self``.

        .. warning::

            The polyhedron is built from the variables stored by the LP solver
            (i.e. the output of :meth:`show`). While they usually match the ones
            created explicitly when defining the LP, a solver like Gurobi has
            been known to introduce additional variables to store constraints of
            the type ``lower_bound <= linear_function <= upper bound``. You
            should be fine if you did not install Gurobi or if you do not use it
            as a solver, but keep an eye on the number of variables in the
            polyhedron, or on the output of :meth:`show`. Just in case.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.to_linear_program`
            -- return the :class:`MixedIntegerLinearProgram` object associated
            with a :func:`Polyhedron` object.

        EXAMPLES:

        A LP on two variables::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] <= 1)
            sage: p.add_constraint(0 <= 3*p['y'] + p['x'] <= 2)
            sage: P = p.polyhedron(); P
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        3-D Polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] + 3*p['z'] <= 1)
            sage: p.add_constraint(0 <= 2*p['y'] + p['z'] + 3*p['x'] <= 1)
            sage: p.add_constraint(0 <= 2*p['z'] + p['x'] + 3*p['y'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 8 vertices

        An empty polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(2*v['x'] + v['y'] + 3*v['z'] <= 1)
            sage: p.add_constraint(2*v['y'] + v['z'] + 3*v['x'] <= 1)
            sage: p.add_constraint(2*v['z'] + v['x'] + 3*v['y'] >= 2)
            sage: P = p.polyhedron(); P
            The empty polyhedron in RDF^3

        An unbounded polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(2*p['x'] + p['y'] - p['z'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 1 vertex, 1 ray, 2 lines

        A square (see :issue:`14395`) ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        We can also use a backend that supports exact arithmetic::

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        TESTS:

        Check if :issue:`23326` is fixed::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p['x'], p['y']
            sage: p.set_min(x, 0); p.set_min(y, 0)
            sage: p.set_objective(3.5*x + 2.5*y)
            sage: p.add_constraint(x + y <= 10)
            sage: p.add_constraint(18.5*x + 5.1*y <= 110.3)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices"""
    @overload
    def polyhedron(self) -> Any:
        """MixedIntegerLinearProgram.polyhedron(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1037)

        Return the polyhedron defined by the Linear Program.

        INPUT:

        All arguments given to this method are forwarded to the constructor of
        the :func:`Polyhedron` class.

        OUTPUT:

        A :func:`Polyhedron` object whose `i`-th variable represents the `i`-th
        variable of ``self``.

        .. warning::

            The polyhedron is built from the variables stored by the LP solver
            (i.e. the output of :meth:`show`). While they usually match the ones
            created explicitly when defining the LP, a solver like Gurobi has
            been known to introduce additional variables to store constraints of
            the type ``lower_bound <= linear_function <= upper bound``. You
            should be fine if you did not install Gurobi or if you do not use it
            as a solver, but keep an eye on the number of variables in the
            polyhedron, or on the output of :meth:`show`. Just in case.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.to_linear_program`
            -- return the :class:`MixedIntegerLinearProgram` object associated
            with a :func:`Polyhedron` object.

        EXAMPLES:

        A LP on two variables::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] <= 1)
            sage: p.add_constraint(0 <= 3*p['y'] + p['x'] <= 2)
            sage: P = p.polyhedron(); P
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        3-D Polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] + 3*p['z'] <= 1)
            sage: p.add_constraint(0 <= 2*p['y'] + p['z'] + 3*p['x'] <= 1)
            sage: p.add_constraint(0 <= 2*p['z'] + p['x'] + 3*p['y'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 8 vertices

        An empty polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(2*v['x'] + v['y'] + 3*v['z'] <= 1)
            sage: p.add_constraint(2*v['y'] + v['z'] + 3*v['x'] <= 1)
            sage: p.add_constraint(2*v['z'] + v['x'] + 3*v['y'] >= 2)
            sage: P = p.polyhedron(); P
            The empty polyhedron in RDF^3

        An unbounded polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(2*p['x'] + p['y'] - p['z'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 1 vertex, 1 ray, 2 lines

        A square (see :issue:`14395`) ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        We can also use a backend that supports exact arithmetic::

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        TESTS:

        Check if :issue:`23326` is fixed::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p['x'], p['y']
            sage: p.set_min(x, 0); p.set_min(y, 0)
            sage: p.set_objective(3.5*x + 2.5*y)
            sage: p.add_constraint(x + y <= 10)
            sage: p.add_constraint(18.5*x + 5.1*y <= 110.3)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices"""
    @overload
    def polyhedron(self) -> Any:
        """MixedIntegerLinearProgram.polyhedron(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1037)

        Return the polyhedron defined by the Linear Program.

        INPUT:

        All arguments given to this method are forwarded to the constructor of
        the :func:`Polyhedron` class.

        OUTPUT:

        A :func:`Polyhedron` object whose `i`-th variable represents the `i`-th
        variable of ``self``.

        .. warning::

            The polyhedron is built from the variables stored by the LP solver
            (i.e. the output of :meth:`show`). While they usually match the ones
            created explicitly when defining the LP, a solver like Gurobi has
            been known to introduce additional variables to store constraints of
            the type ``lower_bound <= linear_function <= upper bound``. You
            should be fine if you did not install Gurobi or if you do not use it
            as a solver, but keep an eye on the number of variables in the
            polyhedron, or on the output of :meth:`show`. Just in case.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.to_linear_program`
            -- return the :class:`MixedIntegerLinearProgram` object associated
            with a :func:`Polyhedron` object.

        EXAMPLES:

        A LP on two variables::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] <= 1)
            sage: p.add_constraint(0 <= 3*p['y'] + p['x'] <= 2)
            sage: P = p.polyhedron(); P
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        3-D Polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] + 3*p['z'] <= 1)
            sage: p.add_constraint(0 <= 2*p['y'] + p['z'] + 3*p['x'] <= 1)
            sage: p.add_constraint(0 <= 2*p['z'] + p['x'] + 3*p['y'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 8 vertices

        An empty polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(2*v['x'] + v['y'] + 3*v['z'] <= 1)
            sage: p.add_constraint(2*v['y'] + v['z'] + 3*v['x'] <= 1)
            sage: p.add_constraint(2*v['z'] + v['x'] + 3*v['y'] >= 2)
            sage: P = p.polyhedron(); P
            The empty polyhedron in RDF^3

        An unbounded polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(2*p['x'] + p['y'] - p['z'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 1 vertex, 1 ray, 2 lines

        A square (see :issue:`14395`) ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        We can also use a backend that supports exact arithmetic::

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        TESTS:

        Check if :issue:`23326` is fixed::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p['x'], p['y']
            sage: p.set_min(x, 0); p.set_min(y, 0)
            sage: p.set_objective(3.5*x + 2.5*y)
            sage: p.add_constraint(x + y <= 10)
            sage: p.add_constraint(18.5*x + 5.1*y <= 110.3)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices"""
    @overload
    def polyhedron(self) -> Any:
        """MixedIntegerLinearProgram.polyhedron(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1037)

        Return the polyhedron defined by the Linear Program.

        INPUT:

        All arguments given to this method are forwarded to the constructor of
        the :func:`Polyhedron` class.

        OUTPUT:

        A :func:`Polyhedron` object whose `i`-th variable represents the `i`-th
        variable of ``self``.

        .. warning::

            The polyhedron is built from the variables stored by the LP solver
            (i.e. the output of :meth:`show`). While they usually match the ones
            created explicitly when defining the LP, a solver like Gurobi has
            been known to introduce additional variables to store constraints of
            the type ``lower_bound <= linear_function <= upper bound``. You
            should be fine if you did not install Gurobi or if you do not use it
            as a solver, but keep an eye on the number of variables in the
            polyhedron, or on the output of :meth:`show`. Just in case.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.to_linear_program`
            -- return the :class:`MixedIntegerLinearProgram` object associated
            with a :func:`Polyhedron` object.

        EXAMPLES:

        A LP on two variables::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] <= 1)
            sage: p.add_constraint(0 <= 3*p['y'] + p['x'] <= 2)
            sage: P = p.polyhedron(); P
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        3-D Polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] + 3*p['z'] <= 1)
            sage: p.add_constraint(0 <= 2*p['y'] + p['z'] + 3*p['x'] <= 1)
            sage: p.add_constraint(0 <= 2*p['z'] + p['x'] + 3*p['y'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 8 vertices

        An empty polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(2*v['x'] + v['y'] + 3*v['z'] <= 1)
            sage: p.add_constraint(2*v['y'] + v['z'] + 3*v['x'] <= 1)
            sage: p.add_constraint(2*v['z'] + v['x'] + 3*v['y'] >= 2)
            sage: P = p.polyhedron(); P
            The empty polyhedron in RDF^3

        An unbounded polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(2*p['x'] + p['y'] - p['z'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 1 vertex, 1 ray, 2 lines

        A square (see :issue:`14395`) ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        We can also use a backend that supports exact arithmetic::

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        TESTS:

        Check if :issue:`23326` is fixed::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p['x'], p['y']
            sage: p.set_min(x, 0); p.set_min(y, 0)
            sage: p.set_objective(3.5*x + 2.5*y)
            sage: p.add_constraint(x + y <= 10)
            sage: p.add_constraint(18.5*x + 5.1*y <= 110.3)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices"""
    @overload
    def polyhedron(self) -> Any:
        """MixedIntegerLinearProgram.polyhedron(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1037)

        Return the polyhedron defined by the Linear Program.

        INPUT:

        All arguments given to this method are forwarded to the constructor of
        the :func:`Polyhedron` class.

        OUTPUT:

        A :func:`Polyhedron` object whose `i`-th variable represents the `i`-th
        variable of ``self``.

        .. warning::

            The polyhedron is built from the variables stored by the LP solver
            (i.e. the output of :meth:`show`). While they usually match the ones
            created explicitly when defining the LP, a solver like Gurobi has
            been known to introduce additional variables to store constraints of
            the type ``lower_bound <= linear_function <= upper bound``. You
            should be fine if you did not install Gurobi or if you do not use it
            as a solver, but keep an eye on the number of variables in the
            polyhedron, or on the output of :meth:`show`. Just in case.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.to_linear_program`
            -- return the :class:`MixedIntegerLinearProgram` object associated
            with a :func:`Polyhedron` object.

        EXAMPLES:

        A LP on two variables::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] <= 1)
            sage: p.add_constraint(0 <= 3*p['y'] + p['x'] <= 2)
            sage: P = p.polyhedron(); P
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        3-D Polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] + 3*p['z'] <= 1)
            sage: p.add_constraint(0 <= 2*p['y'] + p['z'] + 3*p['x'] <= 1)
            sage: p.add_constraint(0 <= 2*p['z'] + p['x'] + 3*p['y'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 8 vertices

        An empty polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(2*v['x'] + v['y'] + 3*v['z'] <= 1)
            sage: p.add_constraint(2*v['y'] + v['z'] + 3*v['x'] <= 1)
            sage: p.add_constraint(2*v['z'] + v['x'] + 3*v['y'] >= 2)
            sage: P = p.polyhedron(); P
            The empty polyhedron in RDF^3

        An unbounded polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(2*p['x'] + p['y'] - p['z'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 1 vertex, 1 ray, 2 lines

        A square (see :issue:`14395`) ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        We can also use a backend that supports exact arithmetic::

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        TESTS:

        Check if :issue:`23326` is fixed::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p['x'], p['y']
            sage: p.set_min(x, 0); p.set_min(y, 0)
            sage: p.set_objective(3.5*x + 2.5*y)
            sage: p.add_constraint(x + y <= 10)
            sage: p.add_constraint(18.5*x + 5.1*y <= 110.3)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices"""
    @overload
    def polyhedron(self) -> Any:
        """MixedIntegerLinearProgram.polyhedron(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1037)

        Return the polyhedron defined by the Linear Program.

        INPUT:

        All arguments given to this method are forwarded to the constructor of
        the :func:`Polyhedron` class.

        OUTPUT:

        A :func:`Polyhedron` object whose `i`-th variable represents the `i`-th
        variable of ``self``.

        .. warning::

            The polyhedron is built from the variables stored by the LP solver
            (i.e. the output of :meth:`show`). While they usually match the ones
            created explicitly when defining the LP, a solver like Gurobi has
            been known to introduce additional variables to store constraints of
            the type ``lower_bound <= linear_function <= upper bound``. You
            should be fine if you did not install Gurobi or if you do not use it
            as a solver, but keep an eye on the number of variables in the
            polyhedron, or on the output of :meth:`show`. Just in case.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.to_linear_program`
            -- return the :class:`MixedIntegerLinearProgram` object associated
            with a :func:`Polyhedron` object.

        EXAMPLES:

        A LP on two variables::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] <= 1)
            sage: p.add_constraint(0 <= 3*p['y'] + p['x'] <= 2)
            sage: P = p.polyhedron(); P
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        3-D Polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] + 3*p['z'] <= 1)
            sage: p.add_constraint(0 <= 2*p['y'] + p['z'] + 3*p['x'] <= 1)
            sage: p.add_constraint(0 <= 2*p['z'] + p['x'] + 3*p['y'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 8 vertices

        An empty polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(2*v['x'] + v['y'] + 3*v['z'] <= 1)
            sage: p.add_constraint(2*v['y'] + v['z'] + 3*v['x'] <= 1)
            sage: p.add_constraint(2*v['z'] + v['x'] + 3*v['y'] >= 2)
            sage: P = p.polyhedron(); P
            The empty polyhedron in RDF^3

        An unbounded polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(2*p['x'] + p['y'] - p['z'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 1 vertex, 1 ray, 2 lines

        A square (see :issue:`14395`) ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        We can also use a backend that supports exact arithmetic::

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        TESTS:

        Check if :issue:`23326` is fixed::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p['x'], p['y']
            sage: p.set_min(x, 0); p.set_min(y, 0)
            sage: p.set_objective(3.5*x + 2.5*y)
            sage: p.add_constraint(x + y <= 10)
            sage: p.add_constraint(18.5*x + 5.1*y <= 110.3)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices"""
    @overload
    def polyhedron(self) -> Any:
        """MixedIntegerLinearProgram.polyhedron(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1037)

        Return the polyhedron defined by the Linear Program.

        INPUT:

        All arguments given to this method are forwarded to the constructor of
        the :func:`Polyhedron` class.

        OUTPUT:

        A :func:`Polyhedron` object whose `i`-th variable represents the `i`-th
        variable of ``self``.

        .. warning::

            The polyhedron is built from the variables stored by the LP solver
            (i.e. the output of :meth:`show`). While they usually match the ones
            created explicitly when defining the LP, a solver like Gurobi has
            been known to introduce additional variables to store constraints of
            the type ``lower_bound <= linear_function <= upper bound``. You
            should be fine if you did not install Gurobi or if you do not use it
            as a solver, but keep an eye on the number of variables in the
            polyhedron, or on the output of :meth:`show`. Just in case.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.to_linear_program`
            -- return the :class:`MixedIntegerLinearProgram` object associated
            with a :func:`Polyhedron` object.

        EXAMPLES:

        A LP on two variables::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] <= 1)
            sage: p.add_constraint(0 <= 3*p['y'] + p['x'] <= 2)
            sage: P = p.polyhedron(); P
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        3-D Polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] + 3*p['z'] <= 1)
            sage: p.add_constraint(0 <= 2*p['y'] + p['z'] + 3*p['x'] <= 1)
            sage: p.add_constraint(0 <= 2*p['z'] + p['x'] + 3*p['y'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 8 vertices

        An empty polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(2*v['x'] + v['y'] + 3*v['z'] <= 1)
            sage: p.add_constraint(2*v['y'] + v['z'] + 3*v['x'] <= 1)
            sage: p.add_constraint(2*v['z'] + v['x'] + 3*v['y'] >= 2)
            sage: P = p.polyhedron(); P
            The empty polyhedron in RDF^3

        An unbounded polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(2*p['x'] + p['y'] - p['z'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 1 vertex, 1 ray, 2 lines

        A square (see :issue:`14395`) ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        We can also use a backend that supports exact arithmetic::

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        TESTS:

        Check if :issue:`23326` is fixed::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p['x'], p['y']
            sage: p.set_min(x, 0); p.set_min(y, 0)
            sage: p.set_objective(3.5*x + 2.5*y)
            sage: p.add_constraint(x + y <= 10)
            sage: p.add_constraint(18.5*x + 5.1*y <= 110.3)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices"""
    @overload
    def polyhedron(self) -> Any:
        """MixedIntegerLinearProgram.polyhedron(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1037)

        Return the polyhedron defined by the Linear Program.

        INPUT:

        All arguments given to this method are forwarded to the constructor of
        the :func:`Polyhedron` class.

        OUTPUT:

        A :func:`Polyhedron` object whose `i`-th variable represents the `i`-th
        variable of ``self``.

        .. warning::

            The polyhedron is built from the variables stored by the LP solver
            (i.e. the output of :meth:`show`). While they usually match the ones
            created explicitly when defining the LP, a solver like Gurobi has
            been known to introduce additional variables to store constraints of
            the type ``lower_bound <= linear_function <= upper bound``. You
            should be fine if you did not install Gurobi or if you do not use it
            as a solver, but keep an eye on the number of variables in the
            polyhedron, or on the output of :meth:`show`. Just in case.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.to_linear_program`
            -- return the :class:`MixedIntegerLinearProgram` object associated
            with a :func:`Polyhedron` object.

        EXAMPLES:

        A LP on two variables::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] <= 1)
            sage: p.add_constraint(0 <= 3*p['y'] + p['x'] <= 2)
            sage: P = p.polyhedron(); P
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        3-D Polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(0 <= 2*p['x'] + p['y'] + 3*p['z'] <= 1)
            sage: p.add_constraint(0 <= 2*p['y'] + p['z'] + 3*p['x'] <= 1)
            sage: p.add_constraint(0 <= 2*p['z'] + p['x'] + 3*p['y'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 8 vertices

        An empty polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(2*v['x'] + v['y'] + 3*v['z'] <= 1)
            sage: p.add_constraint(2*v['y'] + v['z'] + 3*v['x'] <= 1)
            sage: p.add_constraint(2*v['z'] + v['x'] + 3*v['y'] >= 2)
            sage: P = p.polyhedron(); P
            The empty polyhedron in RDF^3

        An unbounded polyhedron::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.add_constraint(2*p['x'] + p['y'] - p['z'] <= 1)
            sage: P = p.polyhedron(); P
            A 3-dimensional polyhedron in RDF^3 defined as the convex hull of 1 vertex, 1 ray, 2 lines

        A square (see :issue:`14395`) ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices

        We can also use a backend that supports exact arithmetic::

            sage: p = MixedIntegerLinearProgram(solver='PPL')
            sage: x,y = p['x'], p['y']
            sage: p.add_constraint(x <= 1)
            sage: p.add_constraint(x >= -1)
            sage: p.add_constraint(y <= 1)
            sage: p.add_constraint(y >= -1)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        TESTS:

        Check if :issue:`23326` is fixed::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p['x'], p['y']
            sage: p.set_min(x, 0); p.set_min(y, 0)
            sage: p.set_objective(3.5*x + 2.5*y)
            sage: p.add_constraint(x + y <= 10)
            sage: p.add_constraint(18.5*x + 5.1*y <= 110.3)
            sage: p.polyhedron()
            A 2-dimensional polyhedron in RDF^2 defined as the convex hull of 4 vertices"""
    def remove_constraint(self, inti) -> Any:
        """MixedIntegerLinearProgram.remove_constraint(self, int i)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2268)

        Removes a constraint from ``self``.

        INPUT:

        - ``i`` -- index of the constraint to remove

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p[0], p[1]
            sage: p.add_constraint(x + y, max=10)
            sage: p.add_constraint(x - y, max=0)
            sage: p.add_constraint(x, max=4)
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 10.0
              x_0 - x_1 <= 0.0
              x_0 <= 4.0
            ...
            sage: p.remove_constraint(1)
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 10.0
              x_0 <= 4.0
            ...
            sage: p.number_of_constraints()
            2"""
    def remove_constraints(self, constraints) -> Any:
        """MixedIntegerLinearProgram.remove_constraints(self, constraints)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2302)

        Remove several constraints.

        INPUT:

        - ``constraints`` -- an iterable containing the indices of the rows to remove

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p[0], p[1]
            sage: p.add_constraint(x + y, max=10)
            sage: p.add_constraint(x - y, max=0)
            sage: p.add_constraint(x, max=4)
            sage: p.show()
            Constraints:
              x_0 + x_1 <= 10.0
              x_0 - x_1 <= 0.0
              x_0 <= 4.0
            ...
            sage: p.remove_constraints([0, 1])
            sage: p.show()
            Constraints:
              x_0 <= 4.0
            ...
            sage: p.number_of_constraints()
            1

        When checking for redundant constraints, make sure you remove only
        the constraints that were actually added. Problems could arise if
        you have a function that builds lps non-interactively, but it fails
        to check whether adding a constraint actually increases the number of
        constraints. The function might later try to remove constraints that
        are not actually there::

            sage: p = MixedIntegerLinearProgram(check_redundant=True, solver='GLPK')
            sage: x, y = p[0], p[1]
            sage: p.add_constraint(x + y, max=10)
            sage: for each in range(10):
            ....:     p.add_constraint(x - y, max=10)
            sage: p.add_constraint(x, max=4)
            sage: p.number_of_constraints()
            3
            sage: p.remove_constraints(range(1, 9))
            Traceback (most recent call last):
            ...
            IndexError: pop index out of range
            sage: p.remove_constraint(1)
            sage: p.number_of_constraints()
            2

        We should now be able to add the old constraint back in::

            sage: for each in range(10):
            ....:     p.add_constraint(x - y, max=10)
            sage: p.number_of_constraints()
            3

        TESTS:

        Removing no constraints does not make Sage crash, see
        :issue:`34881`::

             sage: MixedIntegerLinearProgram().remove_constraints([])"""
    @overload
    def set_binary(self, ee) -> Any:
        """MixedIntegerLinearProgram.set_binary(self, ee)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2374)

        Set a variable or a ``MIPVariable`` as binary.

        INPUT:

        - ``ee`` -- an instance of ``MIPVariable`` or one of
          its elements

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)

        With the following instruction, all the variables
        from x will be binary::

            sage: p.set_binary(x)
            sage: p.set_objective(x[0] + x[1])
            sage: p.add_constraint(-3*x[0] + 2*x[1], max=2)

        It is still possible, though, to set one of these
        variables as integer while keeping the others as they are::

            sage: p.set_integer(x[3])"""
    @overload
    def set_binary(self, x) -> Any:
        """MixedIntegerLinearProgram.set_binary(self, ee)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2374)

        Set a variable or a ``MIPVariable`` as binary.

        INPUT:

        - ``ee`` -- an instance of ``MIPVariable`` or one of
          its elements

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)

        With the following instruction, all the variables
        from x will be binary::

            sage: p.set_binary(x)
            sage: p.set_objective(x[0] + x[1])
            sage: p.add_constraint(-3*x[0] + 2*x[1], max=2)

        It is still possible, though, to set one of these
        variables as integer while keeping the others as they are::

            sage: p.set_integer(x[3])"""
    @overload
    def set_integer(self, ee) -> Any:
        """MixedIntegerLinearProgram.set_integer(self, ee)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2436)

        Set a variable or a ``MIPVariable`` as integer.

        INPUT:

        - ``ee`` -- an instance of ``MIPVariable`` or one of
          its elements

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)

        With the following instruction, all the variables
        from x will be integers::

            sage: p.set_integer(x)
            sage: p.set_objective(x[0] + x[1])
            sage: p.add_constraint(-3*x[0] + 2*x[1], max=2)

        It is still possible, though, to set one of these
        variables as binary while keeping the others as they are::

            sage: p.set_binary(x[3])"""
    @overload
    def set_integer(self, x) -> Any:
        """MixedIntegerLinearProgram.set_integer(self, ee)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2436)

        Set a variable or a ``MIPVariable`` as integer.

        INPUT:

        - ``ee`` -- an instance of ``MIPVariable`` or one of
          its elements

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)

        With the following instruction, all the variables
        from x will be integers::

            sage: p.set_integer(x)
            sage: p.set_objective(x[0] + x[1])
            sage: p.add_constraint(-3*x[0] + 2*x[1], max=2)

        It is still possible, though, to set one of these
        variables as binary while keeping the others as they are::

            sage: p.set_binary(x[3])"""
    def set_max(self, v, max) -> Any:
        """MixedIntegerLinearProgram.set_max(self, v, max)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2688)

        Set the maximum value of a variable.

        INPUT:

        - ``v`` -- a variable

        - ``max`` -- the maximum value the variable can take; when
          ``max=None``, the variable has no upper bound

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[1])
            sage: p.get_max(v[1])
            sage: p.set_max(v[1],6)
            sage: p.get_max(v[1])
            6.0

        With a :class:`MIPVariable` as an argument::

            sage: vv = p.new_variable(real=True)
            sage: p.get_max(vv)
            sage: p.get_max(vv[0])
            sage: p.set_max(vv,5)
            sage: p.get_max(vv[0])
            5.0
            sage: p.get_max(vv[9])
            5.0"""
    def set_min(self, v, min) -> Any:
        """MixedIntegerLinearProgram.set_min(self, v, min)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2644)

        Set the minimum value of a variable.

        INPUT:

        - ``v`` -- a variable

        - ``min`` -- the minimum value the variable can take; when
          ``min=None``, the variable has no lower bound

        .. SEEALSO::

            - :meth:`get_min` -- get the minimum value of a variable

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.set_objective(v[1])
            sage: p.get_min(v[1])
            0.0
            sage: p.set_min(v[1],6)
            sage: p.get_min(v[1])
            6.0
            sage: p.set_min(v[1], None)
            sage: p.get_min(v[1])

        With a :class:`MIPVariable` as an argument::

            sage: vv = p.new_variable(real=True)
            sage: p.get_min(vv)
            sage: p.get_min(vv[0])
            sage: p.set_min(vv,5)
            sage: p.get_min(vv[0])
            5.0
            sage: p.get_min(vv[9])
            5.0"""
    def set_objective(self, obj) -> Any:
        """MixedIntegerLinearProgram.set_objective(self, obj)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1804)

        Set the objective of the ``MixedIntegerLinearProgram``.

        INPUT:

        - ``obj`` -- a linear function to be optimized
          ( can also be set to ``None`` or ``0`` or any number when just
          looking for a feasible solution )

        EXAMPLES:

        Let's solve the following linear program::

            Maximize:
              x + 5 * y
            Constraints:
              x + 0.2 y       <= 4
              1.5 * x + 3 * y <= 4
            Variables:
              x is Real (min = 0, max = None)
              y is Real (min = 0, max = None)

        This linear program can be solved as follows::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + 5*x[2])
            sage: p.add_constraint(x[1] + 2/10*x[2], max=4)
            sage: p.add_constraint(1.5*x[1] + 3*x[2], max=4)
            sage: round(p.solve(),5)
            6.66667
            sage: p.set_objective(None)
            sage: _ = p.solve()

        TESTS:

        Test whether numbers as constant objective functions are accepted::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(42)
            sage: p.solve() # tol 1e-8
            42"""
    def set_problem_name(self, name) -> Any:
        '''MixedIntegerLinearProgram.set_problem_name(self, name)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 699)

        Set the name of the ``MixedIntegerLinearProgram``.

        INPUT:

        - ``name`` -- string representing the name of the
          ``MixedIntegerLinearProgram``

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.set_problem_name("Test program")
            sage: p
            Mixed Integer Program "Test program" (no objective, 0 variables, 0 constraints)'''
    def set_real(self, *args, **kwargs):
        """MixedIntegerLinearProgram.set_real(self, ee)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2498)

        Set a variable or a ``MIPVariable`` as real.

        INPUT:

        - ``ee`` -- an instance of ``MIPVariable`` or one of
          its elements

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)

        With the following instruction, all the variables
        from x will be real::

            sage: p.set_real(x)
            sage: p.set_objective(x[0] + x[1])
            sage: p.add_constraint(-3*x[0] + 2*x[1], max=2)

         It is still possible, though, to set one of these
         variables as binary while keeping the others as they are::

            sage: p.set_binary(x[3])"""
    @overload
    def show(self) -> Any:
        """MixedIntegerLinearProgram.show(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1194)

        Displays the ``MixedIntegerLinearProgram`` in a human-readable
        way.

        EXAMPLES:

        When constraints and variables have names ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(name='Hey')
            sage: p.set_objective(x[1] + x[2])
            sage: p.add_constraint(-3*x[1] + 2*x[2], max=2, name='Constraint_1')
            sage: p.show()
            Maximization:
              Hey[1] + Hey[2]
            Constraints:
              Constraint_1: -3.0 Hey[1] + 2.0 Hey[2] <= 2.0
            Variables:
              Hey[1] = x_0 is a continuous variable (min=-oo, max=+oo)
              Hey[2] = x_1 is a continuous variable (min=-oo, max=+oo)

        Without any names ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + x[2])
            sage: p.add_constraint(-3*x[1] + 2*x[2], max=2)
            sage: p.show()
            Maximization:
              x_0 + x_1
            Constraints:
              -3.0 x_0 + 2.0 x_1 <= 2.0
            Variables:
              x_0 is a continuous variable (min=0.0, max=+oo)
              x_1 is a continuous variable (min=0.0, max=+oo)

        With `\\QQ` coefficients::

            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + 1/2*x[2])
            sage: p.add_constraint(-3/5*x[1] + 2/7*x[2], max=2/5)
            sage: p.show()
            Maximization:
              x_0 + 1/2 x_1
            Constraints:
              constraint_0: -3/5 x_0 + 2/7 x_1 <= 2/5
            Variables:
              x_0 is a continuous variable (min=0, max=+oo)
              x_1 is a continuous variable (min=0, max=+oo)

        With a constant term in the objective::

            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 42)
            sage: p.show()
            Maximization:
              x_0 + 42
            Constraints:
            Variables:
              x_0 is a continuous variable (min=0, max=+oo)"""
    @overload
    def show(self) -> Any:
        """MixedIntegerLinearProgram.show(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1194)

        Displays the ``MixedIntegerLinearProgram`` in a human-readable
        way.

        EXAMPLES:

        When constraints and variables have names ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(name='Hey')
            sage: p.set_objective(x[1] + x[2])
            sage: p.add_constraint(-3*x[1] + 2*x[2], max=2, name='Constraint_1')
            sage: p.show()
            Maximization:
              Hey[1] + Hey[2]
            Constraints:
              Constraint_1: -3.0 Hey[1] + 2.0 Hey[2] <= 2.0
            Variables:
              Hey[1] = x_0 is a continuous variable (min=-oo, max=+oo)
              Hey[2] = x_1 is a continuous variable (min=-oo, max=+oo)

        Without any names ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + x[2])
            sage: p.add_constraint(-3*x[1] + 2*x[2], max=2)
            sage: p.show()
            Maximization:
              x_0 + x_1
            Constraints:
              -3.0 x_0 + 2.0 x_1 <= 2.0
            Variables:
              x_0 is a continuous variable (min=0.0, max=+oo)
              x_1 is a continuous variable (min=0.0, max=+oo)

        With `\\QQ` coefficients::

            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + 1/2*x[2])
            sage: p.add_constraint(-3/5*x[1] + 2/7*x[2], max=2/5)
            sage: p.show()
            Maximization:
              x_0 + 1/2 x_1
            Constraints:
              constraint_0: -3/5 x_0 + 2/7 x_1 <= 2/5
            Variables:
              x_0 is a continuous variable (min=0, max=+oo)
              x_1 is a continuous variable (min=0, max=+oo)

        With a constant term in the objective::

            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 42)
            sage: p.show()
            Maximization:
              x_0 + 42
            Constraints:
            Variables:
              x_0 is a continuous variable (min=0, max=+oo)"""
    @overload
    def show(self) -> Any:
        """MixedIntegerLinearProgram.show(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1194)

        Displays the ``MixedIntegerLinearProgram`` in a human-readable
        way.

        EXAMPLES:

        When constraints and variables have names ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(name='Hey')
            sage: p.set_objective(x[1] + x[2])
            sage: p.add_constraint(-3*x[1] + 2*x[2], max=2, name='Constraint_1')
            sage: p.show()
            Maximization:
              Hey[1] + Hey[2]
            Constraints:
              Constraint_1: -3.0 Hey[1] + 2.0 Hey[2] <= 2.0
            Variables:
              Hey[1] = x_0 is a continuous variable (min=-oo, max=+oo)
              Hey[2] = x_1 is a continuous variable (min=-oo, max=+oo)

        Without any names ::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + x[2])
            sage: p.add_constraint(-3*x[1] + 2*x[2], max=2)
            sage: p.show()
            Maximization:
              x_0 + x_1
            Constraints:
              -3.0 x_0 + 2.0 x_1 <= 2.0
            Variables:
              x_0 is a continuous variable (min=0.0, max=+oo)
              x_1 is a continuous variable (min=0.0, max=+oo)

        With `\\QQ` coefficients::

            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + 1/2*x[2])
            sage: p.add_constraint(-3/5*x[1] + 2/7*x[2], max=2/5)
            sage: p.show()
            Maximization:
              x_0 + 1/2 x_1
            Constraints:
              constraint_0: -3/5 x_0 + 2/7 x_1 <= 2/5
            Variables:
              x_0 is a continuous variable (min=0, max=+oo)
              x_1 is a continuous variable (min=0, max=+oo)

        With a constant term in the objective::

            sage: p = MixedIntegerLinearProgram(solver='ppl')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[0] + 42)
            sage: p.show()
            Maximization:
              x_0 + 42
            Constraints:
            Variables:
              x_0 is a continuous variable (min=0, max=+oo)"""
    def solve(self, *args, **kwargs):
        """MixedIntegerLinearProgram.solve(self, log=None, objective_only=False)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2564)

        Solve the ``MixedIntegerLinearProgram``.

        INPUT:

        - ``log`` -- integer (default: ``None``); the verbosity level. Indicates
          whether progress should be printed during computation. The solver is
          initialized to report no progress.

        - ``objective_only`` -- boolean:

          - When set to ``True``, only the objective function is returned.
          - When set to ``False`` (default), the optimal numerical values
            are stored (takes computational time).

        OUTPUT: the optimal value taken by the objective function

        .. WARNING::

            By default, no additional assumption is made on the domain of an LP
            variable. See :meth:`set_min` and :meth:`set_max` to change it.

        EXAMPLES:

        Consider the following linear program::

            Maximize:
              x + 5 * y
            Constraints:
              x + 0.2 y       <= 4
              1.5 * x + 3 * y <= 4
            Variables:
              x is Real (min = 0, max = None)
              y is Real (min = 0, max = None)

        This linear program can be solved as follows::

            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + 5*x[2])
            sage: p.add_constraint(x[1] + 0.2*x[2], max=4)
            sage: p.add_constraint(1.5*x[1] + 3*x[2], max=4)
            sage: round(p.solve(),6)
            6.666667
            sage: x = p.get_values(x)
            sage: round(x[1],6) # abs tol 1e-15
            0.0
            sage: round(x[2],6)
            1.333333

         Computation of a maximum stable set in Petersen's graph::

            sage: # needs sage.graphs
            sage: g = graphs.PetersenGraph()
            sage: p = MixedIntegerLinearProgram(maximization=True, solver='GLPK')
            sage: b = p.new_variable(nonnegative=True)
            sage: p.set_objective(sum([b[v] for v in g]))
            sage: for (u,v) in g.edges(sort=False, labels=None):
            ....:     p.add_constraint(b[u] + b[v], max=1)
            sage: p.set_binary(b)
            sage: p.solve(objective_only=True)
            4.0

        Constraints in the objective function are respected::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x, y = p[0], p[1]
            sage: p.add_constraint(2*x + 3*y, max=6)
            sage: p.add_constraint(3*x + 2*y, max=6)
            sage: p.set_objective(x + y + 7)
            sage: p.set_integer(x); p.set_integer(y)
            sage: p.solve()
            9.0"""
    def solver_parameter(self, name, value=...) -> Any:
        '''MixedIntegerLinearProgram.solver_parameter(self, name, value=None)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2784)

        Return or define a solver parameter.

        The solver parameters are by essence solver-specific, which means their
        meaning heavily depends on the solver used.

        (If you do not know which solver you are using, then you use GLPK).

        Aliases:

        Very common parameters have aliases making them solver-independent. For
        example, the following::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.solver_parameter("timelimit", 60)

        Sets the solver to stop its computations after 60 seconds, and works
        with GLPK, CPLEX , SCIP, and Gurobi.

            - ``\'timelimit\'`` -- defines the maximum time spent on a
              computation (measured in seconds)

        Another example is the ``\'logfile\'`` parameter, which is used to specify
        the file in which computation logs are recorded. By default, the logs
        are not recorded, and we can disable this feature providing an empty
        filename. This is currently working with CPLEX and Gurobi::

            sage: # optional - cplex
            sage: p = MixedIntegerLinearProgram(solver=\'CPLEX\')
            sage: p.solver_parameter("logfile")
            \'\'
            sage: p.solver_parameter("logfile", "/dev/null")
            sage: p.solver_parameter("logfile")
            \'/dev/null\'
            sage: p.solver_parameter("logfile", \'\')
            sage: p.solver_parameter("logfile")
            \'\'

        Solver-specific parameters:

            - GLPK : We have implemented very close to comprehensive coverage of
              the GLPK solver parameters for the simplex and integer
              optimization methods. For details, see the documentation of
              :meth:`GLPKBackend.solver_parameter
              <sage.numerical.backends.glpk_backend.GLPKBackend.solver_parameter>`.

            - CPLEX\'s parameters are identified by a string. Their
              list is available `on ILOG\'s website
              <http://publib.boulder.ibm.com/infocenter/odmeinfo/v3r4/index.jsp?topic=/ilog.odms.ide.odme.help/Content/Optimization/Documentation/ODME/_pubskel/ODME_pubskels/startall_ODME34_Eclipse1590.html>`_.

              The command ::

                  sage: p = MixedIntegerLinearProgram(solver=\'CPLEX\')   # optional - CPLEX
                  sage: p.solver_parameter("CPX_PARAM_TILIM", 60)       # optional - CPLEX

              works as intended.

            - Gurobi\'s parameters should all be available through this
              method. Their list is available on Gurobi\'s website
              `<http://www.gurobi.com/documentation/5.5/reference-manual/node798>`_.

              SCIP\'s parameter can be found here:
              `<http://scip.zib.de/doc-5.0.1/html/PARAMETERS.php>`_.

        INPUT:

        - ``name`` -- string; the parameter

        - ``value`` -- the parameter\'s value if it is to be defined,
          or ``None`` (default) to obtain its current value

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver=\'GLPK\')
            sage: p.solver_parameter("timelimit", 60)
            sage: p.solver_parameter("timelimit")
            60.0'''
    def sum(self, L) -> Any:
        """MixedIntegerLinearProgram.sum(self, L)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 2868)

        Efficiently compute the sum of a sequence of
        :class:`~sage.numerical.linear_functions.LinearFunction` elements

        INPUT:

        - ``mip`` -- the :class:`MixedIntegerLinearProgram` parent

        - ``L`` -- list of
          :class:`~sage.numerical.linear_functions.LinearFunction` instances

        .. NOTE::

            The use of the regular ``sum`` function is not recommended
            as it is much less efficient than this one

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)

        The following command::

            sage: s = p.sum(v[i] for i in range(90))

        is much more efficient than::

            sage: s = sum(v[i] for i in range(90))"""
    def write_lp(self, filename) -> Any:
        """MixedIntegerLinearProgram.write_lp(self, filename)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1365)

        Write the linear program as a LP file.

        This function export the problem as a LP file.

        INPUT:

        - ``filename`` -- the file in which you want the problem
          to be written

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + x[2])
            sage: p.add_constraint(-3*x[1] + 2*x[2], max=2)
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix='.lp') as f:
            ....:     p.write_lp(f.name)
            Writing problem data to ...
            9 lines were written

        For more information about the LP file format :
        http://lpsolve.sourceforge.net/5.5/lp-format.htm"""
    def write_mps(self, filename, modern=...) -> Any:
        """MixedIntegerLinearProgram.write_mps(self, filename, modern=True)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 1332)

        Write the linear program as a MPS file.

        This function export the problem as a MPS file.

        INPUT:

        - ``filename`` -- the file in which you want the problem
          to be written

        - ``modern`` -- lets you choose between Fixed MPS and Free MPS:

            - ``True`` -- outputs the problem in Free MPS
            - ``False`` -- outputs the problem in Fixed MPS

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: x = p.new_variable(nonnegative=True)
            sage: p.set_objective(x[1] + x[2])
            sage: p.add_constraint(-3*x[1] + 2*x[2], max=2, name='OneConstraint')
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix='.mps') as f:
            ....:     p.write_mps(f.name)
            Writing problem data to ...
            17 records were written

        For information about the MPS file format, see
        :wikipedia:`MPS_(format)`"""
    def __copy__(self) -> Any:
        """MixedIntegerLinearProgram.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 578)

        Return a copy of the current ``MixedIntegerLinearProgram`` instance.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: v = p.new_variable(nonnegative=True)
            sage: p.add_constraint(v[0] + v[1], max=10)
            sage: q = copy(p)
            sage: q.number_of_constraints()
            1

        TESTS:

        Test that the default MIP variables are independent after copying::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p[0]
            x_0
            sage: q = copy(p)
            sage: q[0]
            x_0
            sage: q[1]
            x_1
            sage: p.number_of_variables()
            1
            sage: q.number_of_variables()
            2"""
    def __deepcopy__(self, memo=...) -> Any:
        """MixedIntegerLinearProgram.__deepcopy__(self, memo={})

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 624)

        Return a deep copy of ``self``.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: b = p.new_variable()
            sage: p.add_constraint(b[1] + b[2] <= 6)
            sage: p.set_objective(b[1] + b[2])
            sage: cp = deepcopy(p)
            sage: cp.solve()
            6.0

        TESTS:

        Test that `deepcopy` makes actual copies but preserves identities::

            sage: mip = MixedIntegerLinearProgram(solver='GLPK')
            sage: ll = [mip, mip]
            sage: dcll=deepcopy(ll)
            sage: ll[0] is dcll[0]
            False
            sage: dcll[0] is dcll[1]
            True"""
    def __getitem__(self, v) -> Any:
        """MixedIntegerLinearProgram.__getitem__(self, v)

        File: /build/sagemath/src/sage/src/sage/numerical/mip.pyx (starting at line 652)

        Return the symbolic variable corresponding to the key
        from the default :class:`MIPVariable` instance.

        It returns the element asked, creating it if necessary.
        If necessary, it also creates the default :class:`MIPVariable` instance.

        See :meth:`new_variable` for a way to have separate :class:`MIPVariable`s
        each of which have their own key space.

        EXAMPLES::

            sage: p = MixedIntegerLinearProgram(solver='GLPK')
            sage: p.set_objective(p['x'] + p['z'])
            sage: p['x']
            x_0"""
