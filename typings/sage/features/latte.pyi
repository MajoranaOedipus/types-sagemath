from . import Executable as Executable
from .join_feature import JoinFeature as JoinFeature

LATTE_URL: str

class Latte_count(Executable):
    """
    Feature for the executable ``count`` from :ref:`LattE integrale <spkg_latte_int>`.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.latte import Latte_count
            sage: isinstance(Latte_count(), Latte_count)
            True
        """

class Latte_integrate(Executable):
    """
    Feature for the executable ``integrate`` from :ref:`LattE integrale <spkg_latte_int>`.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.latte import Latte_integrate
            sage: isinstance(Latte_integrate(), Latte_integrate)
            True
        """

class Latte(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of executables
    from :ref:`LattE integrale <spkg_latte_int>`.

    EXAMPLES::

        sage: from sage.features.latte import Latte
        sage: Latte().is_present()  # optional - latte_int
        FeatureTestResult('latte_int', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.latte import Latte
            sage: isinstance(Latte(), Latte)
            True
        """

def all_features(): ...
