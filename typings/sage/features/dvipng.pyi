from . import Executable as Executable

class dvipng(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of ``dvipng``.

    EXAMPLES::

        sage: from sage.features.dvipng import dvipng
        sage: dvipng().is_present()             # optional - dvipng
        FeatureTestResult('dvipng', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.dvipng import dvipng
            sage: isinstance(dvipng(), dvipng)
            True
        """

def all_features(): ...
