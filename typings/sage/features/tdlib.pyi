from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class Tdlib(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the SageMath interface to the :ref:`tdlib <spkg_tdlib>` library.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.tdlib import Tdlib
            sage: isinstance(Tdlib(), Tdlib)
            True
        """

def all_features(): ...
