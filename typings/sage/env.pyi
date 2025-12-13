from _typeshed import Incomplete
from sage import version as version

SAGE_ENV: Incomplete

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

HOSTNAME: Incomplete
LOCAL_IDENTIFIER: Incomplete
SAGE_VERSION: Incomplete
SAGE_DATE: Incomplete
SAGE_VERSION_BANNER: Incomplete
SAGE_VENV: Incomplete
SAGE_LIB: Incomplete
SAGE_EXTCODE: Incomplete
SAGE_VENV_SPKG_INST: Incomplete
SAGE_LOCAL: Incomplete
SAGE_SHARE: Incomplete
SAGE_DOC: Incomplete
SAGE_LOCAL_SPKG_INST: Incomplete
SAGE_SPKG_INST: Incomplete
SAGE_ROOT: Incomplete
SAGE_SRC: Incomplete
SAGE_DOC_SRC: Incomplete
SAGE_PKGS: Incomplete
SAGE_ROOT_GIT: Incomplete
SAGE_DOC_SERVER_URL: Incomplete
SAGE_DOC_LOCAL_PORT: Incomplete
home_dir: Incomplete
DOT_SAGE: Incomplete
SAGE_STARTUP_FILE: Incomplete
SAGE_ARCHFLAGS: Incomplete
SAGE_PKG_CONFIG_PATH: Incomplete
SAGE_DATA_PATH: Incomplete
CREMONA_LARGE_DATA_DIR: Incomplete
CREMONA_MINI_DATA_DIR: Incomplete
ELLCURVE_DATA_DIR: Incomplete
GRAPHS_DATA_DIR: Incomplete
POLYTOPE_DATA_DIR: Incomplete
JMOL_DIR: Incomplete
MATHJAX_DIR: Incomplete
MTXLIB: Incomplete
THREEJS_DIR: Incomplete
PPLPY_DOCS: Incomplete
MAXIMA: Incomplete
MAXIMA_FAS: Incomplete
MAXIMA_SHARE: Incomplete
KENZO_FAS: Incomplete
SAGE_NAUTY_BINS_PREFIX: Incomplete
SAGE_ECMBIN: Incomplete
RUBIKS_BINS_PREFIX: Incomplete
FOURTITWO_HILBERT: Incomplete
FOURTITWO_MARKOV: Incomplete
FOURTITWO_GRAVER: Incomplete
FOURTITWO_ZSOLVE: Incomplete
FOURTITWO_QSOLVE: Incomplete
FOURTITWO_RAYS: Incomplete
FOURTITWO_PPI: Incomplete
FOURTITWO_CIRCUITS: Incomplete
FOURTITWO_GROEBNER: Incomplete
CBLAS_PC_MODULES: Incomplete
ECL_CONFIG: Incomplete
NTL_INCDIR: Incomplete
NTL_LIBDIR: Incomplete
LIE_INFO_DIR: Incomplete
SINGULAR_BIN: Incomplete
OPENMP_CFLAGS: Incomplete
OPENMP_CXXFLAGS: Incomplete
SAGE_BANNER: Incomplete
SAGE_IMPORTALL: Incomplete
SAGE_GAP_MEMORY: Incomplete
SAGE_GAP_COMMAND: Incomplete
GAP_ROOT_PATHS: Incomplete

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

default_required_modules: Incomplete
default_optional_modules: Incomplete

def cython_aliases(required_modules=None, optional_modules=None):
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
