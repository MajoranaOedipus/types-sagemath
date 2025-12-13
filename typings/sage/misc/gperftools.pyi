from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.sage_object import SageObject as SageObject

libc: Incomplete
libprofiler: Incomplete

class Profiler(SageObject):
    def __init__(self, filename=None) -> None:
        """
        Interface to the gperftools profiler.

        INPUT:

        - ``filename`` -- string or ``None`` (default). The file name
          to log to. By default, a new temporary file is created.

        EXAMPLES::

            sage: from sage.misc.gperftools import Profiler
            sage: Profiler()
            Profiler logging to ...
        """
    def filename(self) -> str:
        """
        Return the file name.

        OUTPUT: string

        EXAMPLES::

            sage: from sage.misc.gperftools import Profiler
            sage: prof = Profiler()
            sage: prof.filename()
            '.../tmp_....perf'
        """
    def start(self) -> None:
        """
        Start profiling.

        EXAMPLES::

            sage: from sage.misc.gperftools import Profiler, run_100ms
            sage: prof = Profiler()
            sage: prof.start()    # optional - gperftools
            sage: run_100ms()
            sage: prof.stop()     # optional - gperftools
            PROFILE: interrupts/evictions/bytes = ...
        """
    def stop(self) -> None:
        """
        Stop the CPU profiler.

        EXAMPLES::

            sage: from sage.misc.gperftools import Profiler, run_100ms
            sage: prof = Profiler()
            sage: prof.start()    # optional - gperftools
            sage: run_100ms()
            sage: prof.stop()     # optional - gperftools
            PROFILE: interrupts/evictions/bytes = ...
        """
    def top(self, cumulative: bool = True) -> None:
        """
        Print text report.

        OUTPUT: nothing; a textual report is printed to stdout

        EXAMPLES::

            sage: from sage.misc.gperftools import Profiler
            sage: prof = Profiler()
            sage: prof.start()    # optional - gperftools
            sage: # do something
            sage: prof.stop()     # optional - gperftools
            PROFILE: interrupts/evictions/bytes = ...
            sage: prof.top()   # optional - gperftools
            Using local file ...
            Using local file ...
        """
    def save(self, filename, cumulative: bool = True, verbose: bool = True) -> None:
        """
        Save report to disk.

        INPUT:

        - ``filename`` -- string; the filename to save at. Must end
          with one of ``.dot``, ``.ps``, ``.pdf``, ``.svg``, ``.gif``,
          or ``.txt`` to specify the output file format.

        - ``cumulative`` -- boolean (default: ``True``); whether to return
          cumulative timings

        - ``verbose`` -- boolean (default: ``True``); whether to print
          informational messages

        EXAMPLES::

            sage: from sage.misc.gperftools import Profiler, run_100ms
            sage: prof = Profiler()
            sage: prof.start()    # optional - gperftools
            sage: run_100ms()     # optional - gperftools
            sage: prof.stop()     # optional - gperftools
            PROFILE: interrupts/evictions/bytes = ...
            sage: f = tmp_filename(ext='.txt')      # optional - gperftools
            sage: prof.save(f, verbose=False)       # optional - gperftools
        """

def crun(s, evaluator) -> None:
    """
    Profile single statement.

    - ``s`` -- string; Sage code to profile

    - ``evaluator`` -- callable to evaluate

    EXAMPLES::

        sage: import sage.misc.gperftools as gperf
        sage: ev = lambda ex:eval(ex, globals(), locals())
        sage: gperf.crun('gperf.run_100ms()', evaluator=ev)   # optional - gperftools
        PROFILE: interrupts/evictions/bytes = ...
        Using local file ...
        Using local file ...
    """
def run_100ms() -> None:
    """
    Used for doctesting.

    A function that performs some computation for more than (but not
    that much more than) 100ms.

    EXAMPLES::

        sage: from sage.misc.gperftools import run_100ms
        sage: run_100ms()
    """
