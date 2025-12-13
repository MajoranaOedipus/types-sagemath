from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class Sirocco(JoinFeature):
    """
    A :class:`~sage.features.Feature` which describes whether the :mod:`sage.libs.sirocco`
    module is available in this installation of Sage.

    EXAMPLES::

        sage: from sage.features.sirocco import Sirocco
        sage: Sirocco().require()  # optional - sirocco
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.sirocco import Sirocco
            sage: Sirocco()
            Feature('sirocco')
        """

def all_features(): ...
