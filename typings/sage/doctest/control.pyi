from _typeshed import Incomplete
from sage.doctest.external import available_software as available_software
from sage.doctest.forker import DocTestDispatcher as DocTestDispatcher
from sage.doctest.parsing import optional_tag_regex as optional_tag_regex, parse_file_optional_tags as parse_file_optional_tags, unparse_optional_tags as unparse_optional_tags
from sage.doctest.reporting import DocTestReporter as DocTestReporter
from sage.doctest.sources import DictAsObject as DictAsObject, FileDocTestSource as FileDocTestSource, get_basename as get_basename
from sage.doctest.util import Timer as Timer, count_noun as count_noun, dict_difference as dict_difference
from sage.env import DOT_SAGE as DOT_SAGE, SAGE_EXTCODE as SAGE_EXTCODE, SAGE_LIB as SAGE_LIB, SAGE_SRC as SAGE_SRC
from sage.misc import randstate as randstate
from sage.misc.temporary_file import tmp_dir as tmp_dir
from sage.structure.sage_object import SageObject as SageObject

auto_optional_tags: Incomplete

class DocTestDefaults(SageObject):
    """
    This class is used for doctesting the Sage doctest module.

    INPUT:

    - ``runtest_default`` -- (boolean, default ``False``); if ``True``,
      fills in attribute to be the same as the defaults defined in
      ``sage-runtests``. If ``False``, change defaults in a few places
      for use in doctests of the doctester, which is mostly to make
      doctesting more predictable.

    - ``**kwds`` -- attributes to override defaults

    EXAMPLES::

        sage: from sage.doctest.control import DocTestDefaults
        sage: D = DocTestDefaults(); D
        DocTestDefaults()
        sage: D.timeout
        -1

    Keyword arguments become attributes::

        sage: D = DocTestDefaults(timeout=100); D
        DocTestDefaults(timeout=100)
        sage: D.timeout
        100

    The defaults for ``sage-runtests``::

        sage: D = DocTestDefaults(runtest_default=True); D
        DocTestDefaults(abspath=False, file_iterations=0, global_iterations=0,
                        optional='sage,optional', random_seed=None,
                        stats_path='.../timings2.json')
    """
    nthreads: int
    serial: bool
    timeout: int
    die_timeout: int
    all: bool
    installed: bool
    logfile: Incomplete
    long: bool
    warn_long: float
    randorder: Incomplete
    random_seed: Incomplete
    global_iterations: Incomplete
    file_iterations: Incomplete
    environment: str
    initial: bool
    exitfirst: bool
    force_lib: bool
    if_installed: bool
    abspath: Incomplete
    verbose: bool
    debug: bool
    only_errors: bool
    gdb: bool
    lldb: bool
    valgrind: bool
    massif: bool
    cachegrind: bool
    omega: bool
    failed: bool
    new: bool
    show_skipped: bool
    target_walltime: int
    baseline_stats_path: Incomplete
    format: str
    optional: Incomplete
    hide: str
    probe: str
    gc: int
    stats_path: Incomplete
    def __init__(self, runtest_default: bool = False, **kwds) -> None:
        """
        Edit these parameters after creating an instance.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: D = DocTestDefaults()
            sage: 'sage' in D.optional
            True
        """
    def __eq__(self, other):
        """
        Comparison by __dict__.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: DD1 = DocTestDefaults(long=True)
            sage: DD2 = DocTestDefaults(long=True)
            sage: DD1 == DD2
            True
        """
    def __ne__(self, other):
        """
        Test for non-equality.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults
            sage: DD1 = DocTestDefaults(long=True)
            sage: DD2 = DocTestDefaults(long=True)
            sage: DD1 != DD2
            False
        """

def skipdir(dirname) -> bool:
    '''
    Return ``True`` if and only if the directory ``dirname`` should not be
    doctested.

    EXAMPLES::

        sage: from sage.doctest.control import skipdir
        sage: skipdir(sage.env.SAGE_SRC)
        False
        sage: skipdir(os.path.join(sage.env.SAGE_SRC, "sage", "doctest", "tests"))
        True
    '''
def skipfile(filename, tested_optional_tags: bool = False, *, if_installed: bool = False, log=None):
    '''
    Return ``True`` if and only if the file ``filename`` should not be doctested.

    INPUT:

    - ``filename`` -- name of a file

    - ``tested_optional_tags`` -- list or tuple or set of optional tags to test,
      or ``False`` (no optional test) or ``True`` (all optional tests)

    - ``if_installed`` -- boolean (default: ``False``); whether to skip Python/Cython files
      that are not installed as modules

    - ``log`` -- function to call with log messages, or ``None``

    If ``filename`` contains a line of the form ``"# sage.doctest:
    optional - xyz")``, then this will return ``False`` if "xyz" is in
    ``tested_optional_tags``. Otherwise, it returns the matching tag
    ("optional - xyz").

    EXAMPLES::

        sage: from sage.doctest.control import skipfile
        sage: skipfile("skipme.c")
        True
        sage: filename = tmp_filename(ext=\'.pyx\')
        sage: skipfile(filename)
        False
        sage: with open(filename, "w") as f:
        ....:     _ = f.write("# nodoctest")
        sage: skipfile(filename)
        True
        sage: with open(filename, "w") as f:
        ....:     _ = f.write("# sage.doctest: "    # broken in two source lines to avoid the pattern
        ....:                 "optional - xyz")     # of relint (multiline_doctest_comment)
        sage: skipfile(filename, False)
        \'optional - xyz\'
        sage: bool(skipfile(filename, False))
        True
        sage: skipfile(filename, [\'abc\'])
        \'optional - xyz\'
        sage: skipfile(filename, [\'abc\', \'xyz\'])
        False
        sage: skipfile(filename, True)
        False
    '''

class Logger:
    '''
    File-like object which implements writing to multiple files at
    once.

    EXAMPLES::

        sage: from sage.doctest.control import Logger
        sage: with open(tmp_filename(), "w+") as t:
        ....:     L = Logger(sys.stdout, t)
        ....:     _ = L.write("hello world\\n")
        ....:     _ = t.seek(0)
        ....:     t.read()
        hello world
        \'hello world\\n\'
    '''
    files: Incomplete
    def __init__(self, *files) -> None:
        '''
        Initialize the logger for writing to all files in ``files``.

        TESTS::

            sage: from sage.doctest.control import Logger
            sage: Logger().write("hello world\\n")  # no-op
        '''
    def write(self, x) -> None:
        '''
        Write ``x`` to all files.

        TESTS::

            sage: from sage.doctest.control import Logger
            sage: Logger(sys.stdout).write("hello world\\n")
            hello world
        '''
    def flush(self) -> None:
        """
        Flush all files.

        TESTS::

            sage: from sage.doctest.control import Logger
            sage: Logger(sys.stdout).flush()
        """

class DocTestController(SageObject):
    """
    This class controls doctesting of files.

    After creating it with appropriate options, call the :meth:`run` method to run the doctests.
    """
    options: Incomplete
    files: Incomplete
    logfile: Incomplete
    logger: Incomplete
    stats: Incomplete
    baseline_stats: Incomplete
    def __init__(self, options, args) -> None:
        """
        Initialization.

        INPUT:

        - ``options`` -- either options generated from the command line by sage-runtests
          or a DocTestDefaults object (possibly with some entries modified)
        - ``args`` -- list of filenames to doctest

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: DC = DocTestController(DocTestDefaults(), [])
            sage: DC
            DocTest Controller
        """
    def __del__(self) -> None: ...
    def load_environment(self):
        """
        Return the module that provides the global environment.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: DC = DocTestController(DocTestDefaults(), [])
            sage: 'BipartiteGraph' in DC.load_environment().__dict__
            True
            sage: DC = DocTestController(DocTestDefaults(environment='sage.doctest.all'), [])
            sage: 'BipartiteGraph' in  DC.load_environment().__dict__
            False
            sage: 'run_doctests' in DC.load_environment().__dict__
            True
        """
    def load_baseline_stats(self, filename) -> None:
        '''
        Load baseline stats.

        This must be a JSON file in the same format that :meth:`load_stats`
        expects.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: DC = DocTestController(DocTestDefaults(), [])
            sage: import json
            sage: filename = tmp_filename()
            sage: with open(filename, \'w\') as stats_file:
            ....:     json.dump({\'sage.doctest.control\':{\'failed\':True}}, stats_file)
            sage: DC.load_baseline_stats(filename)
            sage: DC.baseline_stats[\'sage.doctest.control\']
            {\'failed\': True}

        If the file doesn\'t exist, nothing happens. If there is an
        error, print a message. In any case, leave the stats alone::

            sage: d = tmp_dir()
            sage: DC.load_baseline_stats(os.path.join(d))  # Cannot read a directory
            Error loading baseline stats from ...
            sage: DC.load_baseline_stats(os.path.join(d, "no_such_file"))
            sage: DC.baseline_stats[\'sage.doctest.control\']
            {\'failed\': True}
        '''
    def load_stats(self, filename) -> None:
        '''
        Load stats from the most recent run(s).

        Stats are stored as a JSON file, and include information on
        which files failed tests and the walltime used for execution
        of the doctests.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: DC = DocTestController(DocTestDefaults(), [])
            sage: import json
            sage: filename = tmp_filename()
            sage: with open(filename, \'w\') as stats_file:
            ....:     json.dump({\'sage.doctest.control\': {\'walltime\': 1.0r}}, stats_file)
            sage: DC.load_stats(filename)
            sage: DC.stats[\'sage.doctest.control\']
            {\'walltime\': 1.0}

        If the file doesn\'t exist, nothing happens. If there is an
        error, print a message. In any case, leave the stats alone::

            sage: d = tmp_dir()
            sage: DC.load_stats(os.path.join(d))  # Cannot read a directory
            Error loading stats from ...
            sage: DC.load_stats(os.path.join(d, "no_such_file"))
            sage: DC.stats[\'sage.doctest.control\']
            {\'walltime\': 1.0}
        '''
    def save_stats(self, filename) -> None:
        """
        Save stats from the most recent run as a JSON file.

        WARNING: This function overwrites the file.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: DC = DocTestController(DocTestDefaults(), [])
            sage: DC.stats['sage.doctest.control'] = {'walltime': 1.0r}
            sage: filename = tmp_filename()
            sage: DC.save_stats(filename)
            sage: import json
            sage: with open(filename) as f:
            ....:     D = json.load(f)
            sage: D['sage.doctest.control']
            {'walltime': 1.0}
        """
    def log(self, s, end: str = '\n') -> None:
        '''
        Log the string ``s + end`` (where ``end`` is a newline by default)
        to the logfile and print it to the standard output.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: DD = DocTestDefaults(logfile=tmp_filename())
            sage: DC = DocTestController(DD, [])
            sage: DC.log("hello world")
            hello world
            sage: DC.logfile.close()
            sage: with open(DD.logfile) as f:
            ....:     print(f.read())
            hello world

        In serial mode, check that logging works even if ``stdout`` is
        redirected::

            sage: DD = DocTestDefaults(logfile=tmp_filename(), serial=True)
            sage: DC = DocTestController(DD, [])
            sage: from sage.doctest.forker import SageSpoofInOut
            sage: with open(os.devnull, \'w\') as devnull:
            ....:     S = SageSpoofInOut(devnull)
            ....:     S.start_spoofing()
            ....:     DC.log("hello world")
            ....:     S.stop_spoofing()
            hello world
            sage: DC.logfile.close()
            sage: with open(DD.logfile) as f:
            ....:     print(f.read())
            hello world

        Check that no duplicate logs appear, even when forking (:issue:`15244`)::

            sage: DD = DocTestDefaults(logfile=tmp_filename())
            sage: DC = DocTestController(DD, [])
            sage: DC.log("hello world")
            hello world
            sage: if os.fork() == 0:
            ....:     DC.logfile.close()
            ....:     os._exit(0)
            sage: DC.logfile.close()
            sage: with open(DD.logfile) as f:
            ....:     print(f.read())
            hello world
        '''
    run_id: Incomplete
    def create_run_id(self) -> None:
        """
        Create the run id.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: DC = DocTestController(DocTestDefaults(), [])
            sage: DC.create_run_id()
            Running doctests with ID ...
        """
    def add_files(self):
        """
        Check for the flags '--all' and '--new'.

        For each one present, this function adds the appropriate directories and files to the todo list.

        EXAMPLES::

            sage: from sage.doctest.control import (DocTestDefaults,
            ....:                                   DocTestController)
            sage: from sage.env import SAGE_SRC
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile() as f:
            ....:     DD = DocTestDefaults(all=True, logfile=f.name)
            ....:     DC = DocTestController(DD, [])
            ....:     DC.add_files()
            Doctesting ...
            sage: os.path.join(SAGE_SRC, 'sage') in DC.files
            True

        ::

            sage: DD = DocTestDefaults(new = True)
            sage: DC = DocTestController(DD, [])
            sage: DC.add_files()
            Doctesting ...
        """
    sources: Incomplete
    def expand_files_into_sources(self) -> None:
        '''
        Expand ``self.files``, which may include directories, into a
        list of :class:`sage.doctest.FileDocTestSource`

        This function also handles the optional command line option.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: from sage.env import SAGE_SRC
            sage: import os
            sage: dirname = os.path.join(SAGE_SRC, \'sage\', \'doctest\')
            sage: DD = DocTestDefaults(optional=\'all\')
            sage: DC = DocTestController(DD, [dirname])
            sage: DC.expand_files_into_sources()
            sage: len(DC.sources)
            15
            sage: DC.sources[0].options.optional
            True

        ::

            sage: DD = DocTestDefaults(optional=\'magma,guava\')
            sage: DC = DocTestController(DD, [dirname])
            sage: DC.expand_files_into_sources()
            sage: all(t in DC.sources[0].options.optional for t in [\'magma\',\'guava\'])
            True

        We check that files are skipped appropriately::

            sage: dirname = tmp_dir()
            sage: filename = os.path.join(dirname, \'not_tested.py\')
            sage: with open(filename, \'w\') as f:
            ....:     _ = f.write("#"*80 + "\\n\\n\\n\\n## nodoctest\\n    sage: 1+1\\n    4")
            sage: DC = DocTestController(DD, [dirname])
            sage: DC.expand_files_into_sources()
            sage: DC.sources
            []

        The directory ``sage/doctest/tests`` contains ``nodoctest.py``
        but the files should still be tested when that directory is
        explicitly given (as opposed to being recursed into)::

            sage: DC = DocTestController(DD, [os.path.join(SAGE_SRC, \'sage\', \'doctest\', \'tests\')])
            sage: DC.expand_files_into_sources()
            sage: len(DC.sources) >= 10
            True
        '''
    def filter_sources(self):
        """

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: from sage.env import SAGE_SRC
            sage: import os
            sage: dirname = os.path.join(SAGE_SRC, 'sage', 'doctest')
            sage: DD = DocTestDefaults(failed=True)
            sage: DC = DocTestController(DD, [dirname])
            sage: DC.expand_files_into_sources()
            sage: for i, source in enumerate(DC.sources):
            ....:     DC.stats[source.basename] = {'walltime': 0.1r * (i+1)}
            sage: DC.stats['sage.doctest.control'] = {'failed': True, 'walltime': 1.0r}
            sage: DC.filter_sources()
            Only doctesting files that failed last test.
            sage: len(DC.sources)
            1
        """
    def sort_sources(self):
        '''
        This function sorts the sources so that slower doctests are run first.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: from sage.env import SAGE_SRC
            sage: import os
            sage: dirname = os.path.join(SAGE_SRC, \'sage\', \'doctest\')
            sage: DD = DocTestDefaults(nthreads=2)
            sage: DC = DocTestController(DD, [dirname])
            sage: DC.expand_files_into_sources()
            sage: DC.sources.sort(key=lambda s:s.basename)
            sage: for i, source in enumerate(DC.sources):
            ....:     DC.stats[source.basename] = {\'walltime\': 0.1r * (i+1)}
            sage: DC.sort_sources()
            Sorting sources by runtime so that slower doctests are run first....
            sage: print("\\n".join(source.basename for source in DC.sources))
            sage.doctest.util
            sage.doctest.test
            sage.doctest.sources
            sage.doctest.rif_tol
            sage.doctest.reporting
            sage.doctest.parsing_test
            sage.doctest.parsing
            sage.doctest.marked_output
            sage.doctest.forker
            sage.doctest.fixtures
            sage.doctest.external
            sage.doctest.control
            sage.doctest.check_tolerance
            sage.doctest.all
            sage.doctest
        '''
    def source_baseline(self, source):
        """
        Return the ``baseline_stats`` value of ``source``.

        INPUT:

        - ``source`` -- a :class:`DocTestSource` instance

        OUTPUT: a dictionary

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: filename = sage.doctest.util.__file__
            sage: DD = DocTestDefaults()
            sage: DC = DocTestController(DD, [filename])
            sage: DC.expand_files_into_sources()
            sage: DC.source_baseline(DC.sources[0])
            {}
        """
    reporter: Incomplete
    dispatcher: Incomplete
    timer: Incomplete
    def run_doctests(self) -> None:
        """
        Actually run the doctests.

        This function is called by :meth:`run`.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: from sage.env import SAGE_SRC
            sage: import os
            sage: dirname = os.path.join(SAGE_SRC, 'sage', 'rings', 'homset.py')
            sage: DD = DocTestDefaults()
            sage: DC = DocTestController(DD, [dirname])
            sage: DC.expand_files_into_sources()
            sage: DC.run_doctests()
            Doctesting 1 file.
            sage -t .../sage/rings/homset.py
                [... tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds...
        """
    def cleanup(self, final: bool = True) -> None:
        """
        Run cleanup activities after actually running doctests.

        In particular, saves the stats to disk and closes the logfile.

        INPUT:

        - ``final`` -- whether to close the logfile

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: from sage.env import SAGE_SRC
            sage: import os
            sage: dirname = os.path.join(SAGE_SRC, 'sage', 'rings', 'all.py')
            sage: DD = DocTestDefaults()

            sage: DC = DocTestController(DD, [dirname])
            sage: DC.expand_files_into_sources()
            sage: DC.sources.sort(key=lambda s:s.basename)

            sage: for i, source in enumerate(DC.sources):
            ....:     DC.stats[source.basename] = {'walltime': 0.1r * (i+1)}
            ....:

            sage: DC.run()
            Running doctests with ID ...
            Doctesting 1 file.
            sage -t .../rings/all.py
                [... tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds
            Features detected...
            0
            sage: DC.cleanup()
        """
    def run_val_gdb(self, testing: bool = False):
        '''
        Spawns a subprocess to run tests under the control of gdb, lldb, or valgrind.

        INPUT:

        - ``testing`` -- boolean (default: ``False``); if ``True`` then the
          command to be run will be printed rather than a subprocess started

        EXAMPLES:

        Note that the command lines include unexpanded environment
        variables. It is safer to let the shell expand them than to
        expand them here and risk insufficient quoting. ::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: DD = DocTestDefaults(gdb=True)
            sage: DC = DocTestController(DD, ["hello_world.py"])
            sage: DC.run_val_gdb(testing=True)
            exec gdb --eval-command="run" --args ...python... -m sage.doctest --serial... --timeout=0... hello_world.py

        ::

            sage: DD = DocTestDefaults(valgrind=True, optional=\'all\', timeout=172800)
            sage: DC = DocTestController(DD, ["hello_world.py"])
            sage: DC.run_val_gdb(testing=True)
            exec valgrind --tool=memcheck --leak-resolution=high --leak-check=full --num-callers=25 --suppressions=.../valgrind/pyalloc.supp --suppressions=.../valgrind/sage.supp --suppressions=.../valgrind/sage-additional.supp --suppressions=.../valgrind/valgrind-python.supp  --log-file=.../valgrind/sage-memcheck.%p ...python... -m sage.doctest --serial... --timeout=172800... --optional=all hello_world.py
        '''
    def run(self):
        '''
        This function is called after initialization to set up and run all doctests.

        EXAMPLES::

            sage: from sage.doctest.control import DocTestDefaults, DocTestController
            sage: from sage.env import SAGE_SRC
            sage: import os
            sage: DD = DocTestDefaults()
            sage: filename = os.path.join(SAGE_SRC, "sage", "sets", "non_negative_integers.py")
            sage: DC = DocTestController(DD, [filename])
            sage: DC.run()
            Running doctests with ID ...
            Doctesting 1 file.
            sage -t .../sage/sets/non_negative_integers.py
                [... tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds
            Features detected...
            0

        We check that :issue:`25378` is fixed (testing external packages
        while providing a logfile does not raise a ValueError: I/O
        operation on closed file)::

            sage: logfile = tmp_filename(ext=\'.log\')
            sage: DD = DocTestDefaults(optional=set([\'sage\', \'external\']), logfile=logfile)
            sage: filename = tmp_filename(ext=\'.py\')
            sage: DC = DocTestController(DD, [filename])
            sage: DC.run()
            Running doctests with ID ...
            Using --optional=external,sage
            Features to be detected: ...
            Doctesting 1 file.
            sage -t ....py
                [0 tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds
            Features detected...
            0

        We test the ``--hide`` option (:issue:`34185`)::

            sage: from sage.doctest.control import test_hide
            sage: filename = tmp_filename(ext=\'.py\')
            sage: with open(filename, \'w\') as f:
            ....:     f.write(test_hide)
            ....:     f.close()
            714
            sage: DF = DocTestDefaults(hide=\'buckygen,all\')
            sage: DC = DocTestController(DF, [filename])
            sage: DC.run()
            Running doctests with ID ...
            Using --optional=sage...
            Features to be detected: ...
            Doctesting 1 file.
            sage -t ....py
                [4 tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds
            Features detected...
            0

            sage: DF = DocTestDefaults(hide=\'benzene,optional\')
            sage: DC = DocTestController(DF, [filename])
            sage: DC.run()
            Running doctests with ID ...
            Using --optional=sage
            Features to be detected: ...
            Doctesting 1 file.
            sage -t ....py
                [4 tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds
            Features detected...
            0

        Test *Features that have been hidden* message::

            sage: DC.run()                              # optional - meataxe
            Running doctests with ID ...
            Using --optional=sage
            Features to be detected: ...
            Doctesting 1 file.
            sage -t ....py
                [4 tests, ...s wall]
            ----------------------------------------------------------------------
            All tests passed!
            ----------------------------------------------------------------------
            Total time for all tests: ... seconds
                cpu time: ... seconds
                cumulative wall time: ... seconds
            Features detected...
            Features that have been hidden: ...meataxe...
            0
        '''

def run_doctests(module, options=None):
    """
    Run the doctests in a given file.

    INPUT:

    - ``module`` -- a Sage module, a string, or a list of such

    - ``options`` -- a DocTestDefaults object or ``None``

    EXAMPLES::

        sage: run_doctests(sage.rings.all)
        Running doctests with ID ...
        Doctesting 1 file.
        sage -t .../sage/rings/all.py
            [... tests, ...s wall]
        ----------------------------------------------------------------------
        All tests passed!
        ----------------------------------------------------------------------
        Total time for all tests: ... seconds
            cpu time: ... seconds
            cumulative wall time: ... seconds
        Features detected...
    """

test_hide: Incomplete
