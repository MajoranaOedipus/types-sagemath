from sage.env import DOT_SAGE as DOT_SAGE, HOSTNAME as HOSTNAME
from sage.interfaces.expect import Expect as Expect
from sage.misc.cachefunc import cached_function as cached_function
from weakref import ReferenceType

@cached_function
def sage_spawned_process_file() -> str:
    """
    EXAMPLES::

        sage: from sage.interfaces.quit import sage_spawned_process_file
        sage: len(sage_spawned_process_file()) > 1
        True
    """
def register_spawned_process(pid: int, cmd: str = '') -> None:
    """
    Write a line to the ``spawned_processes`` file with the given
    ``pid`` and ``cmd``.
    """

expect_objects: list[ReferenceType[Expect]]

def expect_quitall(verbose: bool = False) -> None:
    """
    EXAMPLES::

        sage: sage.interfaces.quit.expect_quitall()
        sage: gp.eval('a=10')                                                           # needs sage.libs.pari
        '10'
        sage: gp('a')                                                                   # needs sage.libs.pari
        10
        sage: sage.interfaces.quit.expect_quitall()
        sage: gp('a')                                                                   # needs sage.libs.pari
        a
        sage: sage.interfaces.quit.expect_quitall(verbose=True)                         # needs sage.libs.pari
        Exiting PARI/GP interpreter with PID ... running .../gp --fast --emacs --quiet --stacksize 10000000
    """
def kill_spawned_jobs(verbose: bool = False):
    """
    INPUT:

    - ``verbose`` -- boolean (default: ``False``); if ``True``, display a
      message each time a process is sent a kill signal

    EXAMPLES::

        sage: gp.eval('a=10')                                                           # needs sage.libs.pari
        '10'
        sage: sage.interfaces.quit.kill_spawned_jobs(verbose=False)
        sage: sage.interfaces.quit.expect_quitall()
        sage: gp.eval('a=10')                                                           # needs sage.libs.pari
        '10'
        sage: sage.interfaces.quit.kill_spawned_jobs(verbose=True)                      # needs sage.libs.pari
        Killing spawned job ...

    After doing the above, we do the following to avoid confusion in other doctests::

        sage: sage.interfaces.quit.expect_quitall()
    """
def is_running(pid: int) -> bool:
    """
    Return ``True`` if and only if there is a process with id pid running.
    """
def invalidate_all() -> None:
    """
    Invalidate all of the expect interfaces.

    This is used, e.g., by the fork-based ``@parallel`` decorator.

    EXAMPLES::

        sage: # needs sage.libs.pari sage.symbolic
        sage: a = maxima(2); b = gp(3)
        sage: a, b
        (2, 3)
        sage: sage.interfaces.quit.invalidate_all()
        sage: a
        (invalid Maxima object -- The maxima session in which this object was defined is no longer running.)
        sage: b
        (invalid PARI/GP interpreter object -- The pari session in which this object was defined is no longer running.)

    However the maxima and gp sessions should still work out, though with their state reset::

        sage: a = maxima(2); b = gp(3)                                                  # needs sage.libs.pari sage.symbolic
        sage: a, b                                                                      # needs sage.libs.pari sage.symbolic
        (2, 3)
    """
