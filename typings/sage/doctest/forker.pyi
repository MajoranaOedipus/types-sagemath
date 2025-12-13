import doctest
import multiprocessing
from _typeshed import Incomplete
from sage.cpython.atexit import restore_atexit as restore_atexit
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.doctest.control import DocTestController as DocTestController
from sage.doctest.parsing import OriginalSource as OriginalSource, SageOutputChecker as SageOutputChecker, get_source as get_source, pre_hash as pre_hash, reduce_hex as reduce_hex, unparse_optional_tags as unparse_optional_tags
from sage.doctest.sources import DictAsObject as DictAsObject
from sage.doctest.util import RecordingDict as RecordingDict, Timer as Timer, count_noun as count_noun
from sage.misc import randstate as randstate
from sage.repl.user_globals import set_globals as set_globals
from sage.structure.sage_object import SageObject as SageObject
from typing import NamedTuple

def init_sage(controller: DocTestController | None = None) -> None:
    '''
    Import the Sage library.

    This function is called once at the beginning of a doctest run
    (rather than once for each file).  It imports the Sage library,
    sets DOCTEST_MODE to True, and invalidates any interfaces.

    EXAMPLES::

        sage: from sage.doctest.forker import init_sage
        sage: sage.doctest.DOCTEST_MODE = False
        sage: init_sage()
        sage: sage.doctest.DOCTEST_MODE
        True

    Check that pexpect interfaces are invalidated, but still work::

        sage: gap.eval("my_test_var := 42;")
        \'42\'
        sage: gap.eval("my_test_var;")
        \'42\'
        sage: init_sage()
        sage: gap(\'Group((1,2,3)(4,5), (3,4))\')
        Group( [ (1,2,3)(4,5), (3,4) ] )
        sage: gap.eval("my_test_var;")
        Traceback (most recent call last):
        ...
        RuntimeError: Gap produced error output...

    Check that SymPy equation pretty printer is limited in doctest
    mode to default width (80 chars)::

        sage: # needs sympy
        sage: from sympy import sympify
        sage: from sympy.printing.pretty.pretty import PrettyPrinter
        sage: s = sympify(\'+x^\'.join(str(i) for i in range(30)))
        sage: print(PrettyPrinter(settings={\'wrap_line\': True}).doprint(s))
         29    28    27    26    25    24    23    22    21    20    19    18    17...
        x   + x   + x   + x   + x   + x   + x   + x   + x   + x   + x   + x   + x...
        <BLANKLINE>
        ... 16    15    14    13    12    11    10    9    8    7    6    5    4    3...
        ...x   + x   + x   + x   + x   + x   + x   + x  + x  + x  + x  + x  + x  + x...
        <BLANKLINE>
        ...

    The displayhook sorts dictionary keys to simplify doctesting of
    dictionary output::

        sage: {\'a\':23, \'b\':34, \'au\':56, \'bbf\':234, \'aaa\':234}
        {\'a\': 23, \'aaa\': 234, \'au\': 56, \'b\': 34, \'bbf\': 234}
    '''
def showwarning_with_traceback(message, category, filename, lineno, file=None, line=None) -> None:
    '''
    Displays a warning message with a traceback.

    INPUT: see :func:`warnings.showwarning` with the difference that with ``file=None``
           the message will be written to stdout.

    OUTPUT: none

    EXAMPLES::

        sage: from sage.doctest.forker import showwarning_with_traceback
        sage: showwarning_with_traceback("bad stuff", UserWarning, "myfile.py", 0)
        doctest:warning...
          File "<doctest sage.doctest.forker.showwarning_with_traceback[1]>", line 1, in <module>
            showwarning_with_traceback("bad stuff", UserWarning, "myfile.py", Integer(0))
        :
        UserWarning: bad stuff
    '''

class SageSpoofInOut(SageObject):
    '''
    We replace the standard :class:`doctest._SpoofOut` for three reasons:

    - we need to divert the output of C programs that don\'t print
      through sys.stdout,
    - we want the ability to recover partial output from doctest
      processes that segfault.
    - we also redirect stdin (usually from /dev/null) during doctests.

    This class defines streams ``self.real_stdin``, ``self.real_stdout``
    and ``self.real_stderr`` which refer to the original streams.

    INPUT:

    - ``outfile`` -- (default: ``tempfile.TemporaryFile()``) a seekable open file
      object to which stdout and stderr should be redirected

    - ``infile`` -- (default: ``open(os.devnull)``) an open file object
      from which stdin should be redirected

    EXAMPLES::

        sage: import subprocess, tempfile
        sage: from sage.doctest.forker import SageSpoofInOut
        sage: O = tempfile.TemporaryFile()
        sage: S = SageSpoofInOut(O)
        sage: try:
        ....:     S.start_spoofing()
        ....:     print("hello world")
        ....: finally:
        ....:     S.stop_spoofing()
        ....:
        sage: S.getvalue()
        \'hello world\\n\'
        sage: _ = O.seek(0)
        sage: S = SageSpoofInOut(outfile=sys.stdout, infile=O)
        sage: try:
        ....:     S.start_spoofing()
        ....:     _ = subprocess.check_call("cat")
        ....: finally:
        ....:     S.stop_spoofing()
        ....:
        hello world
        sage: O.close()
    '''
    infile: Incomplete
    outfile: Incomplete
    spoofing: bool
    real_stdin: Incomplete
    real_stdout: Incomplete
    real_stderr: Incomplete
    position: int
    def __init__(self, outfile=None, infile=None) -> None:
        """
        Initialization.

        TESTS::

            sage: from tempfile import TemporaryFile
            sage: from sage.doctest.forker import SageSpoofInOut
            sage: with TemporaryFile() as outfile:
            ....:     with TemporaryFile() as infile:
            ....:         SageSpoofInOut(outfile, infile)
            <sage.doctest.forker.SageSpoofInOut object at ...>
        """
    def __del__(self) -> None:
        '''
        Stop spoofing.

        TESTS::

            sage: from sage.doctest.forker import SageSpoofInOut
            sage: spoof = SageSpoofInOut()
            sage: spoof.start_spoofing()
            sage: print("Spoofed!")  # No output
            sage: del spoof
            sage: print("Not spoofed!")
            Not spoofed!
        '''
    def start_spoofing(self) -> None:
        '''
        Set stdin to read from ``self.infile`` and stdout to print to
        ``self.outfile``.

        EXAMPLES::

            sage: import os, tempfile
            sage: from sage.doctest.forker import SageSpoofInOut
            sage: O = tempfile.TemporaryFile()
            sage: S = SageSpoofInOut(O)
            sage: try:
            ....:     S.start_spoofing()
            ....:     print("this is not printed")
            ....: finally:
            ....:     S.stop_spoofing()
            ....:
            sage: S.getvalue()
            \'this is not printed\\n\'
            sage: _ = O.seek(0)
            sage: S = SageSpoofInOut(infile=O)
            sage: try:
            ....:     S.start_spoofing()
            ....:     v = sys.stdin.read()
            ....: finally:
            ....:     S.stop_spoofing()
            ....:
            sage: v
            \'this is not printed\\n\'

        We also catch non-Python output::

            sage: try:
            ....:     S.start_spoofing()
            ....:     retval = os.system(\'\'\'echo "Hello there"\\nif [ $? -eq 0 ]; then\\necho "good"\\nfi\'\'\')
            ....: finally:
            ....:     S.stop_spoofing()
            ....:
            sage: S.getvalue()
            \'Hello there\\ngood\\n\'
            sage: O.close()
        '''
    def stop_spoofing(self) -> None:
        '''
        Reset stdin and stdout to their original values.

        EXAMPLES::

            sage: from sage.doctest.forker import SageSpoofInOut
            sage: S = SageSpoofInOut()
            sage: try:
            ....:     S.start_spoofing()
            ....:     print("this is not printed")
            ....: finally:
            ....:     S.stop_spoofing()
            ....:
            sage: print("this is now printed")
            this is now printed
        '''
    def getvalue(self):
        '''
        Get the value that has been printed to ``outfile`` since the
        last time this function was called.

        EXAMPLES::

            sage: from sage.doctest.forker import SageSpoofInOut
            sage: S = SageSpoofInOut()
            sage: try:
            ....:     S.start_spoofing()
            ....:     print("step 1")
            ....: finally:
            ....:     S.stop_spoofing()
            ....:
            sage: S.getvalue()
            \'step 1\\n\'
            sage: try:
            ....:     S.start_spoofing()
            ....:     print("step 2")
            ....: finally:
            ....:     S.stop_spoofing()
            ....:
            sage: S.getvalue()
            \'step 2\\n\'
        '''

class TestResults(NamedTuple):
    failed: Incomplete
    attempted: Incomplete

class SageDocTestRunner(doctest.DocTestRunner):
    msgfile: Incomplete
    options: Incomplete
    baseline: Incomplete
    history: Incomplete
    references: Incomplete
    setters: Incomplete
    running_global_digest: Incomplete
    total_walltime_skips: int
    total_performed_tests: int
    total_walltime: int
    def __init__(self, *args, **kwds) -> None:
        """
        A customized version of DocTestRunner that tracks dependencies
        of doctests.

        INPUT:

        - ``stdout`` -- an open file to restore for debugging

        - ``checker`` -- ``None``, or an instance of
          :class:`doctest.OutputChecker`

        - ``verbose`` -- boolean, determines whether verbose printing
          is enabled

        - ``optionflags`` -- controls the comparison with the expected
          output.  See :mod:`testmod` for more information

        - ``baseline`` -- dictionary, the ``baseline_stats`` value

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: import doctest, sys, os
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=False, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: DTR
            <sage.doctest.forker.SageDocTestRunner object at ...>
        """
    running_doctest_digest: Incomplete
    test: Incomplete
    debugger: Incomplete
    save_linecache_getlines: Incomplete
    no_failure_yet: bool
    def run(self, test, compileflags: int = 0, out=None, clear_globs: bool = True):
        """
        Run the examples in a given doctest.

        This function replaces :class:`doctest.DocTestRunner.run`
        since it needs to handle spoofing. It also leaves the display
        hook in place.

        INPUT:

        - ``test`` -- an instance of :class:`doctest.DocTest`

        - ``compileflags`` -- integer (default: 0) the set of compiler flags
          used to execute examples (passed in to the :func:`compile`)

        - ``out`` -- a function for writing the output (defaults to
          :func:`sys.stdout.write`)

        - ``clear_globs`` -- boolean (default: ``True``); whether to clear
          the namespace after running this doctest

        OUTPUT:

        - ``f`` -- integer, the number of examples that failed

        - ``t`` -- the number of examples tried

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: import doctest, sys, os
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=False, sage_options=DD,
            ....:                         optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DD)
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: DTR.run(doctests[0], clear_globs=False)
            TestResults(failed=0, attempted=4)
        """
    def summarize(self, verbose=None):
        """
        Print results of testing to ``self.msgfile`` and return number
        of failures and tests run.

        INPUT:

        - ``verbose`` -- whether to print lots of stuff

        OUTPUT:

        - returns ``(f, t)``, a :class:`doctest.TestResults` instance
          giving the number of failures and the total number of tests
          run.

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: import doctest, sys, os
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=False, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: DTR._stats['sage.doctest.forker'] = (1,120)
            sage: results = DTR.summarize()
            **********************************************************************
            1 item had failures:
                1 of 120 in sage.doctest.forker
            sage: results
            TestResults(failed=1, attempted=120)
        """
    def update_digests(self, example) -> None:
        """
        Update global and doctest digests.

        Sage's doctest runner tracks the state of doctests so that
        their dependencies are known.  For example, in the following
        two lines ::

            sage: R.<x> = ZZ[]
            sage: f = x^2 + 1

        it records that the second line depends on the first since the
        first INSERTS ``x`` into the global namespace and the second
        line RETRIEVES ``x`` from the global namespace.

        This function updates the hashes that record these
        dependencies.

        INPUT:

        - ``example`` -- a :class:`doctest.Example` instance

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: import doctest, sys, os, hashlib
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=False, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DD)
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: DTR.running_global_digest.hexdigest()
            'd41d8cd98f00b204e9800998ecf8427e'
            sage: DTR.running_doctest_digest = hashlib.md5()
            sage: ex = doctests[0].examples[0]; ex.predecessors = None
            sage: DTR.update_digests(ex)
            sage: DTR.running_global_digest.hexdigest()
            '3cb44104292c3a3ab4da3112ce5dc35c'
        """
    def compile_and_execute(self, example, compiler, globs) -> None:
        """
        Run the given example, recording dependencies.

        Rather than using a basic dictionary, Sage's doctest runner
        uses a :class:`sage.doctest.util.RecordingDict`, which records
        every time a value is set or retrieved.  Executing the given
        code with this recording dictionary as the namespace allows
        Sage to track dependencies between doctest lines.  For
        example, in the following two lines ::

            sage: R.<x> = ZZ[]
            sage: f = x^2 + 1

        the recording dictionary records that the second line depends
        on the first since the first INSERTS ``x`` into the global
        namespace and the second line RETRIEVES ``x`` from the global
        namespace.

        INPUT:

        - ``example`` -- a :class:`doctest.Example` instance

        - ``compiler`` -- a callable that, applied to example,
          produces a code object

        - ``globs`` -- dictionary in which to execute the code

        OUTPUT: the output of the compiled code snippet

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.util import RecordingDict
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: import doctest, sys, os, hashlib
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=False, sage_options=DD,
            ....:           optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: DTR.running_doctest_digest = hashlib.md5()
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DD)
            sage: globs = RecordingDict(globals())
            sage: 'doctest_var' in globs
            False
            sage: doctests, extras = FDS.create_doctests(globs)
            sage: ex0 = doctests[0].examples[0]
            sage: flags = 524288
            sage: def compiler(ex):
            ....:     return compile(ex.source, '<doctest sage.doctest.forker[0]>',
            ....:                    'single', flags, 1)
            sage: DTR.compile_and_execute(ex0, compiler, globs)
            1764
            sage: globs['doctest_var']
            42
            sage: globs.set
            {'doctest_var'}
            sage: globs.got
            {'Integer'}

        Now we can execute some more doctests to see the dependencies. ::

            sage: ex1 = doctests[0].examples[1]
            sage: def compiler(ex):
            ....:     return compile(ex.source, '<doctest sage.doctest.forker[1]>',
            ....:                    'single', flags, 1)
            sage: DTR.compile_and_execute(ex1, compiler, globs)
            sage: sorted(list(globs.set))
            ['R', 'a']
            sage: globs.got
            {'ZZ'}
            sage: ex1.predecessors
            []

        ::

            sage: ex2 = doctests[0].examples[2]
            sage: def compiler(ex):
            ....:     return compile(ex.source, '<doctest sage.doctest.forker[2]>',
            ....:                    'single', flags, 1)
            sage: DTR.compile_and_execute(ex2, compiler, globs)
            a + 42
            sage: list(globs.set)
            []
            sage: sorted(list(globs.got))
            ['a', 'doctest_var']
            sage: set(ex2.predecessors) == set([ex0,ex1])
            True
        """
    def report_start(self, out, test, example) -> None:
        """
        Called when an example starts.

        INPUT:

        - ``out`` -- a function for printing

        - ``test`` -- a :class:`doctest.DocTest` instance

        - ``example`` -- a :class:`doctest.Example` instance in ``test``

        OUTPUT: prints a report to ``out``

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: import doctest, sys, os
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=True, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DD)
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: ex = doctests[0].examples[0]
            sage: DTR.report_start(sys.stdout.write, doctests[0], ex)
            Trying (line 12):    doctest_var = 42; doctest_var^2
            Expecting:
                1764
        """
    def report_success(self, out, test, example, got, *, check_timer=None) -> None:
        """
        Called when an example succeeds.

        INPUT:

        - ``out`` -- a function for printing

        - ``test`` -- a :class:`doctest.DocTest` instance

        - ``example`` -- a :class:`doctest.Example` instance in ``test``

        - ``got`` -- string; the result of running ``example``

        - ``check_timer`` -- a :class:`sage.doctest.util.Timer` (default:
          ``None``) that measures the time spent checking whether or not
          the output was correct

        OUTPUT: prints a report to ``out``; if in debugging mode, starts an
        IPython prompt at the point of the failure

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: from sage.doctest.util import Timer
            sage: import doctest, sys, os
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=True, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DD)
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: ex = doctests[0].examples[0]
            sage: ex.cputime = 1.01
            sage: ex.walltime = 1.12
            sage: check = Timer()
            sage: check.cputime = 2.14
            sage: check.walltime = 2.71
            sage: DTR.report_success(sys.stdout.write, doctests[0], ex, '1764',
            ....:                    check_timer=check)
            ok [3.83s wall]
        """
    def report_failure(self, out, test, example, got, globs):
        '''
        Called when a doctest fails.

        INPUT:

        - ``out`` -- a function for printing

        - ``test`` -- a :class:`doctest.DocTest` instance

        - ``example`` -- a :class:`doctest.Example` instance in ``test``

        - ``got`` -- string, the result of running ``example``

        - ``globs`` -- dictionary of globals, used if in debugging mode

        OUTPUT: prints a report to ``out``

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: import doctest, sys, os
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=True, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DD)
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: ex = doctests[0].examples[0]
            sage: DTR.no_failure_yet = True
            sage: DTR.report_failure(sys.stdout.write, doctests[0], ex, \'BAD ANSWER\\n\', {})
            **********************************************************************
            File ".../sage/doctest/forker.py", line 12, in sage.doctest.forker
            Failed example:
                doctest_var = 42; doctest_var^2
            Expected:
                1764
            Got:
                BAD ANSWER

        If debugging is turned on this function starts an IPython
        prompt when a test returns an incorrect answer::

            sage: sage0.quit()
            sage: _ = sage0.eval("import doctest, sys, os, multiprocessing, subprocess")
            sage: _ = sage0.eval("from sage.doctest.parsing import SageOutputChecker")
            sage: _ = sage0.eval("import sage.doctest.forker as sdf")
            sage: _ = sage0.eval("from sage.doctest.control import DocTestDefaults")
            sage: _ = sage0.eval("DD = DocTestDefaults(debug=True)")
            sage: _ = sage0.eval("ex1 = doctest.Example(\'a = 17\', \'\')")
            sage: _ = sage0.eval("ex2 = doctest.Example(\'2*a\', \'1\')")
            sage: _ = sage0.eval("DT = doctest.DocTest([ex1,ex2], globals(), \'doubling\', None, 0, None)")
            sage: _ = sage0.eval("DTR = sdf.SageDocTestRunner(SageOutputChecker(), verbose=False, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)")
            sage: print(sage0.eval("sdf.init_sage(); DTR.run(DT, clear_globs=False)")) # indirect doctest
            **********************************************************************
            Line 1, in doubling
            Failed example:
                2*a
            Expected:
                1
            Got:
                34
            **********************************************************************
            Previously executed commands:
            sage: sage0._expect.expect(\'sage: \')   # sage0 just mis-identified the output as prompt, synchronize
            0
            sage: sage0.eval("a")
            \'...17\'
            sage: sage0.eval("quit")
            \'Returning to doctests...TestResults(failed=1, attempted=2)\'
        '''
    def report_overtime(self, out, test, example, got, *, check_timer=None) -> None:
        '''
        Called when the ``warn_long`` option flag is set and a doctest
        runs longer than the specified time.

        INPUT:

        - ``out`` -- a function for printing

        - ``test`` -- a :class:`doctest.DocTest` instance

        - ``example`` -- a :class:`doctest.Example` instance in ``test``

        - ``got`` -- string; the result of running ``example``

        - ``check_timer`` -- a :class:`sage.doctest.util.Timer` (default:
          ``None``) that measures the time spent checking whether or not
          the output was correct

        OUTPUT: prints a report to ``out``

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: from sage.doctest.util import Timer
            sage: import doctest, sys, os
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=True, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DD)
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: ex = doctests[0].examples[0]
            sage: ex.cputime = 1.23
            sage: ex.walltime = 2.50
            sage: check = Timer()
            sage: check.cputime = 2.34
            sage: check.walltime = 3.12
            sage: DTR.report_overtime(sys.stdout.write, doctests[0], ex, \'BAD ANSWER\\n\', check_timer=check)
            **********************************************************************
            File ".../sage/doctest/forker.py", line 12, in sage.doctest.forker
            Warning: slow doctest:
                doctest_var = 42; doctest_var^2
            Test ran for 1.23s cpu, 2.50s wall
            Check ran for 2.34s cpu, 3.12s wall
        '''
    def report_unexpected_exception(self, out, test, example, exc_info):
        '''
        Called when a doctest raises an exception that\'s not matched by the expected output.

        If debugging has been turned on, starts an interactive debugger.

        INPUT:

        - ``out`` -- a function for printing

        - ``test`` -- a :class:`doctest.DocTest` instance

        - ``example`` -- a :class:`doctest.Example` instance in ``test``

        - ``exc_info`` -- the result of ``sys.exc_info()``

        OUTPUT: prints a report to ``out``

        - if in debugging mode, starts PDB with the given traceback

        EXAMPLES::

            sage: from sage.interfaces.sage0 import sage0
            sage: sage0.quit()
            sage: _ = sage0.eval("import doctest, sys, os, multiprocessing, subprocess")
            sage: _ = sage0.eval("from sage.doctest.parsing import SageOutputChecker")
            sage: _ = sage0.eval("import sage.doctest.forker as sdf")
            sage: _ = sage0.eval("from sage.doctest.control import DocTestDefaults")
            sage: _ = sage0.eval("DD = DocTestDefaults(debug=True)")
            sage: _ = sage0.eval("ex = doctest.Example(\'E = EllipticCurve([0,0]); E\', \'A singular Elliptic Curve\')")
            sage: _ = sage0.eval("DT = doctest.DocTest([ex], globals(), \'singular_curve\', None, 0, None)")
            sage: _ = sage0.eval("DTR = sdf.SageDocTestRunner(SageOutputChecker(), verbose=False, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)")
            sage: old_prompt = sage0._prompt
            sage: sage0._prompt = r"\\(Pdb\\) "
            sage: sage0.eval("DTR.run(DT, clear_globs=False)") # indirect doctest
            \'... ArithmeticError(self._equation_string() + " defines a singular curve")\'
            sage: sage0.eval("l")
            \'...if self.discriminant() == 0:...raise ArithmeticError...\'
            sage: sage0.eval("u")
            \'...-> super().__init__(R, data, category=category)\'
            sage: sage0.eval("u")
            \'...EllipticCurve_field.__init__(self, K, ainvs)\'
            sage: sage0.eval("p ainvs")
            \'(0, 0, 0, 0, 0)\'
            sage: sage0._prompt = old_prompt
            sage: sage0.eval("quit")
            \'TestResults(failed=1, attempted=1)\'
        '''
    def update_results(self, D):
        """
        When returning results we pick out the results of interest
        since many attributes are not pickleable.

        INPUT:

        - ``D`` -- dictionary to update with cputime and walltime

        OUTPUT: the number of failures (or ``False`` if there is no failure
        attribute)

        EXAMPLES::

            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.sources import FileDocTestSource, DictAsObject
            sage: from sage.doctest.control import DocTestDefaults; DD = DocTestDefaults()
            sage: import doctest, sys, os
            sage: DTR = SageDocTestRunner(SageOutputChecker(), verbose=False, sage_options=DD, optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: filename = sage.doctest.forker.__file__
            sage: FDS = FileDocTestSource(filename, DD)
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: from sage.doctest.util import Timer
            sage: T = Timer().start()
            sage: DTR.run(doctests[0])
            TestResults(failed=0, attempted=4)
            sage: T.stop().annotate(DTR)
            sage: D = DictAsObject({'cputime': [], 'walltime': [], 'err': None})
            sage: DTR.update_results(D)
            0
            sage: sorted(list(D.items()))
            [('cputime', [...]), ('err', None), ('failures', 0), ('tests', 4),
             ('walltime', [...]), ('walltime_skips', 0)]
        """

def dummy_handler(sig, frame) -> None:
    """
    Dummy signal handler for SIGCHLD (just to ensure the signal
    isn't ignored).

    TESTS::

        sage: import signal
        sage: from sage.doctest.forker import dummy_handler
        sage: _ = signal.signal(signal.SIGUSR1, dummy_handler)
        sage: os.kill(os.getpid(), signal.SIGUSR1)
        sage: signal.signal(signal.SIGUSR1, signal.SIG_DFL)
        <function dummy_handler at ...>
    """

class DocTestDispatcher(SageObject):
    """
    Create parallel :class:`DocTestWorker` processes and dispatches
    doctesting tasks.
    """
    controller: Incomplete
    def __init__(self, controller: DocTestController) -> None:
        """
        INPUT:

        - ``controller`` -- a :class:`sage.doctest.control.DocTestController` instance

        EXAMPLES::

            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: from sage.doctest.forker import DocTestDispatcher
            sage: DocTestDispatcher(DocTestController(DocTestDefaults(), []))
            <sage.doctest.forker.DocTestDispatcher object at ...>
        """
    def serial_dispatch(self) -> None:
        """
        Run the doctests from the controller's specified sources in series.

        There is no graceful handling for signals, no possibility of
        interrupting tests and no timeout.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: from sage.doctest.forker import DocTestDispatcher
            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.util import Timer
            sage: import os
            sage: homset = os.path.join(SAGE_SRC, 'sage', 'rings', 'homset.py')
            sage: ideal = os.path.join(SAGE_SRC, 'sage', 'rings', 'ideal.py')
            sage: DC = DocTestController(DocTestDefaults(), [homset, ideal])
            sage: DC.expand_files_into_sources()
            sage: DD = DocTestDispatcher(DC)
            sage: DR = DocTestReporter(DC)
            sage: DC.reporter = DR
            sage: DC.dispatcher = DD
            sage: DC.timer = Timer().start()
            sage: DD.serial_dispatch()
            sage -t .../rings/homset.py
                [... tests, ...s wall]
            sage -t .../rings/ideal.py
                [... tests, ...s wall]
        """
    def parallel_dispatch(self) -> None:
        '''
        Run the doctests from the controller\'s specified sources in parallel.

        This creates :class:`DocTestWorker` subprocesses, while the master
        process checks for timeouts and collects and displays the results.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: from sage.doctest.forker import DocTestDispatcher
            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.util import Timer
            sage: import os
            sage: crem = os.path.join(SAGE_SRC, \'sage\', \'databases\', \'cremona.py\')
            sage: bigo = os.path.join(SAGE_SRC, \'sage\', \'rings\', \'big_oh.py\')
            sage: DC = DocTestController(DocTestDefaults(), [crem, bigo])
            sage: DC.expand_files_into_sources()
            sage: DD = DocTestDispatcher(DC)
            sage: DR = DocTestReporter(DC)
            sage: DC.reporter = DR
            sage: DC.dispatcher = DD
            sage: DC.timer = Timer().start()
            sage: DD.parallel_dispatch()
            sage -t .../databases/cremona.py
                [... tests, ...s wall]
            sage -t .../rings/big_oh.py
                [... tests, ...s wall]

        If the ``exitfirst=True`` option is given, the results for a failing
        module will be immediately printed and any other ongoing tests
        canceled::

            sage: from tempfile import NamedTemporaryFile as NTF
            sage: with (NTF(suffix=\'.py\', mode=\'w+t\') as f1,
            ....:       NTF(suffix=\'.py\', mode=\'w+t\') as f2):
            ....:     _ = f1.write("\'\'\'\\nsage: import time; time.sleep(60)\\n\'\'\'")
            ....:     f1.flush()
            ....:     _ = f2.write("\'\'\'\\nsage: True\\nFalse\\n\'\'\'")
            ....:     f2.flush()
            ....:     DC = DocTestController(DocTestDefaults(exitfirst=True,
            ....:                                            nthreads=2),
            ....:                            [f1.name, f2.name])
            ....:     DC.expand_files_into_sources()
            ....:     DD = DocTestDispatcher(DC)
            ....:     DR = DocTestReporter(DC)
            ....:     DC.reporter = DR
            ....:     DC.dispatcher = DD
            ....:     DC.timer = Timer().start()
            ....:     DD.parallel_dispatch()
            sage -t ...
            **********************************************************************
            File "...", line 2, in ...
            Failed example:
                True
            Expected:
                False
            Got:
                True
            **********************************************************************
            1 item had failures:
               1 of   1 in ...
                [1 test, 1 failure, ...s wall]
            Killing test ...
        '''
    def dispatch(self) -> None:
        """
        Run the doctests for the controller's specified sources,
        by calling :meth:`parallel_dispatch` or :meth:`serial_dispatch`
        according to the ``--serial`` option.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: from sage.doctest.forker import DocTestDispatcher
            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.util import Timer
            sage: import os
            sage: freehom = os.path.join(SAGE_SRC, 'sage', 'modules', 'free_module_homspace.py')
            sage: bigo = os.path.join(SAGE_SRC, 'sage', 'rings', 'big_oh.py')
            sage: DC = DocTestController(DocTestDefaults(), [freehom, bigo])
            sage: DC.expand_files_into_sources()
            sage: DD = DocTestDispatcher(DC)
            sage: DR = DocTestReporter(DC)
            sage: DC.reporter = DR
            sage: DC.dispatcher = DD
            sage: DC.timer = Timer().start()
            sage: DD.dispatch()
            sage -t .../sage/modules/free_module_homspace.py
                [... tests, ...s wall]
            sage -t .../sage/rings/big_oh.py
                [... tests, ...s wall]
        """

class DocTestWorker(multiprocessing.Process):
    '''
    The DocTestWorker process runs one :class:`DocTestTask` for a given
    source. It returns messages about doctest failures (or all tests if
    verbose doctesting) through a pipe and returns results through a
    ``multiprocessing.Queue`` instance (both these are created in the
    :meth:`start` method).

    It runs the task in its own process-group, such that killing the
    process group kills this process together with its child processes.

    The class has additional methods and attributes for bookkeeping
    by the master process. Except in :meth:`run`, nothing from this
    class should be accessed by the child process.

    INPUT:

    - ``source`` -- a :class:`DocTestSource` instance

    - ``options`` -- an object representing doctest options

    - ``funclist`` -- list of callables to be called at the start of
      the child process

    - ``baseline`` -- dictionary, the ``baseline_stats`` value

    EXAMPLES::

        sage: # long time
        sage: from sage.doctest.forker import DocTestWorker, DocTestTask
        sage: from sage.doctest.sources import FileDocTestSource
        sage: from sage.doctest.reporting import DocTestReporter
        sage: from sage.doctest.control import DocTestController, DocTestDefaults
        sage: filename = sage.doctest.util.__file__
        sage: DD = DocTestDefaults()
        sage: FDS = FileDocTestSource(filename, DD)
        sage: W = DocTestWorker(FDS, DD)
        sage: W.start()
        sage: DC = DocTestController(DD, filename)
        sage: reporter = DocTestReporter(DC)
        sage: W.join()  # Wait for worker to finish
        sage: result = W.result_queue.get()
        sage: reporter.report(FDS, False, W.exitcode, result, "")
            [... tests, ...s wall]
    '''
    source: Incomplete
    options: Incomplete
    funclist: Incomplete
    baseline: Incomplete
    result_queue: Incomplete
    outtmpfile: Incomplete
    messages: str
    killed: bool
    def __init__(self, source, options, funclist=[], baseline=None) -> None:
        """
        Initialization.

        TESTS::

            sage: run_doctests(sage.rings.big_oh) # indirect doctest
            Running doctests with ID ...
            Doctesting 1 file.
            sage -t .../sage/rings/big_oh.py
                [... tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds
            Features detected...
        """
    def run(self) -> None:
        """
        Run the :class:`DocTestTask` under its own PGID.

        TESTS::

            sage: run_doctests(sage.symbolic.units)  # indirect doctest                 # needs sage.symbolic
            Running doctests with ID ...
            Doctesting 1 file.
            sage -t .../sage/symbolic/units.py
                [... tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds
            Features detected...
        """
    def start(self) -> None:
        '''
        Start the worker and close the writing end of the message pipe.

        TESTS::

            sage: # long time
            sage: from sage.doctest.forker import DocTestWorker, DocTestTask
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: filename = sage.doctest.util.__file__
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)
            sage: W = DocTestWorker(FDS, DD)
            sage: W.start()
            sage: try:
            ....:     os.fstat(W.wmessages)
            ....: except OSError:
            ....:     print("Write end of pipe successfully closed")
            Write end of pipe successfully closed
            sage: W.join()  # Wait for worker to finish
        '''
    rmessages: Incomplete
    def read_messages(self) -> None:
        """
        In the master process, read from the pipe and store the data
        read in the ``messages`` attribute.

        .. NOTE::

            This function may need to be called multiple times in
            order to read all of the messages.

        EXAMPLES::

            sage: # long time
            sage: from sage.doctest.forker import DocTestWorker, DocTestTask
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: filename = sage.doctest.util.__file__
            sage: DD = DocTestDefaults(verbose=True,nthreads=2)
            sage: FDS = FileDocTestSource(filename, DD)
            sage: W = DocTestWorker(FDS, DD)
            sage: W.start()
            sage: while W.rmessages is not None:
            ....:     W.read_messages()
            sage: W.join()
            sage: len(W.messages) > 0
            True
        """
    result: Incomplete
    output: Incomplete
    def save_result_output(self) -> None:
        """
        Annotate ``self`` with ``self.result`` (the result read through
        the ``result_queue`` and with ``self.output``, the complete
        contents of ``self.outtmpfile``. Then close the Queue and
        ``self.outtmpfile``.

        EXAMPLES::

            sage: # long time
            sage: from sage.doctest.forker import DocTestWorker, DocTestTask
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: filename = sage.doctest.util.__file__
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)
            sage: W = DocTestWorker(FDS, DD)
            sage: W.start()
            sage: W.join()
            sage: W.save_result_output()
            sage: sorted(W.result[1].keys())
            ['cputime', 'err', 'failures', 'optionals', 'tests', 'walltime', 'walltime_skips']
            sage: len(W.output) > 0
            True

        .. NOTE::

            This method is called from the parent process, not from the
            subprocess.
        """
    def kill(self):
        """
        Kill this worker.  Return ``True`` if the signal(s) are sent
        successfully or ``False`` if the worker process no longer exists.

        This method is only called if there is something wrong with the
        worker. Under normal circumstances, the worker is supposed to
        exit by itself after finishing.

        The first time this is called, use ``SIGQUIT``. This will trigger
        the cysignals ``SIGQUIT`` handler and try to print an enhanced
        traceback.

        Subsequent times, use ``SIGKILL``.  Also close the message pipe
        if it was still open.

        EXAMPLES::

            sage: import time
            sage: from sage.doctest.forker import DocTestWorker, DocTestTask
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: filename = os.path.join(SAGE_SRC,'sage','doctest','tests','99seconds.rst')
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)

        We set up the worker to start by blocking ``SIGQUIT``, such that
        killing will fail initially::

            sage: from cysignals.pselect import PSelecter
            sage: import signal
            sage: def block_hup():
            ....:     # We never __exit__()
            ....:     PSelecter([signal.SIGQUIT]).__enter__()
            sage: W = DocTestWorker(FDS, DD, [block_hup])
            sage: W.start()
            sage: W.killed
            False
            sage: W.kill()
            True
            sage: W.killed
            True
            sage: time.sleep(float(0.2))  # Worker doesn't die
            sage: W.kill()         # Worker dies now
            True
            sage: time.sleep(1)
            sage: W.is_alive()
            False
        """

class DocTestTask:
    """
    This class encapsulates the tests from a single source.

    This class does not insulate from problems in the source
    (e.g. entering an infinite loop or causing a segfault), that has to
    be dealt with at a higher level.

    INPUT:

    - ``source`` -- a :class:`sage.doctest.sources.DocTestSource` instance

    - ``verbose`` -- boolean, controls reporting of progress by :class:`doctest.DocTestRunner`

    EXAMPLES::

        sage: from sage.doctest.forker import DocTestTask
        sage: from sage.doctest.sources import FileDocTestSource
        sage: from sage.doctest.control import DocTestDefaults, DocTestController
        sage: import os
        sage: filename = sage.doctest.sources.__file__
        sage: DD = DocTestDefaults()
        sage: FDS = FileDocTestSource(filename, DD)
        sage: DTT = DocTestTask(FDS)
        sage: DC = DocTestController(DD,[filename])
        sage: ntests, results = DTT(options=DD)
        sage: ntests >= 300 or ntests
        True
        sage: sorted(results.keys())
        ['cputime', 'err', 'failures', 'optionals', 'tests', 'walltime', 'walltime_skips']
    """
    source: Incomplete
    def __init__(self, source) -> None:
        """
        Initialization.

        TESTS::

            sage: from sage.doctest.forker import DocTestTask
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults
            sage: import os
            sage: filename = sage.doctest.sources.__file__
            sage: FDS = FileDocTestSource(filename, DocTestDefaults())
            sage: DocTestTask(FDS)
            <sage.doctest.forker.DocTestTask object at ...>
        """
    def __call__(self, options, outtmpfile=None, msgfile=None, result_queue=None, *, baseline=None):
        """
        Calling the task does the actual work of running the doctests.

        INPUT:

        - ``options`` -- an object representing doctest options

        - ``outtmpfile`` -- a seekable file that's used by the doctest
          runner to redirect stdout and stderr of the doctests

        - ``msgfile`` -- a file or pipe to send doctest messages about
          doctest failures (or all tests in verbose mode)

        - ``result_queue`` -- an instance of :class:`multiprocessing.Queue`
          to store the doctest result. For testing, this can also be ``None``

        - ``baseline`` -- dictionary, the ``baseline_stats`` value

        OUTPUT:

        - ``(doctests, result_dict)`` where ``doctests`` is the number of
          doctests and ``result_dict`` is a dictionary annotated with
          timings and error information.

        - Also put ``(doctests, result_dict)`` onto the ``result_queue``
          if the latter isn't None.

        EXAMPLES::

            sage: from sage.doctest.forker import DocTestTask
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: import os
            sage: filename = sage.doctest.parsing.__file__
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)
            sage: DTT = DocTestTask(FDS)
            sage: DC = DocTestController(DD, [filename])
            sage: ntests, runner = DTT(options=DD)
            sage: runner.failures
            0
            sage: ntests >= 200 or ntests
            True
        """
