from IPython.core.magic import Magics, cell_magic, line_magic
from _typeshed import Incomplete
from sage.env import SAGE_IMPORTALL as SAGE_IMPORTALL, SAGE_STARTUP_FILE as SAGE_STARTUP_FILE
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.misc.misc import run_once as run_once
from sage.repl.load import load_wrap as load_wrap

class SageMagics(Magics):
    @line_magic
    def crun(self, s) -> None:
        """
        Profile C function calls.

        INPUT:

        - ``s`` -- string; Sage command to profile

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell('%crun sum(1/(1+n^2) for n in range(100))')   # optional - gperftools
            PROFILE: interrupts/evictions/bytes = ...
            Using local file ...
            Using local file ...
            sage: shell.quit()
        """
    @line_magic
    def runfile(self, s):
        """
        Execute the code contained in the file ``s``.

        This is designed to be used from the command line as
        ``%runfile /path/to/file``.

        - ``s`` -- string; the file to be loaded

        .. SEEALSO::

            This is the same as :func:`~sage.repl.load.load`.

        EXAMPLES::

            sage: import os
            sage: from sage.repl.interpreter import get_test_shell
            sage: from sage.misc.temporary_file import tmp_dir
            sage: shell = get_test_shell()
            sage: tmp = os.path.join(tmp_dir(), 'run_cell.py')
            sage: with open(tmp, 'w') as f:
            ....:     _ = f.write('a = 2\\n')
            sage: shell.run_cell('%runfile '+tmp)
            sage: shell.run_cell('a')
            2
            sage: shell.quit()
        """
    @line_magic
    def attach(self, s):
        """
        Attach the code contained in the file ``s``.

        This is designed to be used from the command line as ``%attach
        /path/to/file``.

        - ``s`` -- string. The file to be attached

        .. SEEALSO::

            This is the same as :func:`~sage.repl.attach.attach`.

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: from tempfile import NamedTemporaryFile as NTF
            sage: with NTF(mode='w+t', suffix='.py', delete=False) as f:
            ....:     _ = f.write('a = 2\\n')
            sage: shell.run_cell('%attach ' + f.name)
            sage: shell.run_cell('a')
            2
            sage: sleep(1)  # filesystem timestamp granularity
            sage: with open(f.name, 'w') as f: _ = f.write('a = 3\\n')

        Note that the doctests are never really at the command prompt, so
        we call the input hook manually::

            sage: shell.run_cell('from sage.repl.attach import reload_attached_files_if_modified')
            sage: shell.run_cell('reload_attached_files_if_modified()')
            ### reloading attached file ... modified at ... ###

            sage: shell.run_cell('a')
            3
            sage: shell.run_cell('detach(%r)' % f.name)
            sage: shell.run_cell('attached_files()')
            []
            sage: os.remove(f.name)
            sage: shell.quit()
        """
    @line_magic
    def iload(self, args) -> None:
        '''
        A magic command to interactively load a file as in MAGMA.

        - ``args`` -- string. The file to be interactively loaded

        .. NOTE::

            Currently, this cannot be completely doctested as it
            relies on :func:`raw_input`.

        EXAMPLES::

            sage: ip = get_ipython()           # not tested: works only in interactive shell
            sage: ip.magic_iload(\'/dev/null\')  # not tested: works only in interactive shell
            Interactively loading "/dev/null"  # not tested: works only in interactive shell
        '''
    @line_magic
    def display(self, args) -> None:
        '''
        A magic command to switch between simple display and ASCII art display.

        - ``args`` -- string.  See
          :mod:`sage.repl.rich_output.preferences`
          for allowed values. If the mode is ``ascii_art``, it can
          optionally be followed by a width.

        How to use: if you want to activate the ASCII art mode::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell(\'%display ascii_art\')

        That means you do not have to use :func:`ascii_art` to get an ASCII art
        output::

            sage: shell.run_cell("i = var(\'i\')")                                        # needs sage.symbolic
            sage: shell.run_cell(\'sum(i^2*x^i, i, 0, 10)\')                              # needs sage.symbolic
                 10       9       8       7       6       5       4      3      2
            100*x   + 81*x  + 64*x  + 49*x  + 36*x  + 25*x  + 16*x  + 9*x  + 4*x  + x

        Then when you want to return to \'textual mode\'::

            sage: shell.run_cell(\'%display text plain\')
            sage: shell.run_cell(\'%display plain\')        # shortcut for "text plain"
            sage: shell.run_cell(\'sum(i^2*x^i, i, 0, 10)\')                              # needs sage.symbolic
            100*x^10 + 81*x^9 + 64*x^8 + 49*x^7 + 36*x^6 + 25*x^5 + 16*x^4 + 9*x^3 + 4*x^2 + x

        Sometime you could have to use a special output width and you
        could specify it::

            sage: shell.run_cell(\'%display ascii_art\')
            sage: shell.run_cell(\'StandardTableaux(4).list()\')                          # needs sage.combinat
            [
            [                                                                  1  4    1  3
            [                 1  3  4    1  2  4    1  2  3    1  3    1  2    2       2
            [   1  2  3  4,   2      ,   3      ,   4      ,   2  4,   3  4,   3   ,   4   ,
            <BLANKLINE>
                       1 ]
               1  2    2 ]
               3       3 ]
               4   ,   4 ]
            sage: shell.run_cell(\'%display ascii_art 50\')
            sage: shell.run_cell(\'StandardTableaux(4).list()\')                          # needs sage.combinat
            [
            [
            [                 1  3  4    1  2  4    1  2  3
            [   1  2  3  4,   2      ,   3      ,   4      ,
            <BLANKLINE>
                                                      1 ]
                              1  4    1  3    1  2    2 ]
              1  3    1  2    2       2       3       3 ]
              2  4,   3  4,   3   ,   4   ,   4   ,   4 ]

        As yet another option, typeset mode. This is used in the emacs
        interface::

            sage: shell.run_cell(\'%display text latex\')
            sage: shell.run_cell(\'1/2\')
            1/2

        Switch back::

            sage: shell.run_cell(\'%display default\')

        Switch graphics to default to vector or raster graphics file
        formats::

            sage: shell.run_cell(\'%display graphics vector\')

        TESTS::

            sage: shell.run_cell(\'%display invalid_mode\')
            value must be unset (None) or one of (\'plain\', \'ascii_art\', \'unicode_art\', \'latex\'), got invalid_mode
            sage: shell.quit()
        '''
    @cell_magic
    def cython(self, line, cell):
        """
        Cython cell magic.

        This is syntactic sugar on the
        :func:`~sage.misc.cython.cython_compile` function.

        Note that there is also the ``%%cython`` cell magic provided by Cython,
        which can be loaded with ``%load_ext cython``, see
        `Cython documentation <https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compiling-with-a-jupyter-notebook>`_
        for more details.
        The semantic is slightly different from the version provided by Sage.

        INPUT:

        - ``line`` -- parsed as keyword arguments. The allowed arguments are:

          - ``--verbose N`` / ``-v N``
          - ``--compile-message``
          - ``--use-cache``
          - ``--create-local-c-file``
          - ``--annotate``
          - ``--view-annotate``
          - ``--sage-namespace``
          - ``--create-local-so-file``
          - ``--no-compile-message``, ``--no-use-cache``, etc.

          See :func:`~sage.misc.cython.cython` for details.

          If ``--view-annotate`` is given, the annotation is either displayed
          inline in the Sage notebook or opened in a new web browser, depending
          on whether the Sage notebook is used.

          You can override the selection by specifying
          ``--view-annotate=webbrowser`` or ``--view-annotate=displayhtml``.

        - ``cell`` -- string; the Cython source code to process

        OUTPUT: none; the Cython code is compiled and loaded

        EXAMPLES::

            sage: # needs sage.misc.cython
            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell(
            ....: '''
            ....: %%cython -v1 --annotate --no-sage-namespace
            ....: def f():
            ....:     print('test')
            ....: ''')
            Compiling ....pyx because it changed.
            [1/1] Cythonizing ....pyx
            sage: f()
            test

        TESTS:

        Test unrecognized arguments::

            sage: # needs sage.misc.cython
            sage: shell.run_cell('''
            ....: %%cython --some-unrecognized-argument
            ....: print(1)
            ....: ''')
            UsageError: unrecognized arguments: --some-unrecognized-argument

        Test ``--help`` is disabled::

            sage: # needs sage.misc.cython
            sage: shell.run_cell('''
            ....: %%cython --help
            ....: print(1)
            ....: ''')
            UsageError: unrecognized arguments: --help

        Test ``--view-annotate`` invalid arguments::

            sage: # needs sage.misc.cython
            sage: shell.run_cell('''
            ....: %%cython --view-annotate=xx
            ....: print(1)
            ....: ''')  # exact error message differ between Python 3.11/3.13
            UsageError: argument --view-annotate: invalid choice: 'xx' (choose from ...)

        Test ``--view-annotate=displayhtml`` (note that in a notebook environment
        an inline HTML frame will be displayed)::

            sage: # needs sage.misc.cython
            sage: shell.run_cell('''
            ....: %%cython --view-annotate=displayhtml
            ....: print(1)
            ....: ''')
            1
            <IPython.core.display.HTML object>

        Test ``--view-annotate=webbrowser``::

            sage: # needs sage.misc.cython webbrowser
            sage: shell.run_cell('''
            ....: %%cython --view-annotate
            ....: print(1)
            ....: ''')
            1
            sage: shell.run_cell('''
            ....: %%cython --view-annotate=auto
            ....: print(1)
            ....: ''')  # --view-annotate=auto is undocumented feature, equivalent to --view-annotate
            1
            sage: shell.run_cell('''
            ....: %%cython --view-annotate=webbrowser
            ....: print(1)
            ....: ''')
            1

        Test invalid quotes::

            sage: # needs sage.misc.cython
            sage: shell.run_cell('''
            ....: %%cython --a='
            ....: print(1)
            ....: ''')
            ...
            ValueError...Traceback (most recent call last)
            ...
            ValueError: No closing quotation
        """
    @cell_magic
    def fortran(self, line, cell):
        """
        Fortran cell magic.

        This is syntactic sugar on the
        :func:`~sage.misc.inline_fortran.fortran` function.

        INPUT:

        - ``line`` -- ignored

        - ``cell`` -- string; the Cython source code to process

        OUTPUT: none; the Fortran code is compiled and loaded

        EXAMPLES::

            sage: # needs numpy
            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell('''
            ....: %%fortran
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
            ....: ''')
            sage: fib
            <fortran ...>
            sage: from numpy import array
            sage: a = array(range(10), dtype=float)
            sage: fib(a, 10)
            sage: a
            array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])
        """

class SageCustomizations:
    shell: Incomplete
    auto_magics: Incomplete
    def __init__(self, shell=None) -> None:
        """
        Initialize the Sage plugin.
        """
    def register_interface_magics(self) -> None:
        """
        Register magics for each of the Sage interfaces
        """
    @staticmethod
    def all_globals():
        """
        Return a Python module containing all globals which should be
        made available to the user.

        EXAMPLES::

            sage: from sage.repl.ipython_extension import SageCustomizations
            sage: SageCustomizations.all_globals()
            <module 'sage.all_cmdline' ...>
        """
    def init_environment(self) -> None:
        """
        Set up Sage command-line environment
        """
    def run_init(self) -> None:
        """
        Run Sage's initial startup file.
        """
    def init_inspector(self) -> None: ...
    def init_line_transforms(self) -> None:
        """
        Set up transforms (like the preparser).

        TESTS:

        Check that :issue:`31951` is fixed::

             sage: # indirect doctest
             sage: from IPython import get_ipython
             sage: ip = get_ipython()
             sage: ip.input_transformer_manager.check_complete('''
             ....: for i in [1 .. 2]:
             ....:     a = 2''')
             ('incomplete', 4)
             sage: ip.input_transformer_manager.check_complete('''
             ....: def foo(L)
             ....:     K.<a> = L''')
             ('invalid', None)
             sage: ip.input_transformer_manager.check_complete('''
             ....: def foo(L):
             ....:     K.<a> = L''')
             ('incomplete', 4)
             sage: ip.input_transformer_manager.check_complete('''
             ....: def foo(L):
             ....:     K.<a> = L''')
             ('incomplete', 4)
             sage: ip.input_transformer_manager.check_complete('''
             ....: def foo(R):
             ....:     a = R.0''')
             ('incomplete', 4)
             sage: ip.input_transformer_manager.check_complete('''
             ....: def foo(a):
             ....:     b = 2a''')
             ('invalid', None)
             sage: implicit_multiplication(True)
             sage: ip.input_transformer_manager.check_complete('''
             ....: def foo(a):
             ....:     b = 2a''')
             ('incomplete', 4)
             sage: ip.input_transformer_manager.check_complete('''
             ....: def foo():
             ....:     f(x) = x^2''')
             ('incomplete', 4)
             sage: ip.input_transformer_manager.check_complete('''
             ....: def foo():
             ....:     2.factor()''')
             ('incomplete', 4)
        """

class SageJupyterCustomizations(SageCustomizations):
    @staticmethod
    def all_globals():
        """
        Return a Python module containing all globals which should be
        made available to the user when running the Jupyter notebook.

        EXAMPLES::

            sage: from sage.repl.ipython_extension import SageJupyterCustomizations
            sage: SageJupyterCustomizations.all_globals()
            <module 'sage.repl.ipython_kernel.all_jupyter' ...>
        """

@run_once
def load_ipython_extension(ip) -> None:
    """
    Load the extension in IPython.
    """
