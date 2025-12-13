from _typeshed import Incomplete
from sage.env import SAGE_LOCAL as SAGE_LOCAL, SAGE_SHARE as SAGE_SHARE, SAGE_VENV as SAGE_VENV

class TrivialClasscallMetaClass(type):
    """
    A trivial version of :class:`sage.misc.classcall_metaclass.ClasscallMetaclass` without Cython dependencies.
    """
    def __call__(cls, *args, **kwds):
        """
        This method implements ``cls(<some arguments>)``.
        """

class TrivialUniqueRepresentation(metaclass=TrivialClasscallMetaClass):
    """
    A trivial version of :class:`UniqueRepresentation` without Cython dependencies.
    """
    @staticmethod
    def __classcall__(cls, *args, **options):
        """
        Construct a new object of this class or reuse an existing one.
        """

class Feature(TrivialUniqueRepresentation):
    '''
    A feature of the runtime environment.

    INPUT:

    - ``name`` -- string; name of the feature. This should be suitable as an optional tag
      for the Sage doctester, i.e., lowercase alphanumeric with underscores (``_``) allowed;
      features that correspond to Python modules/packages may use periods (``.``)

    - ``spkg`` -- string; name of the SPKG providing the feature

    - ``description`` -- string (optional); plain English description of the feature

    - ``url`` -- a URL for the upstream package providing the feature

    - ``type`` -- string; one of ``\'standard\'``, ``\'optional\'`` (default), ``\'experimental\'``

    Overwrite :meth:`_is_present` to add feature checks.

    EXAMPLES::

        sage: from sage.features.gap import GapPackage
        sage: GapPackage("grape", spkg=\'gap_packages\')  # indirect doctest
        Feature(\'gap_package_grape\')

    For efficiency, features are unique::

        sage: GapPackage("grape") is GapPackage("grape")
        True
    '''
    name: Incomplete
    spkg: Incomplete
    url: Incomplete
    description: Incomplete
    def __init__(self, name, spkg=None, url=None, description=None, type: str = 'optional') -> None:
        '''
        TESTS::

            sage: from sage.features import Feature
            sage: from sage.features.gap import GapPackage
            sage: isinstance(GapPackage("grape", spkg=\'gap_packages\'), Feature)  # indirect doctest
            True
        '''
    def is_present(self):
        '''
        Return whether the feature is present.

        OUTPUT:

        A :class:`FeatureTestResult` which can be used as a boolean and
        contains additional information about the feature test.

        EXAMPLES::

            sage: from sage.features.gap import GapPackage
            sage: GapPackage("grape", spkg=\'gap_packages\').is_present()  # optional - gap_package_grape
            FeatureTestResult(\'gap_package_grape\', True)
            sage: GapPackage("NOT_A_PACKAGE", spkg=\'gap_packages\').is_present()
            FeatureTestResult(\'gap_package_NOT_A_PACKAGE\', False)

        The result is cached::

            sage: from sage.features import Feature
            sage: class TestFeature(Feature):
            ....:     def _is_present(self):
            ....:         print("checking presence")
            ....:         return True
            sage: TestFeature("test").is_present()
            checking presence
            FeatureTestResult(\'test\', True)
            sage: TestFeature("test").is_present()
            FeatureTestResult(\'test\', True)
            sage: TestFeature("other").is_present()
            checking presence
            FeatureTestResult(\'other\', True)
            sage: TestFeature("other").is_present()
            FeatureTestResult(\'other\', True)
        '''
    def require(self) -> None:
        '''
        Raise a :exc:`FeatureNotPresentError` if the feature is not present.

        EXAMPLES::

            sage: from sage.features.gap import GapPackage
            sage: GapPackage("ve1EeThu").require()                                      # needs sage.libs.gap
            Traceback (most recent call last):
            ...
            FeatureNotPresentError: gap_package_ve1EeThu is not available.
            `LoadPackage("ve1EeThu")` evaluated to `fail` in GAP.
        '''
    def resolution(self):
        """
        Return a suggestion on how to make :meth:`is_present` pass if it did not
        pass.

        OUTPUT: string

        EXAMPLES::

            sage: from sage.features import Executable
            sage: Executable(name='CSDP', spkg='csdp', executable='theta', url='https://github.com/dimpase/csdp').resolution()  # optional - sage_spkg
            '...To install CSDP...you can try to run...sage -i csdp...Further installation instructions might be available at https://github.com/dimpase/csdp.'
        """
    def joined_features(self):
        """
        Return a list of features that ``self`` is the join of.

        OUTPUT:

        A (possibly empty) list of instances of :class:`Feature`.

        EXAMPLES::

            sage: from sage.features.graphviz import Graphviz
            sage: Graphviz().joined_features()
            [Feature('dot'), Feature('neato'), Feature('twopi')]
            sage: from sage.features.sagemath import sage__rings__function_field
            sage: sage__rings__function_field().joined_features()
            [Feature('sage.rings.function_field.function_field_polymod'),
            Feature('sage.libs.singular'),
            Feature('sage.libs.singular.singular'),
            Feature('sage.interfaces.singular')]
            sage: from sage.features.interfaces import Mathematica
            sage: Mathematica().joined_features()
            []
        """
    def is_standard(self):
        """
        Return whether this feature corresponds to a standard SPKG.

        EXAMPLES::

            sage: from sage.features.databases import DatabaseCremona
            sage: DatabaseCremona().is_standard()
            False
        """
    def is_optional(self) -> bool:
        """
        Return whether this feature corresponds to an optional SPKG.

        EXAMPLES::

            sage: from sage.features.databases import DatabaseCremona
            sage: DatabaseCremona().is_optional()
            True
        """
    def hide(self) -> None:
        """
        Hide this feature. For example this is used when the doctest option
        ``--hide`` is set. Setting an installed feature as hidden pretends
        that it is not available. To revert this use :meth:`unhide`.

        EXAMPLES:

        Benzene is an optional SPKG. The following test fails if it is hidden or
        not installed. Thus, in the second invocation the optional tag is needed::

            sage: from sage.features.graph_generators import Benzene
            sage: Benzene().hide()
            sage: len(list(graphs.fusenes(2)))                                          # needs sage.graphs
            Traceback (most recent call last):
            ...
            FeatureNotPresentError: benzene is not available.
            Feature `benzene` is hidden.
            Use method `unhide` to make it available again.

            sage: Benzene().unhide()            # optional - benzene, needs sage.graphs
            sage: len(list(graphs.fusenes(2)))  # optional - benzene, needs sage.graphs
            1
        """
    def unhide(self) -> None:
        """
        Revert what :meth:`hide` did.

        EXAMPLES:

            sage: from sage.features.sagemath import sage__plot
            sage: sage__plot().hide()
            sage: sage__plot().is_present()
            FeatureTestResult('sage.plot', False)
            sage: sage__plot().unhide()                                                 # needs sage.plot
            sage: sage__plot().is_present()                                             # needs sage.plot
            FeatureTestResult('sage.plot', True)
        """
    def is_hidden(self) -> bool:
        """
        Return whether ``self`` is present but currently hidden.

        EXAMPLES:

            sage: from sage.features.sagemath import sage__plot
            sage: sage__plot().hide()
            sage: sage__plot().is_hidden()                                              # needs sage.plot
            True
            sage: sage__plot().unhide()
            sage: sage__plot().is_hidden()
            False
        """

class FeatureNotPresentError(RuntimeError):
    """
    A missing feature error.

    EXAMPLES::

        sage: from sage.features import Feature, FeatureTestResult
        sage: class Missing(Feature):
        ....:     def _is_present(self):
        ....:         return False

        sage: Missing(name='missing').require()
        Traceback (most recent call last):
        ...
        FeatureNotPresentError: missing is not available.
    """
    feature: Incomplete
    reason: Incomplete
    def __init__(self, feature, reason=None, resolution=None) -> None: ...
    @property
    def resolution(self): ...

class FeatureTestResult:
    '''
    The result of a :meth:`Feature.is_present` call.

    Behaves like a boolean with some extra data which may explain why a feature
    is not present and how this may be resolved.

    EXAMPLES::

        sage: from sage.features.gap import GapPackage
        sage: presence = GapPackage("NOT_A_PACKAGE").is_present(); presence  # indirect doctest
        FeatureTestResult(\'gap_package_NOT_A_PACKAGE\', False)
        sage: bool(presence)
        False

    Explanatory messages might be available as ``reason`` and
    ``resolution``::

        sage: presence.reason                                                           # needs sage.libs.gap
        \'`LoadPackage("NOT_A_PACKAGE")` evaluated to `fail` in GAP.\'
        sage: bool(presence.resolution)
        False

    If a feature is not present, ``resolution`` defaults to
    ``feature.resolution()`` if this is defined. If you do not want to use this
    default you need explicitly set ``resolution`` to a string::

        sage: from sage.features import FeatureTestResult
        sage: package = GapPackage("NOT_A_PACKAGE", spkg=\'no_package\')
        sage: str(FeatureTestResult(package, True).resolution)  # optional - sage_spkg
        \'...To install gap_package_NOT_A_PACKAGE...you can try to run...sage -i no_package...\'
        sage: str(FeatureTestResult(package, False).resolution) # optional - sage_spkg
        \'...To install gap_package_NOT_A_PACKAGE...you can try to run...sage -i no_package...\'
        sage: FeatureTestResult(package, False, resolution=\'rtm\').resolution
        \'rtm\'
    '''
    feature: Incomplete
    is_present: Incomplete
    reason: Incomplete
    def __init__(self, feature, is_present, reason=None, resolution=None) -> None:
        """
        TESTS::

            sage: from sage.features import Executable, FeatureTestResult
            sage: isinstance(Executable(name='sh', executable='sh').is_present(), FeatureTestResult)
            True
        """
    @property
    def resolution(self): ...
    def __bool__(self) -> bool:
        '''
        Whether the tested :class:`Feature` is present.

        TESTS::

            sage: from sage.features import Feature, FeatureTestResult
            sage: bool(FeatureTestResult(Feature("SomePresentFeature"), True))  # indirect doctest
            True
            sage: bool(FeatureTestResult(Feature("SomeMissingFeature"), False))
            False
        '''

def package_systems():
    """
    Return a list of :class:`~sage.features.pkg_systems.PackageSystem` objects
    representing the available package systems.

    The list is ordered by decreasing preference.

    EXAMPLES::

        sage: from sage.features import package_systems
        sage: package_systems()    # random
        [Feature('homebrew'), Feature('sage_spkg'), Feature('pip')]
    """

class FileFeature(Feature):
    """
    Base class for features that describe a file or directory in the file system.

    A subclass should implement a method :meth:`absolute_filename`.

    EXAMPLES:

    Two direct concrete subclasses of :class:`FileFeature` are defined::

        sage: from sage.features import StaticFile, Executable, FileFeature
        sage: issubclass(StaticFile, FileFeature)
        True
        sage: issubclass(Executable, FileFeature)
        True

    To work with the file described by the feature, use the method :meth:`absolute_filename`.
    A :exc:`FeatureNotPresentError` is raised if the file cannot be found::

        sage: Executable(name='does-not-exist', executable='does-not-exist-xxxxyxyyxyy').absolute_filename()
        Traceback (most recent call last):
        ...
        sage.features.FeatureNotPresentError: does-not-exist is not available.
        Executable 'does-not-exist-xxxxyxyyxyy' not found on PATH.

    A :class:`FileFeature` also provides the :meth:`is_present` method to test for
    the presence of the file at run time. This is inherited from the base class
    :class:`Feature`::

        sage: Executable(name='sh', executable='sh').is_present()
        FeatureTestResult('sh', True)
    """
    def absolute_filename(self) -> str:
        """
        The absolute path of the file as a string.

        Concrete subclasses must override this abstract method.

        TESTS::

            sage: from sage.features import FileFeature
            sage: FileFeature(name='abstract_file').absolute_filename()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """

class Executable(FileFeature):
    """
    A feature describing an executable in the ``PATH``.

    In an installation of Sage with ``SAGE_LOCAL`` different from ``SAGE_VENV``, the
    executable is searched first in ``SAGE_VENV/bin``, then in ``SAGE_LOCAL/bin``,
    then in ``PATH``.

    .. NOTE::

        Overwrite :meth:`is_functional` if you also want to check whether
        the executable shows proper behaviour.

        Calls to :meth:`is_present` are cached. You might want to cache the
        :class:`Executable` object to prevent unnecessary calls to the
        executable.

    EXAMPLES::

        sage: from sage.features import Executable
        sage: Executable(name='sh', executable='sh').is_present()
        FeatureTestResult('sh', True)
        sage: Executable(name='does-not-exist', executable='does-not-exist-xxxxyxyyxyy').is_present()
        FeatureTestResult('does-not-exist', False)
    """
    executable: Incomplete
    def __init__(self, name, executable, **kwds) -> None:
        """
        TESTS::

            sage: from sage.features import Executable
            sage: isinstance(Executable(name='sh', executable='sh'), Executable)
            True
        """
    def is_functional(self):
        """
        Return whether an executable in the path is functional.

        This method is used internally and can be overridden in subclasses
        in order to implement a feature test. It should not be called directly.
        Use :meth:`Feature.is_present` instead.

        EXAMPLES:

        The function returns ``True`` unless explicitly overwritten::

            sage: from sage.features import Executable
            sage: Executable(name='sh', executable='sh').is_functional()
            FeatureTestResult('sh', True)
        """
    def absolute_filename(self) -> str:
        """
        The absolute path of the executable as a string.

        EXAMPLES::

            sage: from sage.features import Executable
            sage: Executable(name='sh', executable='sh').absolute_filename()
            '/...bin/sh'

        A :exc:`FeatureNotPresentError` is raised if the file cannot be found::

            sage: Executable(name='does-not-exist', executable='does-not-exist-xxxxyxyyxyy').absolute_filename()
            Traceback (most recent call last):
            ...
            sage.features.FeatureNotPresentError: does-not-exist is not available.
            Executable 'does-not-exist-xxxxyxyyxyy' not found on PATH.
        """

class StaticFile(FileFeature):
    """
    A :class:`Feature` which describes the presence of a certain file such as a
    database.

    EXAMPLES::

        sage: from sage.features import StaticFile
        sage: StaticFile(name='no_such_file', filename='KaT1aihu',              # optional - sage_spkg
        ....:            search_path='/', spkg='some_spkg',
        ....:            url='http://rand.om').require()
        Traceback (most recent call last):
        ...
        FeatureNotPresentError: no_such_file is not available.
        'KaT1aihu' not found in any of ['/']...
        To install no_such_file...you can try to run...sage -i some_spkg...
        Further installation instructions might be available at http://rand.om.
    """
    filename: Incomplete
    search_path: Incomplete
    def __init__(self, name, filename, *, search_path=None, type: str = 'optional', **kwds) -> None:
        '''
        TESTS::

            sage: from sage.features import StaticFile
            sage: StaticFile(name=\'null\', filename=\'null\', search_path=\'/dev\')
            Feature(\'null\')
            sage: sh = StaticFile(name=\'shell\', filename=\'sh\',
            ....:                 search_path=("/dev", "/bin", "/usr"))
            sage: sh
            Feature(\'shell\')
            sage: sh.absolute_filename()
            \'/bin/sh\'
        '''
    def absolute_filename(self) -> str:
        '''
        The absolute path of the file as a string.

        EXAMPLES::

            sage: from sage.features import StaticFile
            sage: from sage.misc.temporary_file import tmp_dir
            sage: dir_with_file = tmp_dir()
            sage: file_path = os.path.join(dir_with_file, "file.txt")
            sage: open(file_path, \'a\').close() # make sure the file exists
            sage: search_path = ( \'/foo/bar\', dir_with_file ) # file is somewhere in the search path
            sage: feature = StaticFile(name=\'file\', filename=\'file.txt\', search_path=search_path)
            sage: feature.absolute_filename() == file_path
            True

        A :exc:`FeatureNotPresentError` is raised if the file cannot be found::

            sage: from sage.features import StaticFile
            sage: StaticFile(name=\'no_such_file\', filename=\'KaT1aihu\',  # optional - sage_spkg
            ....:            search_path=(), spkg=\'some_spkg\',
            ....:            url=\'http://rand.om\').absolute_filename()
            Traceback (most recent call last):
            ...
            FeatureNotPresentError: no_such_file is not available.
            \'KaT1aihu\' not found in any of []...
            To install no_such_file...you can try to run...sage -i some_spkg...
            Further installation instructions might be available at http://rand.om.
        '''

class CythonFeature(Feature):
    '''
    A :class:`Feature` which describes the ability to compile and import
    a particular piece of Cython code.

    To test the presence of ``name``, the cython compiler is run on
    ``test_code`` and the resulting module is imported.

    EXAMPLES::

        sage: from sage.features import CythonFeature
        sage: fabs_test_code = \'\'\'
        ....: cdef extern from "<math.h>":
        ....:     double fabs(double x)
        ....:
        ....: assert fabs(-1) == 1
        ....: \'\'\'
        sage: fabs = CythonFeature("fabs", test_code=fabs_test_code,                    # needs sage.misc.cython
        ....:                      spkg=\'gcc\', url=\'https://gnu.org\',
        ....:                      type=\'standard\')
        sage: fabs.is_present()                                                         # needs sage.misc.cython
        FeatureTestResult(\'fabs\', True)

    Test various failures::

        sage: broken_code = \'\'\'this is not a valid Cython program!\'\'\'
        sage: broken = CythonFeature("broken", test_code=broken_code)
        sage: broken.is_present()
        FeatureTestResult(\'broken\', False)

    ::

        sage: broken_code = \'\'\'cdef extern from "no_such_header_file": pass\'\'\'
        sage: broken = CythonFeature("broken", test_code=broken_code)
        sage: broken.is_present()
        FeatureTestResult(\'broken\', False)

    ::

        sage: broken_code = \'\'\'import no_such_python_module\'\'\'
        sage: broken = CythonFeature("broken", test_code=broken_code)
        sage: broken.is_present()
        FeatureTestResult(\'broken\', False)

    ::

        sage: broken_code = \'\'\'raise AssertionError("sorry!")\'\'\'
        sage: broken = CythonFeature("broken", test_code=broken_code)
        sage: broken.is_present()
        FeatureTestResult(\'broken\', False)
    '''
    test_code: Incomplete
    def __init__(self, name, test_code, **kwds) -> None:
        """
        TESTS::

            sage: from sage.features import CythonFeature
            sage: from sage.features.bliss import BlissLibrary
            sage: isinstance(BlissLibrary(), CythonFeature)  # indirect doctest
            True
        """

class PythonModule(Feature):
    '''
    A :class:`Feature` which describes whether a python module can be imported.

    EXAMPLES:

    Not all builds of python include the ``ssl`` module, so you could check
    whether it is available::

        sage: from sage.features import PythonModule
        sage: PythonModule("ssl").require()  # not tested - output depends on the python build
    '''
    def __init__(self, name, **kwds) -> None:
        """
        TESTS::

            sage: from sage.features import PythonModule
            sage: from sage.features.databases import DatabaseKnotInfo
            sage: isinstance(DatabaseKnotInfo(), PythonModule)  # indirect doctest
            True
        """
