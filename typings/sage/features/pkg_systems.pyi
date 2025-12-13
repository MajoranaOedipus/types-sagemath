from . import Feature as Feature

class PackageSystem(Feature):
    """
    A :class:`Feature` describing a system package manager.

    EXAMPLES::

        sage: from sage.features.pkg_systems import PackageSystem
        sage: PackageSystem('conda')
        Feature('conda')
    """
    def spkg_installation_hint(self, spkgs, *, prompt: str = '  !', feature=None):
        """
        Return a string that explains how to install ``feature``.

        EXAMPLES::

            sage: from sage.features.pkg_systems import PackageSystem
            sage: homebrew = PackageSystem('homebrew')
            sage: homebrew.spkg_installation_hint('openblas')  # optional - SAGE_ROOT
            'To install openblas using the homebrew package manager, you can try to run:\\n!brew install openblas'
        """

class SagePackageSystem(PackageSystem):
    """
    A :class:`Feature` describing the package manager of the SageMath distribution.

    EXAMPLES::

        sage: from sage.features.pkg_systems import SagePackageSystem
        sage: SagePackageSystem()
        Feature('sage_spkg')
    """
    @staticmethod
    def __classcall__(cls):
        """
        Normalize initargs.

        TESTS::

            sage: from sage.features.pkg_systems import SagePackageSystem
            sage: SagePackageSystem() is SagePackageSystem()  # indirect doctest
            True
        """

class PipPackageSystem(PackageSystem):
    """
    A :class:`Feature` describing the Pip package manager.

    EXAMPLES::

        sage: from sage.features.pkg_systems import PipPackageSystem
        sage: PipPackageSystem()
        Feature('pip')
    """
    @staticmethod
    def __classcall__(cls):
        """
        Normalize initargs.

        TESTS::

            sage: from sage.features.pkg_systems import PipPackageSystem
            sage: PipPackageSystem() is PipPackageSystem()  # indirect doctest
            True
        """
