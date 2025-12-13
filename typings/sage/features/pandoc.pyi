from . import Executable as Executable

class Pandoc(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`pandoc <spkg_pandoc>`.

    EXAMPLES::

        sage: from sage.features.pandoc import Pandoc
        sage: Pandoc().is_present()  # optional - pandoc
        FeatureTestResult('pandoc', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.pandoc import Pandoc
            sage: isinstance(Pandoc(), Pandoc)
            True
        """

def all_features(): ...
