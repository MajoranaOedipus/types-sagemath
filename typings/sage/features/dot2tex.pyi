from . import PythonModule as PythonModule

class dot2tex(PythonModule):
    """
    A :class:`sage.features.Feature` describing the presence of :ref:`dot2tex <spkg_dot2tex>`.

    dot2tex is provided by an optional package in the Sage distribution.

    EXAMPLES::

        sage: from sage.features.dot2tex import dot2tex
        sage: dot2tex().is_present()                     # optional - dot2tex
        FeatureTestResult('dot2tex', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.dot2tex import dot2tex
            sage: isinstance(dot2tex(), dot2tex)
            True
        """

def all_features(): ...
