from . import Executable as Executable
from .join_feature import JoinFeature as JoinFeature

class TOPCOMExecutable(Executable):
    """
    A :class:`~sage.features.Feature` which checks for executables from the :ref:`TOPCOM <spkg_topcom>` package.

    EXAMPLES::

        sage: from sage.features.topcom import TOPCOMExecutable
        sage: TOPCOMExecutable('points2allfinetriangs').is_present()    # optional - topcom
        FeatureTestResult('topcom_points2allfinetriangs', True)
    """
    def __init__(self, name) -> None:
        """
        TESTS::

            sage: from sage.features.topcom import TOPCOMExecutable
            sage: isinstance(TOPCOMExecutable('points2finetriangs'), TOPCOMExecutable)
            True
        """

class TOPCOM(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the executables
    which comes as a part of :ref:`TOPCOM <spkg_topcom>`.

    EXAMPLES::

        sage: from sage.features.topcom import TOPCOM
        sage: TOPCOM().is_present()                             # optional - topcom
        FeatureTestResult('topcom', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.topcom import TOPCOM
            sage: isinstance(TOPCOM(), TOPCOM)
            True
        """

def all_features(): ...
