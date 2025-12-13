import sage.interfaces.abc
import types
from . import quit as quit
from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.env import LOCAL_IDENTIFIER as LOCAL_IDENTIFIER, SAGE_EXTCODE as SAGE_EXTCODE
from sage.interfaces.interface import Interface as Interface, InterfaceElement as InterfaceElement, InterfaceFunction as InterfaceFunction, InterfaceFunctionElement as InterfaceFunctionElement
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.object_multiplexer import Multiplex as Multiplex
from sage.structure.element import RingElement as RingElement

BAD_SESSION: int

class gc_disabled:
    '''
    This is a "with" statement context manager. Garbage collection is
    disabled within its scope. Nested usage is properly handled.

    EXAMPLES::

        sage: import gc
        sage: from sage.interfaces.expect import gc_disabled
        sage: gc.isenabled()
        True
        sage: with gc_disabled():
        ....:     print(gc.isenabled())
        ....:     with gc_disabled():
        ....:         print(gc.isenabled())
        ....:     print(gc.isenabled())
        False
        False
        False
        sage: gc.isenabled()
        True
    '''
    def __enter__(self) -> None: ...
    def __exit__(self, ty: type[BaseException] | None, val: BaseException | None, tb: types.TracebackType | None): ...

class Expect(Interface):
    """
    Expect interface object.
    """
    def __init__(self, name, prompt, command=None, env={}, server=None, server_tmpdir=None, ulimit=None, maxread=None, script_subdirectory=None, restart_on_ctrlc: bool = False, verbose_start: bool = False, init_code=[], max_startup_time=None, logfile=None, eval_using_file_cutoff: int = 0, do_cleaner: bool = True, remote_cleaner: bool = False, path=None, terminal_echo: bool = True) -> None: ...
    def set_server_and_command(self, server=None, command=None, server_tmpdir=None, ulimit=None) -> None:
        """
        Changes the server and the command to use for this interface.

        This raises a :exc:`RuntimeError` if the interface is already started.

        INPUT:

        - ``server`` -- string or ``None`` (default); name of a remote host to connect to using ``ssh``

        - ``command`` -- one of:

          - a string; command line passed to the shell

          - a sequence of an :class:`~sage.features.Executable` and strings, arguments to
            pass to the executable.

        EXAMPLES::

            sage: magma.set_server_and_command(server='remote', command='mymagma')  # indirect doctest
            No remote temporary directory (option server_tmpdir) specified, using /tmp/ on remote
            sage: magma.server()
            'remote'
            sage: magma.command()
            'ssh -t remote mymagma'
        """
    def server(self):
        """
        Return the server used in this interface.

        EXAMPLES::

            sage: magma.set_server_and_command(server='remote')
            No remote temporary directory (option server_tmpdir) specified, using /tmp/ on remote
            sage: magma.server() # indirect doctest
            'remote'
        """
    def command(self):
        """
        Return the command used in this interface as a string.

        EXAMPLES::

            sage: magma.set_server_and_command(command='magma-2.19')
            sage: magma.command()  # indirect doctest
            'magma-2.19'
        """
    def is_running(self):
        """
        Return ``True`` if ``self`` is currently running.
        """
    def is_remote(self): ...
    def is_local(self): ...
    def user_dir(self): ...
    def path(self): ...
    def expect(self): ...
    def pid(self):
        """
        Return the PID of the underlying sub-process.

        REMARK:

        If the interface terminates unexpectedly, the original
        PID will still be used. But if it was terminated using
        :meth:`quit`, a new sub-process with a new PID is
        automatically started.

        EXAMPLES::

            sage: pid = gap.pid()
            sage: gap.eval('quit;')
            ''
            sage: pid == gap.pid()
            True
            sage: gap.quit()
            sage: pid == gap.pid()
            False
        """
    def clear_prompts(self) -> None: ...
    def quit(self, verbose: bool = False) -> None:
        """
        Quit the running subprocess.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); whether to print a
          message when quitting the process

        EXAMPLES::

            sage: a = maxima('y')
            sage: maxima.quit(verbose=True)
            Exiting Maxima with PID ... running ...maxima...
            sage: a._check_valid()
            Traceback (most recent call last):
            ...
            ValueError: The maxima session in which this object was defined is no longer running.

        Calling ``quit()`` a second time does nothing::

            sage: maxima.quit(verbose=True)
        """
    def detach(self) -> None:
        """
        Forget the running subprocess: keep it running but pretend that
        it's no longer running.

        EXAMPLES::

            sage: a = maxima('y')
            sage: saved_expect = maxima._expect  # Save this to close later
            sage: maxima.detach()
            sage: a._check_valid()
            Traceback (most recent call last):
            ...
            ValueError: The maxima session in which this object was defined is no longer running.
            sage: saved_expect.close()  # Close child process

        Calling ``detach()`` a second time does nothing::

            sage: maxima.detach()
        """
    def interrupt(self, tries: int = 5, timeout: float = 2.0, quit_on_fail: bool = True): ...
    def eval(self, code, strip: bool = True, synchronize: bool = False, locals=None, allow_use_file: bool = True, split_lines: str = 'nofile', **kwds):
        '''
        INPUT:

        - ``code`` -- text to evaluate

        - ``strip`` -- boolean; whether to strip output prompts,
          etc. (ignored in the base class)

        - ``locals`` -- None (ignored); this is used for compatibility
          with the Sage notebook\'s generic system interface

        - ``allow_use_file`` -- boolean (default: ``True``); if ``True`` and
          ``code`` exceeds an interface-specific threshold then ``code`` will
          be communicated via a temporary file rather that the character-based
          interface. If ``False`` then the code will be communicated via the
          character interface.

        - ``split_lines`` -- Tri-state (default: ``\'nofile\'``); if "nofile"
          then ``code`` is sent line by line unless it gets communicated via a
          temporary file. If ``True`` then ``code`` is sent line by line, but
          some lines individually might be sent via temporary file. Depending
          on the interface, this may transform grammatical ``code`` into
          ungrammatical input. If ``False``, then the whole block of code is
          evaluated all at once.

        - ``**kwds`` -- all other arguments are passed onto the ``_eval_line``
          method. An often useful example is ``reformat=False``.
        '''

class ExpectFunction(InterfaceFunction):
    """
    Expect function.
    """
class FunctionElement(InterfaceFunctionElement):
    """
    Expect function element.
    """

def is_ExpectElement(x):
    """
    Return ``True`` if ``x`` is of type :class:`ExpectElement`.

    This function is deprecated; use :func:`isinstance`
    (of :class:`sage.interfaces.abc.ExpectElement`) instead.

    EXAMPLES::

        sage: from sage.interfaces.expect import is_ExpectElement
        sage: is_ExpectElement(2)
        doctest:...: DeprecationWarning: the function is_ExpectElement is deprecated; use isinstance(x, sage.interfaces.abc.ExpectElement) instead
        See https://github.com/sagemath/sage/issues/34804 for details.
        False
    """

class ExpectElement(InterfaceElement, sage.interfaces.abc.ExpectElement):
    """
    Expect element.
    """
    def __init__(self, parent, value, is_name: bool = False, name=None) -> None: ...
    def __hash__(self):
        """
        Return the hash of ``self``.

        This is a default implementation of hash
        which just takes the hash of the string of ``self``.
        """
    def __del__(self) -> None: ...

class StdOutContext:
    """
    A context in which all communication between Sage and a subprocess
    interfaced via pexpect is printed to stdout.
    """
    interface: Incomplete
    silent: Incomplete
    stdout: Incomplete
    def __init__(self, interface, silent: bool = False, stdout=None) -> None:
        """
        Construct a new context in which all communication between Sage
        and a subprocess interfaced via pexpect is printed to stdout.

        INPUT:

        - ``interface`` -- the interface whose communication shall be dumped

        - ``silent`` -- if ``True`` this context does nothing

        - ``stdout`` -- (optional) parameter for alternative stdout device (default: ``None``)

        EXAMPLES::

            sage: from sage.interfaces.expect import StdOutContext
            sage: with StdOutContext(Gp()) as g:
            ....:     g('1+1')
            sage=...
        """
    def __enter__(self):
        """
        EXAMPLES::

            sage: from sage.interfaces.expect import StdOutContext
            sage: with StdOutContext(singular):
            ....:     singular.eval('1+1')
            1+1;
            ...
        """
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None:
        """
        EXAMPLES::

            sage: from sage.interfaces.expect import StdOutContext
            sage: with StdOutContext(gap):
            ....:     gap('1+1')
            \\$sage...
        """
