from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager

class SourceDistributionFilter:
    """
    A :class:`collections.abc.Container` for source files in distributions.

    INPUT:

    - ``include_distributions`` -- (default: ``None``) if not ``None``,
      should be a sequence or set of strings: include files whose
      ``distribution`` (from a ``# sage_setup:`` ``distribution = PACKAGE``
      directive in the source file) is an element of ``distributions``.

    - ``exclude_distributions`` -- (default: ``None``) if not ``None``,
      should be a sequence or set of strings: exclude files whose
      ``distribution`` (from a ``# sage_setup:`` ``distribution = PACKAGE``
      directive in the module source file) is in ``exclude_distributions``.

    EXAMPLES::

        sage: from sage.misc.package_dir import SourceDistributionFilter
        sage: F = SourceDistributionFilter()
        sage: sage.misc.package_dir.__file__ in F
        True
        sage: F = SourceDistributionFilter(include_distributions=['sagemath-environment'])
        sage: sage.misc.package_dir.__file__ in F
        True
        sage: F = SourceDistributionFilter(exclude_distributions=['sagemath-environment'])
        sage: sage.misc.package_dir.__file__ in F
        False
    """
    def __init__(self, include_distributions=None, exclude_distributions=None) -> None:
        """
        TESTS:

        ``exclude_distributions=None`` is normalized to the empty tuple::

            sage: from sage.misc.package_dir import SourceDistributionFilter
            sage: F = SourceDistributionFilter()
            sage: F._exclude_distributions
            ()
        """
    def __contains__(self, filename) -> bool:
        """
        TESTS:

        No file access is used when neither ``include_distributions`` nor
        ``exclude_distributions`` is given::

            sage: from sage.misc.package_dir import SourceDistributionFilter
            sage: F = SourceDistributionFilter()
            sage: '/doesnotexist' in F
            True

        ``exclude_distributions`` can also be an empty container::

            sage: F = SourceDistributionFilter(exclude_distributions=())
            sage: '/doesnotexist' in F
            True
        """

distribution_directive: Incomplete

def read_distribution(src_file):
    """
    Parse ``src_file`` for a ``# sage_setup:`` ``distribution = PKG`` directive.

    INPUT:

    - ``src_file`` -- file name of a Python or Cython source file

    OUTPUT:

    A string, the name of the distribution package (``PKG``), or the empty
    string if no directive was found.

    EXAMPLES::

        sage: # needs SAGE_SRC
        sage: from sage.env import SAGE_SRC
        sage: from sage.misc.package_dir import read_distribution
        sage: read_distribution(os.path.join(SAGE_SRC, 'sage', 'graphs', 'graph_decompositions', 'tdlib.pyx'))
        'sagemath-tdlib'
        sage: read_distribution(os.path.join(SAGE_SRC, 'sage', 'graphs', 'graph_decompositions', 'modular_decomposition.py'))
        ''
    """
def update_distribution(src_file, distribution, *, verbose: bool = False) -> None:
    '''
    Add or update a ``# sage_setup:`` ``distribution = PKG`` directive in ``src_file``.

    For a Python or Cython file, if a ``distribution`` directive
    is not already present, it is added.

    For any other file, if a ``distribution`` directive is not already
    present, no action is taken.

    INPUT:

    - ``src_file`` -- file name of a source file

    EXAMPLES::

        sage: from sage.misc.package_dir import read_distribution, update_distribution
        sage: import tempfile
        sage: def test(filename, file_contents):
        ....:     with tempfile.TemporaryDirectory() as d:
        ....:         fname = os.path.join(d, filename)
        ....:         with open(fname, \'w\') as f:
        ....:             f.write(file_contents)
        ....:         with open(fname, \'r\') as f:
        ....:             print(f.read() + "====")
        ....:         update_distribution(fname, \'sagemath-categories\')
        ....:         with open(fname, \'r\') as f:
        ....:             print(f.read() + "====")
        ....:         update_distribution(fname, \'\')
        ....:         with open(fname, \'r\') as f:
        ....:             print(f.read(), end="")
        sage: test(\'module.py\', \'# Python file\\n\')
        # Python file
        ====
        # sage_setup: distribution...= sagemath-categories
        # Python file
        ====
        # sage_setup: distribution...=
        # Python file
        sage: test(\'file.cpp\', \'// sage_setup: \' \'distribution=sagemath-modules\\n\'
        ....:                  \'// C++ file with existing directive\\n\')
        // sage_setup: distribution...=sagemath-modules
        // C++ file with existing directive
        ====
        // sage_setup: distribution...= sagemath-categories
        // C++ file with existing directive
        ====
        // sage_setup: distribution...=
        // C++ file with existing directive
        sage: test(\'file.cpp\', \'// C++ file without existing directive\\n\')
        // C++ file without existing directive
        ====
        // C++ file without existing directive
        ====
        // C++ file without existing directive
    '''
def is_package_or_sage_namespace_package_dir(path, *, distribution_filter=None):
    """
    Return whether ``path`` is a directory that contains a Python package.

    Ordinary Python packages are recognized by the presence of ``__init__.py``.

    Implicit namespace packages (PEP 420) are only recognized if they
    follow the conventions of the Sage library, i.e., the directory contains
    a file ``all.py`` or a file matching the pattern ``all__*.py``.

    INPUT:

    - ``path`` -- a directory name

    - ``distribution_filter`` -- (default: ``None``)
      only consider ``all*.py`` files whose distribution (from a
      ``# sage_setup:`` ``distribution = PACKAGE`` directive in the source file)
      is an element of ``distribution_filter``.

    EXAMPLES:

    :mod:`sage.cpython` is an ordinary package::

        sage: # optional - !meson_editable
        sage: from sage.misc.package_dir import is_package_or_sage_namespace_package_dir
        sage: directory = sage.cpython.__path__[0]; directory
        '.../sage/cpython'
        sage: is_package_or_sage_namespace_package_dir(directory)
        True

    :mod:`sage.libs.mpfr` only has an ``__init__.pxd`` file, but we consider
    it a package directory for consistency with Cython::

        sage: # optional - !meson_editable
        sage: directory = os.path.join(sage.libs.__path__[0], 'mpfr'); directory
        '.../sage/libs/mpfr'
        sage: is_package_or_sage_namespace_package_dir(directory)       # known bug (seen in build.yml)
        True

    :mod:`sage` is designated to become an implicit namespace package::

        sage: # optional - !meson_editable
        sage: directory = sage.__path__[0]; directory
        '.../sage'
        sage: is_package_or_sage_namespace_package_dir(directory)
        True

    Not a package::

        sage: # optional - !meson_editable
        sage: directory = os.path.join(sage.symbolic.__path__[0], 'ginac'); directory   # needs sage.symbolic
        '.../sage/symbolic/ginac'
        sage: is_package_or_sage_namespace_package_dir(directory)                       # needs sage.symbolic
        False

    TESTS::

        sage: # optional - meson_editable
        sage: from sage.misc.package_dir import is_package_or_sage_namespace_package_dir
        sage: directory = os.path.dirname(sage.cpython.__file__); directory
        '.../sage/cpython'
        sage: is_package_or_sage_namespace_package_dir(directory)
        True

        sage: # optional - meson_editable
        sage: directory = os.path.join(os.path.dirname(sage.libs.__file__), 'mpfr'); directory
        '.../sage/libs/mpfr'
        sage: is_package_or_sage_namespace_package_dir(directory)
        True

        sage: # optional - meson_editable, sage.symbolic
        sage: directory = os.path.join(os.path.dirname(sage.symbolic.__file__), 'ginac'); directory
        '.../sage/symbolic/ginac'
        sage: is_package_or_sage_namespace_package_dir(directory)
        False
    """
@contextmanager
def cython_namespace_package_support() -> Generator[None]:
    """
    Activate namespace package support in Cython 0.x.

    See https://github.com/cython/cython/issues/2918#issuecomment-991799049
    """
def walk_packages(path=None, prefix: str = '', onerror=None) -> Generator[Incomplete, Incomplete, Incomplete]:
    """
    Yield :class:`pkgutil.ModuleInfo` for all modules recursively on ``path``.

    This version of the standard library function :func:`pkgutil.walk_packages`
    addresses https://github.com/python/cpython/issues/73444 by handling
    the implicit namespace packages in the package layout used by Sage;
    see :func:`is_package_or_sage_namespace_package_dir`.

    INPUT:

    - ``path`` -- list of paths to look for modules in or
      ``None`` (all accessible modules)

    - ``prefix`` -- string to output on the front of every module name
      on output

    - ``onerror`` -- a function which gets called with one argument (the
      name of the package which was being imported) if any exception
      occurs while trying to import a package.  If ``None``, ignore
      :exc:`ImportError` but propagate all other exceptions.

    EXAMPLES::

        sage: # optional - !meson_editable
        sage: sorted(sage.misc.package_dir.walk_packages(sage.misc.__path__))  # a namespace package
        [..., ModuleInfo(module_finder=FileFinder('.../sage/misc'), name='package_dir', ispkg=False), ...]

    TESTS::

        sage: # optional - meson_editable
        sage: sorted(sage.misc.package_dir.walk_packages(sage.misc.__path__))
        [..., ModuleInfo(module_finder=<...MesonpyPathFinder object...>, name='package_dir', ispkg=False), ...]
    """
