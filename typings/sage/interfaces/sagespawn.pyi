import pexpect.pty_spawn
import ptyprocess.ptyprocess
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from typing import Any, overload

__revision__: str
__version__: str

class SagePtyProcess(ptyprocess.ptyprocess.PtyProcess):
    def close(self, force=...) -> Any:
        '''SagePtyProcess.close(self, force=None)

        File: /build/sagemath/src/sage/src/sage/interfaces/sagespawn.pyx (starting at line 178)

        Quit the child process: send the quit string, close the
        pseudo-tty and kill the process.

        This function returns immediately, it doesn\'t wait for the
        child process to die.

        EXAMPLES::

            sage: from sage.interfaces.sagespawn import SageSpawn
            sage: s = SageSpawn("sleep 1000")
            sage: s.close()
            sage: while s.isalive():  # long time (5 seconds)
            ....:     sleep(float(0.1))'''
    @overload
    def terminate_async(self, interval=...) -> Any:
        '''SagePtyProcess.terminate_async(self, interval=5.0)

        File: /build/sagemath/src/sage/src/sage/interfaces/sagespawn.pyx (starting at line 210)

        Terminate the child process group asynchronously.

        This function returns immediately, while the child is slowly
        being killed in the background.

        INPUT:

        - ``interval`` -- (default: 5) how much seconds to wait between
          sending two signals

        EXAMPLES:

        Run an infinite loop in the shell::

            sage: from sage.interfaces.sagespawn import SageSpawn
            sage: s = SageSpawn("sh", ["-c", "while true; do sleep 1; done"])

        Check that the process eventually dies after calling
        ``terminate_async``::

            sage: s.ptyproc.terminate_async(interval=float(0.2))
            sage: while True:
            ....:     try:
            ....:         os.kill(s.pid, 0)
            ....:     except OSError:
            ....:         sleep(float(0.1))
            ....:     else:
            ....:         break  # process got killed'''
    @overload
    def terminate_async(self, interval=...) -> Any:
        '''SagePtyProcess.terminate_async(self, interval=5.0)

        File: /build/sagemath/src/sage/src/sage/interfaces/sagespawn.pyx (starting at line 210)

        Terminate the child process group asynchronously.

        This function returns immediately, while the child is slowly
        being killed in the background.

        INPUT:

        - ``interval`` -- (default: 5) how much seconds to wait between
          sending two signals

        EXAMPLES:

        Run an infinite loop in the shell::

            sage: from sage.interfaces.sagespawn import SageSpawn
            sage: s = SageSpawn("sh", ["-c", "while true; do sleep 1; done"])

        Check that the process eventually dies after calling
        ``terminate_async``::

            sage: s.ptyproc.terminate_async(interval=float(0.2))
            sage: while True:
            ....:     try:
            ....:         os.kill(s.pid, 0)
            ....:     except OSError:
            ....:         sleep(float(0.1))
            ....:     else:
            ....:         break  # process got killed'''

class SageSpawn(pexpect.pty_spawn.spawn):
    def __init__(self, *args, **kwds) -> Any:
        '''SageSpawn.__init__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/interfaces/sagespawn.pyx (starting at line 39)

        Spawn a subprocess in a pseudo-tty.

        - ``*args``, ``**kwds`` -- see :class:`pexpect.spawn`

        - ``name`` -- human-readable name for this process, used for
          display purposes only

        - ``quit_string`` -- (default: ``None``) if not ``None``, send
          this string to the child process before killing it

        EXAMPLES::

            sage: from sage.interfaces.sagespawn import SageSpawn
            sage: SageSpawn("sleep 1", name="Sleeping Beauty")
            Sleeping Beauty with PID ... running ...'''
    def expect_peek(self, *args, **kwds) -> Any:
        '''SageSpawn.expect_peek(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/interfaces/sagespawn.pyx (starting at line 138)

        Like :meth:`expect` but restore the read buffer such that it
        looks like nothing was actually read. The next reading will
        continue at the current position.

        EXAMPLES::

            sage: from sage.interfaces.sagespawn import SageSpawn
            sage: E = SageSpawn("sh", ["-c", "echo hello world"])
            sage: _ = E.expect_peek("w")
            sage: E.read().decode(\'ascii\')
            \'hello world\\r\\n\''''
    def expect_upto(self, *args, **kwds) -> Any:
        '''SageSpawn.expect_upto(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/interfaces/sagespawn.pyx (starting at line 157)

        Like :meth:`expect` but restore the read buffer starting from
        the matched string. The next reading will continue starting
        with the matched string.

        EXAMPLES::

            sage: from sage.interfaces.sagespawn import SageSpawn
            sage: E = SageSpawn("sh", ["-c", "echo hello world"])
            sage: _ = E.expect_upto("w")
            sage: E.read().decode(\'ascii\')
            \'world\\r\\n\''''
