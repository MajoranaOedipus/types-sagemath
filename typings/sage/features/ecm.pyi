from . import Executable as Executable
from sage.env import SAGE_ECMBIN as SAGE_ECMBIN

class Ecm(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`GMP-ECM <spkg_ecm>`.

    EXAMPLES::

        sage: from sage.features.ecm import Ecm
        sage: Ecm().is_present()
        FeatureTestResult('ecm', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.ecm import Ecm
            sage: isinstance(Ecm(), Ecm)
            True
        """

def all_features(): ...
