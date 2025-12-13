import _cython_3_2_1
from typing import Any, Callable, ClassVar

have_program: _cython_3_2_1.cython_function_or_method
restore_cwd: Callable

class redirection:
    '''redirection(source, dest, close=None)

    File: /build/sagemath/src/sage/src/sage/misc/sage_ostools.pyx (starting at line 103)

    Context to implement redirection of files, analogous to the
    ``>file`` or ``1>&2`` syntax in POSIX shells.

    Unlike the ``redirect_stdout`` and ``redirect_stderr`` contexts in
    the Python 3.4 standard library, this acts on the OS level, not on
    the Python level. This implies that it only works for true files,
    not duck-type file objects such as ``StringIO``.

    INPUT:

    - ``source`` -- the file to be redirected

    - ``dest`` -- where the source file should be redirected to

    - ``close`` -- boolean (default: ``True``); whether to close the
      destination file upon exiting the context. This is only supported
      if ``dest`` is a Python file.

    The ``source`` and ``dest`` arguments can be either Python files
    or file descriptors.

    EXAMPLES::

        sage: from sage.misc.sage_ostools import redirection
        sage: fn = tmp_filename()

    ::

        sage: with redirection(sys.stdout, open(fn, \'w\')):
        ....:     print("hello world!")
        sage: with open(fn) as f:
        ....:     _ = sys.stdout.write(f.read())
        hello world!

    We can do the same using a file descriptor as source::

        sage: fd = sys.stdout.fileno()
        sage: with redirection(fd, open(fn, \'wb\')):
        ....:     _ = os.write(fd, b"hello world!\\n")
        sage: with open(fn) as f:
        ....:     _ = sys.stdout.write(f.read())
        hello world!

    The converse also works::

        sage: with open(fn, \'w\') as f:
        ....:     _ = f.write("This goes to the file\\n")
        ....:     with redirection(f, sys.stdout, close=False):
        ....:         _ = f.write("This goes to stdout\\n")
        ....:     _ = f.write("This goes to the file again\\n")
        This goes to stdout
        sage: with open(fn) as f:
        ....:     _ = sys.stdout.write(f.read())
        This goes to the file
        This goes to the file again

    The same :class:`redirection` instance can be reused multiple times,
    provided that ``close=False``::

        sage: f = open(fn, \'w+\')
        sage: r = redirection(sys.stdout, f, close=False)
        sage: with r:
        ....:     print("Line 1")
        sage: with r:
        ....:     print("Line 2")
        sage: with f:
        ....:     _ = f.seek(0)
        ....:     _ = sys.stdout.write(f.read())
        Line 1
        Line 2

    The redirection also works for subprocesses::

        sage: import subprocess
        sage: with redirection(sys.stdout, open(fn, \'w\')):
        ....:     _ = subprocess.call(["echo", "hello world"])
        sage: with open(fn) as f:
        ....:     _ = sys.stdout.write(f.read())
        hello world

    TESTS::

        sage: import io
        sage: redirection(sys.stdout, io.StringIO())
        Traceback (most recent call last):
        ...
        io.UnsupportedOperation: fileno

    The redirection is removed and the destination file is closed even
    in the case of errors::

        sage: f = open(os.devnull, \'w\')
        sage: with redirection(sys.stdout, f):
        ....:     raise KeyboardInterrupt
        Traceback (most recent call last):
        ...
        KeyboardInterrupt
        sage: f.closed
        True

    Reusing a :class:`redirection` instance with ``close=True``::

        sage: f = open(fn, \'w+\')
        sage: r = redirection(sys.stdout, f, close=True)
        sage: with r:
        ....:     print("Line 1")
        sage: with r:
        ....:     print("Line 2")
        Traceback (most recent call last):
        ...
        ValueError: invalid destination file

    Using ``close=True`` on a non-file::

        sage: redirection(sys.stdout, 0, close=True)
        Traceback (most recent call last):
        ...
        ValueError: close=True requires a Python destination file

    Passing invalid file descriptors::

        sage: with redirection(-123, open(os.devnull, \'w\')):
        ....:     pass
        Traceback (most recent call last):
        ...
        OSError: [Errno 9] Bad file descriptor
        sage: with redirection(sys.stdout, -123):
        ....:     pass
        Traceback (most recent call last):
        ...
        OSError: [Errno 9] Bad file descriptor

    Nesting the same :class:`redirection` object is not allowed::

        sage: with redirection(sys.stdout, open(os.devnull, \'w\')) as r:
        ....:     with r:
        ....:         pass
        Traceback (most recent call last):
        ...
        ValueError: source already redirected'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    dest_fd: File
    dest_file: File
    dup_source_fd: File
    source_fd: File
    source_file: File
    def __init__(self, source, dest, close=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/sage_ostools.pyx (starting at line 255)"""
    def __enter__(self) -> Any:
        """redirection.__enter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/sage_ostools.pyx (starting at line 271)"""
    def __exit__(self, *args) -> Any:
        """redirection.__exit__(self, *args)

        File: /build/sagemath/src/sage/src/sage/misc/sage_ostools.pyx (starting at line 294)"""
