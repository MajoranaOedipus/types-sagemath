r"""
Sage Runtime Environment

Verify that importing ``sage.all`` works in Sage's Python without any
``SAGE_`` environment variables, and has the same ``SAGE_ROOT`` and
``SAGE_LOCAL`` (see also :issue:`29446`). If ``SAGE_ROOT`` is a path,
we normalize it, but keep in mind that ``SAGE_ROOT`` may also be
``None``::

    sage: env = {k:v for (k,v) in os.environ.items() if not k.startswith("SAGE_")}
    sage: from subprocess import check_output
    sage: module_name = "sage.all"   # hide .all import from the linter
    sage: cmd  = f"from {module_name} import SAGE_ROOT, SAGE_LOCAL;"
    sage: cmd +=  "from os.path import samefile;"
    sage: if SAGE_ROOT is None:
    ....:     cmd +=  "s1 = SAGE_ROOT is None;"
    ....: else:
    ....:     cmd += f"s1 = samefile(SAGE_ROOT, '{SAGE_ROOT}');"
    sage: cmd += f"s2 = samefile(SAGE_LOCAL, '{SAGE_LOCAL}');"
    sage: cmd += "print(s1 and s2);"
    sage: out = check_output([sys.executable, "-c", cmd], env=env).decode().strip()   # long time
    sage: out == "True"                                                               # long time
    True

AUTHORS:

- \R. Andrew Ohana (2012): initial version
"""
from _typeshed import Incomplete
from collections.abc import Iterable
from sage import version as version

SAGE_ENV: dict

def join(*args) -> str | None:
    '''
    Join paths like ``os.path.join`` except that the result is ``None``
    if any of the components is ``None``.

    EXAMPLES::

        sage: from sage.env import join
        sage: print(join("hello", "world"))
        hello/world
        sage: print(join("hello", None))
        None
    '''
def var(key: str, *fallbacks: str | None, force: bool = False) -> str | None:
    """
    Set ``SAGE_ENV[key]`` and return the value.

    If ``key`` is an environment variable, this is the value.
    Otherwise, the ``fallbacks`` are tried until one is found which
    is not ``None``. If the environment variable is not set and all
    fallbacks are ``None``, then the final value is ``None``.

    INPUT:

    - ``key`` -- string

    - ``fallbacks`` -- tuple containing ``str`` or ``None`` values

    - ``force`` -- boolean (default: ``False``); if
      ``True``, skip the environment variable and only use the
      fallbacks

    OUTPUT: the value of the environment variable or its fallbacks

    EXAMPLES::

        sage: import os, sage.env
        sage: sage.env.SAGE_ENV = dict()
        sage: os.environ['SAGE_FOO'] = 'foo'
        sage: sage.env.var('SAGE_FOO', 'unused')
        'foo'
        sage: sage.env.SAGE_FOO
        'foo'
        sage: sage.env.SAGE_ENV['SAGE_FOO']
        'foo'

    If the environment variable does not exist, the fallbacks (if any)
    are used. In most typical uses, there is exactly one fallback::

        sage: _ = os.environ.pop('SAGE_BAR', None)  # ensure that SAGE_BAR does not exist
        sage: sage.env.var('SAGE_BAR', 'bar')
        'bar'
        sage: sage.env.SAGE_BAR
        'bar'
        sage: sage.env.SAGE_ENV['SAGE_BAR']
        'bar'

    Test multiple fallbacks::

        sage: sage.env.var('SAGE_BAR', None, 'yes', 'no')
        'yes'
        sage: sage.env.SAGE_BAR
        'yes'

    If all fallbacks are ``None``, the result is ``None``::

        sage: sage.env.var('SAGE_BAR')
        sage: print(sage.env.SAGE_BAR)
        None
        sage: sage.env.var('SAGE_BAR', None)
        sage: print(sage.env.SAGE_BAR)
        None

    Test the ``force`` keyword::

        sage: os.environ['SAGE_FOO'] = 'foo'
        sage: sage.env.var('SAGE_FOO', 'forced', force=True)
        'forced'
        sage: sage.env.SAGE_FOO
        'forced'
        sage: sage.env.var('SAGE_FOO', 'forced', force=False)
        'foo'
        sage: sage.env.SAGE_FOO
        'foo'
    """

HOSTNAME: str
LOCAL_IDENTIFIER: str
SAGE_VERSION: str
SAGE_DATE: str
SAGE_VERSION_BANNER: str
SAGE_VENV: str
SAGE_LIB: str
SAGE_EXTCODE: str
SAGE_VENV_SPKG_INST: str
SAGE_LOCAL: str
SAGE_SHARE: str
SAGE_DOC: str
SAGE_LOCAL_SPKG_INST: str
SAGE_SPKG_INST: str
SAGE_ROOT: str
SAGE_SRC: str
SAGE_DOC_SRC: str
SAGE_PKGS: str
SAGE_ROOT_GIT: str
SAGE_DOC_SERVER_URL: str
SAGE_DOC_LOCAL_PORT: str
home_dir: str
DOT_SAGE: str
SAGE_STARTUP_FILE: str
SAGE_ARCHFLAGS: str
SAGE_PKG_CONFIG_PATH: str
SAGE_DATA_PATH: str
CREMONA_LARGE_DATA_DIR: str
CREMONA_MINI_DATA_DIR: str
ELLCURVE_DATA_DIR: str
GRAPHS_DATA_DIR: str
POLYTOPE_DATA_DIR: str
JMOL_DIR: str
MATHJAX_DIR: str
MTXLIB: str
THREEJS_DIR: str
PPLPY_DOCS: str
MAXIMA: str
MAXIMA_FAS: str
MAXIMA_SHARE: str
KENZO_FAS: str
SAGE_NAUTY_BINS_PREFIX: str
SAGE_ECMBIN: str
RUBIKS_BINS_PREFIX: str
FOURTITWO_HILBERT: str
FOURTITWO_MARKOV: str
FOURTITWO_GRAVER: str
FOURTITWO_ZSOLVE: str
FOURTITWO_QSOLVE: str
FOURTITWO_RAYS: str
FOURTITWO_PPI: str
FOURTITWO_CIRCUITS: str
FOURTITWO_GROEBNER: str
CBLAS_PC_MODULES: str
ECL_CONFIG: str
NTL_INCDIR: str
NTL_LIBDIR: str
LIE_INFO_DIR: str
SINGULAR_BIN: str
OPENMP_CFLAGS: str
OPENMP_CXXFLAGS: str
SAGE_BANNER: str
SAGE_IMPORTALL: str
SAGE_GAP_MEMORY: str
SAGE_GAP_COMMAND: str
GAP_ROOT_PATHS: str

def sage_include_directories(use_sources: bool = False):
    '''
    Return the list of include directories for compiling Sage extension modules.

    INPUT:

    - ``use_sources`` -- boolean (default: ``False``)

    OUTPUT:

    a list of include directories to be used to compile sage code
    1. while building sage (use_sources=\'True\')
    2. while using sage (use_sources=\'False\')

    EXAMPLES:

    Expected output while using Sage::

        sage: import sage.env
        sage: sage.env.sage_include_directories()
        [\'...\',
         \'.../numpy/...core/include\',
         \'.../include/python...\']

    To check that C/C++ files are correctly found, we verify that we can
    always find the include file ``sage/cpython/cython_metaclass.h``,
    with both values for ``use_sources``::

        sage: file = os.path.join("sage", "cpython", "cython_metaclass.h")
        sage: dirs = sage.env.sage_include_directories(use_sources=True)
        sage: any(os.path.isfile(os.path.join(d, file)) for d in dirs)
        True

    ::

        sage: # optional - !meson_editable (no need, see :issue:`39275`)
        sage: dirs = sage.env.sage_include_directories(use_sources=False)
        sage: any(os.path.isfile(os.path.join(d, file)) for d in dirs)
        True
    '''
def get_cblas_pc_module_name() -> str:
    """
    Return the name of the BLAS libraries to be used.
    """

default_required_modules: tuple[str, ...]
default_optional_modules: tuple[str, ...]

def cython_aliases(required_modules: Iterable[str] | None = None, optional_modules: Iterable[str] | None = None) -> dict[str, list[str]]:
    """
    Return the aliases for compiling Cython code. These aliases are
    macros which can occur in ``# distutils`` headers.

    INPUT:

    - ``required_modules`` -- (default: taken from ``default_required_modules``)
      iterable of string values

    - ``optional_modules`` -- (default: taken from ``default_optional_modules``)
      iterable of string values

    EXAMPLES::

        sage: from sage.env import cython_aliases
        sage: cython_aliases()
        {...}
        sage: sorted(cython_aliases().keys())
        ['CBLAS_CFLAGS',
         ...,
         'ZLIB_LIBRARIES']
        sage: cython_aliases(required_modules=('module-that-is-assumed-to-not-exist'))
        Traceback (most recent call last):
        ...
        PackageNotFoundError: ...
        sage: cython_aliases(required_modules=(), optional_modules=('module-that-is-assumed-to-not-exist'))
        {...}

    TESTS:

    We can use ``cython.parallel`` regardless of whether OpenMP is supported.
    This will run in parallel, if OpenMP is supported::

        sage: cython(                                               # optional - sage.misc.cython
        ....: '''
        ....: #distutils: extra_compile_args = OPENMP_CFLAGS
        ....: #distutils: extra_link_args = OPENMP_CFLAGS
        ....: from cython.parallel import prange
        ....:
        ....: cdef int i
        ....: cdef int n = 30
        ....: cdef int sum = 0
        ....:
        ....: for i in prange(n, num_threads=4, nogil=True):
        ....:     sum += i
        ....:
        ....: print(sum)
        ....: ''')
        435
    """
def sage_data_paths(name: str | None) -> set[str]:
    '''
    Search paths for general data files.

    If specified, the subdirectory ``name`` is appended to the
    directories. Otherwise, the directories are returned as is.

    EXAMPLES::

        sage: from sage.env import sage_data_paths
        sage: sage_data_paths("cremona")
        {\'.../cremona\'}
    '''
