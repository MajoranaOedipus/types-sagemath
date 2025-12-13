from .expect import Expect as Expect, ExpectFunction as ExpectFunction
from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.env import SAGE_LOCAL as SAGE_LOCAL
from sage.interfaces.interface import AsciiArtString as AsciiArtString
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.flatten import flatten as flatten
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.repl.preparse import implicit_mul as implicit_mul

class Qepcad_expect(ExtraTabCompletion, Expect):
    """
    The low-level wrapper for QEPCAD.
    """
    def __init__(self, memcells=None, maxread=None, logfile=None, server=None) -> None:
        """
        Initialize a low-level wrapper for QEPCAD.

        You can specify
        the number of memory cells that QEPCAD allocates on startup
        (which controls the maximum problem size QEPCAD can handle),
        and specify a logfile.  You can also specify a server, and the
        interface will run QEPCAD on that server, using ssh.  (UNTESTED)

        EXAMPLES::

            sage: from sage.interfaces.qepcad import Qepcad_expect
            sage: Qepcad_expect(memcells=100000, logfile=sys.stdout)
            Qepcad
        """

class Qepcad:
    """
    The wrapper for QEPCAD.
    """
    def __init__(self, formula, vars=None, logfile=None, verbose: bool = False, memcells=None, server=None) -> None:
        """
        Construct a QEPCAD wrapper object.

        Requires a formula, which
        may be a :class:`qformula` as returned by the methods of
        ``qepcad_formula``, a symbolic equality or inequality, a
        polynomial `p` (meaning `p = 0`), or a string, which is passed
        straight to QEPCAD.

        ``vars`` specifies the variables to use; this gives the variable
        ordering, which may be very important.  If ``formula`` is
        given as a string, then ``vars`` is required; otherwise,
        if ``vars`` is omitted, then a default ordering is used
        (alphabetical ordering for the free variables).

        A logfile can be specified with ``logfile``.
        If ``verbose=True`` is given, then the logfile is automatically
        set to ``sys.stdout.buffer``, so all QEPCAD interaction is echoed to
        the terminal.

        You can set the amount of memory that QEPCAD allocates with
        ``memcells``, and you can use ``server`` to run QEPCAD on
        another machine using ssh.  (UNTESTED)

        Usually you will not call this directly, but use ``qepcad``
        to do so.  Check the ``qepcad`` documentation for more
        information.

        EXAMPLES::

            sage: from sage.interfaces.qepcad import Qepcad
            sage: Qepcad(x^2 - 1 == 0)            # optional - qepcad
            QEPCAD object in phase 'Before Normalization'

        To check that :issue:`20126` is fixed::

            sage: (x, y, z) = var('x, y, z')
            sage: conds = [-z < 0, -y + z < 0, x^2 + x*y + 2*x*z + 2*y*z - x < 0, \\\n            ....:          x^2 + x*y + 3*x*z + 2*y*z + 2*z^2 - x - z < 0, \\\n            ....:          -2*x + 1 < 0, -x*y - x*z - 2*y*z - 2*z^2 + z < 0, \\\n            ....:          x + 3*y + 3*z - 1 < 0]
            sage: qepcad(conds, memcells=3000000) # optional - qepcad
            2 x - 1 > 0 /\\ z > 0 /\\ z - y < 0 /\\ 3 z + 3 y + x - 1 < 0
        """
    def assume(self, assume):
        """
        The following documentation is from ``qepcad.help``.

        Add an assumption to the problem.  These will not be
        included in the solution formula.

        For example, with input  (E x)[ a x^2 + b x + c = 0],
        if we issue the command

            assume [ a /= 0 ]

        we will get the solution formula b^2 - 4 a c >= 0.  Without
        the assumption we'd get something like [a = 0 /\\ b /= 0] \\/
        [a /= 0 /\\ 4 a c - b^2 <= 0] \\/ [a = 0 /\\ b = 0 /\\ c = 0].

        EXAMPLES::

            sage: var('a,b,c,x')
            (a, b, c, x)
            sage: qf = qepcad_formula
            sage: qe = qepcad(qf.exists(x, a*x^2 + b*x + c == 0), interact=True) # optional - qepcad
            sage: qe.assume(a != 0) # optional - qepcad
            sage: qe.finish() # optional - qepcad
            4 a c - b^2 <= 0
        """
    def solution_extension(self, kind):
        """
        The following documentation is modified from ``qepcad.help``:

        solution-extension x

        Use an alternative solution formula construction method.  The
        parameter x is allowed to be T,E, or G.  If x is T, then a
        formula in the usual language of Tarski formulas is produced.
        If x is E, a formula in the language of Extended Tarski formulas
        is produced.  If x is G, then a geometry-based formula is
        produced.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qf = qepcad_formula
            sage: qe = qepcad(qf.and_(x^2 + y^2 - 3 == 0, x + y > 0), interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.solution_extension('E')                    # not tested (random order)
            x > _root_1 2 x^2 - 3 /\\ y^2 + x^2 - 3 = 0 /\\ [ 2 x^2 - 3 > 0 \\/ y = _root_-1 y^2 + x^2 - 3 ]
            sage: qe.solution_extension('G')                    # not tested (random order)
            [
              [
                2 x^2 - 3 < 0
                \\/
                x = _root_-1 2 x^2 - 3
              ]
              /\\\n              y = _root_-1 y^2 + x^2 - 3
            ]
            \\/
            [
              x^2 - 3 <= 0
              /\\\n              x > _root_-1 2 x^2 - 3
              /\\\n              y^2 + x^2 - 3 = 0
            ]
            sage: qe.solution_extension('T')                    # not tested (random order)
            y + x > 0 /\\ y^2 + x^2 - 3 = 0

        TESTS:

        Tests related to the not tested examples (nondeterministic order of atoms)::

            sage: from sage.interfaces.qepcad import _qepcad_atoms
            sage: var('x,y')
            (x, y)
            sage: qf = qepcad_formula
            sage: qe = qepcad(qf.and_(x^2 + y^2 - 3 == 0, x + y > 0), interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: _qepcad_atoms(qe.solution_extension('E'))        # optional - qepcad
            {'2 x^2 - 3 > 0',
             'x > _root_1 2 x^2 - 3',
             'y = _root_-1 y^2 + x^2 - 3',
             'y^2 + x^2 - 3 = 0'}
            sage: _qepcad_atoms(qe.solution_extension('G'))        # optional - qepcad
            {'2 x^2 - 3 < 0',
             'x = _root_-1 2 x^2 - 3',
             'x > _root_-1 2 x^2 - 3',
             'x^2 - 3 <= 0',
             'y = _root_-1 y^2 + x^2 - 3',
             'y^2 + x^2 - 3 = 0'}
            sage: _qepcad_atoms(qe.solution_extension('T'))        # optional - qepcad
            {'y + x > 0', 'y^2 + x^2 - 3 = 0'}
        """
    def set_truth_value(self, index, nv) -> None:
        """
        Given a cell index (or a cell) and an integer, set the truth value
        of the cell to that integer.

        Valid integers are 0 (false), 1 (true), and 2 (undetermined).

        EXAMPLES::

            sage: qe = qepcad(x == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'At the end of projection phase'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.set_truth_value(1, 1) # optional - qepcad
        """
    def phase(self):
        """
        Return the current phase of the QEPCAD program.

        EXAMPLES::

            sage: # optional - qepcad
            sage: qe = qepcad(x > 2/3, interact=True)
            sage: qe.phase()
            'Before Normalization'
            sage: qe.go()
            QEPCAD object has moved to phase 'At the end of projection phase'
            sage: qe.phase()
            'At the end of projection phase'
            sage: qe.go()
            QEPCAD object has moved to phase 'Before Choice'
            sage: qe.phase()
            'Before Choice'
            sage: qe.go()
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.phase()
            'Before Solution'
            sage: qe.go()
            3 x - 2 > 0
            sage: qe.phase()
            'EXITED'
        """
    def answer(self):
        """
        For a QEPCAD instance which is finished, return the
        simplified quantifier-free formula that it printed just before
        exiting.

        EXAMPLES::

            sage: qe = qepcad(x^3 - x == 0, interact=True)  # optional - qepcad
            sage: qe.finish()                               # not tested (random order)
            x - 1 <= 0 /\\ x + 1 >= 0 /\\ [ x = 0 \\/ x - 1 = 0 \\/ x + 1 = 0 ]
            sage: qe.answer()                               # not tested (random order)
            x - 1 <= 0 /\\ x + 1 >= 0 /\\ [ x = 0 \\/ x - 1 = 0 \\/ x + 1 = 0 ]

        TESTS:

        Tests related to the not tested examples (nondeterministic order of atoms)::

            sage: from sage.interfaces.qepcad import _qepcad_atoms
            sage: qe = qepcad(x^3 - x == 0, interact=True)  # optional - qepcad
            sage: qe.finish()                               # random, optional - qepcad
            x - 1 <= 0 /\\ x + 1 >= 0 /\\ [ x = 0 \\/ x - 1 = 0 \\/ x + 1 = 0 ]
            sage: _qepcad_atoms(qe.answer())                                       # optional - qepcad
            {'x + 1 = 0', 'x + 1 >= 0', 'x - 1 <= 0', 'x - 1 = 0', 'x = 0'}
        """
    def final_stats(self):
        """
        For a QEPCAD instance which is finished, return the
        statistics that it printed just before exiting.

        EXAMPLES::

            sage: qe = qepcad(x == 0, interact=True)  # optional - qepcad
            sage: qe.finish()  # optional - qepcad
            x = 0
            sage: qe.final_stats()  # random, optional - qepcad
            -----------------------------------------------------------------------------
            0 Garbage collections, 0 Cells and 0 Arrays reclaimed, in 0 milliseconds.
            492840 Cells in AVAIL, 500000 Cells in SPACE.
            System time: 8 milliseconds.
            System time after the initialization: 4 milliseconds.
            -----------------------------------------------------------------------------
        """
    def cell(self, *index):
        """
        Given a cell index, returns a :class:`QepcadCell` wrapper for that
        cell.  Uses a cache for efficiency.

        EXAMPLES::

            sage: # optional - qepcad
            sage: qe = qepcad(x + 3 == 42, interact=True)
            sage: qe.go(); qe.go(); qe.go()
            QEPCAD object has moved to phase 'At the end of projection phase'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.cell(2)
            QEPCAD cell (2)
            sage: qe.cell(2) is qe.cell(2)
            True
        """
    def make_cells(self, text):
        """
        Given the result of some QEPCAD command that returns cells
        (such as :meth:`d_cell`, :meth:`d_witness_list`, etc.),
        return a list of cell objects.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.make_cells(qe.d_false_cells()) # optional - qepcad
            [QEPCAD cell (5, 1), QEPCAD cell (4, 3), QEPCAD cell (4, 1), QEPCAD cell (3, 5), QEPCAD cell (3, 3), QEPCAD cell (3, 1), QEPCAD cell (2, 3), QEPCAD cell (2, 1), QEPCAD cell (1, 1)]
        """
    def __getattr__(self, attrname):
        """
        Return a :class:`QepcadFunction` object for any QEPCAD command.

        EXAMPLES::

            sage: qe = qepcad(x^3 == 8, interact=True) # optional - qepcad
            sage: qe.d_cell # optional - qepcad
            d_cell
        """

class QepcadFunction(ExpectFunction):
    """
    A wrapper for a QEPCAD command.
    """
    def __call__(self, *args):
        """
        Call QEPCAD with the command this is a wrapper for.

        For commands which take cell indexes, :func:`_format_cell_index`
        is automatically called.  For commands which take 'y' or 'n',
        booleans are also allowed.  (These special commands were hand-selected
        after reading ``qepcad.help``.)

        EXAMPLES::

            sage: qe = qepcad(x^2 < 1, interact=True) # optional - qepcad
            sage: cmd = qe.d_formula # optional - qepcad
            sage: cmd.__call__() # optional - qepcad
            x^2 - 1 < 0
        """

def qepcad(formula, assume=None, interact: bool = False, solution=None, vars=None, **kwargs):
    """
    Quantifier elimination and formula simplification using QEPCAD B.

    If ``assume`` is specified, then the given formula is ``'assumed'``,
    which is taken into account during final solution formula construction.

    If ``interact=True`` is given, then a :class:`Qepcad` object is
    returned which can be interacted with either at the command line
    or programmatically.

    The type of solution returned can be adjusted with ``solution``.
    The options are ``'geometric'``, which tries to construct a
    solution formula with geometric meaning; ``'extended'``, which
    gives a solution formula in an extended language that may be more
    efficient to construct; ``'any-point'``, which returns any
    point where the formula is true; ``'all-points'``, which
    returns a list of all points where the formula is true (or raises
    an exception if there are infinitely many); and ``'cell-points'``,
    which returns one point in each cell where the formula is true.

    All other keyword arguments are passed through to the :class:`Qepcad`
    constructor.

    For much more documentation and many more examples, see the module
    docstring for this module (type ``sage.interfaces.qepcad?`` to
    read this docstring from the \\sage command line).

    The examples below require that the optional qepcad package is installed.

    EXAMPLES::

        sage: qf = qepcad_formula

        sage: var('a,b,c,d,x,y,z,long_with_underscore_314159')
        (a, b, c, d, x, y, z, long_with_underscore_314159)
        sage: K.<q,r> = QQ[]

        sage: qepcad('(E x)[a x + b > 0]', vars='(a,b,x)')      # not tested (random order)
        a /= 0 \\/ b > 0

        sage: qepcad(a > b)                            # optional - qepcad
        b - a < 0

        sage: qepcad(qf.exists(x, a*x^2 + b*x + c == 0))        # not tested (random order)
        4 a c - b^2 <= 0 /\\ [ c = 0 \\/ a /= 0 \\/ 4 a c - b^2 < 0 ]

        sage: qepcad(qf.exists(x, a*x^2 + b*x + c == 0), assume=(a != 0))    # optional - qepcad
        4 a c - b^2 <= 0

    For which values of `a`, `b`, `c` does `a x^2 + b x + c` have
    2 real zeroes? ::

        sage: exact2 = qepcad(qf.exactly_k(2, x, a*x^2 + b*x + c == 0)); exact2   # not tested (random order)
        a /= 0 /\\ 4 a c - b^2 < 0

    one real zero? ::

        sage: exact1 = qepcad(qf.exactly_k(1, x, a*x^2 + b*x + c == 0)); exact1   # not tested (random order)
        [ a > 0 /\\ 4 a c - b^2 = 0 ] \\/ [ a < 0 /\\ 4 a c - b^2 = 0 ] \\/ [ a = 0 /\\ 4 a c - b^2 < 0 ]

    No real zeroes? ::

        sage: exact0 = qepcad(qf.forall(x, a*x^2 + b*x + c != 0)); exact0     # not tested (random order)
        4 a c - b^2 >= 0 /\\ c /= 0 /\\ [ b = 0 \\/ 4 a c - b^2 > 0 ]

    `3^{75}` real zeroes? ::

        sage: qepcad(qf.exactly_k(3^75, x, a*x^2 + b*x + c == 0))    # optional - qepcad
        FALSE

    We can check that the results don't overlap::

        sage: qepcad(r'[[%s] /\\ [%s]]' % (exact0, exact1), vars='a,b,c')      # not tested (random order)
        FALSE
        sage: qepcad(r'[[%s] /\\ [%s]]' % (exact0, exact2), vars='a,b,c')      # not tested (random order)
        FALSE
        sage: qepcad(r'[[%s] /\\ [%s]]' % (exact1, exact2), vars='a,b,c')      # not tested (random order)
        FALSE

    and that the union of the results is as expected::

        sage: qepcad(r'[[%s] \\/ [%s] \\/ [%s]]' % (exact0, exact1, exact2), vars=(a,b,c))  # not tested (random order)
        b /= 0 \\/ a /= 0 \\/ c /= 0

    So we have finitely many zeroes if `a`, `b`, or `c` is nonzero;
    which means we should have infinitely many zeroes if they are all
    zero. ::

        sage: qepcad(qf.infinitely_many(x, a*x^2 + b*x + c == 0))          # not tested (random order)
        a = 0 /\\ b = 0 /\\ c = 0

    The polynomial is nonzero almost everywhere iff it is not
    identically zero. ::

        sage: qepcad(qf.all_but_finitely_many(x, a*x^2 + b*x + c != 0))    # not tested (random order)
        b /= 0 \\/ a /= 0 \\/ c /= 0

    The nonzeroes are continuous iff there are no zeroes or if
    the polynomial is zero. ::

        sage: qepcad(qf.connected_subset(x, a*x^2 + b*x + c != 0))         # not tested (random order)
        4 a c - b^2 >= 0 /\\ [ a = 0 \\/ 4 a c - b^2 > 0 ]

    The zeroes are continuous iff there are no or one zeroes, or if the
    polynomial is zero::

        sage: qepcad(qf.connected_subset(x, a*x^2 + b*x + c == 0))         # not tested (random order)
        a = 0 \\/ 4 a c - b^2 >= 0
        sage: qepcad(r'[[%s] \\/ [%s] \\/ [a = 0 /\\ b = 0 /\\ c = 0]]' % (exact0, exact1), vars='a,b,c')   # not tested (random order)
        a = 0 \\/ 4 a c - b^2 >= 0

    Since polynomials are continuous and `y > 0` is an open set,
    they are positive infinitely often iff they are positive at
    least once. ::

        sage: qepcad(qf.infinitely_many(x, a*x^2 + b*x + c > 0))        # not tested (random order)
        c > 0 \\/ a > 0 \\/ 4 a c - b^2 < 0
        sage: qepcad(qf.exists(x, a*x^2 + b*x + c > 0))                 # not tested (random order)
        c > 0 \\/ a > 0 \\/ 4 a c - b^2 < 0

    However, since `y >= 0` is not open, the equivalence does not
    hold if you replace 'positive' with 'nonnegative'.
    (We assume `a \\neq 0` to get simpler formulas.) ::

        sage: qepcad(qf.infinitely_many(x, a*x^2 + b*x + c >= 0), assume=(a != 0))    # not tested (random order)
        a > 0 \\/ 4 a c - b^2 < 0
        sage: qepcad(qf.exists(x, a*x^2 + b*x + c >= 0), assume=(a != 0))             # not tested (random order)
        a > 0 \\/ 4 a c - b^2 <= 0

    TESTS:

    We verify that long variable names work.  (Note that QEPCAD
    does not support underscores, so they are stripped from the formula.) ::

        sage: qepcad(qf.exists(a, a*long_with_underscore_314159 == 1))                # optional - qepcad
        longwithunderscore314159 /= 0

    Tests related to the not tested examples (nondeterministic order of atoms)::

        sage: from sage.interfaces.qepcad import _qepcad_atoms
        sage: var('a,b,c,d,x,y,z,long_with_underscore_314159')
        (a, b, c, d, x, y, z, long_with_underscore_314159)
        sage: K.<q,r> = QQ[]

        sage: _qepcad_atoms(qepcad('(E x)[a x + b > 0]', vars='(a,b,x)'))                       # optional - qepcad
        {'a /= 0', 'b > 0'}

        sage: _qepcad_atoms(qepcad(qf.exists(x, a*x^2 + b*x + c == 0)))                         # optional - qepcad
        {'4 a c - b^2 < 0', '4 a c - b^2 <= 0', 'a /= 0', 'c = 0'}

        sage: exact2 = qepcad(qf.exactly_k(2, x, a*x^2 + b*x + c == 0)); _qepcad_atoms(exact2)  # optional - qepcad
        {'4 a c - b^2 < 0', 'a /= 0'}

        sage: exact1 = qepcad(qf.exactly_k(1, x, a*x^2 + b*x + c == 0)); _qepcad_atoms(exact1)  # optional - qepcad
        {'4 a c - b^2 < 0', '4 a c - b^2 = 0', 'a < 0', 'a = 0', 'a > 0'}

        sage: exact0 = qepcad(qf.forall(x, a*x^2 + b*x + c != 0)); _qepcad_atoms(exact0)        # optional - qepcad
        {'4 a c - b^2 > 0', '4 a c - b^2 >= 0', 'b = 0', 'c /= 0'}

        sage: qepcad(r'[[%s] /\\ [%s]]' % (exact0, exact1), vars='a,b,c')                        # optional - qepcad
        FALSE
        sage: qepcad(r'[[%s] /\\ [%s]]' % (exact0, exact2), vars='a,b,c')                        # optional - qepcad
        FALSE
        sage: qepcad(r'[[%s] /\\ [%s]]' % (exact1, exact2), vars='a,b,c')                        # optional - qepcad
        FALSE

        sage: _qepcad_atoms(qepcad(r'[[%s] \\/ [%s] \\/ [%s]]' % (exact0, exact1, exact2), vars=(a,b,c)))    # optional - qepcad
        {'a /= 0', 'b /= 0', 'c /= 0'}

        sage: _qepcad_atoms(qepcad(qf.infinitely_many(x, a*x^2 + b*x + c == 0)))               # optional - qepcad
        {'a = 0', 'b = 0', 'c = 0'}

        sage: _qepcad_atoms(qepcad(qf.all_but_finitely_many(x, a*x^2 + b*x + c != 0)))         # optional - qepcad
        {'a /= 0', 'b /= 0', 'c /= 0'}

        sage: _qepcad_atoms(qepcad(qf.connected_subset(x, a*x^2 + b*x + c != 0)))              # optional - qepcad
        {'4 a c - b^2 > 0', '4 a c - b^2 >= 0', 'a = 0'}

        sage: _qepcad_atoms(qepcad(qf.connected_subset(x, a*x^2 + b*x + c == 0)))              # optional - qepcad
        {'4 a c - b^2 >= 0', 'a = 0'}

        sage: _qepcad_atoms(qepcad(r'[[%s] \\/ [%s] \\/ [a = 0 /\\ b = 0 /\\ c = 0]]' % (exact0, exact1), vars='a,b,c'))   # optional - qepcad
        {'4 a c - b^2 >= 0', 'a = 0'}

        sage: _qepcad_atoms(qepcad(qf.infinitely_many(x, a*x^2 + b*x + c > 0)))                # optional - qepcad
        {'4 a c - b^2 < 0', 'a > 0', 'c > 0'}

        sage: _qepcad_atoms(qepcad(qf.exists(x, a*x^2 + b*x + c > 0)))                         # optional - qepcad
        {'4 a c - b^2 < 0', 'a > 0', 'c > 0'}

        sage: _qepcad_atoms(qepcad(qf.infinitely_many(x, a*x^2 + b*x + c >= 0), assume=(a != 0)))  # optional - qepcad
        {'4 a c - b^2 < 0', 'a > 0'}

        sage: _qepcad_atoms(qepcad(qf.exists(x, a*x^2 + b*x + c >= 0), assume=(a != 0)))       # optional - qepcad
        {'4 a c - b^2 <= 0', 'a > 0'}
    """
def qepcad_console(memcells=None) -> None:
    """
    Run QEPCAD directly.  To exit early, press :kbd:`Control` + :kbd:`C`.

    EXAMPLES::

        sage: qepcad_console() # not tested
        ...
        Enter an informal description  between '[' and ']':
    """
def qepcad_banner():
    """
    Return the QEPCAD startup banner.

    EXAMPLES::

        sage: from sage.interfaces.qepcad import qepcad_banner
        sage: qepcad_banner() # optional - qepcad
        =======================================================
                        Quantifier Elimination
                                  in
                    Elementary Algebra and Geometry
                                  by
              Partial Cylindrical Algebraic Decomposition
        ...
                                  by
                               Hoon Hong
                         (hhong@math.ncsu.edu)
        With contributions by: Christopher W. Brown, George E.
        Collins, Mark J. Encarnacion, Jeremy R. Johnson
        Werner Krandick, Richard Liska, Scott McCallum,
        Nicolas Robidoux, and Stanly Steinberg
        =======================================================
    """
def qepcad_version():
    """
    Return a string containing the current QEPCAD version number.

    EXAMPLES::

        sage: qepcad_version() # random, optional - qepcad
        'Version B 1.69, 16 Mar 2012'

    TESTS::

        sage: qepcad_version() # optional - qepcad
        'Version B ..., ...'
    """

class qformula:
    """
    A qformula holds a string describing a formula in QEPCAD's syntax,
    and a set of variables used.
    """
    formula: Incomplete
    vars: Incomplete
    qvars: Incomplete
    def __init__(self, formula, vars, qvars=[]) -> None:
        """
        Construct a qformula from a string, a frozenset of variable names,
        and (optionally) a list of ordered quantified names.

        EXAMPLES::

            sage: from sage.interfaces.qepcad import qformula
            sage: f = qformula('x + y = 0', frozenset(['x','y']))
            sage: f
            x + y = 0
            sage: f.formula
            'x + y = 0'
            sage: f.vars
            frozenset({'x', 'y'})
            sage: f.qvars
            []
        """

class qepcad_formula_factory:
    """
    Contains routines to help construct formulas in QEPCAD syntax.
    """
    def atomic(self, lhs, op: str = '=', rhs: int = 0):
        """
        Construct a QEPCAD formula from the given inputs.

        INPUT:

        - ``lhs`` -- a polynomial, or a symbolic equality or inequality
        - ``op`` -- a relational operator, default '='
        - ``rhs`` -- a polynomial, default 0

        If ``lhs`` is a symbolic equality or inequality, then ``op``
        and ``rhs`` are ignored.

        This method works by printing the given polynomials, so we do not
        care what ring they are in (as long as they print with integral
        or rational coefficients).

        EXAMPLES::

            sage: qf = qepcad_formula
            sage: var('a,b,c')
            (a, b, c)
            sage: K.<x,y> = QQ[]
            sage: def test_qf(qf):
            ....:     return qf, qf.vars
            sage: test_qf(qf.atomic(a^2 + 17))
            (a^2 + 17 = 0, frozenset({'a'}))
            sage: test_qf(qf.atomic(a*b*c <= c^3))
            (a b c <= c^3, frozenset({'a', 'b', 'c'}))
            sage: test_qf(qf.atomic(x+y^2, '!=', a+b))
            (y^2 + x /= a + b, frozenset({'a', 'b', 'x', 'y'}))
            sage: test_qf(qf.atomic(x, operator.lt))
            (x < 0, frozenset({'x'}))
        """
    def formula(self, formula):
        """
        Construct a QEPCAD formula from the given input.

        INPUT:

        - ``formula`` -- a polynomial, a symbolic equality or inequality,
          or a list of polynomials, equalities, or inequalities

        A polynomial `p` is interpreted as the equation `p = 0`.
        A list is interpreted as the conjunction ('and') of the elements.

        EXAMPLES::

            sage: var('a,b,c,x')
            (a, b, c, x)
            sage: qf = qepcad_formula
            sage: qf.formula(a*x + b)
            a x + b = 0
            sage: qf.formula((a*x^2 + b*x + c, a != 0))
            [a x^2 + b x + c = 0 /\\ a /= 0]
        """
    def and_(self, *formulas):
        """
        Return the conjunction of its input formulas.

        (This method would be named 'and' if that were not a Python
        keyword.)

        Each input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b,c,x')
            (a, b, c, x)
            sage: qf = qepcad_formula
            sage: qf.and_(a*b, a*c, b*c != 0)
            [a b = 0 /\\ a c = 0 /\\ b c /= 0]
            sage: qf.and_(a*x^2 == 3, qf.or_(a > b, b > c))
            [a x^2 = 3 /\\ [a > b \\/ b > c]]
        """
    def or_(self, *formulas):
        """
        Return the disjunction of its input formulas.

        (This method would be named 'or' if that were not a Python
        keyword.)

        Each input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b,c,x')
            (a, b, c, x)
            sage: qf = qepcad_formula
            sage: qf.or_(a*b, a*c, b*c != 0)
            [a b = 0 \\/ a c = 0 \\/ b c /= 0]
            sage: qf.or_(a*x^2 == 3, qf.and_(a > b, b > c))
            [a x^2 = 3 \\/ [a > b /\\ b > c]]
        """
    def not_(self, formula):
        """
        Return the negation of its input formula.

        (This method would be named 'not' if that were not a Python
        keyword.)

        The input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.not_(a > b)
            [~a > b]
            sage: qf.not_(a^2 + b^2)
            [~a^2 + b^2 = 0]
            sage: qf.not_(qf.and_(a > 0, b < 0))
            [~[a > 0 /\\ b < 0]]
        """
    def implies(self, f1, f2):
        """
        Return the implication of its input formulas (that is, given
        formulas `P` and `Q`, returns '`P` implies `Q`').

        The input formulas may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.implies(a, b)
            [a = 0 ==> b = 0]
            sage: qf.implies(a^2 < b, b^2 < a)
            [a^2 < b ==> b^2 < a]
        """
    def iff(self, f1, f2):
        """
        Return the equivalence of its input formulas (that is, given
        formulas `P` and `Q`, returns '`P` iff `Q`').

        The input formulas may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.iff(a, b)
            [a = 0 <==> b = 0]
            sage: qf.iff(a^2 < b, b^2 < a)
            [a^2 < b <==> b^2 < a]
        """
    def exists(self, v, formula):
        """
        Given a variable (or list of variables) and a formula, returns
        the existential quantification of the formula over the variables.

        This method is available both as :meth:`exists` and :meth:`E`
        (the QEPCAD name for this quantifier).

        The input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.exists(a, a^2 + b > b^2 + a)
            (E a)[a^2 + b > b^2 + a]
            sage: qf.exists((a, b), a^2 + b^2 < 0)
            (E a)(E b)[a^2 + b^2 < 0]
            sage: qf.E(b, b^2 == a)
            (E b)[b^2 = a]
        """
    E = exists
    def forall(self, v, formula):
        """
        Given a variable (or list of variables) and a formula, returns
        the universal quantification of the formula over the variables.

        This method is available both as :meth:`forall` and :meth:`A`
        (the QEPCAD name for this quantifier).

        The input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.forall(a, a^2 + b > b^2 + a)
            (A a)[a^2 + b > b^2 + a]
            sage: qf.forall((a, b), a^2 + b^2 > 0)
            (A a)(A b)[a^2 + b^2 > 0]
            sage: qf.A(b, b^2 != a)
            (A b)[b^2 /= a]
        """
    A = forall
    def infinitely_many(self, v, formula):
        """
        Given a variable and a formula, returns a new formula which is
        true iff the original formula was true for infinitely many
        values of the variable.

        This method is available both as :meth:`infinitely_many`
        and :meth:`F` (the QEPCAD name for this quantifier).

        The input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.infinitely_many(a, a^2 + b > b^2 + a)
            (F a)[a^2 + b > b^2 + a]
            sage: qf.F(b, b^2 != a)
            (F b)[b^2 /= a]
        """
    F = infinitely_many
    def all_but_finitely_many(self, v, formula):
        """
        Given a variable and a formula, returns a new formula which is
        true iff the original formula was true for all but finitely many
        values of the variable.

        This method is available both as :meth:`all_but_finitely_many`
        and :meth:`G` (the QEPCAD name for this quantifier).

        The input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.all_but_finitely_many(a, a^2 + b > b^2 + a)
            (G a)[a^2 + b > b^2 + a]
            sage: qf.G(b, b^2 != a)
            (G b)[b^2 /= a]
        """
    G = all_but_finitely_many
    def connected_subset(self, v, formula, allow_multi: bool = False):
        """
        Given a variable and a formula, returns a new formula which is
        true iff the set of values for the variable at which the
        original formula was true is connected (including cases where
        this set is empty or is a single point).

        This method is available both as :meth:`connected_subset`
        and :meth:`C` (the QEPCAD name for this quantifier).

        The input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.connected_subset(a, a^2 + b > b^2 + a)
            (C a)[a^2 + b > b^2 + a]
            sage: qf.C(b, b^2 != a)
            (C b)[b^2 /= a]
        """
    C = connected_subset
    def exactly_k(self, k, v, formula, allow_multi: bool = False):
        """
        Given a nonnegative integer `k`, a variable, and a formula,
        returns a new formula which is true iff the original formula
        is true for exactly `k` values of the variable.

        This method is available both as :meth:`exactly_k`
        and :meth:`X` (the QEPCAD name for this quantifier).

        (Note that QEPCAD does not support `k=0` with this syntax, so if
        `k=0` is requested we implement it with :meth:`forall` and
        :meth:`not_`.)

        The input formula may be a :class:`qformula` as returned by the
        methods of ``qepcad_formula``, a symbolic equality or
        inequality, or a polynomial `p` (meaning `p = 0`).

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.exactly_k(1, x, x^2 + a*x + b == 0)
            (X1 x)[a x + x^2 + b = 0]
            sage: qf.exactly_k(0, b, a*b == 1)
            (A b)[~a b = 1]
        """
    X = exactly_k
    def quantifier(self, kind, v, formula, allow_multi: bool = True):
        """
        A helper method for building quantified QEPCAD formulas; not
        expected to be called directly.

        Takes the quantifier kind (the string label of this quantifier),
        a variable or list of variables, and a formula, and returns
        the quantified formula.

        EXAMPLES::

            sage: var('a,b')
            (a, b)
            sage: qf = qepcad_formula
            sage: qf.quantifier('NOT_A_REAL_QEPCAD_QUANTIFIER', a, a*b==0)
            (NOT_A_REAL_QEPCAD_QUANTIFIER a)[a b = 0]
            sage: qf.quantifier('FOO', (a, b), a*b)
            (FOO a)(FOO b)[a b = 0]
        """

qepcad_formula: Incomplete

class QepcadCell:
    """
    A wrapper for a QEPCAD cell.
    """
    def __init__(self, parent, lines) -> None:
        """
        Construct a :class:`QepcadCell` wrapper for a QEPCAD cell, given
        a :class:`Qepcad` object and a list of lines holding QEPCAD's
        cell output.

        This is typically called by the :meth:`Qepcad.make_cells`
        method of :class:`Qepcad`.

        EXAMPLES::

            sage: from sage.interfaces.qepcad import QepcadCell
            sage: var('a,b')
            (a, b)
            sage: qe = qepcad(a^2 + b^2 == 5, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (b)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.d_cell(4, 3) # optional - qepcad
            ---------- Information about the cell (4,3) ----------
            Level                       : 2
            Dimension                   : 1
            Number of children          : 0
            Truth value                 : F    by trial evaluation.
            Degrees after substitution  : Not known yet or No polynomial.
            Multiplicities              : ()
            Signs of Projection Factors
            Level 1  : (0)
            Level 2  : (+)
            ----------   Sample point  ----------
            The sample point is in a PRIMITIVE representation.
            <BLANKLINE>
            alpha = the unique root of x^2 - 5 between 2289/1024 and 1145/512
                  = 2.2360679775-
            <BLANKLINE>
            Coordinate 1 = alpha
                         = 2.2360679775-
            Coordinate 2 = 1
                         = 1.0000000000
            ----------------------------------------------------

            sage: QepcadCell(qe, str(qe.d_cell(4, 3)).splitlines()) # optional - qepcad
            QEPCAD cell (4, 3)
        """
    def __iter__(self):
        """
        Iterate through the stack over a QEPCAD cell.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: [c.sample_point() for c in qe.cell(3)] # optional - qepcad
            [(0, -3), (0, -1), (0, -1/2), (0, 1), (0, 3)]
        """
    def __getitem__(self, i):
        """
        Select an element from the stack over a QEPCAD cell.

        Note that cells are numbered starting with 1.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True)  # optional - qepcad
            sage: qe.go(); qe.go(); qe.go()  # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.cell(2).__getitem__(3)  # optional - qepcad
            QEPCAD cell (2, 3)
        """
    def __len__(self) -> int:
        """
        Return the number of elements in the stack over a QEPCAD cell.

        This is always an odd number, if the stack has been constructed.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: len(qe.cell()) # optional - qepcad
            5
            sage: [len(c) for c in qe.cell()] # optional - qepcad
            [1, 3, 5, 3, 1]
        """
    def index(self):
        """
        Give the index of a QEPCAD cell.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.cell().index() # optional - qepcad
            ()
            sage: qe.cell(1).index() # optional - qepcad
            (1,)
            sage: qe.cell(2, 2).index() # optional - qepcad
            (2, 2)
        """
    def level(self):
        """
        Return the level of a QEPCAD cell.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.cell().level() # optional - qepcad
            0
            sage: qe.cell(1).level() # optional - qepcad
            1
            sage: qe.cell(2, 2).level() # optional - qepcad
            2
        """
    def signs(self):
        """
        Return the sign vector of a QEPCAD cell.

        This is a list of lists.
        The outer list contains one element for each level of the cell;
        the inner list contains one element for each projection factor at
        that level.  These elements are either -1, 0, or 1.

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: from sage.interfaces.qepcad import QepcadCell
            sage: all_cells = flatten(qe.cell(), ltypes=QepcadCell, max_level=1) # optional - qepcad
            sage: [(c, c.signs()[1][0]) for c in all_cells] # optional - qepcad
            [(QEPCAD cell (1, 1), 1), (QEPCAD cell (2, 1), 1), (QEPCAD cell (2, 2), 0), (QEPCAD cell (2, 3), 1), (QEPCAD cell (3, 1), 1), (QEPCAD cell (3, 2), 0), (QEPCAD cell (3, 3), -1), (QEPCAD cell (3, 4), 0), (QEPCAD cell (3, 5), 1), (QEPCAD cell (4, 1), 1), (QEPCAD cell (4, 2), 0), (QEPCAD cell (4, 3), 1), (QEPCAD cell (5, 1), 1)]
        """
    def number_of_children(self):
        """
        Return the number of elements in the stack over a QEPCAD cell.
        (This is always an odd number, if the stack has been constructed.)

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.cell().number_of_children() # optional - qepcad
            5
            sage: [c.number_of_children() for c in qe.cell()] # optional - qepcad
            [1, 3, 5, 3, 1]
        """
    def set_truth(self, v) -> None:
        """
        Set the truth value of this cell, as used by QEPCAD for solution
        formula construction.

        The argument ``v`` should be either a boolean or ``None``
        (which will set the truth value to ``'undetermined'``).

        EXAMPLES::

            sage: var('x,y')
            (x, y)
            sage: qe = qepcad(x^2 + y^2 == 1, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'Before Projection (y)'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.solution_extension('T') # optional - qepcad
            y^2 + x^2 - 1 = 0
            sage: qe.cell(3, 3).set_truth(True) # optional - qepcad
            sage: qe.solution_extension('T') # optional - qepcad
            y^2 + x^2 - 1 <= 0
        """
    def sample_point(self):
        """
        Return the coordinates of a point in the cell, as a tuple of
        \\sage algebraic reals.

        EXAMPLES::

            sage: # optional - qepcad
            sage: qe = qepcad(x^2 - x - 1 == 0, interact=True)
            sage: qe.go(); qe.go(); qe.go()
            QEPCAD object has moved to phase 'At the end of projection phase'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: v1 = qe.cell(2).sample_point()[0]; v1
            -0.618033988749895?
            sage: v2 = qe.cell(4).sample_point()[0]; v2
            1.618033988749895?
            sage: v1 + v2 == 1
            True
        """
    def sample_point_dict(self):
        """
        Return the coordinates of a point in the cell, as a dictionary
        mapping variable names (as strings) to \\sage algebraic reals.

        EXAMPLES::

            sage: qe = qepcad(x^2 - x - 1 == 0, interact=True) # optional - qepcad
            sage: qe.go(); qe.go(); qe.go() # optional - qepcad
            QEPCAD object has moved to phase 'At the end of projection phase'
            QEPCAD object has moved to phase 'Before Choice'
            QEPCAD object has moved to phase 'Before Solution'
            sage: qe.cell(4).sample_point_dict() # optional - qepcad
            {'x': 1.618033988749895?}
        """
