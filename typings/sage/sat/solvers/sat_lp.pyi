from .satsolver import SatSolver as SatSolver
from sage.numerical.mip import MIPSolverException as MIPSolverException, MixedIntegerLinearProgram as MixedIntegerLinearProgram

class SatLP(SatSolver):
    def __init__(self, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001) -> None:
        """
        Initialize the instance.

        INPUT:

        - ``solver`` -- (default: ``None``) specify a Mixed Integer Linear Programming
          (MILP) solver to be used. If set to ``None``, the default one is used. For
          more information on MILP solvers and which default solver is used, see
          the method
          :meth:`solve <sage.numerical.mip.MixedIntegerLinearProgram.solve>`
          of the class
          :class:`MixedIntegerLinearProgram <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of verbosity
          of the LP solver. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- parameter for use with MILP solvers over an
          inexact base ring; see :meth:`MixedIntegerLinearProgram.get_values`

        EXAMPLES::

            sage: S=SAT(solver='LP'); S
            an ILP-based SAT Solver
        """
    def var(self):
        """
        Return a *new* variable.

        EXAMPLES::

            sage: S=SAT(solver='LP'); S
            an ILP-based SAT Solver
            sage: S.var()
            1
        """
    def nvars(self):
        """
        Return the number of variables.

        EXAMPLES::

            sage: S=SAT(solver='LP'); S
            an ILP-based SAT Solver
            sage: S.var()
            1
            sage: S.var()
            2
            sage: S.nvars()
            2
        """
    def add_clause(self, lits) -> None:
        """
        Add a new clause to set of clauses.

        INPUT:

        - ``lits`` -- tuple of nonzero integers

        .. NOTE::

            If any element ``e`` in ``lits`` has ``abs(e)`` greater
            than the number of variables generated so far, then new
            variables are created automatically.

        EXAMPLES::

            sage: S=SAT(solver='LP'); S
            an ILP-based SAT Solver
            sage: for u,v in graphs.CycleGraph(6).edges(sort=False, labels=False):
            ....:     u,v = u+1,v+1
            ....:     S.add_clause((u,v))
            ....:     S.add_clause((-u,-v))
        """
    def __call__(self):
        """
        Solve this instance.

        OUTPUT:

        - If this instance is SAT: A tuple of length ``nvars()+1``
          where the ``i``-th entry holds an assignment for the
          ``i``-th variables (the ``0``-th entry is always ``None``).

        - If this instance is UNSAT: ``False``

        EXAMPLES::

            sage: def is_bipartite_SAT(G):
            ....:     S=SAT(solver='LP'); S
            ....:     for u,v in G.edges(sort=False, labels=False):
            ....:         u,v = u+1,v+1
            ....:         S.add_clause((u,v))
            ....:         S.add_clause((-u,-v))
            ....:     return S
            sage: S = is_bipartite_SAT(graphs.CycleGraph(6))
            sage: S() # random
            [None, True, False, True, False, True, False]
            sage: True in S()
            True
            sage: S = is_bipartite_SAT(graphs.CycleGraph(7))
            sage: S()
            False
        """
