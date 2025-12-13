from _typeshed import Incomplete
from typing import NamedTuple

DEFAULT_PYPI: str

def pkgname_split(name):
    """
    Split a pkgname into a list of strings, 'name, version'.

    For some packages, the version string might be empty.

    EXAMPLES::

        sage: from sage.misc.package import pkgname_split
        sage: pkgname_split('hello_world-1.2')
        ['hello_world', '1.2']
    """
def pip_remote_version(pkg, pypi_url=..., ignore_URLError: bool = False):
    """
    Return the version of this pip package available on PyPI.

    INPUT:

    - ``pkg`` -- the package

    - ``pypi_url`` -- string (default: standard PyPI url) an optional Python
      package repository to use

    - ``ignore_URLError`` -- boolean (default: ``False``); if set to ``True`` then no
      error is raised if the connection fails and the function returns ``None``

    EXAMPLES:

    The following test does fail if there is no TLS support (see e.g.
    :issue:`19213`)::

        sage: from sage.misc.package import pip_remote_version
        sage: pip_remote_version('beautifulsoup4') # optional - internet # not tested
        '...'

    These tests are reliable since the tested package does not exist::

        sage: nap = 'hey_this_is_NOT_a_python_package'
        sage: pypi = 'http://this.is.not.pypi.com/'
        sage: pip_remote_version(nap, pypi_url=pypi, ignore_URLError=True) # optional - internet
        doctest:...: UserWarning: failed to fetch the version of
        pkg='hey_this_is_NOT_a_python_package' at
        http://this.is.not.pypi.com/.../json
        sage: pip_remote_version(nap, pypi_url=pypi, ignore_URLError=False) # optional - internet
        Traceback (most recent call last):
        ...
        HTTPError: HTTP Error 404: Not Found
    """
def spkg_type(name):
    """
    Return the type of the Sage package with the given name.

    INPUT:

    - ``name`` -- string giving the subdirectory name of the package under
      ``SAGE_PKGS``

    EXAMPLES::

        sage: from sage.misc.package import spkg_type
        sage: spkg_type('pip')                                  # optional - sage_spkg
        'standard'

    OUTPUT:

    The type as a string in ``('base', 'standard', 'optional', 'experimental')``.
    If no ``SPKG`` exists with the given name (or the directory ``SAGE_PKGS`` is
    not available), ``None`` is returned.
    """
def pip_installed_packages(normalization=None):
    """
    Return a dictionary `name->version` of installed pip packages.

    This command returns *all* pip-installed packages. Not only Sage packages.

    INPUT:

    - ``normalization`` -- (default: ``None``) according to which rule to
      normalize the package name, either ``None`` (as is) or ``'spkg'`` (format
      as in the Sage distribution in ``build/pkgs/``), i.e., lowercased and
      dots and dashes replaced by underscores.

    EXAMPLES::

        sage: # optional - sage_spkg
        sage: from sage.misc.package import pip_installed_packages
        sage: d = pip_installed_packages()
        sage: 'scipy' in d or 'SciPy' in d                                              # needs scipy
        True
        sage: 'beautifulsoup4' in d                             # needs beautifulsoup4
        True
        sage: 'prompt-toolkit' in d or 'prompt_toolkit' in d    # whether - or _ appears in the name depends on the setuptools version used for building the package
        True
        sage: d = pip_installed_packages(normalization='spkg')
        sage: d['prompt_toolkit']
        '...'
        sage: d['scipy']                                                                # needs scipy
        '...'
    """

class PackageInfo(NamedTuple):
    """Represents information about a package."""
    name: str
    type: str | None = ...
    source: str | None = ...
    installed_version: str | None = ...
    remote_version: str | None = ...
    def is_installed(self) -> bool:
        """
        Whether the package is installed in the system.
        """

def list_packages(*pkg_types: str, pkg_sources: list[str] = ['normal', 'pip', 'script'], local: bool = False, ignore_URLError: bool = False, exclude_pip: bool = False) -> dict[str, PackageInfo]:
    """
    Return a dictionary of information about each package.

    The keys are package names and values are named tuples with the following keys:

    - ``'type'`` -- either ``'base``, ``'standard'``, ``'optional'``, or ``'experimental'``
    - ``'source'`` -- either ``'normal', ``'pip'``, or ``'script'``
    - ``'installed'`` -- boolean
    - ``'installed_version'`` -- ``None`` or a string
    - ``'remote_version'`` -- string

    INPUT:

    - ``pkg_types`` -- (optional) a sublist of ``'base``, ``'standard'``, ``'optional'``,
      or ``'experimental'``.  If provided, list only the packages with the
      given type(s), otherwise list all packages.

    - ``pkg_sources`` -- (optional) a sublist of ``'normal', ``'pip'``, or ``'script'``.
      If provided, list only the packages with the given source(s), otherwise list all
      packages.

    - ``local`` -- boolean (default: ``False``); if set to ``True``, then do not
      consult remote (PyPI) repositories for package versions (only applicable for
      ``'pip'`` type)

    - ``exclude_pip`` -- boolean (default: ``False``); if set to ``True``, then
      pip packages are not considered.  This is the same as removing ``'pip'``
      from ``pkg_sources``

    - ``ignore_URLError`` -- boolean (default: ``False``); if set to ``True``, then
      connection errors will be ignored

    EXAMPLES::

        sage: # optional - sage_spkg
        sage: from sage.misc.package import list_packages
        sage: L = list_packages('standard')
        sage: sorted(L.keys())  # random
        ['alabaster',
         'babel',
         ...
         'zlib']
        sage: sage_conf_info = L['sage_conf']
        sage: sage_conf_info.type
        'standard'
        sage: sage_conf_info.is_installed()
        True
        sage: sage_conf_info.source
        'script'

        sage: # optional - sage_spkg internet
        sage: L = list_packages(pkg_sources=['pip'], local=True)
        sage: bp_info = L['biopython']
        sage: bp_info.type
        'optional'
        sage: bp_info.source
        'pip'

    Check the option ``exclude_pip``::

        sage: [p for p, d in list_packages('optional', exclude_pip=True).items()  # optional - sage_spkg
        ....:  if d.source == 'pip']
        []
    """
def installed_packages(exclude_pip: bool = True):
    '''
    Return a dictionary of all installed packages, with version numbers.

    INPUT:

    - ``exclude_pip`` -- boolean (default: ``True``); whether "pip" packages
      are excluded from the list

    EXAMPLES:

    Below we test for a standard package without ``spkg-configure.m4`` script
    that should be installed in ``SAGE_LOCAL``. When Sage is installed by
    the Sage distribution (indicated by feature ``sage_spkg``), we should have
    the installation record for this package. (We do not test for installation
    records of Python packages. Our ``SAGE_VENV`` is not necessarily the
    main Sage venv; it could be a user-created venv or a venv created by tox.)::

        sage: # optional - sage_spkg
        sage: from sage.misc.package import installed_packages
        sage: sorted(installed_packages().keys())
        [...\'gnulib\', ...]
        sage: installed_packages()[\'gnulib\']  # random
        \'f9b39c4e337f1dc0dd07c4f3985c476fb875d799\'

    .. SEEALSO::

        :func:`sage.misc.package.list_packages`
    '''
def is_package_installed(package, exclude_pip: bool = True):
    '''
    Return whether (any version of) ``package`` is installed.

    INPUT:

    - ``package`` -- the name of the package

    - ``exclude_pip`` -- boolean (default: ``True``); whether to consider pip
      type packages

    EXAMPLES::

        sage: from sage.misc.package import is_package_installed
        sage: is_package_installed(\'gnulib\')  # optional - sage_spkg
        True

    Giving just the beginning of the package name is not good enough::

        sage: is_package_installed(\'conway_poly\')         # optional - sage_spkg
        False

    Otherwise, installing "pillow" would cause this function to think
    that "pil" is installed, for example.

    .. NOTE::

        Do not use this function to check whether you can use a feature from an
        external library. This only checks whether something was installed with
        ``sage -i`` but it may have been installed by other means (for example
        if this copy of Sage has been installed as part of a distribution.)
        Use the framework provided by :mod:`sage.features` to check
        whether a library is installed and functional.
    '''
def is_package_installed_and_updated(package: str) -> bool:
    '''
    Return whether the given package is installed and up-to-date.

    INPUT:

    - ``package`` -- the name of the package

    EXAMPLES::

        sage: from sage.misc.package import is_package_installed_and_updated
        sage: is_package_installed_and_updated("alabaster")    # optional - build, random
        False
    '''
def package_versions(package_type, local: bool = False):
    """
    Return version information for each Sage package.

    INPUT:

    - ``package_type`` -- string; one of ``'standard'``, ``'optional'`` or
      ``'experimental'``

    - ``local`` -- boolean (default: ``False``); only query local data (no internet needed)

    For packages of the given type, return a dictionary whose entries
    are of the form ``'package': (installed, latest)``, where
    ``installed`` is the installed version (or ``None`` if not
    installed) and ``latest`` is the latest available version. If the
    package has a directory in ``SAGE_ROOT/build/pkgs/``, then
    ``latest`` is determined by the file ``package-version.txt`` in
    that directory.  If ``local`` is ``False``, then Sage's servers are
    queried for package information.

    .. SEEALSO:: :func:`sage.misc.package.list_packages`

    EXAMPLES::

        sage: # optional - sage_spkg
        sage: from sage.misc.package import package_versions
        sage: std = package_versions('standard', local=True)
        sage: 'gap' in std
        True
        sage: std['zlib']  # random
        ('1.2.11.p0', '1.2.11.p0')
    """
def package_manifest(package):
    """
    Return the manifest for ``package``.

    INPUT:

    - ``package`` -- package name

    The manifest is written in the file
    ``SAGE_SPKG_INST/package-VERSION``. It is a JSON file containing a
    dictionary with the package name, version, installation date, list
    of installed files, etc.

    EXAMPLES::

        sage: # optional - sage_spkg
        sage: from sage.misc.package import package_manifest
        sage: manifest = package_manifest('gnulib')
        sage: manifest['package_name'] == 'gnulib'
        True
        sage: 'files' in manifest
        True

    Test a nonexistent package::

        sage: package_manifest('dummy-package')                  # optional - sage_spkg
        Traceback (most recent call last):
        ...
        KeyError: 'dummy-package'
    """

PackageNotFoundError: Incomplete
