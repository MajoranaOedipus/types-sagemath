from . import CythonFeature as CythonFeature, PythonModule as PythonModule
from .join_feature import JoinFeature as JoinFeature

TEST_CODE: str

class BlissLibrary(CythonFeature):
    """
    A :class:`~sage.features.Feature` which describes whether the :ref:`Bliss library <spkg_bliss>` is
    present and functional.

    EXAMPLES::

        sage: from sage.features.bliss import BlissLibrary
        sage: BlissLibrary().require()  # optional - libbliss
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.bliss import BlissLibrary
            sage: BlissLibrary()
            Feature('libbliss')
        """

class Bliss(JoinFeature):
    """
    A :class:`~sage.features.Feature` which describes whether the :mod:`sage.graphs.bliss`
    module is available in this installation of Sage.

    EXAMPLES::

        sage: from sage.features.bliss import Bliss
        sage: Bliss().require()  # optional - bliss
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.bliss import Bliss
            sage: Bliss()
            Feature('bliss')
        """

def all_features(): ...
