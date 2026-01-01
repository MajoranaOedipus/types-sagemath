r"""
Interface to Scilab

Scilab is a scientific software package for numerical computations
providing a powerful open computing environment for engineering and
scientific applications.  Scilab includes hundreds of mathematical
functions with the possibility to add interactively programs from
various languages (C, C++, Fortran...).  It has sophisticated data
structures (including lists, polynomials, rational functions, linear
systems...), an interpreter and a high level programming language.

The commands in this section only work if you have the "scilab"
interpreter installed and available in your PATH.  It's not necessary
to install any special Sage packages.

EXAMPLES::

    sage: # optional - scilab
    sage: scilab.eval('2+2')
    'ans  =\n \n    4.'
    sage: scilab('2+2')
    4.
    sage: a = scilab(10)
    sage: a**10
    1.000D+10

Tutorial based the MATLAB interface tutorial:

EXAMPLES::

    sage: # optional - scilab
    sage: scilab('4+10')
    14.
    sage: scilab('date')
    15-Feb-2010
    sage: scilab('5*10 + 6')
    56.
    sage: scilab('(6+6)/3')
    4.
    sage: scilab('9')^2
    81.
    sage: a = scilab(10); b = scilab(20); c = scilab(30)
    sage: avg = (a+b+c)/3
    sage: avg
    20.
    sage: parent(avg)
    Scilab

    sage: # optional - scilab
    sage: my_scalar = scilab('3.1415')
    sage: my_scalar
    3.1415
    sage: my_vector1 = scilab('[1,5,7]')
    sage: my_vector1
    1.    5.    7.
    sage: my_vector2 = scilab('[1;5;7]')
    sage: my_vector2
    1.
    5.
    7.
    sage: my_vector1 * my_vector2
    75.

    sage: # optional - scilab
    sage: row_vector1 = scilab('[1 2 3]')
    sage: row_vector2 = scilab('[3 2 1]')
    sage: matrix_from_row_vec = scilab('[%s; %s]'%(row_vector1.name(), row_vector2.name()))
    sage: matrix_from_row_vec
    1.    2.    3.
    3.    2.    1.

    sage: # optional - scilab
    sage: column_vector1 = scilab('[1;3]')
    sage: column_vector2 = scilab('[2;8]')
    sage: matrix_from_col_vec = scilab('[%s %s]'%(column_vector1.name(), column_vector2.name()))
    sage: matrix_from_col_vec
    1.    2.
    3.    8.

    sage: my_matrix = scilab('[8, 12, 19; 7, 3, 2; 12, 4, 23; 8, 1, 1]')    # optional - scilab
    sage: my_matrix                                      # optional - scilab
        8.     12.    19.
        7.     3.     2.
        12.    4.     23.
        8.     1.     1.

    sage: combined_matrix = scilab('[%s, %s]'%(my_matrix.name(), my_matrix.name()))                                        # optional - scilab
    sage: combined_matrix                               # optional - scilab
    8.     12.    19.    8.     12.    19.
    7.     3.     2.     7.     3.     2.
    12.    4.     23.    12.    4.     23.
    8.     1.     1.     8.     1.     1.

    sage: tm = scilab('0.5:2:10')                       # optional - scilab
    sage: tm                                            # optional - scilab
    0.5    2.5    4.5    6.5    8.5

    sage: # optional - scilab
    sage: my_vector1 = scilab('[1,5,7]')
    sage: my_vector1(1)
    1.
    sage: my_vector1(2)
    5.
    sage: my_vector1(3)
    7.

Matrix indexing works as follows::

    sage: my_matrix = scilab('[8, 12, 19; 7, 3, 2; 12, 4, 23; 8, 1, 1]')     # optional - scilab
    sage: my_matrix(3,2)                                # optional - scilab
    4.

One can also use square brackets::

    sage: my_matrix[3,2]                                # optional - scilab
    4.


Setting using parenthesis cannot work (because of how the Python
language works).  Use square brackets or the set function::

    sage: # optional - scilab
    sage: my_matrix = scilab('[8, 12, 19; 7, 3, 2; 12, 4, 23; 8, 1, 1]')
    sage: my_matrix.set(2,3, 1999)
    sage: my_matrix
           8.         12.         19.
           7.          3.       1999.
          12.          4.         23.
           8.          1.          1.
    sage: my_matrix[2,3] = -126
    sage: my_matrix
           8.         12.         19.
           7.          3.      - 126.
          12.          4.         23.
           8.          1.          1.

TESTS::

    sage: # optional - scilab
    sage: M = scilab(x)
    Traceback (most recent call last):
    ...
    TypeError: ..._interface_init_() takes exactly one argument (0 given)
    sage: M = scilab(matrix(3,range(9))); M
        0.    1.    2.
        3.    4.    5.
        6.    7.    8.
    sage: M(10)
    Traceback (most recent call last):
    ...
    TypeError: Error executing code in Scilab
    ...
    Invalid index.
    sage: M[10]
    Traceback (most recent call last):
    ...
    TypeError: Error executing code in Scilab
    ...
    Invalid index.
    sage: M(4,2)
    Traceback (most recent call last):
    ...
    TypeError: Error executing code in Scilab
    ...
    Invalid index.
    sage: M[2,4]
    Traceback (most recent call last):
    ...
    TypeError: Error executing code in Scilab
    ...
    Invalid index.
    sage: M(9) = x
    Traceback (most recent call last):
    ...
    SyntaxError: can...t assign to function call (..., line 1)

AUTHORS:

- Ronan Paixao (2008-11-26), based on the MATLAB tutorial by
  William Stein (2006-10-11)
"""
from .expect import Expect as Expect, ExpectElement as ExpectElement
from sage.misc.instancedoc import instancedoc as instancedoc

class Scilab(Expect):
    """
    Interface to the Scilab interpreter.

    EXAMPLES::

        sage: # optional - scilab
        sage: a = scilab('[ 1, 1, 2; 3, 5, 8; 13, 21, 33 ]')
        sage: b = scilab('[ 1; 3; 13]')
        sage: c = a * b
        sage: print(c)
          30.
          122.
          505.
    """
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, seed=None) -> None:
        """
        Initialize the Scilab class.

        EXAMPLES::

            sage: from sage.interfaces.scilab import Scilab
            sage: sci_obj = Scilab()
            sage: del sci_obj
        """
    def set_seed(self, seed=None):
        """
        Set the seed for gp interpreter.

        The seed should be an integer.

        EXAMPLES::

            sage: # optional - scilab
            sage: from sage.interfaces.scilab import Scilab
            sage: s = Scilab()
            sage: s.set_seed(1)
            1
            sage: [s.rand() for i in range(5)]
            [
            <BLANKLINE>
                 0.6040239,
            <BLANKLINE>
                 0.0079647,
            <BLANKLINE>
                 0.6643966,
            <BLANKLINE>
                 0.9832111,
            <BLANKLINE>
                 0.5321420]
        """
    def eval(self, command, *args, **kwds):
        '''
        Evaluates commands.

        EXAMPLES::

            sage: scilab.eval("5")                      # optional - scilab
            \'ans  =
 
    5.\'
            sage: scilab.eval("d=44")                   # optional - scilab
            \'d  =
 
    44.\'
        '''
    def whos(self, name=None, typ=None):
        '''
        Return information about current objects.
        Arguments:
        nam: first characters of selected names
        typ: name of selected Scilab variable type

        EXAMPLES::

            sage: scilab.whos("core")                   # optional - scilab
            \'Name                     Type           Size           Bytes...\'
            sage: scilab.whos(typ=\'function\')           # optional - scilab
            \'Name                     Type           Size           Bytes...\'
        '''
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: scilab.set('a', 123)        # optional - scilab
            sage: scilab.get('a')               # optional - scilab
            '
 
    123.'
        """
    def get(self, var):
        """
        Get the value of the variable ``var``.

        EXAMPLES::

            sage: scilab.eval('b=124;')                 # optional - scilab
            ''
            sage: scilab.get('b')                       # optional - scilab
            '
 
    124.'
        """
    def console(self) -> None:
        """
        Starts Scilab console.

        EXAMPLES::

            sage: scilab.console()          # optional - scilab; not tested
        """
    def version(self):
        """
        Return the version of the Scilab software used.

        EXAMPLES::

            sage: scilab.version()                      # optional - scilab
            'scilab-...'
        """
    def sage2scilab_matrix_string(self, A):
        """
        Return a Scilab matrix from a Sage matrix.

        INPUT:

        - ``A`` -- Sage matrix with entries in the rationals or reals

        OUTPUT: string that evaluates to a Scilab matrix

        EXAMPLES::

            sage: M33 = MatrixSpace(QQ,3,3)             # optional - scilab
            sage: A = M33([1,2,3,4,5,6,7,8,0])          # optional - scilab
            sage: scilab.sage2scilab_matrix_string(A)   # optional - scilab
            '[1, 2, 3; 4, 5, 6; 7, 8, 0]'
        """

class ScilabElement(ExpectElement):
    def __getitem__(self, n):
        """
        Use parenthesis for Scilab matrices instead.

        EXAMPLES::

            sage: # optional - scilab
            sage: M = scilab('[1,2,3;4,5,6;7,8,9]')
            sage: M[1]
            1.
            sage: M[7]
            3.
            sage: M[3,2]
            8.
        """
    def __setitem__(self, n, value) -> None:
        """
        Set an element of a matrix.

        EXAMPLES::

            sage: # optional - scilab
            sage: M = scilab('[1,2,3;4,5,6;7,8,9]')
            sage: M[6] = 0
            sage: M
            1.    2.    3.
            4.    5.    6.
            7.    0.    9.
            sage: M[3,2] = 10
            sage: M
            1.    2.    3.
            4.    5.    6.
            7.    10.    9.
        """
    def set(self, i, j, x) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: scilab.set('c', 125)          # optional - scilab
            sage: scilab.get('c')               # optional - scilab
            '
 
    125.'
        """

scilab: Scilab

def scilab_console() -> None:
    """
    This requires that the optional Scilab program be installed and in
    your PATH, but no optional Sage packages need to be installed.

    EXAMPLES::

        sage: from sage.interfaces.scilab import scilab_console  # optional - scilab
        sage: scilab_console()                               # optional - scilab; not tested
                ___________________________________________
                               scilab-5.0.3

                         Consortium Scilab (DIGITEO)
                       Copyright (c) 1989-2008 (INRIA)
                       Copyright (c) 1989-2007 (ENPC)
                ___________________________________________


        Startup execution:
          loading initial environment

        -->2+3
        ans  =

           5.

        -->quit

    Typing quit exits the Scilab console and returns you to Sage.
    Scilab, like Sage, remembers its history from one session to
    another.
    """
def scilab_version():
    """
    Return the version of Scilab installed.

    EXAMPLES::

        sage: from sage.interfaces.scilab import scilab_version  # optional - scilab
        sage: scilab_version()    # optional - scilab
        'scilab-...'
    """
