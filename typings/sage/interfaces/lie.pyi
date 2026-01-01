r"""
Interface to LiE

LiE is a software package under development at CWI since
January 1988.  Its purpose is to enable mathematicians and
physicists to obtain on-line information as well as to
interactively perform computations of a Lie group theoretic
nature.  It focuses on the representation theory of complex
semisimple (reductive) Lie groups and algebras, and on the
structure of their Weyl groups and root systems.

Type ``lie.[tab]`` for a list of all the functions available
from your LiE install.  Type ``lie.[tab]?`` for LiE's
help about a given function.  Type ``lie(...)`` to create
a new LiE object, and ``lie.eval(...)`` to run a string
using LiE (and get the result back as a string).

To access the LiE interpreter directly, run lie_console().

EXAMPLES::

    sage: a4 = lie('A4')             # optional - lie
    sage: lie.diagram('A4')          # optional - lie
    O---O---O---O
    1   2   3   4
    A4

    sage: lie.diagram(a4)            # optional - lie
    O---O---O---O
    1   2   3   4
    A4

    sage: a4.diagram()               # optional - lie
    O---O---O---O
    1   2   3   4
    A4

    sage: a4.Cartan()                # optional - lie
         [[ 2,-1, 0, 0]
         ,[-1, 2,-1, 0]
         ,[ 0,-1, 2,-1]
         ,[ 0, 0,-1, 2]
         ]
    sage: lie.LR_tensor([3,1],[2,2]) # optional - lie
    1X[5,3]


Tutorial
--------

The following examples are taken from Section 2.1 of the LiE manual.

You can perform basic arithmetic operations in LiE. ::

    sage: # optional - lie
    sage: lie.eval('19+68')
    '87'
    sage: a = lie('1111111111*1111111111')
    sage: a
    1234567900987654321
    sage: a/1111111111
    1111111111
    sage: a = lie('345')
    sage: a^2+3*a-5
    120055
    sage: _ / 7*a
    5916750

Vectors in LiE are created using square brackets.  Notice that
the indexing in LiE is 1-based, unlike Python/Sage which is 0-based. ::

    sage: # optional - lie
    sage: v = lie('[3,2,6873,-38]')
    sage: v
    [3,2,6873,-38]
    sage: v[3]
    6873
    sage: v+v
    [6,4,13746,-76]
    sage: v*v
    47239586
    sage: v+234786
    [3,2,6873,-38,234786]
    sage: v-3
    [3,2,-38]
    sage: v^v
    [3,2,6873,-38,3,2,6873,-38]

You can also work with matrices in LiE. ::

    sage: m = lie('[[1,0,3,3],[12,4,-4,7],[-1,9,8,0],[3,-5,-2,9]]') # optional - lie
    sage: m # optional - lie
         [[ 1, 0, 3,3]
         ,[12, 4,-4,7]
         ,[-1, 9, 8,0]
         ,[ 3,-5,-2,9]
         ]
    sage: print(lie.eval('*'+m._name))  # optional - lie
         [[1,12,-1, 3]
         ,[0, 4, 9,-5]
         ,[3,-4, 8,-2]
         ,[3, 7, 0, 9]
         ]

    sage: # optional - lie
    sage: m^3
         [[ 220,   87, 81, 375]
         ,[-168,-1089, 13,1013]
         ,[1550,  357,-55,1593]
         ,[-854, -652, 98,-170]
         ]
    sage: v*m
    [-6960,62055,55061,-319]
    sage: m*v
    [20508,-27714,54999,-14089]
    sage: v*m*v
    378549605
    sage: m+v
         [[ 1, 0,   3,  3]
         ,[12, 4,  -4,  7]
         ,[-1, 9,   8,  0]
         ,[ 3,-5,  -2,  9]
         ,[ 3, 2,6873,-38]
         ]

    sage: m-2 # optional - lie
         [[ 1, 0, 3,3]
         ,[-1, 9, 8,0]
         ,[ 3,-5,-2,9]
         ]


LiE handles multivariate (Laurent) polynomials. ::

    sage: # optional - lie
    sage: lie('X[1,2]')
    1X[1,2]
    sage: -3*_
    -3X[1,2]
    sage: _ + lie('4X[-1,4]')
    4X[-1,4] - 3X[ 1,2]
    sage: _^2
    16X[-2,8] - 24X[ 0,6] +  9X[ 2,4]
    sage: lie('(4X[-1,4]-3X[1,2])*(X[2,0]-X[0,-4])')
    -4X[-1, 0] + 3X[ 1,-2] + 4X[ 1, 4] - 3X[ 3, 2]
    sage: _ - _
    0X[0,0]


You can call LiE's built-in functions using ``lie.functionname``. ::

    sage: lie.partitions(6) # optional - lie
         [[6,0,0,0,0,0]
         ,[5,1,0,0,0,0]
         ,[4,2,0,0,0,0]
         ,[4,1,1,0,0,0]
         ,[3,3,0,0,0,0]
         ,[3,2,1,0,0,0]
         ,[3,1,1,1,0,0]
         ,[2,2,2,0,0,0]
         ,[2,2,1,1,0,0]
         ,[2,1,1,1,1,0]
         ,[1,1,1,1,1,1]
         ]
    sage: lie.diagram('E8') # optional - lie
            O 2
            |
            |
    O---O---O---O---O---O---O
    1   3   4   5   6   7   8
    E8


You can define your own functions in ``LiE`` using ``lie.eval``.  Once
you have defined a function (say ``f``), you can call it using
``lie.f`` ; however, user-defined functions do not show up when using
tab-completion. ::

    sage: # optional - lie
    sage: lie.eval('f(int x) = 2*x')
    ''
    sage: lie.f(984)
    1968
    sage: lie.eval('f(int n) = a=3*n-7; if a < 0 then a = -a fi; 7^a+a^3-4*a-57')
    ''
    sage: lie.f(2)
    -53
    sage: lie.f(5)
    5765224


LiE's help can be accessed through lie.help('functionname') where
functionname is the function you want to receive help for. ::

   sage: print(lie.help('diagram'))  # optional - lie
   diagram(g).   Prints the Dynkin diagram of g, also indicating
      the type of each simple component printed, and labeling the nodes as
      done by Bourbaki (for the second and further simple components the
      labels are given an offset so as to make them disjoint from earlier
      labels). The labeling of the vertices of the Dynkin diagram prescribes
      the order of the coordinates of root- and weight vectors used in LiE.

This can also be accessed with lie.functionname? .


With the exception of groups, all LiE data types can be converted into
native Sage data types by calling the .sage() method.

Integers::

    sage: a = lie('1234') # optional - lie
    sage: b = a.sage(); b # optional - lie
    1234
    sage: type(b) # optional - lie
    <class 'sage.rings.integer.Integer'>

Vectors::

    sage: a = lie('[1,2,3]') # optional - lie
    sage: b = a.sage(); b # optional - lie
    [1, 2, 3]
    sage: type(b) # optional - lie
    <... 'list'>

Matrices::

    sage: a = lie('[[1,2],[3,4]]') # optional - lie
    sage: b = a.sage(); b # optional - lie
    [1 2]
    [3 4]
    sage: type(b) # optional - lie
    <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>

Polynomials::

    sage: a = lie('X[1,2] - 2*X[2,1]') # optional - lie
    sage: b = a.sage(); b              # optional - lie
    -2*x0^2*x1 + x0*x1^2
    sage: type(b)                      # optional - lie
    <class 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>

Text::

    sage: a = lie('"text"') # optional - lie
    sage: b = a.sage(); b # optional - lie
    'text'
    sage: type(b) # optional - lie
    <... 'str'>


LiE can be programmed using the Sage interface as well. Section 5.1.5
of the manual gives an example of a function written in LiE's language
which evaluates a polynomial at a point.  Below is a (roughly) direct
translation of that program into Python / Sage. ::

    sage: # optional - lie
    sage: def eval_pol(p, pt):
    ....:     s = 0
    ....:     for i in range(1,p.length().sage()+1):
    ....:         m = 1
    ....:         for j in range(1,pt.size().sage()+1):
    ....:             m *= pt[j]^p.expon(i)[j]
    ....:         s += p.coef(i)*m
    ....:     return s
    sage: a = lie('X[1,2]')
    sage: b1 = lie('[1,2]')
    sage: b2 = lie('[2,3]')
    sage: eval_pol(a, b1)
    4
    sage: eval_pol(a, b2)
    18

AUTHORS:

- Mike Hansen 2007-08-27
- William Stein (template)
"""

from sage.env import DOT_SAGE as DOT_SAGE, LIE_INFO_DIR as LIE_INFO_DIR
from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.interface import AsciiArtString as AsciiArtString
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.misc_c import prod as prod
from sage.misc.sage_eval import sage_eval as sage_eval

COMMANDS_CACHE: str
HELP_CACHE: str

class LiE(ExtraTabCompletion, Expect):
    """
    Interface to the LiE interpreter.

    Type ``lie.[tab]`` for a list of all the functions available
    from your LiE install.  Type ``lie.[tab]?`` for LiE's
    help about a given function.  Type ``lie(...)`` to create
    a new LiE object, and ``lie.eval(...)`` to run a string
    using LiE (and get the result back as a string).
    """
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.lie import lie
            sage: lie == loads(dumps(lie))
            True
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: LiE().__reduce__()
            (<function reduce_load_lie at 0x...>, ())
        """
    def read(self, filename) -> None:
        """
        EXAMPLES::

            sage: filename = tmp_filename()
            sage: with open(filename, 'w') as f:
            ....:     _ = f.write('x = 2\\n')
            sage: lie.read(filename)  # optional - lie
            sage: lie.get('x')        # optional - lie
            '2'
            sage: import os
            sage: os.unlink(filename)
        """
    def console(self) -> None:
        """
        Spawn a new LiE command-line session.

        EXAMPLES::

            sage: lie.console()                    # not tested
            LiE version 2.2.2 created on Sep 26 2007 at 18:13:19
            Authors: Arjeh M. Cohen, Marc van Leeuwen, Bert Lisser.
            Free source code distribution
            ...
        """
    def version(self) -> str:
        """
        EXAMPLES::

            sage: lie.version() # optional - lie
            '2...'
        """
    def help(self, command):
        """
        Return a string of the LiE help for command.

        EXAMPLES::

            sage: lie.help('diagram') # optional - lie
            'diagram(g)...'
        """
    def eval(self, code, strip: bool = True, **kwds):
        """
        EXAMPLES::

            sage: lie.eval('2+2')  # optional - lie
            '4'
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: lie.set('x', '2')  # optional - lie
            sage: lie.get('x')       # optional - lie
            '2'
        """
    def get(self, var):
        """
        Get the value of the variable var.

        EXAMPLES::

            sage: lie.set('x', '2')  # optional - lie
            sage: lie.get('x')       # optional - lie
            '2'
        """
    def get_using_file(self, var) -> None:
        """
        EXAMPLES::

            sage: lie.get_using_file('x')
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def function_call(self, function, args=None, kwds=None):
        '''
        EXAMPLES::

            sage: lie.function_call("diagram", args=[\'A4\']) # optional - lie
            O---O---O---O
            1   2   3   4
            A4
        '''

class LiEElement(ExtraTabCompletion, ExpectElement):
    def type(self):
        """
        EXAMPLES::

            sage: m = lie('[[1,0,3,3],[12,4,-4,7],[-1,9,8,0],[3,-5,-2,9]]') # optional - lie
            sage: m.type() # optional - lie
            'mat'
        """

class LiEFunctionElement(FunctionElement): ...
class LiEFunction(ExpectFunction): ...

def is_LiEElement(x) -> bool:
    """
    EXAMPLES::

        sage: from sage.interfaces.lie import is_LiEElement
        sage: is_LiEElement(2)
        doctest:...: DeprecationWarning: the function is_LiEElement is deprecated; use isinstance(x, sage.interfaces.abc.LiEElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
        sage: l = lie(2) # optional - lie
        sage: is_LiEElement(l) # optional - lie
        True
    """

lie: LiE

def reduce_load_lie():
    """
    EXAMPLES::

        sage: from sage.interfaces.lie import reduce_load_lie
        sage: reduce_load_lie()
        LiE Interpreter
    """
def lie_console() -> None:
    """
    Spawn a new LiE command-line session.

    EXAMPLES::

        sage: from sage.interfaces.lie import lie_console
        sage: lie_console()                    # not tested
        LiE version 2.2.2 created on Sep 26 2007 at 18:13:19
        Authors: Arjeh M. Cohen, Marc van Leeuwen, Bert Lisser.
        Free source code distribution
        ...
    """
def lie_version():
    """
    EXAMPLES::

        sage: from sage.interfaces.lie import lie_version
        sage: lie_version() # optional - lie
        '2...'
    """
