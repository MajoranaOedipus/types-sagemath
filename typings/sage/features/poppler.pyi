from . import Executable as Executable

class pdftocairo(Executable):
    """
    A :class:`sage.features.Feature` describing the presence of
    ``pdftocairo``

    EXAMPLES::

        sage: from sage.features.poppler import pdftocairo
        sage: pdftocairo().is_present()             # optional: pdftocairo
        FeatureTestResult('pdftocairo', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.poppler import pdftocairo
            sage: isinstance(pdftocairo(), pdftocairo)
            True
        """

def all_features(): ...
