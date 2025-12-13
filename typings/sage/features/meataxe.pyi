from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class Meataxe(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the Sage modules
    that depend on the :ref:`meataxe <spkg_meataxe>` library.

    EXAMPLES::

        sage: from sage.features.meataxe import Meataxe
        sage: Meataxe().is_present()  # optional - meataxe
        FeatureTestResult('meataxe', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.meataxe import Meataxe
            sage: isinstance(Meataxe(), Meataxe)
            True
        """

def all_features(): ...
