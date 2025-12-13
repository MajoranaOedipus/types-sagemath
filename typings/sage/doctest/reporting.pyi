from _typeshed import Incomplete
from sage.doctest.external import available_software as available_software
from sage.doctest.sources import DictAsObject as DictAsObject
from sage.doctest.util import count_noun as count_noun
from sage.structure.sage_object import SageObject as SageObject
from signal import Signals

def signal_name(sig: int | Signals) -> str:
    """
    Return a string describing a signal number.

    EXAMPLES::

        sage: from signal import SIGSEGV
        sage: from sage.doctest.reporting import signal_name
        sage: signal_name(SIGSEGV)
        'segmentation fault'
        sage: signal_name(9)
        'kill signal'
        sage: signal_name(12345)
        'signal 12345'
    """

class DocTestReporter(SageObject):
    """
    This class reports to the users on the results of doctests.
    """
    controller: Incomplete
    postscript: Incomplete
    sources_completed: int
    stats: Incomplete
    error_status: int
    def __init__(self, controller) -> None:
        """
        Initialize the reporter.

        INPUT:

        - ``controller`` -- a
          :class:`sage.doctest.control.DocTestController` instance;
          Note that some methods assume that appropriate tests have
          been run by the controller

        EXAMPLES::

            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: filename = sage.doctest.reporting.__file__
            sage: DC = DocTestController(DocTestDefaults(), [filename])
            sage: DTR = DocTestReporter(DC)
        """
    def were_doctests_with_optional_tag_run(self, tag):
        """
        Return whether doctests marked with this tag were run.

        INPUT:

        - ``tag`` -- string

        EXAMPLES::

            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: filename = sage.doctest.reporting.__file__
            sage: DC = DocTestController(DocTestDefaults(), [filename])
            sage: DTR = DocTestReporter(DC)

        ::

            sage: DTR.were_doctests_with_optional_tag_run('sage')
            True
            sage: DTR.were_doctests_with_optional_tag_run('nice_unavailable_package')
            False

        When latex is available, doctests marked with optional tag
        ``latex`` are run by default since :issue:`32174`::

            sage: # needs SAGE_SRC
            sage: filename = os.path.join(SAGE_SRC, 'sage', 'misc', 'latex.py')
            sage: DC = DocTestController(DocTestDefaults(), [filename])
            sage: DTR = DocTestReporter(DC)
            sage: DTR.were_doctests_with_optional_tag_run('latex')   # optional - latex
            True
        """
    def report_head(self, source, fail_msg=None):
        '''
        Return the ``sage -t [options] file.py`` line as string.

        INPUT:

        - ``source`` -- a source from :mod:`sage.doctest.sources`

        - ``fail_msg`` -- ``None`` or a string

        EXAMPLES::

            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: filename = sage.doctest.reporting.__file__
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)
            sage: DC = DocTestController(DD, [filename])
            sage: DTR = DocTestReporter(DC)
            sage: print(DTR.report_head(FDS))
            sage -t .../sage/doctest/reporting.py

        The same with various options::

            sage: DD.long = True
            sage: print(DTR.report_head(FDS))
            sage -t --long .../sage/doctest/reporting.py
            sage: print(DTR.report_head(FDS, "Failed by self-sabotage"))
            sage -t --long .../sage/doctest/reporting.py  # Failed by self-sabotage
        '''
    def report(self, source, timeout, return_code, results, output, pid=None) -> None:
        '''
        Report on the result of running doctests on a given source.

        This doesn\'t print the :meth:`report_head`, which is assumed
        to be printed already.

        INPUT:

        - ``source`` -- a source from :mod:`sage.doctest.sources`

        - ``timeout`` -- boolean; whether doctests timed out

        - ``return_code`` -- integer; the return code of the process
          running doctests on that file

        - ``results`` -- (irrelevant if ``timeout`` or ``return_code``) a tuple

          - ``ntests`` -- the number of doctests

          - ``timings`` -- a
            :class:`sage.doctest.sources.DictAsObject` instance
            storing timing data

        - ``output`` -- string; printed if there was some kind of failure

        - ``pid`` -- integer (default: ``None``); the pid of the worker process

        EXAMPLES::

            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource, DictAsObject
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.util import Timer
            sage: import doctest
            sage: filename = sage.doctest.reporting.__file__
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)
            sage: DC = DocTestController(DD, [filename])
            sage: DTR = DocTestReporter(DC)

        You can report a timeout::

            sage: DTR.report(FDS, True, 0, None, "Output so far...", pid=1234)
                Timed out
            **********************************************************************
            Tests run before process (pid=1234) timed out:
            Output so far...
            **********************************************************************
            sage: DTR.stats
            {\'sage.doctest.reporting\': {\'failed\': True,
                                        \'ntests\': 0,
                                        \'walltime\': 1000000.0}}

        Or a process that returned a bad exit code::

            sage: DTR.report(FDS, False, 3, None, "Output before trouble")
                Bad exit: 3
            **********************************************************************
            Tests run before process failed:
            Output before trouble
            **********************************************************************
            sage: DTR.stats
            {\'sage.doctest.reporting\': {\'failed\': True,
                                        \'ntests\': 0,
                                        \'walltime\': 1000000.0}}

        Or a process that segfaulted::

            sage: from signal import SIGSEGV
            sage: DTR.report(FDS, False, -SIGSEGV, None, "Output before trouble")
                Killed due to segmentation fault
            **********************************************************************
            Tests run before process failed:
            Output before trouble
            **********************************************************************
            sage: DTR.stats
            {\'sage.doctest.reporting\': {\'failed\': True,
                                        \'ntests\': 0,
                                        \'walltime\': 1000000.0}}

        Report a timeout with results and a ``SIGKILL``::

            sage: from signal import SIGKILL
            sage: DTR.report(FDS, True, -SIGKILL, (1,None), "Output before trouble")
                Timed out after testing finished (and interrupt failed)
            **********************************************************************
            Tests run before process timed out:
            Output before trouble
            **********************************************************************
            sage: DTR.stats
            {\'sage.doctest.reporting\': {\'failed\': True,
                                        \'ntests\': 1,
                                        \'walltime\': 1000000.0}}

        This is an internal error since results is None::

            sage: DTR.report(FDS, False, 0, None, "All output")
                Error in doctesting framework (bad result returned)
            **********************************************************************
            Tests run before error:
            All output
            **********************************************************************
            sage: DTR.stats
            {\'sage.doctest.reporting\': {\'failed\': True,
                                        \'ntests\': 1,
                                        \'walltime\': 1000000.0}}

        Or tell the user that everything succeeded::

            sage: doctests, extras = FDS.create_doctests(globals())
            sage: runner = SageDocTestRunner(
            ....:     SageOutputChecker(), verbose=False, sage_options=DD,
            ....:     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: Timer().start().stop().annotate(runner)
            sage: D = DictAsObject({\'err\':None})
            sage: runner.update_results(D)
            0
            sage: DTR.report(FDS, False, 0, (sum([len(t.examples) for t in doctests]), D),
            ....:            "Good tests")
                [... tests, ...s wall]
            sage: DTR.stats
            {\'sage.doctest.reporting\': {\'ntests\': ..., \'walltime\': ...}}

        Or inform the user that some doctests failed::

            sage: runner.failures = 1
            sage: runner.update_results(D)
            1
            sage: DTR.report(FDS, False, 0, (sum([len(t.examples) for t in doctests]), D),
            ....:            "Doctest output including the failure...")
                [... tests, 1 failure, ...s wall]

        If the user has requested that we report on skipped doctests,
        we do so::

            sage: DC.options = DocTestDefaults(show_skipped=True)
            sage: from collections import defaultdict
            sage: optionals = defaultdict(int)
            sage: optionals[\'magma\'] = 5; optionals[\'long time\'] = 4; optionals[\'\'] = 1; optionals[\'not tested\'] = 2
            sage: D = DictAsObject(dict(err=None, optionals=optionals))
            sage: runner.failures = 0
            sage: runner.update_results(D)
            0
            sage: DTR.report(FDS, False, 0, (sum([len(t.examples) for t in doctests]), D), "Good tests")
                1 unlabeled test not run
                4 long tests not run
                5 magma tests not run
                2 not tested tests not run
                0 tests not run because we ran out of time
                [... tests, ...s wall]

        Test an internal error in the reporter::

            sage: DTR.report(None, None, None, None, None)
            Traceback (most recent call last):
            ...
            AttributeError: \'NoneType\' object has no attribute \'basename\'...

        The only-errors mode does not output anything on success::

            sage: DD = DocTestDefaults(only_errors=True)
            sage: FDS = FileDocTestSource(filename, DD)
            sage: DC = DocTestController(DD, [filename])
            sage: DTR = DocTestReporter(DC)
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: runner = SageDocTestRunner(
            ....:     SageOutputChecker(), verbose=False, sage_options=DD,
            ....:     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: Timer().start().stop().annotate(runner)
            sage: D = DictAsObject({\'err\':None})
            sage: runner.update_results(D)
            0
            sage: DTR.report(FDS, False, 0, (sum([len(t.examples) for t in doctests]), D),
            ....:            "Good tests")

        However, failures are still output in the errors-only mode::

            sage: runner.failures = 1
            sage: runner.update_results(D)
            1
            sage: DTR.report(FDS, False, 0, (sum([len(t.examples) for t in doctests]), D),
            ....:            "Failed test")
                [... tests, 1 failure, ...s wall]
        '''
    def finalize(self) -> None:
        '''
        Print out the postscript that summarizes the doctests that were run.

        EXAMPLES:

        First we have to set up a bunch of stuff::

            sage: from sage.doctest.reporting import DocTestReporter
            sage: from sage.doctest.control import DocTestController, DocTestDefaults
            sage: from sage.doctest.sources import FileDocTestSource, DictAsObject
            sage: from sage.doctest.forker import SageDocTestRunner
            sage: from sage.doctest.parsing import SageOutputChecker
            sage: from sage.doctest.util import Timer
            sage: import doctest
            sage: filename = sage.doctest.reporting.__file__
            sage: DD = DocTestDefaults()
            sage: FDS = FileDocTestSource(filename, DD)
            sage: DC = DocTestController(DD, [filename])
            sage: DTR = DocTestReporter(DC)

        Now we pretend to run some doctests::

            sage: DTR.report(FDS, True, 0, None, "Output so far...", pid=1234)
                Timed out
            **********************************************************************
            Tests run before process (pid=1234) timed out:
            Output so far...
            **********************************************************************
            sage: DTR.report(FDS, False, 3, None, "Output before bad exit")
                Bad exit: 3
            **********************************************************************
            Tests run before process failed:
            Output before bad exit
            **********************************************************************
            sage: doctests, extras = FDS.create_doctests(globals())
            sage: runner = SageDocTestRunner(
            ....:     SageOutputChecker(), verbose=False, sage_options=DD,
            ....:     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
            sage: t = Timer().start().stop()
            sage: t.annotate(runner)
            sage: DC.timer = t
            sage: D = DictAsObject({\'err\':None})
            sage: runner.update_results(D)
            0
            sage: DTR.report(FDS, False, 0, (sum([len(t.examples) for t in doctests]), D),
            ....:            "Good tests")
                [... tests, ...s wall]
            sage: runner.failures = 1
            sage: runner.update_results(D)
            1
            sage: DTR.report(FDS, False, 0, (sum([len(t.examples) for t in doctests]), D),
            ....:            "Doctest output including the failure...")
                [... tests, 1 failure, ...s wall]

        Now we can show the output of finalize::

            sage: DC.sources = [None] * 4 # to fool the finalize method
            sage: DTR.finalize()
            ----------------------------------------------------------------------
            sage -t .../sage/doctest/reporting.py  # Timed out
            sage -t .../sage/doctest/reporting.py  # Bad exit: 3
            sage -t .../sage/doctest/reporting.py  # 1 doctest failed
            ----------------------------------------------------------------------
            Total time for all tests: 0.0 seconds
                cpu time: 0.0 seconds
                cumulative wall time: 0.0 seconds

        If we interrupted doctests, then the number of files tested
        will not match the number of sources on the controller::

            sage: DC.sources = [None] * 6
            sage: DTR.finalize()
            <BLANKLINE>
            ----------------------------------------------------------------------
            sage -t .../sage/doctest/reporting.py  # Timed out
            sage -t .../sage/doctest/reporting.py  # Bad exit: 3
            sage -t .../sage/doctest/reporting.py  # 1 doctest failed
            Doctests interrupted: 4/6 files tested
            ----------------------------------------------------------------------
            Total time for all tests: 0.0 seconds
                cpu time: 0.0 seconds
                cumulative wall time: 0.0 seconds
        '''
