from . import Executable as Executable
from .join_feature import JoinFeature as JoinFeature

class FourTi2Executable(Executable):
    """
    A :class:`~sage.features.Feature` for the :ref:`4ti2 <spkg_4ti2>` executables.
    """
    def __init__(self, name) -> None:
        """
        TESTS::

            sage: from sage.features.four_ti_2 import FourTi2Executable
            sage: isinstance(FourTi2Executable('hilbert'), FourTi2Executable)
            True
        """

class FourTi2(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of all :ref:`4ti2 <spkg_4ti2>` executables.

    EXAMPLES::

        sage: from sage.features.four_ti_2 import FourTi2
        sage: FourTi2().is_present()  # optional - 4ti2
        FeatureTestResult('4ti2', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.four_ti_2 import FourTi2
            sage: isinstance(FourTi2(), FourTi2)
            True
        """

def all_features(): ...
