from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class Mcqd(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the :mod:`~sage.graphs.mcqd` module,
    which is the SageMath interface to the :ref:`mcqd <spkg_mcqd>` library

    EXAMPLES::

        sage: from sage.features.mcqd import Mcqd
        sage: Mcqd().is_present()  # optional - mcqd
        FeatureTestResult('mcqd', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.mcqd import Mcqd
            sage: isinstance(Mcqd(), Mcqd)
            True
        """

def all_features(): ...
