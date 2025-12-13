from . import PythonModule as PythonModule

class Phitigra(PythonModule):
    """
    A :class:`sage.features.Feature` describing the presence of :ref:`phitigra <spkg_phitigra>`.

    Phitigra is provided by an optional package in the Sage distribution.

    EXAMPLES::

        sage: from sage.features.phitigra import Phitigra
        sage: Phitigra().is_present()                     # optional - phitigra
        FeatureTestResult('phitigra', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.phitigra import Phitigra
            sage: isinstance(Phitigra(), Phitigra)
            True
        """

def all_features(): ...
