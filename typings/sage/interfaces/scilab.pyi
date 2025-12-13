from .expect import Expect as Expect, ExpectElement as ExpectElement
from _typeshed import Incomplete
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

scilab: Incomplete

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
