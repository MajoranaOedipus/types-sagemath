from _typeshed import Incomplete
from collections.abc import Generator
from pathlib import Path
from sage.repl.load import load as load, load_wrap as load_wrap

attached: Incomplete
load_debug_mode: bool
attach_debug_mode: bool

def load_attach_mode(load_debug=None, attach_debug=None):
    """
    Get or modify the current debug mode for the behavior of
    :func:`load` and :func:`attach` on ``.sage`` files.

    In debug mode, loaded or attached ``.sage`` files are preparsed
    through a file to make their tracebacks more informative. If not
    in debug mode, then ``.sage`` files are preparsed in memory only
    for performance.

    At startup, debug mode is ``True`` for attaching and ``False``
    for loading.

    .. NOTE::

        This function should really be deprecated and code executed
        from memory should raise proper tracebacks.

    INPUT:

    - ``load_debug`` -- boolean or ``None`` (default); if not
      ``None``, then set a new value for the debug mode for loading
      files

    - ``attach_debug`` -- boolean or ``None`` (default); same as
      ``load_debug``, but for attaching files

    OUTPUT:

    If all input values are ``None``, returns a tuple giving the
    current modes for loading and attaching.

    EXAMPLES::

        sage: load_attach_mode()
        (False, True)
        sage: load_attach_mode(attach_debug=False)
        sage: load_attach_mode()
        (False, False)
        sage: load_attach_mode(load_debug=True)
        sage: load_attach_mode()
        (True, False)
        sage: load_attach_mode(load_debug=False, attach_debug=True)
    """

search_paths: list[Path]

def load_attach_path(path=None, replace: bool = False):
    '''
    Get or modify the current search path for :func:`load` and
    :func:`attach`.

    INPUT:

    - ``path`` -- string or list of strings (default: ``None``);
      path(s) to append to or replace the current path

    - ``replace`` -- boolean (default: ``False``); if ``path`` is not
      ``None``, whether to *replace* the search path instead of
      *appending* to it

    OUTPUT: none or a *reference* to the current search paths

    EXAMPLES:

    First, we extend the example given in :func:`load`\'s docstring::

        sage: sage.repl.attach.reset(); reset_load_attach_path()
        sage: load_attach_path()
        [PosixPath(\'.\')]
        sage: t_dir = tmp_dir()
        sage: fullpath = os.path.join(t_dir, \'test.py\')
        sage: with open(fullpath, \'w\') as f:
        ....:     _ = f.write("print(37 * 3)")

    We put a new, empty directory on the attach path for testing
    (otherwise this will load ``test.py`` from the current working
    directory if that happens to exist)::

        sage: import tempfile
        sage: with tempfile.TemporaryDirectory() as d:
        ....:     load_attach_path(d, replace=True)
        ....:     attach(\'test.py\')
        Traceback (most recent call last):
        ...
        OSError: did not find file \'test.py\' to load or attach
        sage: load_attach_path(t_dir)
        sage: attach(\'test.py\')
        111
        sage: af = attached_files(); len(af)
        1
        sage: af == [fullpath]
        True
        sage: from pathlib import Path
        sage: sage.repl.attach.reset(); reset_load_attach_path()
        sage: load_attach_path() == [Path(\'.\')]
        True
        sage: with tempfile.TemporaryDirectory() as d:
        ....:     load_attach_path(d, replace=True)
        ....:     load(\'test.py\')
        Traceback (most recent call last):
        ...
        OSError: did not find file \'test.py\' to load or attach

    The function returns a reference to the path list::

        sage: reset_load_attach_path(); load_attach_path()
        [PosixPath(\'.\')]
        sage: load_attach_path(\'/path/to/my/sage/scripts\'); load_attach_path()
        [PosixPath(\'.\'), PosixPath(\'/path/to/my/sage/scripts\')]
        sage: load_attach_path([\'good\', \'bad\', \'ugly\'], replace=True)
        sage: load_attach_path()
        [PosixPath(\'good\'), PosixPath(\'bad\'), PosixPath(\'ugly\')]
        sage: p = load_attach_path(); p.pop()
        PosixPath(\'ugly\')
        sage: p[0] = \'weird\'; load_attach_path()
        [\'weird\', PosixPath(\'bad\')]
        sage: reset_load_attach_path(); load_attach_path()
        [PosixPath(\'.\')]
    '''
def reset_load_attach_path() -> None:
    """
    Reset the current search path for :func:`load` and :func:`attach`.

    The default path is ``'.'`` plus any paths specified in the
    environment variable ``SAGE_LOAD_ATTACH_PATH``.

    EXAMPLES::

        sage: load_attach_path()
        [PosixPath('.')]
        sage: t_dir = tmp_dir()
        sage: load_attach_path(t_dir)
        sage: from pathlib import Path
        sage: Path(t_dir) in load_attach_path()
        True
        sage: reset_load_attach_path(); load_attach_path()
        [PosixPath('.')]

    At startup, Sage adds colon-separated paths in the environment
    variable ``SAGE_LOAD_ATTACH_PATH``::

        sage: reset_load_attach_path(); load_attach_path()
        [PosixPath('.')]
        sage: os.environ['SAGE_LOAD_ATTACH_PATH'] = '/veni/vidi:vici:'
        sage: from importlib import reload
        sage: reload(sage.repl.attach)    # Simulate startup
        <module 'sage.repl.attach' from '...'>
        sage: load_attach_path()
        [PosixPath('.'), PosixPath('/veni/vidi'), PosixPath('vici')]
        sage: del os.environ['SAGE_LOAD_ATTACH_PATH']
        sage: reload(sage.repl.preparse)    # Simulate startup
        <module 'sage.repl.preparse' from '...'>
        sage: reset_load_attach_path(); load_attach_path()
        [PosixPath('.')]
    """
def attach(*files) -> None:
    '''
    Attach a file or files to a running instance of Sage and also load
    that file.

    .. NOTE::

        Attaching files uses the Python inputhook, which will conflict
        with other inputhook users. This generally includes GUI main loop
        integrations, for example tkinter. So you can only use tkinter or
        attach, but not both at the same time.

    INPUT:

    - ``files`` -- list of filenames (strings) to attach

    OUTPUT:

    Each file is read in and added to an internal list of watched files.
    The meaning of reading in a file depends on the file type:

    - ``.py`` files are read in with no preparsing (so, e.g., ``2^3`` is 2
      bit-xor 3);

    - ``.sage`` files are preparsed, then the result is read in;

    - ``.pyx`` files are *not* preparsed, but rather are compiled to a
      module ``m`` and then ``from m import *`` is executed.

    The contents of the file are then loaded, which means they are read
    into the running Sage session. For example, if ``foo.sage`` contains
    ``x=5``, after attaching ``foo.sage`` the variable ``x`` will be set
    to 5. Moreover, any time you change ``foo.sage``, before you execute
    a command, the attached file will be re-read automatically (with no
    intervention on your part).

    .. SEEALSO::

        :func:`~sage.repl.load.load` is the same as :func:`attach`, but
        does not automatically reload a file when it changes unless
        ``attach=True`` is passed.

        ``%attach`` magic can also be used, see
        :meth:`~sage.repl.ipython_extension.SageMagics.attach`.

    EXAMPLES:

    You attach a file, e.g., ``foo.sage`` or ``foo.py`` or
    ``foo.pyx``, to a running Sage session by typing::

        sage: attach(\'foo.sage\')  # not tested

    Here we test attaching multiple files at once::

        sage: sage.repl.attach.reset()
        sage: t1 = tmp_filename(ext=\'.py\')
        sage: with open(t1,\'w\') as f: _ = f.write("print(\'hello world\')")
        sage: t2 = tmp_filename(ext=\'.py\')
        sage: with open(t2,\'w\') as f: _ = f.write("print(\'hi there xxx\')")
        sage: attach(t1, t2)
        hello world
        hi there xxx
        sage: af = attached_files(); len(af)
        2
        sage: t1 in af and t2 in af
        True

    .. SEEALSO::

        - :meth:`attached_files` returns a list of
          all currently attached files.

        - :meth:`detach` instructs Sage to remove a
          file from the internal list of watched files.

        - :meth:`load_attach_path` allows you to
          get or modify the current search path for loading and attaching
          files.
    '''
def add_attached_file(filename) -> None:
    """
    Add to the list of attached files.

    This is a callback to be used from
    :func:`~sage.repl.load.load` after evaluating the attached
    file the first time.

    INPUT:

    - ``filename`` -- string (the fully qualified file name)
      or :class:`Path` object

    EXAMPLES::

        sage: import sage.repl.attach as af
        sage: af.reset()
        sage: t = tmp_filename(ext='.py')
        sage: af.add_attached_file(t)
        sage: af.attached_files()
        ['/.../tmp_....py']
        sage: af.detach(t)
        sage: af.attached_files()
        []
    """
def attached_files() -> list:
    '''
    Return a list of all files attached to the current session with
    :meth:`attach`.

    OUTPUT: the filenames in a sorted list of strings

    EXAMPLES::

        sage: sage.repl.attach.reset()
        sage: t = tmp_filename(ext=\'.py\')
        sage: with open(t,\'w\') as f: _ = f.write("print(\'hello world\')")
        sage: attach(t)
        hello world
        sage: af = attached_files(); af
        [\'/....py\']
        sage: af == [t]
        True
    '''
def detach(filename) -> None:
    '''
    Detach a file.

    This is the counterpart to :meth:`attach`.

    INPUT:

    - ``filename`` -- string, a list of strings or a tuple of strings
      or a :class:`Path`, a list of :class:`Path` or a tuple of :class:`Path`

    EXAMPLES::

        sage: sage.repl.attach.reset()
        sage: t = tmp_filename(ext=\'.py\')
        sage: with open(t,\'w\') as f: _ = f.write("print(\'hello world\')")
        sage: attach(t)
        hello world
        sage: af = attached_files(); len(af)
        1
        sage: af == [t]
        True
        sage: detach(t)
        sage: attached_files()
        []

        sage: sage.repl.attach.reset(); reset_load_attach_path()
        sage: load_attach_path()
        [PosixPath(\'.\')]
        sage: t_dir = tmp_dir()
        sage: fullpath = os.path.join(t_dir, \'test.py\')
        sage: with open(fullpath, \'w\') as f: _ = f.write("print(37 * 3)")
        sage: load_attach_path(t_dir, replace=True)
        sage: attach(\'test.py\')
        111
        sage: af = attached_files(); len(af)
        1
        sage: af == [os.path.normpath(fullpath)]
        True
        sage: detach(\'test.py\')
        sage: attached_files()
        []
        sage: attach(\'test.py\')
        111
        sage: fullpath = os.path.join(t_dir, \'test2.py\')
        sage: with open(fullpath, \'w\') as f: _ = f.write("print(3)")
        sage: attach(\'test2.py\')
        3
        sage: detach(attached_files())
        sage: attached_files()
        []

    TESTS::

        sage: detach(\'/dev/null/foobar.sage\')
        Traceback (most recent call last):
        ...
        ValueError: file \'/dev/null/foobar.sage\' is not attached, see attached_files()
    '''
def reset() -> None:
    '''
    Remove all the attached files from the list of attached files.

    EXAMPLES::

        sage: sage.repl.attach.reset()
        sage: t = tmp_filename(ext=\'.py\')
        sage: with open(t,\'w\') as f: _ = f.write("print(\'hello world\')")
        sage: attach(t)
        hello world
        sage: af = attached_files(); len(af)
        1
        sage: af == [t]
        True
        sage: sage.repl.attach.reset()
        sage: attached_files()
        []
    '''
def modified_file_iterator() -> Generator[Incomplete]:
    """
    Iterate over the changed files.

    As a side effect the stored time stamps are updated with the
    actual time stamps. So if you iterate over the attached files in
    order to reload them and you hit an error then the subsequent
    files are not marked as read.

    Files that are in the process of being saved are excluded.

    EXAMPLES::

        sage: sage.repl.attach.reset()
        sage: t = tmp_filename(ext='.py')
        sage: attach(t)
        sage: from sage.repl.attach import modified_file_iterator
        sage: list(modified_file_iterator())
        []
        sage: sleep(1)   # filesystem mtime granularity
        sage: with open(t, 'w') as f: _ = f.write('1')
        sage: list(modified_file_iterator())
        [(PosixPath('/.../tmp_....py'), time.struct_time(...))]
    """
def reload_attached_files_if_modified() -> None:
    """
    Reload attached files that have been modified.

    This is the internal implementation of the attach mechanism.

    EXAMPLES::

        sage: sage.repl.attach.reset()
        sage: from sage.repl.interpreter import get_test_shell
        sage: shell = get_test_shell()
        sage: tmp = tmp_filename(ext='.py')
        sage: with open(tmp, 'w') as f: _ = f.write('a = 2\\n')
        sage: shell.run_cell('attach({0})'.format(repr(tmp)))
        sage: shell.run_cell('a')
        2
        sage: sleep(1)   # filesystem mtime granularity
        sage: with open(tmp, 'w') as f: _ = f.write('a = 3\\n')

    Note that the doctests are never really at the command prompt
    where the automatic reload is triggered. So we have to do it
    manually::

        sage: shell.run_cell('from sage.repl.attach import reload_attached_files_if_modified')
        sage: shell.run_cell('reload_attached_files_if_modified()')
        ### reloading attached file tmp_....py modified at ... ###

        sage: shell.run_cell('a')
        3
        sage: shell.run_cell('detach({0})'.format(repr(tmp)))
        sage: shell.run_cell('attached_files()')
        []
        sage: shell.quit()
    """
