from . import Executable as Executable

class GfanExecutable(Executable):
    """
    A :class:`~sage.features.Feature` for the :ref:`gfan <spkg_gfan>` executables.
    """
    def __init__(self, cmd=None) -> None:
        """
        TESTS::

            sage: from sage.features.gfan import GfanExecutable
            sage: isinstance(GfanExecutable('groebnercone'), GfanExecutable)
            True
        """

def all_features(): ...
