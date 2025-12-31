"""
Abstract SAT Solver

All SAT solvers must inherit from this class.

.. NOTE::

    Our SAT solver interfaces are 1-based, i.e., literals start at
    1. This is consistent with the popular DIMACS format for SAT
    solving but not with Python's 0-based convention. However, this
    also allows to construct clauses using simple integers.

AUTHORS:

- Martin Albrecht (2012): first version
"""
from typing import Any, overload, Literal
from sage.sat.solvers.cryptominisat import CryptoMiniSat
from sage.sat.solvers.picosat import PicoSAT
from sage.sat.solvers.sat_lp import SatLP
from sage.sat.solvers.dimacs import Glucose
from sage.sat.solvers.dimacs import GlucoseSyrup
from sage.sat.solvers.dimacs import Kissat

@overload
def SAT(solver: Literal["cryptominisat"], *args, **kwds) -> CryptoMiniSat:
    ...
@overload
def SAT(solver: Literal["picosat"], *args, **kwds) -> PicoSAT:
    ...
@overload
def SAT(solver: Literal["LP"], *args, **kwds) -> SatLP:
    ...
@overload
def SAT(solver: Literal["glucose"], *args, **kwds) -> Glucose:
    ...
@overload
def SAT(solver: Literal["glucose-syrup"], *args, **kwds) -> GlucoseSyrup:
    ...
@overload
def SAT(solver: Literal["kissat"], *args, **kwds) -> Kissat:
    ...
@overload
def SAT(solver: None = None, *args, **kwds) -> CryptoMiniSat | PicoSAT | SatLP:
    r"""
    Return a :class:`SatSolver` instance.

    Through this class, one can define and solve
    :wikipedia:`SAT problems <Boolean_satisfiability_problem>`.

    INPUT:

    - ``solver`` -- string; select a solver. Admissible values are:

        - ``'cryptominisat'`` -- note that the pycryptosat package must be
          installed

        - ``'picosat'`` -- note that the pycosat package must be installed

        - ``'glucose'`` -- note that the glucose package must be installed

        - ``'glucose-syrup'`` -- note that the glucose package must be installed

        - ``'LP'`` -- use :class:`~sage.sat.solvers.sat_lp.SatLP` to solve the
          SAT instance

        - ``None`` -- default; use CryptoMiniSat if available, else PicoSAT if
          available, and a LP solver otherwise

    EXAMPLES::

        sage: SAT(solver='LP')                                                          # needs sage.numerical.mip
        an ILP-based SAT Solver

    TESTS::

        sage: SAT(solver='Wouhouuuuuu')
        Traceback (most recent call last):
        ...
        ValueError: Solver 'Wouhouuuuuu' is not available

    Forcing CryptoMiniSat::

        sage: SAT(solver='cryptominisat')                                   # optional - pycryptosat
        CryptoMiniSat solver: 0 variables, 0 clauses.

    Forcing PicoSat::

        sage: SAT(solver='picosat')                                         # optional - pycosat
        PicoSAT solver: 0 variables, 0 clauses.

    Forcing Glucose::

        sage: SAT(solver='glucose')
        DIMACS Solver: 'glucose -verb=0 -model {input}'

    Forcing Glucose Syrup::

        sage: SAT(solver='glucose-syrup')
        DIMACS Solver: 'glucose-syrup -model -verb=0 {input}'

    Forcing Kissat::

        sage: SAT(solver='kissat')
        DIMACS Solver: 'kissat -q {input}'
    """

class SatSolver:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def add_clause(self, lits) -> Any:
        """SatSolver.add_clause(self, lits)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 64)

        Add a new clause to set of clauses.

        INPUT:

        - ``lits`` -- tuple of nonzero integers

        .. NOTE::

            If any element ``e`` in ``lits`` has ``abs(e)`` greater
            than the number of variables generated so far, then new
            variables are created automatically.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.add_clause( (1, -2 , 3) )
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def clauses(self, filename=...) -> Any:
        """SatSolver.clauses(self, filename=None)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 254)

        Return original clauses.

        INPUT:

        - ``filename'' -- if not ``None`` clauses are written to ``filename`` in
          DIMACS format (default: ``None``)

        OUTPUT:

            If ``filename`` is ``None`` then a list of ``lits, is_xor, rhs``
            tuples is returned, where ``lits`` is a tuple of literals,
            ``is_xor`` is always ``False`` and ``rhs`` is always ``None``.

            If ``filename`` points to a writable file, then the list of original
            clauses is written to that file in DIMACS format.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.clauses()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def clauses(self) -> Any:
        """SatSolver.clauses(self, filename=None)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 254)

        Return original clauses.

        INPUT:

        - ``filename'' -- if not ``None`` clauses are written to ``filename`` in
          DIMACS format (default: ``None``)

        OUTPUT:

            If ``filename`` is ``None`` then a list of ``lits, is_xor, rhs``
            tuples is returned, where ``lits`` is a tuple of literals,
            ``is_xor`` is always ``False`` and ``rhs`` is always ``None``.

            If ``filename`` points to a writable file, then the list of original
            clauses is written to that file in DIMACS format.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.clauses()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def conflict_clause(self) -> Any:
        """SatSolver.conflict_clause(self)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 203)

        Return conflict clause if this instance is UNSAT and the last
        call used assumptions.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.conflict_clause()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def conflict_clause(self) -> Any:
        """SatSolver.conflict_clause(self)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 203)

        Return conflict clause if this instance is UNSAT and the last
        call used assumptions.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.conflict_clause()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def learnt_clauses(self, unitary_only=...) -> Any:
        """SatSolver.learnt_clauses(self, unitary_only=False)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 219)

        Return learnt clauses.

        INPUT:

        - ``unitary_only`` -- return only unitary learnt clauses (default: ``False``)

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.learnt_clauses()
            Traceback (most recent call last):
            ...
            NotImplementedError

            sage: solver.learnt_clauses(unitary_only=True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def learnt_clauses(self) -> Any:
        """SatSolver.learnt_clauses(self, unitary_only=False)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 219)

        Return learnt clauses.

        INPUT:

        - ``unitary_only`` -- return only unitary learnt clauses (default: ``False``)

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.learnt_clauses()
            Traceback (most recent call last):
            ...
            NotImplementedError

            sage: solver.learnt_clauses(unitary_only=True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def learnt_clauses(self, unitary_only=...) -> Any:
        """SatSolver.learnt_clauses(self, unitary_only=False)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 219)

        Return learnt clauses.

        INPUT:

        - ``unitary_only`` -- return only unitary learnt clauses (default: ``False``)

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.learnt_clauses()
            Traceback (most recent call last):
            ...
            NotImplementedError

            sage: solver.learnt_clauses(unitary_only=True)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def nvars(self) -> Any:
        """SatSolver.nvars(self)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 49)

        Return the number of variables.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.nvars()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def nvars(self) -> Any:
        """SatSolver.nvars(self)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 49)

        Return the number of variables.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.nvars()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def read(self, filename) -> Any:
        '''SatSolver.read(self, filename)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 89)

        Reads DIMAC files.

        Reads in DIMAC formatted lines (lazily) from a file or file object and
        adds the corresponding clauses into this solver instance. Note that the
        DIMACS format is not well specified, see
        http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html,
        https://web.archive.org/web/20090305015900/http://www.satcompetition.org/2009/format-benchmarks2009.html, and
        http://elis.dvo.ru/~lab_11/glpk-doc/cnfsat.pdf.

        The differences were summarized in the discussion on the issue
        :issue:`16924`. This method assumes the following DIMACS format:

        - Any line starting with "c" is a comment
        - Any line starting with "p" is a header
        - Any variable 1-n can be used
        - Every line containing a clause must end with a "0"

        The format is extended to allow lines starting with "x" defining ``xor``
        clauses, with the notation introduced in cryptominisat, see
        https://www.msoos.org/xor-clauses/

        INPUT:

        - ``filename`` -- the name of a file as a string or a file object

        EXAMPLES::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file.\\np cnf 3 2\\n1 -3 0\\n2 3 -1 0 ")
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: solver = DIMACS()
            sage: solver.read(file_object)
            sage: solver.clauses()
            [((1, -3), False, None), ((2, 3, -1), False, None)]

        With xor clauses::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file with xor clauses.\\np cnf 3 3\\n1 2 0\\n3 0\\nx1 2 3 0")
            sage: from sage.sat.solvers.cryptominisat import CryptoMiniSat          # optional - pycryptosat
            sage: solver = CryptoMiniSat()                                          # optional - pycryptosat
            sage: solver.read(file_object)                                          # optional - pycryptosat
            sage: solver.clauses()                                                  # optional - pycryptosat
            [((1, 2), False, None), ((3,), False, None), ((1, 2, 3), True, True)]
            sage: solver()                                                          # optional - pycryptosat
            (None, True, True, True)

        TESTS::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file with xor clauses.\\np cnf 3 3\\n1 2 0\\n3 0\\nx1 2 3 0")
            sage: from sage.sat.solvers.sat_lp import SatLP                             # needs sage.numerical.mip
            sage: solver = SatLP()                                                      # needs sage.numerical.mip
            sage: solver.read(file_object)                                              # needs sage.numerical.mip
            Traceback (most recent call last):
            ...
            NotImplementedError: the solver "an ILP-based SAT Solver" does not support xor clauses'''
    @overload
    def read(self, file_object) -> Any:
        '''SatSolver.read(self, filename)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 89)

        Reads DIMAC files.

        Reads in DIMAC formatted lines (lazily) from a file or file object and
        adds the corresponding clauses into this solver instance. Note that the
        DIMACS format is not well specified, see
        http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html,
        https://web.archive.org/web/20090305015900/http://www.satcompetition.org/2009/format-benchmarks2009.html, and
        http://elis.dvo.ru/~lab_11/glpk-doc/cnfsat.pdf.

        The differences were summarized in the discussion on the issue
        :issue:`16924`. This method assumes the following DIMACS format:

        - Any line starting with "c" is a comment
        - Any line starting with "p" is a header
        - Any variable 1-n can be used
        - Every line containing a clause must end with a "0"

        The format is extended to allow lines starting with "x" defining ``xor``
        clauses, with the notation introduced in cryptominisat, see
        https://www.msoos.org/xor-clauses/

        INPUT:

        - ``filename`` -- the name of a file as a string or a file object

        EXAMPLES::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file.\\np cnf 3 2\\n1 -3 0\\n2 3 -1 0 ")
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: solver = DIMACS()
            sage: solver.read(file_object)
            sage: solver.clauses()
            [((1, -3), False, None), ((2, 3, -1), False, None)]

        With xor clauses::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file with xor clauses.\\np cnf 3 3\\n1 2 0\\n3 0\\nx1 2 3 0")
            sage: from sage.sat.solvers.cryptominisat import CryptoMiniSat          # optional - pycryptosat
            sage: solver = CryptoMiniSat()                                          # optional - pycryptosat
            sage: solver.read(file_object)                                          # optional - pycryptosat
            sage: solver.clauses()                                                  # optional - pycryptosat
            [((1, 2), False, None), ((3,), False, None), ((1, 2, 3), True, True)]
            sage: solver()                                                          # optional - pycryptosat
            (None, True, True, True)

        TESTS::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file with xor clauses.\\np cnf 3 3\\n1 2 0\\n3 0\\nx1 2 3 0")
            sage: from sage.sat.solvers.sat_lp import SatLP                             # needs sage.numerical.mip
            sage: solver = SatLP()                                                      # needs sage.numerical.mip
            sage: solver.read(file_object)                                              # needs sage.numerical.mip
            Traceback (most recent call last):
            ...
            NotImplementedError: the solver "an ILP-based SAT Solver" does not support xor clauses'''
    @overload
    def read(self, file_object) -> Any:
        '''SatSolver.read(self, filename)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 89)

        Reads DIMAC files.

        Reads in DIMAC formatted lines (lazily) from a file or file object and
        adds the corresponding clauses into this solver instance. Note that the
        DIMACS format is not well specified, see
        http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html,
        https://web.archive.org/web/20090305015900/http://www.satcompetition.org/2009/format-benchmarks2009.html, and
        http://elis.dvo.ru/~lab_11/glpk-doc/cnfsat.pdf.

        The differences were summarized in the discussion on the issue
        :issue:`16924`. This method assumes the following DIMACS format:

        - Any line starting with "c" is a comment
        - Any line starting with "p" is a header
        - Any variable 1-n can be used
        - Every line containing a clause must end with a "0"

        The format is extended to allow lines starting with "x" defining ``xor``
        clauses, with the notation introduced in cryptominisat, see
        https://www.msoos.org/xor-clauses/

        INPUT:

        - ``filename`` -- the name of a file as a string or a file object

        EXAMPLES::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file.\\np cnf 3 2\\n1 -3 0\\n2 3 -1 0 ")
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: solver = DIMACS()
            sage: solver.read(file_object)
            sage: solver.clauses()
            [((1, -3), False, None), ((2, 3, -1), False, None)]

        With xor clauses::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file with xor clauses.\\np cnf 3 3\\n1 2 0\\n3 0\\nx1 2 3 0")
            sage: from sage.sat.solvers.cryptominisat import CryptoMiniSat          # optional - pycryptosat
            sage: solver = CryptoMiniSat()                                          # optional - pycryptosat
            sage: solver.read(file_object)                                          # optional - pycryptosat
            sage: solver.clauses()                                                  # optional - pycryptosat
            [((1, 2), False, None), ((3,), False, None), ((1, 2, 3), True, True)]
            sage: solver()                                                          # optional - pycryptosat
            (None, True, True, True)

        TESTS::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file with xor clauses.\\np cnf 3 3\\n1 2 0\\n3 0\\nx1 2 3 0")
            sage: from sage.sat.solvers.sat_lp import SatLP                             # needs sage.numerical.mip
            sage: solver = SatLP()                                                      # needs sage.numerical.mip
            sage: solver.read(file_object)                                              # needs sage.numerical.mip
            Traceback (most recent call last):
            ...
            NotImplementedError: the solver "an ILP-based SAT Solver" does not support xor clauses'''
    @overload
    def read(self, file_object) -> Any:
        '''SatSolver.read(self, filename)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 89)

        Reads DIMAC files.

        Reads in DIMAC formatted lines (lazily) from a file or file object and
        adds the corresponding clauses into this solver instance. Note that the
        DIMACS format is not well specified, see
        http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html,
        https://web.archive.org/web/20090305015900/http://www.satcompetition.org/2009/format-benchmarks2009.html, and
        http://elis.dvo.ru/~lab_11/glpk-doc/cnfsat.pdf.

        The differences were summarized in the discussion on the issue
        :issue:`16924`. This method assumes the following DIMACS format:

        - Any line starting with "c" is a comment
        - Any line starting with "p" is a header
        - Any variable 1-n can be used
        - Every line containing a clause must end with a "0"

        The format is extended to allow lines starting with "x" defining ``xor``
        clauses, with the notation introduced in cryptominisat, see
        https://www.msoos.org/xor-clauses/

        INPUT:

        - ``filename`` -- the name of a file as a string or a file object

        EXAMPLES::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file.\\np cnf 3 2\\n1 -3 0\\n2 3 -1 0 ")
            sage: from sage.sat.solvers.dimacs import DIMACS
            sage: solver = DIMACS()
            sage: solver.read(file_object)
            sage: solver.clauses()
            [((1, -3), False, None), ((2, 3, -1), False, None)]

        With xor clauses::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file with xor clauses.\\np cnf 3 3\\n1 2 0\\n3 0\\nx1 2 3 0")
            sage: from sage.sat.solvers.cryptominisat import CryptoMiniSat          # optional - pycryptosat
            sage: solver = CryptoMiniSat()                                          # optional - pycryptosat
            sage: solver.read(file_object)                                          # optional - pycryptosat
            sage: solver.clauses()                                                  # optional - pycryptosat
            [((1, 2), False, None), ((3,), False, None), ((1, 2, 3), True, True)]
            sage: solver()                                                          # optional - pycryptosat
            (None, True, True, True)

        TESTS::

            sage: from io import StringIO
            sage: file_object = StringIO("c A sample .cnf file with xor clauses.\\np cnf 3 3\\n1 2 0\\n3 0\\nx1 2 3 0")
            sage: from sage.sat.solvers.sat_lp import SatLP                             # needs sage.numerical.mip
            sage: solver = SatLP()                                                      # needs sage.numerical.mip
            sage: solver.read(file_object)                                              # needs sage.numerical.mip
            Traceback (most recent call last):
            ...
            NotImplementedError: the solver "an ILP-based SAT Solver" does not support xor clauses'''
    @overload
    def var(self, decision=...) -> Any:
        """SatSolver.var(self, decision=None)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 30)

        Return a *new* variable.

        INPUT:

        - ``decision`` -- is this variable a decision variable?

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.var()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def var(self) -> Any:
        """SatSolver.var(self, decision=None)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 30)

        Return a *new* variable.

        INPUT:

        - ``decision`` -- is this variable a decision variable?

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver.var()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    def __call__(self, assumptions=...) -> Any:
        """SatSolver.__call__(self, assumptions=None)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 173)

        Solve this instance.

        INPUT:

        - ``assumptions`` -- assumed variable assignments (default: ``None``)

        OUTPUT:

        - If this instance is SAT: A tuple of length ``nvars()+1``
          where the ``i``-th entry holds an assignment for the
          ``i``-th variables (the ``0``-th entry is always ``None``).

        - If this instance is UNSAT: ``False``

        - If the solver was interrupted before deciding satisfiability
          ``None``.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: solver()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def __dir__(self) -> Any:
        """SatSolver.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 298)

        Custom dir for tab-completion.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: 'gens' in solver.__dir__()
            True"""
    @overload
    def __dir__(self) -> Any:
        """SatSolver.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/sat/solvers/satsolver.pyx (starting at line 298)

        Custom dir for tab-completion.

        EXAMPLES::

            sage: from sage.sat.solvers.satsolver import SatSolver
            sage: solver = SatSolver()
            sage: 'gens' in solver.__dir__()
            True"""
