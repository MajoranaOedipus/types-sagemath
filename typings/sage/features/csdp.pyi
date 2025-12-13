from . import Executable as Executable, FeatureTestResult as FeatureTestResult

class CSDP(Executable):
    """
    A :class:`~sage.features.Feature` which checks for the ``theta`` binary
    of :ref:`CSDP <spkg_csdp>`.

    EXAMPLES::

        sage: from sage.features.csdp import CSDP
        sage: CSDP().is_present()  # optional - csdp
        FeatureTestResult('csdp', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.csdp import CSDP
            sage: isinstance(CSDP(), CSDP)
            True
        """
    def is_functional(self):
        """
        Check whether ``theta`` works on a trivial example.

        EXAMPLES::

            sage: from sage.features.csdp import CSDP
            sage: CSDP().is_functional()  # optional - csdp
            FeatureTestResult('csdp', True)
        """

def all_features(): ...
