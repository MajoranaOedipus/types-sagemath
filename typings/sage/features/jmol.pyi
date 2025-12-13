from . import StaticFile as StaticFile

class JmolDataJar(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of
    JmolData.jar in a few standard locations.

    EXAMPLES::

        sage: from sage.features.jmol import JmolDataJar
        sage: bool(JmolDataJar().is_present())  # needs jmol
        True
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.jmol import JmolDataJar
            sage: isinstance(JmolDataJar(), JmolDataJar)
            True
        """

def all_features(): ...
