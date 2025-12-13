from .expect import Expect as Expect, ExpectElement as ExpectElement
from _typeshed import Incomplete
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

matlab: Incomplete

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
