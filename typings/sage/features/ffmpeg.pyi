from . import Executable as Executable, FeatureTestResult as FeatureTestResult

class FFmpeg(Executable):
    """
    A :class:`~sage.features.Feature` describing the presence of :ref:`ffmpeg <spkg_ffmpeg>`.

    EXAMPLES::

        sage: from sage.features.ffmpeg import FFmpeg
        sage: FFmpeg().is_present()  # optional - ffmpeg
        FeatureTestResult('ffmpeg', True)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.features.ffmpeg import FFmpeg
            sage: isinstance(FFmpeg(), FFmpeg)
            True
        """
    def is_functional(self):
        """
        Return whether command ``ffmpeg`` in the path is functional.

        EXAMPLES::

            sage: from sage.features.ffmpeg import FFmpeg
            sage: FFmpeg().is_functional()   # optional - ffmpeg
            FeatureTestResult('ffmpeg', True)
        """

def all_features(): ...
