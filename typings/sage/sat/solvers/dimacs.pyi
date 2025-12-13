from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.sat.solvers.satsolver import SatSolver as SatSolver

class DIMACS(SatSolver):
    """
    Generic DIMACS Solver.

    .. NOTE::

        Usually, users will not have to use this class directly but some
        class which inherits from this class.

    .. automethod:: __init__
    .. automethod:: __call__
    """
    command: str
    def __init__(self, command=None, filename=None, verbosity: int = 0, **kwds) -> None:
        '''
        Construct a new generic DIMACS solver.

        INPUT:

        - ``command`` -- a named format string with the command to
          run. The string must contain {input} and may contain
          {output} if the solvers writes the solution to an output
          file. For example "sat-solver {input}" is a valid
          command. If ``None`` then the class variable ``command`` is
          used. (default: ``None``)

        - ``filename`` -- a filename to write clauses to in DIMACS
          format, must be writable. If ``None`` a temporary filename
          is chosen automatically. (default: ``None``)

        - ``verbosity`` -- a verbosity level, where zero means silent
          and anything else means verbose output. (default: ``0``)

        - ``**kwds`` -- accepted for compatibility with other solvers; ignored

        TESTS::

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: DIMACS()
            DIMACS Solver: \'\'
        '''
    def __del__(self) -> None:
        '''
        TESTS::

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: d = DIMACS(command="iliketurtles {input}")
            sage: del d

        We check that files created during initialization are properly
        deleted (:issue:`38328`)::

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: d = DIMACS(command="iliketurtles {input}")
            sage: filename = d._headname
            sage: os.path.exists(filename)
            True
            sage: del d
            sage: os.path.exists(filename)
            False

        ::

            sage: fn = tmp_filename()
            sage: d = DIMACS(filename=fn)
            sage: del d
        '''
    def var(self, decision=None):
        """
        Return a *new* variable.

        INPUT:

        - ``decision`` -- accepted for compatibility with other solvers; ignored

        EXAMPLES::

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: solver = DIMACS()
            sage: solver.var()
            1
        """
    def nvars(self):
        """
        Return the number of variables.

        EXAMPLES::

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: solver = DIMACS()
            sage: solver.var()
            1
            sage: solver.var(decision=True)
            2
            sage: solver.nvars()
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

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: solver = DIMACS()
            sage: solver.var()
            1
            sage: solver.var(decision=True)
            2
            sage: solver.add_clause( (1, -2 , 3) )
            sage: solver
            DIMACS Solver: ''
        """
    def write(self, filename=None):
        """
        Write DIMACS file.

        INPUT:

        - ``filename`` -- if ``None`` default filename specified at initialization is used for
          writing to (default: ``None``)

        EXAMPLES::

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS(filename=fn)
            sage: solver.add_clause( (1, -2 , 3) )
            sage: _ = solver.write()
            sage: for line in open(fn).readlines():
            ....:     print(line)
            p cnf 3 1
            1 -2 3 0

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS()
            sage: solver.add_clause( (1, -2 , 3) )
            sage: _ = solver.write(fn)
            sage: for line in open(fn).readlines():
            ....:      print(line)
            p cnf 3 1
            1 -2 3 0
        """
    def clauses(self, filename=None):
        """
        Return original clauses.

        INPUT:

        - ``filename`` -- if not ``None`` clauses are written to ``filename`` in
          DIMACS format (default: ``None``)

        OUTPUT:

            If ``filename`` is ``None`` then a list of ``lits, is_xor, rhs``
            tuples is returned, where ``lits`` is a tuple of literals,
            ``is_xor`` is always ``False`` and ``rhs`` is always ``None``.

            If ``filename`` points to a writable file, then the list of original
            clauses is written to that file in DIMACS format.

        EXAMPLES::

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS()
            sage: solver.add_clause( (1, 2, 3) )
            sage: solver.clauses()
            [((1, 2, 3), False, None)]

            sage: solver.add_clause( (1, 2, -3) )
            sage: solver.clauses(fn)
            sage: print(open(fn).read())
            p cnf 3 2
            1 2 3 0
            1 2 -3 0
            <BLANKLINE>
        """
    @staticmethod
    def render_dimacs(clauses, filename, nlits) -> None:
        '''
        Produce DIMACS file ``filename`` from ``clauses``.

        INPUT:

        - ``clauses`` -- list of clauses, either in simple format as a list of
          literals or in extended format for CryptoMiniSat: a tuple of literals,
          ``is_xor`` and ``rhs``.

        - ``filename`` -- the file to write to

        - ``nlits -- the number of literals appearing in ``clauses``

        EXAMPLES::

            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: fn = tmp_filename()
            sage: solver = DIMACS()
            sage: solver.add_clause( (1, 2, -3) )
            sage: DIMACS.render_dimacs(solver.clauses(), fn, solver.nvars())
            sage: print(open(fn).read())
            p cnf 3 1
            1 2 -3 0
            <BLANKLINE>

        This is equivalent to::

            sage: solver.clauses(fn)
            sage: print(open(fn).read())
            p cnf 3 1
            1 2 -3 0
            <BLANKLINE>

        This function also accepts a "simple" format::

            sage: DIMACS.render_dimacs([ (1,2), (1,2,-3) ], fn, 3)
            sage: print(open(fn).read())
            p cnf 3 2
            1 2 0
            1 2 -3 0
            <BLANKLINE>
        '''
    def __call__(self, assumptions=None):
        """
        Solve this instance and return the parsed output.

        INPUT:

        - ``assumptions`` -- ignored, accepted for compatibility with
          other solvers (default: ``None``)

        OUTPUT:

        - If this instance is SAT: A tuple of length ``nvars()+1``
          where the ``i``-th entry holds an assignment for the
          ``i``-th variables (the ``0``-th entry is always ``None``).

        - If this instance is UNSAT: ``False``

        EXAMPLES:

        When the problem is SAT::

            sage: from sage.sat.solvers import RSat
            sage: solver = RSat()
            sage: solver.add_clause( (1, 2, 3) )
            sage: solver.add_clause( (-1,) )
            sage: solver.add_clause( (-2,) )
            sage: solver()                            # optional - rsat
            (None, False, False, True)

        When the problem is UNSAT::

            sage: solver = RSat()
            sage: solver.add_clause((1,2))
            sage: solver.add_clause((-1,2))
            sage: solver.add_clause((1,-2))
            sage: solver.add_clause((-1,-2))
            sage: solver()                            # optional - rsat
            False

        With Glucose::

            sage: from sage.sat.solvers.dimacs import Glucose
            sage: solver = Glucose()
            sage: solver.add_clause((1,2))
            sage: solver.add_clause((-1,2))
            sage: solver.add_clause((1,-2))
            sage: solver()                           # optional - glucose
            (None, True, True)
            sage: solver.add_clause((-1,-2))
            sage: solver()                           # optional - glucose
            False

        With GlucoseSyrup::

            sage: from sage.sat.solvers.dimacs import GlucoseSyrup
            sage: solver = GlucoseSyrup()
            sage: solver.add_clause((1,2))
            sage: solver.add_clause((-1,2))
            sage: solver.add_clause((1,-2))
            sage: solver()                          # optional - glucose
            (None, True, True)
            sage: solver.add_clause((-1,-2))
            sage: solver()                          # optional - glucose
            False

        TESTS::

            sage: from sage.sat.boolean_polynomials import solve as solve_sat
            sage: sr = mq.SR(1, 1, 1, 4, gf2=True, polybori=True)                       # needs sage.rings.finite_rings sage.rings.polynomial.pbori
            sage: while True:  # workaround (see :issue:`31891`)                         # needs sage.rings.finite_rings sage.rings.polynomial.pbori
            ....:     try:
            ....:         F, s = sr.polynomial_system()
            ....:         break
            ....:     except ZeroDivisionError:
            ....:         pass
            sage: solve_sat(F, solver=sage.sat.solvers.RSat)    # optional - rsat, needs sage.rings.finite_rings sage.rings.polynomial.pbori
        """

class RSat(DIMACS):
    """
    An instance of the RSat solver.

    For information on RSat see: http://reasoning.cs.ucla.edu/rsat/

    EXAMPLES::

        sage: from sage.sat.solvers import RSat
        sage: solver = RSat()
        sage: solver
        DIMACS Solver: 'rsat {input} -v -s'

    When the problem is SAT::

        sage: from sage.sat.solvers import RSat
        sage: solver = RSat()
        sage: solver.add_clause( (1, 2, 3) )
        sage: solver.add_clause( (-1,) )
        sage: solver.add_clause( (-2,) )
        sage: solver()                            # optional - rsat
        (None, False, False, True)

    When the problem is UNSAT::

        sage: solver = RSat()
        sage: solver.add_clause((1,2))
        sage: solver.add_clause((-1,2))
        sage: solver.add_clause((1,-2))
        sage: solver.add_clause((-1,-2))
        sage: solver()                            # optional - rsat
        False
    """
    command: str

class Glucose(DIMACS):
    """
    An instance of the Glucose solver.

    For information on Glucose see: http://www.labri.fr/perso/lsimon/glucose/

    EXAMPLES::

        sage: from sage.sat.solvers import Glucose
        sage: solver = Glucose()
        sage: solver
        DIMACS Solver: 'glucose -verb=0 -model {input}'

    When the problem is SAT::

        sage: from sage.sat.solvers import Glucose
        sage: solver1 = Glucose()
        sage: solver1.add_clause( (1, 2, 3) )
        sage: solver1.add_clause( (-1,) )
        sage: solver1.add_clause( (-2,) )
        sage: solver1()                            # optional - glucose
        (None, False, False, True)

    When the problem is UNSAT::

        sage: solver2 = Glucose()
        sage: solver2.add_clause((1,2))
        sage: solver2.add_clause((-1,2))
        sage: solver2.add_clause((1,-2))
        sage: solver2.add_clause((-1,-2))
        sage: solver2()                            # optional - glucose
        False

    With one hundred variables::

        sage: solver3 = Glucose()
        sage: solver3.add_clause( (1, 2, 100) )
        sage: solver3.add_clause( (-1,) )
        sage: solver3.add_clause( (-2,) )
        sage: solver3()                            # optional - glucose
        (None, False, False, ..., True)

    TESTS::

        sage: print(''.join(solver1._output))      # optional - glucose
        c...
        s SATISFIABLE
        v -1 -2 3 0

    ::

        sage: print(''.join(solver2._output))      # optional - glucose
        c...
        s UNSATISFIABLE

    Glucose gives large solution on one single line::

        sage: print(''.join(solver3._output))      # optional - glucose
        c...
        s SATISFIABLE
        v -1 -2 ... 100 0
    """
    command: str

class GlucoseSyrup(DIMACS):
    """
    An instance of the Glucose-syrup parallel solver.

    For information on Glucose see: http://www.labri.fr/perso/lsimon/glucose/

    EXAMPLES::

        sage: from sage.sat.solvers import GlucoseSyrup
        sage: solver = GlucoseSyrup()
        sage: solver
        DIMACS Solver: 'glucose-syrup -model -verb=0 {input}'

    When the problem is SAT::

        sage: solver1 = GlucoseSyrup()
        sage: solver1.add_clause( (1, 2, 3) )
        sage: solver1.add_clause( (-1,) )
        sage: solver1.add_clause( (-2,) )
        sage: solver1()                            # optional - glucose
        (None, False, False, True)

    When the problem is UNSAT::

        sage: solver2 = GlucoseSyrup()
        sage: solver2.add_clause((1,2))
        sage: solver2.add_clause((-1,2))
        sage: solver2.add_clause((1,-2))
        sage: solver2.add_clause((-1,-2))
        sage: solver2()                            # optional - glucose
        False

    With one hundred variables::

        sage: solver3 = GlucoseSyrup()
        sage: solver3.add_clause( (1, 2, 100) )
        sage: solver3.add_clause( (-1,) )
        sage: solver3.add_clause( (-2,) )
        sage: solver3()                            # optional - glucose
        (None, False, False, ..., True)

    TESTS::

        sage: print(''.join(solver1._output))      # optional - glucose
        c...
        s SATISFIABLE
        v -1 -2 3 0

    ::

        sage: print(''.join(solver2._output))      # optional - glucose
        c...
        s UNSATISFIABLE

    GlucoseSyrup gives large solution on one single line::

        sage: print(''.join(solver3._output))      # optional - glucose
        c...
        s SATISFIABLE
        v -1 -2 ... 100 0
    """
    command: str

class Kissat(DIMACS):
    '''
    An instance of the Kissat SAT solver.

    For information on Kissat see: http://fmv.jku.at/kissat/

    EXAMPLES::

        sage: from sage.sat.solvers import Kissat
        sage: solver = Kissat()
        sage: solver
        DIMACS Solver: \'kissat -q {input}\'

    When the problem is SAT::

        sage: solver1 = Kissat()
        sage: solver1.add_clause( (1, 2, 3) )
        sage: solver1.add_clause( (-1,) )
        sage: solver1.add_clause( (-2,) )
        sage: solver1()                           # optional - kissat
        (None, False, False, True)

    When the problem is UNSAT::

        sage: solver2 = Kissat()
        sage: solver2.add_clause((1,2))
        sage: solver2.add_clause((-1,2))
        sage: solver2.add_clause((1,-2))
        sage: solver2.add_clause((-1,-2))
        sage: solver2()                           # optional - kissat
        False

    With one hundred variables::

        sage: solver3 = Kissat()
        sage: solver3.add_clause( (1, 2, 100) )
        sage: solver3.add_clause( (-1,) )
        sage: solver3.add_clause( (-2,) )
        sage: solver3()                           # optional - kissat
        (None, False, False, ..., True)

    TESTS::

        sage: print(\'\'.join(solver1._output))     # optional - kissat
        s SATISFIABLE
        v -1 -2 3 0

    ::

        sage: print(\'\'.join(solver2._output))     # optional - kissat
        s UNSATISFIABLE

    Here the output contains many lines starting with letter "v"::

        sage: print(\'\'.join(solver3._output))     # optional - kissat
        s SATISFIABLE
        v -1 -2 ...
        v ...
        v ...
        v ... 100 0
    '''
    command: str
