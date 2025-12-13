from . import Feature as Feature, FeatureTestResult as FeatureTestResult

class MesonEditable(Feature):
    """
    A :class:`~sage.features.Feature` describing if Meson editable install
    is used.

    EXAMPLES::

        sage: from sage.features.meson_editable import MesonEditable
        sage: MesonEditable()
        Feature('meson_editable')
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.meson_editable import MesonEditable
            sage: MesonEditable() is MesonEditable()
            True
        """

def all_features(): ...
