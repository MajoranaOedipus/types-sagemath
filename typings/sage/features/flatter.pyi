from . import Executable as Executable

class flatter(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``flatter``.

    EXAMPLES::

        sage: from sage.features.flatter import flatter
        sage: flatter().is_present()  # optional - flatter
        FeatureTestResult('flatter', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.flatter import flatter
            sage: isinstance(flatter(), flatter)
            True
        """

def all_features(): ...
