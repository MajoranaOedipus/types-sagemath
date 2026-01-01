r"""
Interface to MATLAB

According to their website, MATLAB is "a high-level language and
interactive environment that enables you to perform computationally
intensive tasks faster than with traditional programming languages
such as C, C++, and Fortran."

The commands in this section only work if you have the "matlab"
interpreter installed and available in your PATH. It's not
necessary to install any special Sage packages.

EXAMPLES::

    sage: matlab.eval('2+2')                 # optional - matlab
    '\nans =\n\n     4\n'

::

    sage: a = matlab(10)                     # optional - matlab
    sage: a**10                              # optional - matlab
       1.0000e+10

AUTHORS:

- William Stein (2006-10-11)

Tutorial
--------

EXAMPLES::

    sage: # optional - matlab
    sage: matlab('4+10')
    14
    sage: matlab('date')
    18-Oct-2006
    sage: matlab('5*10 + 6')
    56
    sage: matlab('(6+6)/3')
    4
    sage: matlab('9')^2
    81
    sage: a = matlab(10); b = matlab(20); c = matlab(30)
    sage: avg = (a+b+c)/3 ; avg
    20
    sage: parent(avg)
    Matlab

::

    sage: # optional - matlab
    sage: my_scalar = matlab('3.1415')
    sage: my_scalar
    3.1415
    sage: my_vector1 = matlab('[1,5,7]')
    sage: my_vector1
    1     5     7
    sage: my_vector2 = matlab('[1;5;7]')
    sage: my_vector2
    1
    5
    7
    sage: my_vector1 * my_vector2
    75

::

    sage: # optional - matlab
    sage: row_vector1 = matlab('[1 2 3]')
    sage: row_vector2 = matlab('[3 2 1]')
    sage: matrix_from_row_vec = matlab('[%s; %s]'%(row_vector1.name(), row_vector2.name()))
    sage: matrix_from_row_vec
    1     2     3
    3     2     1

::

    sage: # optional - matlab
    sage: column_vector1 = matlab('[1;3]')
    sage: column_vector2 = matlab('[2;8]')
    sage: matrix_from_col_vec = matlab('[%s %s]'%(column_vector1.name(), column_vector2.name()))
    sage: matrix_from_col_vec
    1     2
    3     8

::

    sage: my_matrix = matlab('[8, 12, 19; 7, 3, 2; 12, 4, 23; 8, 1, 1]')    # optional - matlab
    sage: my_matrix                                      # optional - matlab
         8    12    19
         7     3     2
        12     4    23
         8     1     1

::

    sage: combined_matrix = matlab('[%s, %s]'%(my_matrix.name(), my_matrix.name()))                                        # optional - matlab
    sage: combined_matrix                               # optional - matlab
     8    12    19     8    12    19
     7     3     2     7     3     2
    12     4    23    12     4    23
     8     1     1     8     1     1

::

    sage: tm = matlab('0.5:2:10')                       # optional - matlab
    sage: tm                                            # optional - matlab
    0.5000    2.5000    4.5000    6.5000    8.5000

::

    sage: # optional - matlab
    sage: my_vector1 = matlab('[1,5,7]')
    sage: my_vector1(1)
    1
    sage: my_vector1(2)
    5
    sage: my_vector1(3)
    7

Matrix indexing works as follows::

    sage: my_matrix = matlab('[8, 12, 19; 7, 3, 2; 12, 4, 23; 8, 1, 1]')     # optional - matlab
    sage: my_matrix(3,2)                                # optional - matlab
    4

Setting using parenthesis cannot work (because of how the Python
language works). Use square brackets or the set function::

    sage: my_matrix = matlab('[8, 12, 19; 7, 3, 2; 12, 4, 23; 8, 1, 1]')    # optional - matlab
    sage: my_matrix.set(2,3, 1999)                          # optional - matlab
    sage: my_matrix                                         # optional - matlab
               8          12          19
               7           3        1999
              12           4          23
               8           1           1
"""
from .expect import Expect as Expect, ExpectElement as ExpectElement
from sage.misc.instancedoc import instancedoc as instancedoc

class Matlab(Expect):
    """
    Interface to the Matlab interpreter.

    EXAMPLES::

        sage: # optional - matlab
        sage: a = matlab('[ 1, 1, 2; 3, 5, 8; 13, 21, 33 ]')
        sage: b = matlab('[ 1; 3; 13]')
        sage: c = a * b
        sage: print(c)
            30
           122
           505
    """
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None) -> None: ...
    def __reduce__(self): ...
    def whos(self): ...
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.
        """
    def get(self, var):
        """
        Get the value of the variable var.

        EXAMPLES::

            sage: s = matlab.eval('a = 2') # optional - matlab
            sage: matlab.get('a')               # optional - matlab
            '     2'
        """
    def strip_answer(self, s):
        """
        Return the string s with Matlab's answer prompt removed.

        EXAMPLES::

            sage: s = '\\nans =\\n\\n     2\\n'
            sage: matlab.strip_answer(s)
            '     2'
        """
    def console(self) -> None: ...
    def version(self): ...
    def chdir(self, directory) -> None:
        """
        Change MATLAB's current working directory.

        EXAMPLES::

            sage: matlab.chdir('/')          # optional - matlab
            sage: matlab.pwd()               # optional - matlab
            /
        """
    def sage2matlab_matrix_string(self, A):
        """
        Return a matlab matrix from a Sage matrix.

        INPUT:

        - ``A`` -- Sage matrix with entries in the rationals or reals

        OUTPUT: string that evaluates to a Matlab matrix

        EXAMPLES::

            sage: M33 = MatrixSpace(QQ,3,3)
            sage: A = M33([1,2,3,4,5,6,7,8,0])
            sage: matlab.sage2matlab_matrix_string(A)   # optional - matlab
            '[1, 2, 3; 4, 5, 6; 7, 8, 0]'

        AUTHOR:

        - David Joyner and William Stein
        """

class MatlabElement(ExpectElement):
    def __getitem__(self, n) -> None: ...
    def set(self, i, j, x) -> None: ...

matlab: Matlab

def reduce_load_Matlab(): ...
def matlab_console() -> None:
    """
    This requires that the optional matlab program be installed and in
    your PATH, but no optional Sage packages need be installed.

    EXAMPLES::

        sage: matlab_console()                # optional - matlab; not tested
                                       < M A T L A B >
                           Copyright 1984-2006 The MathWorks, Inc.
        ...
        >> 2+3

    ans =

    5

    quit

    Typing quit exits the matlab console and returns you to Sage.
    matlab, like Sage, remembers its history from one session to
    another.
    """
def matlab_version():
    """
    Return the version of Matlab installed.

    EXAMPLES::

        sage: matlab_version()    # random; optional - matlab
        '7.2.0.283 (R2006a)'
    """
