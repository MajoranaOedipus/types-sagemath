from . import Executable as Executable, FeatureTestResult as FeatureTestResult

class Plantri(Executable):
    """
    A :class:`~sage.features.Feature` which checks for the :ref:`plantri <spkg_plantri>` binary.

    EXAMPLES::

        sage: from sage.features.graph_generators import Plantri
        sage: Plantri().is_present()  # optional - plantri
        FeatureTestResult('plantri', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.graph_generators import Plantri
            sage: isinstance(Plantri(), Plantri)
            True
        """
    def is_functional(self):
        """
        Check whether ``plantri`` works on trivial input.

        EXAMPLES::

            sage: from sage.features.graph_generators import Plantri
            sage: Plantri().is_functional()  # optional - plantri
            FeatureTestResult('plantri', True)
        """

class Buckygen(Executable):
    """
    A :class:`~sage.features.Feature` which checks for the :ref:`buckygen <spkg_buckygen>` binary.

    EXAMPLES::

        sage: from sage.features.graph_generators import Buckygen
        sage: Buckygen().is_present()  # optional - buckygen
        FeatureTestResult('buckygen', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.graph_generators import Buckygen
            sage: isinstance(Buckygen(), Buckygen)
            True
        """
    def is_functional(self):
        """
        Check whether ``buckygen`` works on trivial input.

        EXAMPLES::

            sage: from sage.features.graph_generators import Buckygen
            sage: Buckygen().is_functional()  # optional - buckygen
            FeatureTestResult('buckygen', True)
        """

class Benzene(Executable):
    """
    A :class:`~sage.features.Feature` which checks for the :ref:`benzene <spkg_benzene>`
    binary.

    EXAMPLES::

        sage: from sage.features.graph_generators import Benzene
        sage: Benzene().is_present()  # optional - benzene
        FeatureTestResult('benzene', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.graph_generators import Benzene
            sage: isinstance(Benzene(), Benzene)
            True
        """
    def is_functional(self):
        """
        Check whether ``benzene`` works on trivial input.

        EXAMPLES::

            sage: from sage.features.graph_generators import Benzene
            sage: Benzene().is_functional()  # optional - benzene
            FeatureTestResult('benzene', True)
        """

def all_features(): ...
