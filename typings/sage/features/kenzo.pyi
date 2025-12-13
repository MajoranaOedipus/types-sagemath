from . import Feature as Feature, FeatureTestResult as FeatureTestResult

class Kenzo(Feature):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`Kenzo <spkg_kenzo>`.

    EXAMPLES::

        sage: from sage.features.kenzo import Kenzo
        sage: Kenzo().is_present()  # optional - kenzo
        FeatureTestResult('kenzo', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.kenzo import Kenzo
            sage: isinstance(Kenzo(), Kenzo)
            True
        """

def all_features(): ...
