from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class symengine_py(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of the
    Python package :ref:`symengine_py <spkg_symengine_py>`.

    EXAMPLES::

        sage: from sage.features.symengine_py import symengine_py
        sage: symengine_py().is_present()                    # optional - symengine_py
        FeatureTestResult('symengine_py', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.symengine_py import symengine_py
            sage: isinstance(symengine_py(), symengine_py)
            True
        """

def all_features(): ...
