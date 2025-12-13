from . import PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

class Coxeter3(JoinFeature):
    """
    A :class:`~sage.features.Feature` which describes whether the :mod:`sage.libs.coxeter3`
    module is available in this installation of Sage.

    EXAMPLES::

        sage: from sage.features.coxeter3 import Coxeter3
        sage: Coxeter3().require()  # optional - coxeter3
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.coxeter3 import Coxeter3
            sage: Coxeter3()
            Feature('coxeter3')
        """

def all_features(): ...
