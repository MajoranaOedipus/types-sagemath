from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class PyNormaliz(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the
    Python package :ref:`PyNormaliz <spkg_pynormaliz>`.

    EXAMPLES::

        sage: from sage.features.normaliz import PyNormaliz
        sage: PyNormaliz().is_present()                    # optional - pynormaliz
        FeatureTestResult('pynormaliz', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.normaliz import PyNormaliz
            sage: isinstance(PyNormaliz(), PyNormaliz)
            True
        """

def all_features(): ...
