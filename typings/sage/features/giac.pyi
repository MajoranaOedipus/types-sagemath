from . import Executable as Executable, FeatureTestResult as FeatureTestResult

class Giac(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`giac <spkg_giac>`.

    EXAMPLES::

        sage: from sage.features.giac import Giac
        sage: Giac().is_present()  # needs giac
        FeatureTestResult('giac', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.giac import Giac
            sage: isinstance(Giac(), Giac)
            True
        """

def all_features(): ...
