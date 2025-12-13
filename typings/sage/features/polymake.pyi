from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class JuPyMake(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of the :ref:`JuPyMake <spkg_jupymake>`
    module, a Python interface to the :ref:`polymake <spkg_polymake>` library.

    EXAMPLES::

        sage: from sage.features.polymake import JuPyMake
        sage: JuPyMake().is_present()  # optional - jupymake
        FeatureTestResult('jupymake', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.polymake import JuPyMake
            sage: isinstance(JuPyMake(), JuPyMake)
            True
        """

def all_features(): ...
