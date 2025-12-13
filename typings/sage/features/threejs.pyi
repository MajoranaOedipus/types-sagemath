from . import StaticFile as StaticFile

class Threejs(StaticFile):
    """
    A :class:`~sage.features.Feature` which describes the presence of
    threejs-sage in a few standard locations.

    EXAMPLES::

        sage: from sage.features.threejs import Threejs
        sage: bool(Threejs().is_present())  # needs threejs
        True
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.threejs import Threejs
            sage: isinstance(Threejs(), Threejs)
            True
        """
    def required_version(self):
        """
        Return the version of threejs that Sage requires.

        Defining what version is required is delegated to the distribution package
        that provides the file ``threejs-version.txt`` in :mod:`sage.ext_data.threejs`.

        If the file is not provided, :exc:`FileNotFoundError` is raised.

        EXAMPLES::

            sage: from sage.features.threejs import Threejs
            sage: Threejs().required_version()
            'r...'
        """

def all_features(): ...
