from sage.cpython.string import FS_ENCODING as FS_ENCODING, bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes

def is_loadable_filename(filename):
    """
    Return whether a file can be loaded into Sage.

    This checks only whether its name ends in one of the supported
    extensions ``.py``, ``.pyx``, ``.sage``, ``.spyx``, ``.f``,
    ``.f90`` and ``.m``.

    .. NOTE:: :func:`load` assumes that `.m` signifies a Magma file.

    INPUT:

    - ``filename`` -- string or :class:`Path` object

    OUTPUT: boolean

    EXAMPLES::

        sage: sage.repl.load.is_loadable_filename('foo.bar')
        False
        sage: sage.repl.load.is_loadable_filename('foo.c')
        False
        sage: sage.repl.load.is_loadable_filename('foo.sage')
        True
        sage: sage.repl.load.is_loadable_filename('FOO.F90')
        True
        sage: sage.repl.load.is_loadable_filename('foo.m')
        True

        sage: from pathlib import Path
        sage: sage.repl.load.is_loadable_filename(Path('foo.py'))
        True
    """
def load_cython(name):
    """
    Helper function to load a Cython file.

    INPUT:

    - ``name`` -- filename of the Cython file

    OUTPUT:

    - A string with Python code to import the names from the compiled
      module.
    """
def load(filename, globals, attach: bool = False) -> None:
    '''
    Execute a file in the scope given by ``globals``. If the name starts with
    ``http://`` or ``https://``, it is treated as a URL and downloaded.

    .. NOTE::

        For Cython files, the situation is more complicated --
        the module is first compiled to a temporary module ``t`` and
        executed via::

            from t import *

    .. NOTE::

        The global ``load`` function is :func:`sage.misc.persist.load`,
        which delegates to this function for code file formats.

        ``%runfile`` magic can also be used, see
        :meth:`~sage.repl.ipython_extension.SageMagics.runfile`.

    INPUT:

    - ``filename`` -- string (denoting a filename or URL) or a :class:`Path` object

    - ``globals`` -- string:object dictionary; the context in which
      to execute the file contents

    - ``attach`` -- boolean (default: ``False``); whether to add the
      file to the list of attached files

    Loading an executable Sage script from the :ref:`command line <section-command-line>`
    will run whatever code is inside an

    ::

        if __name__ == "__main__":

    section, as the condition on ``__name__`` will hold true (code run from the
    command line is considered to be running in the ``__main__`` module.)

    EXAMPLES:

    Note that ``.py`` files are *not* preparsed::

        sage: from tempfile import NamedTemporaryFile
        sage: context = { "z": 1}
        sage: with NamedTemporaryFile(mode=\'w\', suffix=\'.py\') as file:
        ....:     _ = file.write("print((\'hi\', 2^3, z)); z = -2^7")
        ....:     _ = file.seek(0)
        ....:     sage.repl.load.load(file.name, context)
        (\'hi\', 1, 1)
        sage: context["z"]
        -7

    A ``.sage`` file *is* preparsed::

        sage: context = { "z": 1, "Integer": Integer }
        sage: with NamedTemporaryFile(mode=\'w\', suffix=\'.sage\') as file:
        ....:     _ = file.write("print((\'hi\', 2^3, z)); z = -2^7")
        ....:     _ = file.seek(0)
        ....:     sage.repl.load.load(file.name, context)
        (\'hi\', 8, 1)
        sage: context["z"]
        -128

    Cython files are *not* preparsed::

        sage: context = { "z": 1 }
        sage: with NamedTemporaryFile(mode=\'w\', suffix=\'.pyx\') as file:
        ....:     _ = file.write("print((\'hi\', 2^3)); z = -2^7")
        ....:     _ = file.seek(0)
        ....:     sage.repl.load.load(file.name, context)                                         # needs sage.misc.cython
        Compiling ...
        (\'hi\', 1)
        sage: context["z"]
        -7

    If the file is not a Cython, Python, or Sage file, a :exc:`ValueError`
    is raised::

        sage: with NamedTemporaryFile(mode=\'w\', suffix=\'.foo\') as file:
        ....:     sage.repl.load.load(file.name, {})
        Traceback (most recent call last):
        ...
        ValueError: unknown file extension \'.foo\' for load or attach (supported extensions: .py, .pyx, .sage, .spyx, .f, .f90, .m)

    We load a file given at a remote URL (not tested for security reasons)::

        sage: sage.repl.load.load(\'https://www.sagemath.org/files/loadtest.py\', globals())  # not tested
        hi from the net
        5

    We can load files using secure http (https)::

        sage: sage.repl.load.load(\'https://raw.githubusercontent.com/sagemath/sage-patchbot/3.0.0/sage_patchbot/util.py\', globals())  # optional - internet

    We attach a file (note that :func:`~sage.repl.attach.attach`
    is equivalent, but available at the global scope by default)::

        sage: with NamedTemporaryFile(mode=\'w\', suffix=\'.py\') as file:
        ....:     _ = file.write("print(\'hello world\')")
        ....:     _ = file.seek(0)
        ....:     sage.repl.load.load(file.name, {}, attach=True)
        hello world
        sage: file.name in attached_files()
        True

    You cannot attach remote URLs (yet)::

        sage: sage.repl.load.load(\'https://www.sagemath.org/files/loadtest.py\', globals(), attach=True)  # optional - internet
        Traceback (most recent call last):
        ...
        NotImplementedError: you cannot attach a URL

    The default search path for loading and attaching files is the
    current working directory, i.e., ``\'.\'``.  But you can modify the
    path with :func:`load_attach_path`::

        sage: import tempfile
        sage: sage.repl.attach.reset(); reset_load_attach_path()
        sage: load_attach_path()
        [PosixPath(\'.\')]
        sage: with tempfile.TemporaryDirectory() as t_dir:
        ....:     fname = \'test.py\'
        ....:     fullpath = os.path.join(t_dir, fname)
        ....:     with open(fullpath, \'w\') as f:
        ....:         _ = f.write("print(37 * 3)")
        ....:     load_attach_path(t_dir, replace=True)
        ....:     attach(fname)
        111
        sage: sage.repl.attach.reset(); reset_load_attach_path() # clean up

    or by setting the environment variable ``SAGE_LOAD_ATTACH_PATH``
    to a colon-separated list before starting Sage::

        $ export SAGE_LOAD_ATTACH_PATH="/path/to/my/library:/path/to/utils"
        $ sage
        sage: load_attach_path()          # not tested
        [\'.\', \'/path/to/my/library\', \'/path/to/utils\']

    TESTS:

    Make sure that load handles filenames with spaces in the name or path::

        sage: t = tmp_filename(ext=\' b.sage\')
        sage: with open(t, \'w\') as f:
        ....:     _ = f.write("print(2)")
        sage: sage.repl.load.load(t, globals())
        2

    Non-existing files with spaces give correct messages::

        sage: sage.repl.load.load("this file should not exist", globals())
        Traceback (most recent call last):
        ...
        OSError: did not find file \'this file should not exist\' to load or attach
    '''
def load_wrap(filename, attach: bool = False):
    '''
    Encode a load or attach command as valid Python code.

    INPUT:

    - ``filename`` -- string or :class:`Path` object; the argument
      to the load or attach command

    - ``attach`` -- boolean (default: ``False``); whether to attach
      ``filename``, instead of loading it

    OUTPUT: string

    EXAMPLES::

        sage: sage.repl.load.load_wrap(\'foo.py\', True)
        \'sage.repl.load.load(sage.repl.load.base64.b64decode("Zm9vLnB5"),globals(),True)\'
        sage: sage.repl.load.load_wrap(\'foo.sage\')
        \'sage.repl.load.load(sage.repl.load.base64.b64decode("Zm9vLnNhZ2U="),globals(),False)\'
        sage: m = sage.repl.load.base64.b64decode("Zm9vLnNhZ2U=")
        sage: m == b\'foo.sage\'
        True
    '''
