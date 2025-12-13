from typing import Any, Callable, overload

terminate: Callable

class ContainChildren:
    '''ContainChildren(exitcode=0, exceptcode=1, silent=False)

    File: /build/sagemath/src/sage/src/sage/interfaces/process.pyx (starting at line 27)

    Context manager which will ensure that all forked child processes
    will be forced to exit if they try to exit the context.

    This can be used as a guard against race conditions, where a child
    process wants to ``fork`` and ``exec`` but it gets interrupted after
    the ``fork`` but before the ``exec``. In such situations, the child
    would raise ``KeyboardInterrupt`` and execute code which is really
    meant for the parent process.

    INPUT:

    - ``exitcode`` -- integer (default: 0); exit code to use when a
      child process tries to exit the with block normally (not due to
      an exception)

    - ``exceptcode`` -- integer (default: 1); exit code to use when a
      child process tries to exit the with block due to an exception

    - ``silent`` -- boolean (default: ``False``); if ``False``, print
      exceptions raised by the child process

    EXAMPLES::

        sage: from sage.interfaces.process import ContainChildren
        sage: pid = os.getpid()
        sage: with ContainChildren():
        ....:     child = os.fork()
        sage: assert pid == os.getpid()  # We are the parent process

    By default, exceptions raised by the child process are printed::

        sage: with ContainChildren():
        ....:     child = os.fork()
        ....:     if child == 0:
        ....:         raise RuntimeError("Exception raised by child")
        ....:     _ = os.waitpid(child, 0r)
        Exception raised by child process with pid=...:
        Traceback (most recent call last):
        ...
        RuntimeError: Exception raised by child

    The same example with ``silent=True`` does not show the exception::

        sage: with ContainChildren(silent=True):
        ....:     child = os.fork()
        ....:     if child == 0:
        ....:         raise RuntimeError("Exception raised by child")
        ....:     _ = os.waitpid(child, 0r)'''
    @overload
    def __init__(self, exitcode=..., exceptcode=..., silent=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/interfaces/process.pyx (starting at line 78)

                TESTS:

                Check that the exit codes work properly::

                    sage: from sage.interfaces.process import ContainChildren
                    sage: with ContainChildren(exitcode=11):
                    ....:     child = os.fork()
                    sage: pid, st = os.waitpid(child, 0r)
                    sage: os.WEXITSTATUS(st)
                    11
                    sage: with ContainChildren(exceptcode=12, silent=True):
                    ....:     child = os.fork()
                    ....:     if child == 0:
                    ....:         raise RuntimeError("Exception raised by child")
                    sage: pid, st = os.waitpid(child, 0r)
                    sage: os.WEXITSTATUS(st)
                    12
        '''
    @overload
    def __init__(self) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/interfaces/process.pyx (starting at line 78)

                TESTS:

                Check that the exit codes work properly::

                    sage: from sage.interfaces.process import ContainChildren
                    sage: with ContainChildren(exitcode=11):
                    ....:     child = os.fork()
                    sage: pid, st = os.waitpid(child, 0r)
                    sage: os.WEXITSTATUS(st)
                    11
                    sage: with ContainChildren(exceptcode=12, silent=True):
                    ....:     child = os.fork()
                    ....:     if child == 0:
                    ....:         raise RuntimeError("Exception raised by child")
                    sage: pid, st = os.waitpid(child, 0r)
                    sage: os.WEXITSTATUS(st)
                    12
        '''
    @overload
    def __init__(self) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/interfaces/process.pyx (starting at line 78)

                TESTS:

                Check that the exit codes work properly::

                    sage: from sage.interfaces.process import ContainChildren
                    sage: with ContainChildren(exitcode=11):
                    ....:     child = os.fork()
                    sage: pid, st = os.waitpid(child, 0r)
                    sage: os.WEXITSTATUS(st)
                    11
                    sage: with ContainChildren(exceptcode=12, silent=True):
                    ....:     child = os.fork()
                    ....:     if child == 0:
                    ....:         raise RuntimeError("Exception raised by child")
                    sage: pid, st = os.waitpid(child, 0r)
                    sage: os.WEXITSTATUS(st)
                    12
        '''
    @overload
    def __init__(self, silent=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/interfaces/process.pyx (starting at line 78)

                TESTS:

                Check that the exit codes work properly::

                    sage: from sage.interfaces.process import ContainChildren
                    sage: with ContainChildren(exitcode=11):
                    ....:     child = os.fork()
                    sage: pid, st = os.waitpid(child, 0r)
                    sage: os.WEXITSTATUS(st)
                    11
                    sage: with ContainChildren(exceptcode=12, silent=True):
                    ....:     child = os.fork()
                    ....:     if child == 0:
                    ....:         raise RuntimeError("Exception raised by child")
                    sage: pid, st = os.waitpid(child, 0r)
                    sage: os.WEXITSTATUS(st)
                    12
        '''
    def __enter__(self) -> Any:
        '''ContainChildren.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/interfaces/process.pyx (starting at line 102)

        Store the current PID and flush the standard output and error
        streams.

        TESTS:

        The flushing solves the following double-output problem::

            sage: try:
            ....:     _ = sys.stdout.write("X ")
            ....:     if os.fork() == 0:
            ....:         _ = sys.stdout.write("Y ")
            ....:         sys.stdout.flush()
            ....:         os._exit(0)
            ....:     sleep(float(0.5))  # Give the child process time
            ....:     print("Z")
            ....: finally:
            ....:     pass
            X Y X Z

        With ``ContainChildren()``, no additional flushes are needed::

            sage: from sage.interfaces.process import ContainChildren
            sage: try:
            ....:     _ = sys.stdout.write("X ")
            ....:     with ContainChildren():
            ....:         _ = sys.stdout.write("Y ")
            ....:     sleep(float(0.5))  # Give the child process time
            ....:     print("Z")
            ....: finally:
            ....:     pass
            X Y Z'''
    def __exit__(self, *exc) -> Any:
        """ContainChildren.__exit__(self, *exc)

        File: /build/sagemath/src/sage/src/sage/interfaces/process.pyx (starting at line 142)

        TESTS:

        Check that exceptions raised by the parent work normally::

            sage: from sage.interfaces.process import ContainChildren
            sage: with ContainChildren():
            ....:     assert os.fork() == 0
            Traceback (most recent call last):
            ...
            AssertionError"""
