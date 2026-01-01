r"""
Interface to GNU Octave

GNU Octave is a free software (GPL) MATLAB-like program with numerical
routines for integrating, solving systems of equations, special
functions, and solving (numerically) differential equations. Please see
http://octave.org/ for more details.

The commands in this section only work if you have the optional
"octave" interpreter installed and available in your PATH. It's not
necessary to install any special Sage packages.

EXAMPLES::

    sage: octave.eval('2+2')    # optional - octave
    'ans = 4'

    sage: a = octave(10)        # optional - octave
    sage: a**10                 # optional - octave
    1e+10

LOG: - creation (William Stein) - ? (David Joyner, 2005-12-18) -
Examples (David Joyner, 2005-01-03)

Computation of Special Functions
--------------------------------

Octave implements computation of the following special functions
(see the maxima and gp interfaces for even more special
functions)::

    airy
        Airy functions of the first and second kind, and their derivatives.
        airy(0,x) = Ai(x), airy(1,x) = Ai'(x), airy(2,x) = Bi(x), airy(3,x) = Bi'(x)
    besselj
        Bessel functions of the first kind.
    bessely
        Bessel functions of the second kind.
    besseli
        Modified Bessel functions of the first kind.
    besselk
        Modified Bessel functions of the second kind.
    besselh
        Compute Hankel functions of the first (k = 1) or second (k = 2) kind.
    beta
        The Beta function,
              beta (a, b) = gamma (a) * gamma (b) / gamma (a + b).
    betainc
        The incomplete Beta function,
    erf
        The error function,
    erfinv
        The inverse of the error function.
    gamma
        The Gamma function,
    gammainc
        The incomplete gamma function,

For example,

::

    sage: # optional - octave
    sage: octave("airy(3,2)")
    4.10068
    sage: octave("beta(2,2)")
    0.166667
    sage: octave("betainc(0.2,2,2)")
    0.104
    sage: octave("besselh(0,2)")
    (0.223891,0.510376)
    sage: octave("besselh(0,1)")
    (0.765198,0.088257)
    sage: octave("besseli(1,2)")
    1.59064
    sage: octave("besselj(1,2)")
    0.576725
    sage: octave("besselk(1,2)")
    0.139866
    sage: octave("erf(0)")
    0
    sage: octave("erf(1)")
    0.842701
    sage: octave("erfinv(0.842)")
    0.998315
    sage: octave("gamma(1.5)")
    0.886227
    sage: octave("gammainc(1.5,1)")
    0.77687

Tutorial
--------

EXAMPLES::

    sage: # optional - octave
    sage: octave('4+10')
    14
    sage: octave('date')
    18-Oct-2007
    sage: octave('5*10 + 6')
    56
    sage: octave('(6+6)/3')
    4
    sage: octave('9')^2
    81
    sage: a = octave(10); b = octave(20); c = octave(30)
    sage: avg = (a+b+c)/3
    sage: avg
    20
    sage: parent(avg)
    Octave

::

    sage: # optional - octave
    sage: my_scalar = octave('3.1415')
    sage: my_scalar
    3.1415
    sage: my_vector1 = octave('[1,5,7]')
    sage: my_vector1
    1     5     7
    sage: my_vector2 = octave('[1;5;7]')
    sage: my_vector2
    1
    5
    7
    sage: my_vector1 * my_vector2
    75
"""
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

octave_functions: set

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

octave: Octave

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
