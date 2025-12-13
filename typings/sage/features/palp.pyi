from . import Executable as Executable
from .join_feature import JoinFeature as JoinFeature

class PalpExecutable(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of a :ref:`PALP <spkg_palp>` executable.

    INPUT:

    - ``palpprog`` -- string, one of ``'poly'``, ``'class'``, ``'nef'``, ``'cws'``

    - ``suff`` -- string or ``None``
    """
    def __init__(self, palpprog, suff=None) -> None:
        '''
        TESTS::

            sage: from sage.features.palp import PalpExecutable
            sage: isinstance(PalpExecutable("poly", 5), PalpExecutable)
            True
        '''

class Palp(JoinFeature):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`PALP <spkg_palp>`.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.palp import Palp
            sage: isinstance(Palp(), Palp)
            True
        """

def all_features(): ...
