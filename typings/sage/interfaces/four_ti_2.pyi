r"""
Interface to 4ti2

https://4ti2.github.io/

You must have the 4ti2 Sage package installed on your computer
for this interface to work.

Use ``sage -i 4ti2`` to install the package.

AUTHORS:

- Mike Hansen (2009): Initial version.

- Bjarke Hammersholt Roune (2009-06-26): Added Groebner, made code
  usable as part of the Sage library and added documentation and some
  doctests.

- Marshall Hampton (2011): Minor fixes to documentation.
"""
from sage.features.four_ti_2 import FourTi2Executable as FourTi2Executable
from sage.rings.integer_ring import ZZ as ZZ

class FourTi2:
    """
    An interface to the program 4ti2.

    Each 4ti2 command is exposed as a method of this class.
    """
    def __init__(self, directory=None) -> None:
        '''
        Initialize this object.

        INPUT:

        - ``directory`` -- 4ti2 only deals with files, and this is the
          directory that Sage will write input files to and run 4ti2
          in. Use an appropriate temporary directory if the value is
          ``None``.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import FourTi2
            sage: f = FourTi2("/tmp/")
            sage: f.directory()
            \'/tmp/\'
        '''
    def directory(self):
        '''
        Return the directory where the input files for 4ti2 are
        written by Sage and where 4ti2 is run.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import FourTi2
            sage: f = FourTi2("/tmp/")
            sage: f.directory()
            \'/tmp/\'
        '''
    def temp_project(self):
        """
        Return an input project file name that has not been used yet.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.temp_project()
            'project_...'
        """
    def write_matrix(self, mat, filename) -> None:
        '''
        Write the matrix ``mat`` to the file ``filename`` in 4ti2 format.

        INPUT:

        - ``mat`` -- a matrix of integers or something that can be
          converted to that
        - ``filename`` -- a file name not including a path

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.write_matrix([[1,2],[3,4]], "test_file")
        '''
    def write_single_row(self, row, filename) -> None:
        '''
        Write the list ``row`` to the file ``filename`` in 4ti2 format
        as a matrix with one row.

        INPUT:

        - ``row`` -- list of integers
        - ``filename`` -- a file name not including a path

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.write_single_row([1,2,3,4], "test_file")
        '''
    def write_array(self, array, nrows, ncols, filename) -> None:
        '''
        Write the integer matrix ``array`` to the file ``filename``
        in directory ``directory()`` in 4ti2 format.

        The matrix must have ``nrows`` rows and ``ncols`` columns.
        It can be provided as a list of lists.

        INPUT:

        - ``array`` -- a matrix of integers. Can be represented as a list
          of lists
        - ``nrows`` -- the number of rows in ``array``
        - ``ncols`` -- the number of columns in ``array``
        - ``file`` -- a file name not including a path

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.write_array([[1,2,3],[3,4,5]], 2, 3, "test_file")
        '''
    def read_matrix(self, filename):
        '''
        Read a matrix in 4ti2 format from the file ``filename`` in
        directory ``directory()``.

        INPUT:

        - ``filename`` -- the name of the file to read from

        OUTPUT: the data from the file as a matrix over `\\ZZ`

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.write_matrix([[1,2,3],[3,4,6]], "test_file")
            sage: four_ti_2.read_matrix("test_file")
            [1 2 3]
            [3 4 6]
        '''
    def call(self, command, project, verbose: bool = True, *, options=()) -> None:
        '''
        Run the 4ti2 program ``command`` on the project named
        ``project`` in the directory ``directory()``.

        INPUT:

        - ``command`` -- the 4ti2 program to run
        - ``project`` -- the file name of the project to run on
        - ``verbose`` -- display the output of 4ti2 if ``True``
        - ``options`` -- list of strings to pass to the program

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.write_matrix([[6,10,15]], "test_file")
            sage: four_ti_2.call("groebner", "test_file", False)  # optional - 4ti2
            sage: four_ti_2.read_matrix("test_file.gro")  # optional - 4ti2
            [-5  0  2]
            [-5  3  0]
        '''
    def zsolve(self, mat=None, rel=None, rhs=None, sign=None, lat=None, project=None):
        """
        Run the 4ti2 program ``zsolve`` on the parameters.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: A = [[1,1,1],[1,2,3]]
            sage: rel = ['<', '<']
            sage: rhs = [2, 3]
            sage: sign = [1,0,1]
            sage: four_ti_2.zsolve(A, rel, rhs, sign)  # optional - 4ti2
            [
                     [ 1 -1  0]
                     [ 0 -1  0]
            [0 0 1]  [ 0 -3  2]
            [1 1 0]  [ 1 -2  1]
            [0 1 0], [ 0 -2  1], []
            ]
            sage: four_ti_2.zsolve(lat=[[1,2,3],[1,1,1]])  # optional - 4ti2
            [
                         [1 2 3]
            [0 0 0], [], [1 1 1]
            ]
        """
    def qsolve(self, mat=None, rel=None, sign=None, project=None):
        """
        Run the 4ti2 program ``qsolve`` on the parameters.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: A = [[1,1,1],[1,2,3]]
            sage: four_ti_2.qsolve(A)  # optional - 4ti2
            [[], [ 1 -2  1]]
        """
    def rays(self, mat=None, project=None):
        """
        Run the 4ti2 program ``rays`` on the parameters.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.rays(four_ti_2._magic3x3())  # optional - 4ti2
            [0 2 1 2 1 0 1 0 2]
            [1 0 2 2 1 0 0 2 1]
            [1 2 0 0 1 2 2 0 1]
            [2 0 1 0 1 2 1 2 0]
        """
    def hilbert(self, mat=None, lat=None, project=None):
        """
        Run the 4ti2 program ``hilbert`` on the parameters.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.hilbert(four_ti_2._magic3x3())  # optional - 4ti2
            [2 0 1 0 1 2 1 2 0]
            [1 0 2 2 1 0 0 2 1]
            [0 2 1 2 1 0 1 0 2]
            [1 2 0 0 1 2 2 0 1]
            [1 1 1 1 1 1 1 1 1]
            sage: four_ti_2.hilbert(lat=[[1,2,3],[1,1,1]])  # optional - 4ti2
            [2 1 0]
            [0 1 2]
            [1 1 1]
        """
    def graver(self, mat=None, lat=None, project=None):
        """
        Run the 4ti2 program ``graver`` on the parameters.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.graver([1,2,3])  # optional - 4ti2
            [ 2 -1  0]
            [ 3  0 -1]
            [ 1  1 -1]
            [ 1 -2  1]
            [ 0  3 -2]
            sage: four_ti_2.graver(lat=[[1,2,3],[1,1,1]])  # optional - 4ti2
            [ 1  0 -1]
            [ 0  1  2]
            [ 1  1  1]
            [ 2  1  0]
        """
    def ppi(self, n):
        """
        Run the 4ti2 program ``ppi`` on the parameters.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.ppi(3)  # optional - 4ti2
            [-2  1  0]
            [ 0 -3  2]
            [-1 -1  1]
            [-3  0  1]
            [ 1 -2  1]
        """
    def circuits(self, mat=None, project=None):
        """
        Run the 4ti2 program ``circuits`` on the parameters.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.circuits([1,2,3])  # optional - 4ti2
            [ 0  3 -2]
            [ 2 -1  0]
            [ 3  0 -1]
        """
    def minimize(self, mat=None, lat=None) -> None:
        """
        Run the 4ti2 program ``minimize`` on the parameters.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: four_ti_2.minimize()  # optional - 4ti2
            Traceback (most recent call last):
            ...
            NotImplementedError: 4ti2 command 'minimize' not implemented in Sage.
        """
    def groebner(self, mat=None, lat=None, project=None):
        """
        Run the 4ti2 program ``groebner`` on the parameters.

        This computes a toric Groebner basis of a matrix.

        See `4ti2 website <https://4ti2.github.io/>`_ for details.

        EXAMPLES::

            sage: from sage.interfaces.four_ti_2 import four_ti_2
            sage: A = [6,10,15]
            sage: four_ti_2.groebner(A)  # optional - 4ti2
            [-5  0  2]
            [-5  3  0]
            sage: four_ti_2.groebner(lat=[[1,2,3],[1,1,1]])  # optional - 4ti2
            [-1  0  1]
            [ 2  1  0]
        """

four_ti_2: FourTi2
