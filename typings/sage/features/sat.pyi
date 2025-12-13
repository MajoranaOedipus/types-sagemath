from . import Executable as Executable, PythonModule as PythonModule

class Glucose(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of an
    executable from the :ref:`Glucose SAT solver <spkg_glucose>`.

    EXAMPLES::

        sage: from sage.features.sat import Glucose
        sage: Glucose().is_present()                  # optional - glucose
        FeatureTestResult('glucose', True)
    """
    def __init__(self, executable: str = 'glucose') -> None:
        """
        TESTS::

            sage: from sage.features.sat import Glucose
            sage: isinstance(Glucose(), Glucose)
            True
        """

class Kissat(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of the
    :ref:`Kissat SAT solver <spkg_kissat>`.

    EXAMPLES::

        sage: from sage.features.sat import Kissat
        sage: Kissat().is_present()                             # optional - kissat
        FeatureTestResult('kissat', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sat import Kissat
            sage: isinstance(Kissat(), Kissat)
            True
        """

class Pycosat(PythonModule):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`spkg_pycosat`.

    EXAMPLES::

        sage: from sage.features.sat import Pycosat
        sage: Pycosat().is_present()                  # optional - pycosat
        FeatureTestResult('pycosat', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sat import Pycosat
            sage: isinstance(Pycosat(), Pycosat)
            True
        """

class Pycryptosat(PythonModule):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`spkg_pycryptosat`.

    EXAMPLES::

        sage: from sage.features.sat import Pycryptosat
        sage: Pycryptosat().is_present()              # optional - pycryptosat
        FeatureTestResult('pycryptosat', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sat import Pycryptosat
            sage: isinstance(Pycryptosat(), Pycryptosat)
            True
        """

def all_features(): ...
