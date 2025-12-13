from .satsolver import SatSolver as SatSolver
from sage.features.sat import Pycosat as Pycosat
from sage.misc.lazy_import import lazy_import as lazy_import

class PicoSAT(SatSolver):
    """
    PicoSAT Solver.

    INPUT:

    - ``verbosity`` -- integer between 0 and 2 (default: 0)

    - ``prop_limit`` -- integer (default: 0); the propagation limit

    EXAMPLES::

        sage: from sage.sat.solvers.picosat import PicoSAT
        sage: solver = PicoSAT()                           # optional - pycosat
    """
    def __init__(self, verbosity: int = 0, prop_limit: int = 0) -> None:
        """
        Construct a new PicoSAT instance.

        See the documentation class for the description of inputs.

        EXAMPLES::

            sage: from sage.sat.solvers.picosat import PicoSAT
            sage: solver = PicoSAT()                       # optional - pycosat
        """
    def var(self, decision=None):
        """
        Return a *new* variable.

        INPUT:

        - ``decision`` -- ignored; accepted for compatibility with other solvers

        EXAMPLES::

            sage: from sage.sat.solvers.picosat import PicoSAT
            sage: solver = PicoSAT()                       # optional - pycosat
            sage: solver.var()                             # optional - pycosat
            1

            sage: solver.add_clause((-1,2,-4))             # optional - pycosat
            sage: solver.var()                             # optional - pycosat
            5
        """
    def nvars(self):
        """
        Return the number of variables.

        Note that for compatibility with DIMACS convention, the number
        of variables corresponds to the maximal index of the variables used.

        EXAMPLES::

            sage: from sage.sat.solvers.picosat import PicoSAT
            sage: solver = PicoSAT()                       # optional - pycosat
            sage: solver.nvars()                           # optional - pycosat
            0

        If a variable with intermediate index is not used, it is still
        considered as a variable::

            sage: solver.add_clause((1,-2,4))              # optional - pycosat
            sage: solver.nvars()                           # optional - pycosat
            4
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

            sage: from sage.sat.solvers.picosat import PicoSAT
            sage: solver = PicoSAT()                       # optional - pycosat
            sage: solver.add_clause((1, -2 , 3))           # optional - pycosat
        """
    def __call__(self, assumptions=None):
        """
        Solve this instance.

        OUTPUT:

        - If this instance is SAT: A tuple of length ``nvars() + 1``,
          where the ``i``-th entry holds an assignment for the
          ``i``-th variables (the ``0``-th entry is always ``None``).

        - If this instance is UNSAT: ``False``.

        EXAMPLES::

            sage: # optional - pycosat
            sage: from sage.sat.solvers.picosat import PicoSAT
            sage: solver = PicoSAT()
            sage: solver.add_clause((1,2))
            sage: solver.add_clause((-1,2))
            sage: solver.add_clause((-1,-2))
            sage: solver()
            (None, False, True)

            sage: solver.add_clause((1,-2))                # optional - pycosat
            sage: solver()                                 # optional - pycosat
            False
        """
    def clauses(self, filename=None):
        """
        Return original clauses.

        INPUT:

        - ``filename`` -- (optional) if given, clauses are written to
          ``filename`` in DIMACS format

        OUTPUT:

        If ``filename`` is ``None`` then a list of ``lits`` is returned,
        where ``lits`` is a list of literals.

        If ``filename`` points to a writable file, then the list of original
        clauses is written to that file in DIMACS format.

        EXAMPLES::

            sage: from sage.sat.solvers.picosat import PicoSAT
            sage: solver = PicoSAT()                       # optional - pycosat
            sage: solver.add_clause((1,2,3,4,5,6,7,8,-9))  # optional - pycosat
            sage: solver.clauses()                         # optional - pycosat
            [[1, 2, 3, 4, 5, 6, 7, 8, -9]]

        DIMACS format output::

            sage: # optional - pycosat
            sage: from sage.sat.solvers.picosat import PicoSAT
            sage: solver = PicoSAT()
            sage: solver.add_clause((1, 2, 4))
            sage: solver.add_clause((1, 2, -4))
            sage: fn = tmp_filename()
            sage: solver.clauses(fn)
            sage: print(open(fn).read())
            p cnf 4 2
            1 2 4 0
            1 2 -4 0
            <BLANKLINE>
        """
