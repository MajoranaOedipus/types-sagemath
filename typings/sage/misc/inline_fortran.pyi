from _typeshed import Incomplete
from sage.misc.temporary_file import tmp_dir as tmp_dir

class InlineFortran:
    globs: Incomplete
    library_paths: Incomplete
    libraries: Incomplete
    verbose: bool
    def __init__(self, globals=None) -> None: ...
    def __call__(self, *args, **kwds): ...
    def eval(self, x, globals=None, locals=None) -> None:
        '''
        Compile fortran code ``x`` and adds the functions in it to ``globals``.

        INPUT:

        - ``x`` -- fortran code

        - ``globals`` -- dictionary to which to add the functions from the
          fortran module

        - ``locals`` -- ignored

        EXAMPLES::

            sage: # needs numpy
            sage: code = \'\'\'
            ....: C FILE: FIB1.F
            ....:       SUBROUTINE FIB(A,N)
            ....: C
            ....: C     CALCULATE FIRST N FIBONACCI NUMBERS
            ....: C
            ....:       INTEGER N
            ....:       REAL*8 A(N)
            ....:       DO I=1,N
            ....:          IF (I.EQ.1) THEN
            ....:             A(I) = 0.0D0
            ....:          ELSEIF (I.EQ.2) THEN
            ....:             A(I) = 1.0D0
            ....:          ELSE
            ....:             A(I) = A(I-1) + A(I-2)
            ....:          ENDIF
            ....:       ENDDO
            ....:       END
            ....: C END FILE FIB1.F
            ....: \'\'\'
            sage: fortran(code, globals())
            sage: import numpy
            sage: a = numpy.array(range(10), dtype=float)
            sage: fib(a, 10)
            sage: a
            array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])

        TESTS::

            sage: os.chdir(DOT_SAGE)
            sage: fortran.eval("SYNTAX ERROR !@#$")
            Traceback (most recent call last):
            ...
            RuntimeError: failed to compile Fortran code:...
            sage: os.getcwd() == os.path.realpath(DOT_SAGE)
            True
        '''
    def add_library(self, s) -> None: ...
    def add_library_path(self, s) -> None: ...

fortran: Incomplete
