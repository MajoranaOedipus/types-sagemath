from . import Feature as Feature

class SloaneOEIS(Feature):
    """
    A :class:`~sage.features.Feature` which describes the presence of
    the Sloane Online Encyclopedia of Integer Sequences.

    EXAMPLES::

        sage: from sage.features.sloane_database import SloaneOEIS
        sage: bool(SloaneOEIS().is_present())  # optional - sloane_database
        True
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sloane_database import SloaneOEIS
            sage: isinstance(SloaneOEIS(), SloaneOEIS)
            True
        """

def all_features(): ...
