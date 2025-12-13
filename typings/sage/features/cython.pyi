from . import CythonFeature as CythonFeature

class sage__misc__cython(CythonFeature):
    """
    A :class:`~sage.features.Feature` which describes whether :mod:`sage.misc.cython`
    is available and functional.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features import CythonFeature
            sage: from sage.features.cython import sage__misc__cython
            sage: isinstance(sage__misc__cython(), CythonFeature)
            True
        """

def all_features(): ...
