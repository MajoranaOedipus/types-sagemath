from . import Executable as Executable

class pdf2svg(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`pdf2svg <spkg_pdf2svg>`.

    EXAMPLES::

        sage: from sage.features.pdf2svg import pdf2svg
        sage: pdf2svg().is_present()             # optional - pdf2svg
        FeatureTestResult('pdf2svg', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.pdf2svg import pdf2svg
            sage: isinstance(pdf2svg(), pdf2svg)
            True
        """

def all_features(): ...
