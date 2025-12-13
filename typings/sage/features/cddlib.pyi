from . import Executable as Executable

class CddExecutable(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of an executable
    which comes as a part of :ref:`cddlib <spkg_cddlib>`.

    EXAMPLES::

        sage: from sage.features.cddlib import CddExecutable
        sage: CddExecutable().is_present()
        FeatureTestResult('cddexec_gmp', True)
    """
    def __init__(self, name: str = 'cddexec_gmp') -> None:
        """
        TESTS::

            sage: from sage.features.cddlib import CddExecutable
            sage: isinstance(CddExecutable(), CddExecutable)
            True
        """
