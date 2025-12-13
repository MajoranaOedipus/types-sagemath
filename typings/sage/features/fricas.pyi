from . import Executable as Executable, FeatureTestResult as FeatureTestResult

class FriCAS(Executable):
    """
    A :class:`~sage.features.Feature` which checks for the :ref:`fricas <fricas>` binary.

    EXAMPLES::

        sage: from sage.features.fricas import FriCAS
        sage: FriCAS().is_present()  # optional - fricas
        FeatureTestResult('fricas', True)
    """
    MINIMUM_VERSION: str
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.fricas import FriCAS
            sage: isinstance(FriCAS(), FriCAS)
            True
        """
    def get_version(self):
        """
        Retrieve the installed FriCAS version

        EXAMPLES::
            sage: from sage.features.fricas import FriCAS
            sage: FriCAS().get_version() # optional - fricas
            '1.3...'
        """
    def is_functional(self):
        """
        Check whether ``fricas`` works on trivial input.

        EXAMPLES::

            sage: from sage.features.fricas import FriCAS
            sage: FriCAS().is_functional()  # optional - fricas
            FeatureTestResult('fricas', True)
        """

def all_features(): ...
