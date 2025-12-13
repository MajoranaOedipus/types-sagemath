from IPython.core.interactiveshell import InteractiveShell
from IPython.core.prefilter import PrefilterTransformer
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.terminal.ipapp import IPAppCrashHandler, TerminalIPythonApp
from _typeshed import Incomplete
from sage.repl.configuration import SAGE_EXTENSION as SAGE_EXTENSION, sage_ipython_config as sage_ipython_config
from sage.repl.preparse import containing_block as containing_block, preparse as preparse
from sage.repl.prompts import InterfacePrompts as InterfacePrompts

def preparser(on: bool = True) -> None:
    """
    Turn on or off the Sage preparser.

    - ``on`` -- boolean; whether to turn on preparsing

    EXAMPLES::

        sage: 2/3
        2/3
        sage: preparser(False)
        sage: 2/3  # not tested since doctests are always preparsed
        0
        sage: preparser(True)
        sage: 2^3
        8
    """

class SageShellOverride:
    """
    Mixin to override methods in IPython's [Terminal]InteractiveShell
    classes.
    """
    def show_usage(self) -> None:
        """
        Print the basic Sage usage.

        This method ends up being called when you enter ``?`` and
        nothing else on the command line.

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.run_cell('?')
            Welcome to Sage ...
            sage: shell.quit()
        """
    def system_raw(self, cmd):
        """
        Run a system command.

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: shell.system_raw('false')
            sage: shell.user_ns['_exit_code'] > 0
            True
            sage: shell.system_raw('true')
            sage: shell.user_ns['_exit_code']
            0
            sage: shell.system_raw('R --version')   # optional - r
            R version ...
            sage: shell.user_ns['_exit_code']       # optional - r
            0
            sage: shell.quit()
        """

class SageNotebookInteractiveShell(SageShellOverride, InteractiveShell):
    """
    IPython Shell for the Sage IPython Notebook.

    The doctests are not tested since they would change the current
    rich output backend away from the doctest rich output backend.

    EXAMPLES::

        sage: from sage.repl.interpreter import SageNotebookInteractiveShell
        sage: SageNotebookInteractiveShell()   # not tested
        <sage.repl.interpreter.SageNotebookInteractiveShell object at 0x...>
    """
    def init_display_formatter(self) -> None:
        """
        Switch to the Sage IPython notebook rich output backend.

        EXAMPLES::

            sage: from sage.repl.interpreter import SageNotebookInteractiveShell
            sage: SageNotebookInteractiveShell().init_display_formatter()   # not tested
        """

class SageTerminalInteractiveShell(SageShellOverride, TerminalInteractiveShell):
    """
    IPython Shell for the Sage IPython Commandline Interface.

    The doctests are not tested since they would change the current
    rich output backend away from the doctest rich output backend.

    EXAMPLES::

        sage: from sage.repl.interpreter import SageTerminalInteractiveShell
        sage: SageTerminalInteractiveShell()   # not tested
        <sage.repl.interpreter.SageNotebookInteractiveShell object at 0x...>
    """
    def init_display_formatter(self) -> None:
        """
        Switch to the Sage IPython commandline rich output backend.

        EXAMPLES::

            sage: from sage.repl.interpreter import SageTerminalInteractiveShell
            sage: SageTerminalInteractiveShell().init_display_formatter()   # not tested
        """
    def prompt_for_code(self): ...

class SageTestShell(SageShellOverride, TerminalInteractiveShell):
    """
    Test Shell.

    Care must be taken in these doctests to quit the test shell in
    order to switch back the rich output display backend to the
    doctest backend.

    EXAMPLES::

        sage: from sage.repl.interpreter import get_test_shell
        sage: shell = get_test_shell();  shell
        <sage.repl.interpreter.SageTestShell object at 0x...>
        sage: shell.quit()
    """
    def init_display_formatter(self) -> None:
        """
        Switch to the Sage IPython commandline rich output backend.

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell();  shell
            <sage.repl.interpreter.SageTestShell object at 0x...>
            sage: shell.quit()
            sage: shell.init_display_formatter()
            sage: shell.quit()
        """
    def quit(self) -> None:
        """
        Quit the test shell.

        To make the test shell as realistic as possible, we switch to
        the
        :class:`~sage.repl.rich_output.backend_ipython.BackendIPythonCommandline`
        display backend. This method restores the previous display
        backend, which is the
        :class:`~sage.repl.rich_output.backend_doctest.BackendDoctest`
        during doctests.

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: from sage.repl.rich_output import get_display_manager
            sage: get_display_manager()
            The Sage display manager using the doctest backend

            sage: shell = get_test_shell()
            sage: get_display_manager()
            The Sage display manager using the IPython command line backend

            sage: shell.quit()
            sage: get_display_manager()
            The Sage display manager using the doctest backend
        """
    def run_cell(self, *args, **kwds) -> None:
        """
        Run IPython cell.

        Starting with IPython-3.0, this returns an success/failure
        information. Since it is more convenient for doctests, we
        ignore it.

        EXAMPLES::

            sage: from sage.repl.interpreter import get_test_shell
            sage: shell = get_test_shell()
            sage: rc = shell.run_cell('2^50')
            1125899906842624
            sage: rc is None
            True
            sage: shell.quit()
        """

def SagePreparseTransformer(lines):
    '''
    EXAMPLES::

        sage: from sage.repl.interpreter import SagePreparseTransformer
        sage: spt = SagePreparseTransformer
        sage: spt([\'1+1r+2.3^2.3r\\n\'])
        ["Integer(1)+1+RealNumber(\'2.3\')**2.3\\n"]
        sage: preparser(False)
        sage: spt([\'2.3^2\\n\'])
        [\'2.3^2\\n\']

    TESTS:

    Check that syntax errors in the preparser do not crash IPython,
    see :issue:`14961`. ::

        sage: preparser(True)
        sage: bad_syntax = "R.<t> = QQ{]"
        sage: preparse(bad_syntax)
        Traceback (most recent call last):
        ...
        SyntaxError: mismatched \']\'
        sage: from sage.repl.interpreter import get_test_shell
        sage: shell = get_test_shell()
        sage: shell.run_cell(bad_syntax)
          File...<string>...
        SyntaxError: mismatched \']\'
        <BLANKLINE>
        sage: shell.quit()

    Make sure the quote state is carried over across subsequent lines in order
    to avoid interfering with multi-line strings, see :issue:`30417`. ::

        sage: SagePreparseTransformer(["\'\'\'\\n", \'abc-1-2\\n\', "\'\'\'\\n"])
        ["\'\'\'\\n", \'abc-1-2\\n\', "\'\'\'\\n"]
        sage: # instead of ["\'\'\'\\n", \'abc-Integer(1)-Integer(2)\\n\', "\'\'\'\\n"]

    .. NOTE::

        IPython may call this function more than once for the same input lines.
        So when debugging the preparser, print outs may be duplicated. If using
        IPython >= 7.17, try:
        ``sage.repl.interpreter.SagePreparseTransformer.has_side_effects = True``
    '''

SagePromptTransformer: Incomplete

class logstr(str):
    """
    For use by :meth`~InterfaceShellTransformer.transform`.
    This provides a ``_latex_`` method which is just the string
    wrapped in a ``\\verb`` environment.
    """

class InterfaceShellTransformer(PrefilterTransformer):
    priority: int
    temporary_objects: Incomplete
    def __init__(self, *args, **kwds) -> None:
        """
        Initialize this class.  All of the arguments get passed to
        :meth:`PrefilterTransformer.__init__`.

        .. attribute:: temporary_objects

           a list of hold onto interface objects and keep them from being
           garbage collected

        .. SEEALSO:: :func:`interface_shell_embed`

        TESTS::

            sage: # needs sage.symbolic
            sage: from sage.repl.interpreter import interface_shell_embed
            sage: shell = interface_shell_embed(maxima)
            sage: ift = shell.prefilter_manager.transformers[0]
            sage: ift.temporary_objects
            set()
            sage: ift._sage_import_re.findall('sage(a) + maxima(b)')
            ['sage(', 'maxima(']
        """
    def preparse_imports_from_sage(self, line):
        """
        Finds occurrences of strings such as ``sage(object)`` in
        *line*, converts ``object`` to :attr:`shell.interface`,
        and replaces those strings with their identifier in the new
        system.  This also works with strings such as
        ``maxima(object)`` if :attr:`shell.interface` is
        ``maxima``.

        - ``line`` -- string; the line to transform

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.repl.interpreter import interface_shell_embed, InterfaceShellTransformer
            sage: shell = interface_shell_embed(maxima)
            sage: ift = InterfaceShellTransformer(shell=shell, config=shell.config,
            ....:     prefilter_manager=shell.prefilter_manager)
            sage: ift.shell.ex('a = 3')
            sage: ift.preparse_imports_from_sage('2 + sage(a)')
            '2 + sage0 '
            sage: maxima.eval('sage0')
            '3'
            sage: ift.preparse_imports_from_sage('2 + maxima(a)') # maxima calls set_seed on startup which is why 'sage0' will becomes 'sage4' and not just 'sage1'
            '2 +  sage4 '
            sage: ift.preparse_imports_from_sage('2 + gap(a)')
            '2 + gap(a)'

        Since :issue:`28439`, this also works with more complicated expressions
        containing nested parentheses::

            sage: # needs sage.libs.gap sage.symbolic
            sage: shell = interface_shell_embed(gap)
            sage: shell.user_ns = locals()
            sage: ift = InterfaceShellTransformer(shell=shell, config=shell.config,
            ....:     prefilter_manager=shell.prefilter_manager)
            sage: line = '2 + sage((1+2)*gap(-(5-3)^2).sage()) - gap(1+(2-1))'
            sage: line = ift.preparse_imports_from_sage(line)
            sage: gap.eval(line)
            '-12'
        """
    def transform(self, line, continue_prompt):
        '''
        Evaluates *line* in :attr:`shell.interface` and returns a
        string representing the result of that evaluation.

        - ``line`` -- string; the line to be transformed *and evaluated*
        - ``continue_prompt`` -- boolean; whether this line is a continuation in a
          sequence of multiline input

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.repl.interpreter import interface_shell_embed, InterfaceShellTransformer
            sage: shell = interface_shell_embed(maxima)
            sage: ift = InterfaceShellTransformer(shell=shell, config=shell.config,
            ....:     prefilter_manager=shell.prefilter_manager)
            sage: ift.transform(\'2+2\', False)   # note: output contains triple quotation marks
            \'sage.repl.interpreter.logstr(r"""4""")\'
            sage: ift.shell.ex(\'a = 4\')
            sage: ift.transform(r\'sage(a)+4\', False)
            \'sage.repl.interpreter.logstr(r"""8""")\'
            sage: ift.temporary_objects
            set()
            sage: shell = interface_shell_embed(gap)                                    # needs sage.libs.gap
            sage: ift = InterfaceShellTransformer(shell=shell, config=shell.config,     # needs sage.libs.gap
            ....:     prefilter_manager=shell.prefilter_manager)
            sage: ift.transform(\'2+2\', False)
            \'sage.repl.interpreter.logstr(r"""4""")\'

        TESTS:

        Check that whitespace is not stripped and that special characters are
        escaped (:issue:`28439`)::

            sage: shell = interface_shell_embed(gap)                                    # needs sage.libs.gap sage.symbolic
            sage: ift = InterfaceShellTransformer(shell=shell, config=shell.config,     # needs sage.libs.gap sage.symbolic
            ....:     prefilter_manager=shell.prefilter_manager)
            sage: ift.transform(r\'Print("  -\\n\\\\\\\\-  ");\', False)                       # needs sage.symbolic
            \'sage.repl.interpreter.logstr(r"""  -\\n\\\\\\\\-""")\'

            sage: # optional - macaulay2
            sage: shell = interface_shell_embed(macaulay2)
            sage: ift = InterfaceShellTransformer(shell=shell, config=shell.config,
            ....:     prefilter_manager=shell.prefilter_manager)
            sage: ift.transform(\'net(ZZ^2)\', False)
            \'sage.repl.interpreter.logstr(r"""  2\\nZZ""")\'
        '''

def interface_shell_embed(interface):
    """
    Return an IPython shell which uses a Sage interface on the
    backend to perform the evaluations.  It uses
    :class:`InterfaceShellTransformer` to transform the input into the
    appropriate ``interface.eval(...)`` input.

    INPUT:

    - ``interface`` -- a Sage ``PExpect`` interface instance

    EXAMPLES::

        sage: from sage.repl.interpreter import interface_shell_embed
        sage: shell = interface_shell_embed(gap)                                        # needs sage.libs.gap
        sage: shell.run_cell('List( [1..10], IsPrime )')                                # needs sage.libs.gap
        [ false, true, true, false, true, false, true, false, false, false ]
        <ExecutionResult object at ..., execution_count=None error_before_exec=None error_in_exec=None ...result=[ false, true, true, false, true, false, true, false, false, false ]>
    """
def get_test_shell():
    '''
    Return a IPython shell that can be used in testing the functions
    in this module.

    OUTPUT: an IPython shell

    EXAMPLES::

        sage: from sage.repl.interpreter import get_test_shell
        sage: shell = get_test_shell(); shell
        <sage.repl.interpreter.SageTestShell object at 0x...>
        sage: shell.parent.shell_class
        <class \'sage.repl.interpreter.SageTestShell\'>
        sage: shell.parent.test_shell
        True
        sage: shell.quit()

    TESTS:

    Check that :issue:`14070` has been resolved::

        sage: from sage.tests import check_executable
        sage: cmd = \'from sage.repl.interpreter import get_test_shell; shell = get_test_shell()\'
        sage: (out, err, ret) = check_executable(["sage", "-c", cmd])
        sage: out + err
        \'\'
    '''

class SageCrashHandler(IPAppCrashHandler):
    crash_report_fname: str
    def __init__(self, app) -> None:
        """
        A custom :class:`CrashHandler` which gives the user
        instructions on how to post the problem to sage-support.

        EXAMPLES::

            sage: from sage.repl.interpreter import SageTerminalApp, SageCrashHandler
            sage: app = SageTerminalApp.instance()
            sage: sch = SageCrashHandler(app); sch
            <sage.repl.interpreter.SageCrashHandler object at 0x...>
            sage: sorted(sch.info.items())
            [('app_name', 'Sage'),
             ('bug_tracker', 'https://github.com/sagemath/sage/issues'),
             ('contact_email', 'sage-support@googlegroups.com'),
             ('contact_name', 'sage-support'),
             ('crash_report_fname', 'Crash_report_Sage.txt')]
        """

class SageTerminalApp(TerminalIPythonApp):
    name: str
    crash_handler_class = SageCrashHandler
    test_shell: Incomplete
    shell_class: Incomplete
    config: Incomplete
    def load_config_file(self, *args, **kwds) -> None:
        """
        Merges a config file with the default sage config.

        .. NOTE::

            This code is based on :meth:`Application.update_config`.

        TESTS:

        Test that :issue:`15972` has been fixed::

            sage: import tempfile
            sage: from sage.repl.interpreter import SageTerminalApp
            sage: from IPython.paths import get_ipython_dir
            sage: with tempfile.TemporaryDirectory() as d:
            ....:     IPYTHONDIR = get_ipython_dir()
            ....:     os.environ['IPYTHONDIR'] = d
            ....:     SageTerminalApp().load_config_file()
            ....:     os.environ['IPYTHONDIR'] = IPYTHONDIR
        """
    shell: Incomplete
    def init_shell(self) -> None:
        """
        Initialize the :class:`SageInteractiveShell` instance.

        .. NOTE::

            This code is based on
            :meth:`TerminalIPythonApp.init_shell`.

        EXAMPLES::

            sage: from sage.repl.interpreter import SageTerminalApp
            sage: app = SageTerminalApp.instance()
            sage: app.shell
            <sage.repl.interpreter.SageTestShell object at 0x...>
        """
