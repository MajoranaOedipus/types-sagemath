from . import Executable as Executable, FeatureTestResult as FeatureTestResult

class msolve(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`msolve <spkg_msolve>`.

    EXAMPLES::

        sage: from sage.features.msolve import msolve
        sage: msolve().is_present()  # optional - msolve
        FeatureTestResult('msolve', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.msolve import msolve
            sage: isinstance(msolve(), msolve)
            True
        """
    def is_functional(self):
        """
        Test if our installation of msolve is working.

        TESTS::

            sage: from sage.features.msolve import msolve
            sage: msolve().is_functional()  # optional - msolve
            FeatureTestResult('msolve', True)
        """

def all_features(): ...
