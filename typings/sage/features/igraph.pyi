from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class python_igraph(JoinFeature):
    """
    A :class:`sage.features.Feature` describing the presence of the
    Python package :ref:`igraph <spkg_python_igraph>`.

    EXAMPLES::

        sage: from sage.features.igraph import python_igraph
        sage: python_igraph().is_present()                    # optional - python_igraph
        FeatureTestResult('python_igraph', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.igraph import python_igraph
            sage: isinstance(python_igraph(), python_igraph)
            True
        """

def all_features(): ...
