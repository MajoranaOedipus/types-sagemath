from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.misc.verbose import verbose as verbose

class Octave(Expect):
    '''
    Interface to the Octave interpreter.

    EXAMPLES::

        sage: octave.eval("a = [ 1, 1, 2; 3, 5, 8; 13, 21, 33 ]").strip()    # optional - octave
        \'a =\\n\\n 1 1 2\\n 3 5 8\\n 13 21 33\'
        sage: octave.eval("b = [ 1; 3; 13]").strip()                         # optional - octave
        \'b =\\n\\n 1\\n 3\\n 13\'

    The following solves the linear equation: a*c = b::

        sage: octave.eval(r"c=a \\ b").strip()          # optional - octave  # abs tol 0.01
        \'c =\\n\\n 1\\n -0\\n 0\'
        sage: octave.eval("c").strip()                 # optional - octave  # abs tol 0.01
        \'c =\\n\\n 1\\n -0\\n 0\'

    TESTS:

    We check that the interface can handle large inputs (see :issue:`940`)::

        sage: t = \'"{}"\'.format(10^10000)
        sage: a = octave(t)                     # optional - octave
        sage: str(a) == \' {}\'.format(10^10000)  # optional - octave
        True
    '''
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, seed=None, command=None) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.octave import octave
            sage: octave == loads(dumps(octave))
            True
        """
    def set_seed(self, seed=None):
        """
        Set the seed for the random number generator
        for this octave interpreter.

        EXAMPLES::

            sage: o = Octave() # optional - octave
            sage: o.set_seed(1) # optional - octave
            1
            sage: [o.rand() for i in range(5)] # optional - octave
            [ 0.134364,  0.847434,  0.763775,  0.255069,  0.495435]
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: Octave().__reduce__()
            (<function reduce_load_Octave at 0x...>, ())
        """
    def quit(self, verbose: bool = False) -> None:
        """
        EXAMPLES::

            sage: o = Octave()
            sage: o._start()    # optional - octave
            sage: o.quit(True)  # optional - octave
            Exiting spawned Octave process.
        """
    def set(self, var, value) -> None:
        """
        Set the variable ``var`` to the given ``value``.

        EXAMPLES::

            sage: octave.set('x', '2') # optional - octave
            sage: octave.get('x') # optional - octave
            ' 2'
        """
    def get(self, var):
        """
        Get the value of the variable ``var``.

        EXAMPLES::

            sage: octave.set('x', '2') # optional - octave
            sage: octave.get('x') # optional - octave
            ' 2'
        """
    def clear(self, var) -> None:
        '''
        Clear the variable named var.

        EXAMPLES::

            sage: octave.set(\'x\', \'2\') # optional - octave
            sage: octave.clear(\'x\')    # optional - octave
            sage: octave.get(\'x\')      # optional - octave
            "error: \'x\' undefined near line ... column 1"
        '''
    def console(self) -> None:
        """
        Spawn a new Octave command-line session.

        This requires that the optional octave program be installed and in
        your PATH, but no optional Sage packages need be installed.

        EXAMPLES::

            sage: octave_console()         # not tested
            GNU Octave, version 2.1.73 (i386-apple-darwin8.5.3).
            Copyright (C) 2006 John W. Eaton.
            ...
            octave:1> 2+3
            ans = 5
            octave:2> [ctl-d]

        Pressing ctrl-d exits the octave console and returns you to Sage.
        octave, like Sage, remembers its history from one session to
        another.
        """
    def version(self):
        '''
        Return the version of Octave.

        OUTPUT: string

        EXAMPLES::

            sage: v = octave.version()   # optional - octave
            sage: v                      # optional - octave; random
            \'2.13.7\'

            sage: import re
            sage: assert re.match(r"\\d+\\.\\d+\\.\\d+", v)  is not None # optional - octave
        '''
    def solve_linear_system(self, A, b):
        """
        Use Octave to compute a solution x to ``A*x = b``, as a list.

        INPUT:

        - ``A`` -- mxn matrix A with entries in `\\QQ` or `\\RR`

        - ``b`` -- m-vector b entries in `\\QQ` or `\\RR` (resp)

        OUTPUT: list x (if it exists) which solves ``M*x = b``

        EXAMPLES::

            sage: M33 = MatrixSpace(QQ,3,3)
            sage: A   = M33([1,2,3,4,5,6,7,8,0])
            sage: V3  = VectorSpace(QQ,3)
            sage: b   = V3([1,2,3])
            sage: octave.solve_linear_system(A,b)    # optional - octave (and output is slightly random in low order bits)
            [-0.33333299999999999, 0.66666700000000001, -3.5236600000000002e-18]

        AUTHORS:

        - David Joyner and William Stein
        """
    def sage2octave_matrix_string(self, A):
        """
        Return an octave matrix from a Sage matrix.

        INPUT:

        - ``A`` - Sage matrix with entries in the rationals or reals

        OUTPUT: string that evaluates to an Octave matrix

        EXAMPLES::

            sage: M33 = MatrixSpace(QQ,3,3)
            sage: A = M33([1,2,3,4,5,6,7,8,0])
            sage: octave.sage2octave_matrix_string(A)   # optional - octave
            '[1, 2, 3; 4, 5, 6; 7, 8, 0]'

        AUTHORS:

        - David Joyner and William Stein
        """
    def de_system_plot(self, f, ics, trange) -> None:
        """
        Plot (using octave's interface to gnuplot) the solution to a
        `2\\times 2` system of differential equations.

        INPUT:

        - ``f`` -- a pair of strings representing the
          differential equations; the independent variable must be called x
          and the dependent variable must be called y

        - ``ics`` -- a pair [x0,y0] such that x(t0) = x0, y(t0) = y0

        - ``trange`` -- a pair [t0,t1]

        OUTPUT: a gnuplot window appears

        EXAMPLES::

            sage: octave.de_system_plot(['x+y','x-y'], [1,-1], [0,2])  # not tested -- does this actually work (on OS X it fails for me -- William Stein, 2007-10)

        This should yield the two plots `(t,x(t)), (t,y(t))` on the
        same graph (the `t`-axis is the horizontal axis) of the
        system of ODEs

        .. MATH::

                       x' = x+y, x(0) = 1;\\qquad y' = x-y, y(0) = -1,                     \\quad\\text{for}\\quad 0 < t < 2.
        """

octave_functions: Incomplete

def to_complex(octave_string, R):
    """
    Helper function to convert octave complex number.

    TESTS::

        sage: from sage.interfaces.octave import to_complex
        sage: to_complex('(0,1)', CDF)
        1.0*I
        sage: to_complex('(1.3231,-0.2)', CDF)
        1.3231 - 0.2*I
    """

class OctaveElement(ExpectElement):
    def __bool__(self) -> bool:
        """
        Test whether this element is nonzero.

        EXAMPLES::

            sage: # optional - octave
            sage: bool(octave('0'))
            False
            sage: bool(octave('[]'))
            False
            sage: bool(octave('[0,0]'))
            False
            sage: bool(octave('[0,0,0;0,0,0]'))
            False

            sage: bool(octave('0.1'))               # optional - octave
            True
            sage: bool(octave('[0,1,0]'))           # optional - octave
            True
            sage: bool(octave('[0,0,-0.1;0,0,0]'))  # optional - octave
            True
        """

octave: Incomplete

def reduce_load_Octave():
    """
    EXAMPLES::

        sage: from sage.interfaces.octave import reduce_load_Octave
        sage: reduce_load_Octave()
        Octave
    """
def octave_console() -> None:
    """
    Spawn a new Octave command-line session.

    This requires that the optional octave program be installed and in
    your PATH, but no optional Sage packages need be installed.

    EXAMPLES::

        sage: octave_console()         # not tested
        GNU Octave, version 2.1.73 (i386-apple-darwin8.5.3).
        Copyright (C) 2006 John W. Eaton.
        ...
        octave:1> 2+3
        ans = 5
        octave:2> [ctl-d]

    Pressing ctrl-d exits the octave console and returns you to Sage.
    octave, like Sage, remembers its history from one session to
    another.
    """
