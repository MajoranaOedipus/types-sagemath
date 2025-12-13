from . import Executable as Executable, PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature
from .sagemath import sage__libs__singular as sage__libs__singular
from sage.env import SINGULAR_BIN as SINGULAR_BIN

class Singular(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of the :ref:`singular <spkg_singular>` executable.

    .. SEEALSO::

        :class:`Feature sage.libs.singular <~sage.features.sagemath.sage__libs__singular>`

    EXAMPLES::

        sage: from sage.features.singular import Singular
        sage: Singular().is_present()                                                   # needs singular
        FeatureTestResult('singular', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.singular import Singular
            sage: isinstance(Singular(), Singular)
            True
        """

def all_features(): ...
