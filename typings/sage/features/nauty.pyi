from . import Executable as Executable
from .join_feature import JoinFeature as JoinFeature
from sage.env import SAGE_NAUTY_BINS_PREFIX as SAGE_NAUTY_BINS_PREFIX

class NautyExecutable(Executable):
    """
    A :class:`~sage.features.Feature` which checks for executables from the :ref:`nauty <spkg_nauty>` package.

    EXAMPLES::

        sage: from sage.features.nauty import NautyExecutable
        sage: NautyExecutable('converseg').is_present()                                 # needs nauty
        FeatureTestResult('nauty_converseg', True)
    """
    def __init__(self, name) -> None:
        """
        TESTS::

            sage: from sage.features.nauty import NautyExecutable
            sage: isinstance(NautyExecutable('geng'), NautyExecutable)
            True
        """

class Nauty(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the executables
    which comes as a part of :ref:`nauty <spkg_nauty>`.

    EXAMPLES::

        sage: from sage.features.nauty import Nauty
        sage: Nauty().is_present()                                                      # needs nauty
        FeatureTestResult('nauty', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.nauty import Nauty
            sage: isinstance(Nauty(), Nauty)
            True
        """

def all_features(): ...
