from . import Executable as Executable

class Info(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`info <spkg_info>`.

    EXAMPLES::

        sage: from sage.features.info import Info
        sage: Info()
        Feature('info')
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.info import Info
            sage: isinstance(Info(), Info)
            True
        """

def all_features(): ...
